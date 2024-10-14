from contextlib import contextmanager
from typing import Annotated
import json

import pydantic
from sqlalchemy import orm
import Levenshtein
import sqlalchemy as sql

from fastjsonapi import make_filters

from . import api_models
from . import exercise_delta
from . import parsing
from . import renderable
from . import settings
from .api_utils import create_item, get_item, get_page, save_item, delete_item
from .database_utils import OrmBase, SessionDependable
from .projects import Project
from .testing import TransactionTestCase
from .textbooks import Textbook, TextbooksResource
from .users import MandatoryAuthBearerDependable
from .users.mixins import CreatedUpdatedByAtMixin
from .wrapping import set_wrapper, make_sqids, orm_wrapper_with_sqids
from mydantic import PydanticBase


class OldAdaptation(OrmBase, CreatedUpdatedByAtMixin):
    __tablename__ = "adaptations"

    __mapper_args__ = {
        "polymorphic_on": "kind",
        "with_polymorphic": "*",
    }

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    kind: orm.Mapped[str] = orm.mapped_column(sql.String(16))

    exercise: orm.Mapped["Exercise"] = orm.relationship(back_populates="old_adaptation")

    def make_adapted(self):
        return self.exercise.make_adapted()

    def make_delta(self):
        return self.exercise.make_delta()

    def to_generic_adaptation(self):
        def to_generic_or_empty(adapted):
            if adapted is None:
                return ""
            else:
                return adapted.to_generic()

        return GenericOldAdaptation(
            exercise=Exercise(
                project=None,
                textbook=self.exercise.textbook,
                textbook_page=self.exercise.textbook_page,
                number=self.exercise.number,
                instructions=self.make_adapted_instructions().to_generic(),
                wording=self.make_adapted_wording().to_generic(),
                example=to_generic_or_empty(self.make_adapted_example()),
                clue=to_generic_or_empty(self.make_adapted_clue()),
                wording_paragraphs_per_pagelet=self.exercise.wording_paragraphs_per_pagelet,
            ),
        )


class GenericOldAdaptation(OldAdaptation):
    __tablename__ = "adaptations__g"
    __mapper_args__ = {
        "polymorphic_identity": "g",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(OldAdaptation.id), primary_key=True)

    def make_adapted_instructions(self):
        return parsing.adapt_generic_instructions_section(self.exercise.instructions)

    def make_adapted_wording(self):
        return parsing.adapt_generic_wording_section(self.exercise.wording)

    def make_adapted_example(self):
        return parsing.adapt_generic_instructions_section(self.exercise.example)

    def make_adapted_clue(self):
        return parsing.adapt_generic_instructions_section(self.exercise.clue)


class Exercise(OrmBase, CreatedUpdatedByAtMixin):
    __tablename__ = "exercises"

    __table_args__ = (
        sql.UniqueConstraint("textbook_id", "textbook_page", "number"),
        sql.CheckConstraint("(textbook_id IS NULL) = (textbook_page IS NULL)", name="textbook_id_textbook_page_consistently_null"),
        sql.ForeignKeyConstraint(["project_id", "textbook_id"], ["textbooks.project_id", "textbooks.id"]),
    )

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    project_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Project.id))
    project: orm.Mapped[Project] = orm.relationship(back_populates="exercises")

    textbook_id: orm.Mapped[int | None] = orm.mapped_column()
    textbook: orm.Mapped[Textbook | None] = orm.relationship(back_populates="exercises", foreign_keys=[textbook_id])
    textbook_page: orm.Mapped[int | None]
    bounding_rectangle: orm.Mapped[dict | None] = orm.mapped_column(sql.JSON)

    # Custom collation: https://dba.stackexchange.com/a/285230
    number: orm.Mapped[str] = orm.mapped_column(sql.String(None, collation="exercise_number"))
    instructions: orm.Mapped[str]
    wording: orm.Mapped[str]
    example: orm.Mapped[str]
    clue: orm.Mapped[str]

    wording_paragraphs_per_pagelet: orm.Mapped[int] = orm.mapped_column(default=3, server_default="3")

    _rectangles: orm.Mapped[list] = orm.mapped_column(sql.JSON, name="rectangles", default=[], server_default="[]")

    @property
    def rectangles(self) -> list[api_models.PdfRectangle]:
        return [api_models.PdfRectangle(**rectangle) for rectangle in self._rectangles]

    @rectangles.setter
    def rectangles(self, rectangles: list[api_models.PdfRectangle]):
        self._rectangles = [rectangle.model_dump() for rectangle in rectangles]

    old_adaptation_id: orm.Mapped[int | None] = orm.mapped_column(sql.ForeignKey(OldAdaptation.id), name="adaptation_id", unique=True)
    old_adaptation: orm.Mapped[OldAdaptation | None] = orm.relationship(
        back_populates="exercise",
        lazy="joined",
    )

    _adaptation: orm.Mapped[dict] = orm.mapped_column(sql.JSON, name="adaptation", default={"format": 0}, server_default="{\"format\": 0}")

    class AdaptationContainer(PydanticBase):
        # Thin wrapper to use Pydantic's discriminated unions
        adaptation: api_models.Adaptation = pydantic.Field(discriminator="kind")

    @property
    def adaptation(self) -> api_models.Adaptation:
        if self._adaptation is None:  # Before the first flush to DB if not set in constructor.
            self._adaptation = {"format": 0}

        match self._adaptation["format"]:
            case 0:
                if self.old_adaptation is None:
                    return api_models.NullAdaptation(kind="null")
                else:
                    return self.old_adaptation.to_new_adaptation()
            case 1:
                return self.AdaptationContainer(adaptation=self._adaptation["settings"]).adaptation
            case format:
                raise ValueError(f"Unknown format {format}")

    @adaptation.setter
    def adaptation(self, adaptation: api_models.Adaptation):
        self._adaptation = {
            "format": 1,
            "settings": adaptation.model_dump()
        }

    extraction_events: orm.Mapped[list["ExtractionEvent"]] = orm.relationship(
        back_populates="exercise",
        cascade="all, delete-orphan",
        order_by="ExtractionEvent.id",
    )

    def make_adapted(self):
        return renderable.Exercise(
            number=self.number,
            textbook_page=self.textbook_page,
            instructions=self.adaptation.make_adapted_instructions(self),
            wording=self.adaptation.make_adapted_wording(self),
            example=self.adaptation.make_adapted_example(self),
            clue=self.adaptation.make_adapted_clue(self),
            wording_paragraphs_per_pagelet=self.wording_paragraphs_per_pagelet,
        )

    def make_delta(self):
        return exercise_delta.Exercise(
            instructions=self.adaptation.make_instructions_delta(self),
            wording=self.adaptation.make_wording_delta(self),
            example=self.adaptation.make_example_delta(self),
            clue=self.adaptation.make_clue_delta(self),
        )


def check_rectangles_are_consistent_with_extraction_events(session: orm.Session):
    extraction_events_by_exercise_id = {}
    for extraction_event in session.execute(sql.select(ExtractionEvent)):
        event = json.loads(extraction_event[0].event)
        extraction_events_by_exercise_id.setdefault(extraction_event[0].exercise_id, []).append(event)

    for exercise_ in session.execute(sql.select(Exercise)):
        exercise: Exercise = exercise_[0]
        events = extraction_events_by_exercise_id.get(exercise.id, [])

        for event in events:
            assert event["kind"] in {
                "ExerciseNumberSetAutomatically",
                "ExerciseNumberSetManually",
                "InstructionsSetManually",
                "WordingSetManually",
                "ExampleSetManually",
                "ClueSetManually",
                "TextSelectedInPdf",
                "SelectedTextEdited",
                "SelectedTextAddedToInstructions",
                "SelectedTextAddedToWording",
                "SelectedTextAddedToExample",
                "SelectedTextAddedToClue",
                "BoundingRectangleSelectedInPdf",
            }

        text_selected_events_by_text = dict()
        for event in events:
            if event["kind"] == "TextSelectedInPdf":
                text_selected_events_by_text[event["value"]] = event
                if event["value"].startswith(exercise.number):
                    text_selected_events_by_text[event["value"][len(exercise.number):].lstrip()] = event
        for event in events:
            if event["kind"] == "SelectedTextEdited":
                best_distance = None
                for text, text_selected_events in list(text_selected_events_by_text.items()):
                    distance = Levenshtein.distance(event["value"], text)
                    if best_distance is None or distance < best_distance:
                        best_distance = distance
                        text_selected_events_by_text[event["value"]] = text_selected_events

        rectangles = []

        for event in events:
            if event["kind"] == "BoundingRectangleSelectedInPdf":
                rectangles.append(api_models.PdfRectangle(
                    pdf_sha256=event["pdf"]["sha256"],
                    pdf_page=event["pdf"]["page"],
                    coordinates="pdfjs",
                    start=api_models.Point(**event["pdf"]["rectangle"]["start"]),
                    stop=api_models.Point(**event["pdf"]["rectangle"]["stop"]),
                    text=None,
                    role="bounding",
                ))

        if len(rectangles) == 0 and exercise.bounding_rectangle is not None:
            textbook = exercise.textbook
            if textbook is not None:
                textbook_page = exercise.textbook_page
                sections = textbook.sections
                if sections:
                    section = sections[0]
                    pdf_file = section.pdf_file
                    rectangles.append(api_models.PdfRectangle(
                        pdf_sha256=pdf_file.sha256,
                        pdf_page=textbook_page + section.pdf_file_start_page - section.textbook_start_page,
                        coordinates="pdfjs",
                        start=exercise.bounding_rectangle["start"],
                        stop=exercise.bounding_rectangle["stop"],
                        text=None,
                        role="bounding",
                    ))

        for event in events:
            if event["kind"].startswith("SelectedTextAddedTo"):
                if event["valueBefore"] == "":
                    text_added = event["valueAfter"]
                elif event["valueBefore"].endswith("\n"):
                    text_added = event["valueAfter"][len(event["valueBefore"]):]
                else:
                    text_added = event["valueAfter"][len(event["valueBefore"]) + 1:]
                text_selected_event = text_selected_events_by_text[text_added]  # No .get: the text *has* been seen.
                rectangles.append(api_models.PdfRectangle(
                    pdf_sha256=text_selected_event["pdf"]["sha256"],
                    pdf_page=text_selected_event["pdf"]["page"],
                    coordinates="pdfjs",
                    start=api_models.Point(**text_selected_event["pdf"]["rectangle"]["start"]),
                    stop=api_models.Point(**text_selected_event["pdf"]["rectangle"]["stop"]),
                    text=text_selected_event["value"],
                    role=event["kind"][len("SelectedTextAddedTo"):].lower(),
                ))

        if exercise.rectangles != rectangles:
            print(f"Exercise {exercise.number} page {exercise.textbook_page}: rectangles={rectangles}")


class ExerciseTestCase(TransactionTestCase):
    def setUp(self):
        super().setUp()
        self.project = self.create_model(Project, title="Project", description="")
        self.textbook = self.create_model(Textbook, project=self.project, title="Textbook")

    def test_create__with_textbook(self):
        e = self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="5", instructions="", wording="", example="", clue="")
        self.assertEqual(e.project, self.project)
        self.assertEqual(e.textbook, self.textbook)
        self.assertEqual(e.textbook_page, 5)
        self.assertEqual(e.number, "5")

    def test_create__without_textbook(self):
        e = self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="5", instructions="", wording="", example="", clue="")
        self.assertEqual(e.project, self.project)
        self.assertIsNone(e.textbook)
        self.assertIsNone(e.textbook_page)
        self.assertEqual(e.number, "5")

    def test_create_duplicate(self):
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="5", instructions="", wording="", example="", clue="")
        with self.assertRaises(sql.exc.IntegrityError) as cm:
            self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="5", instructions="", wording="", example="", clue="")
        self.assertEqual(cm.exception.orig.diag.constraint_name, "exercises_textbook_id_textbook_page_number_key")

    def test_create_near_duplicates(self):
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="A", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="a", instructions="", wording="", example="", clue="")

    def test_create_with_textbook_but_without_textbook_page(self):
        with self.assertRaises(sql.exc.IntegrityError) as cm:
            self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=None, number="5", instructions="", wording="", example="", clue="")
        self.assertEqual(cm.exception.orig.diag.constraint_name, "textbook_id_textbook_page_consistently_null")

    def test_create_with_textbook_page_but_without_textbook(self):
        with self.assertRaises(sql.exc.IntegrityError) as cm:
            self.create_model(Exercise, project=self.project, textbook=None, textbook_page=5, number="5", instructions="", wording="", example="", clue="")
        self.assertEqual(cm.exception.orig.diag.constraint_name, "textbook_id_textbook_page_consistently_null")

    def test_create_without_project__without_orm(self):
        with self.make_session() as session:
            with self.assertRaises(sql.exc.IntegrityError) as cm:
                session.execute(sql.insert(Exercise).values(
                    project_id=None,
                    textbook_id=self.textbook.id,
                    textbook_page=5,
                    number="5",
                    instructions="",
                    wording="",
                    example="",
                    clue="",
                ))
        self.assertEqual(cm.exception.orig.diag.column_name, "project_id")

    def test_create_without_project__with_orm(self):
        with self.make_session() as session:
            session.add(Exercise(
                project=None,
                textbook=session.get(Textbook, self.textbook.id),
                textbook_page=5,
                number="5",
                instructions="",
                wording="",
                example="",
                clue="",
            ))
            with self.assertRaises(sql.exc.IntegrityError) as cm:
                session.flush()
        self.assertEqual(cm.exception.orig.diag.column_name, "project_id")

    def test_create_with_inconsistent_project__without_orm(self):
        other_project = self.create_model(Project, title="Other project", description="")
        with self.make_session() as session:
            with self.assertRaises(sql.exc.IntegrityError) as cm:
                session.execute(sql.insert(Exercise).values(
                    project_id=other_project.id,
                    textbook_id=self.textbook.id,
                    textbook_page=5,
                    number="5",
                    instructions="",
                    wording="",
                    example="",
                    clue="",
                    created_by_id=self.user_for_create.id,
                    updated_by_id=self.user_for_create.id,
                ))
        self.assertEqual(cm.exception.orig.diag.constraint_name, "exercises_project_id_textbook_id_fkey")

    def test_create_with_inconsistent_project__with_orm(self):
        other_project = self.create_model(Project, title="Other project", description="")
        with self.make_session() as session:
            session.add(Exercise(
                project=session.get(Project, other_project.id),
                textbook=session.get(Textbook, self.textbook.id),
                textbook_page=5,
                number="5",
                instructions="",
                wording="",
                example="",
                clue="",
                created_by_id=self.user_for_create.id,
                updated_by_id=self.user_for_create.id,
            ))
            with self.assertRaises(sql.exc.IntegrityError) as cm:
                session.flush()
        self.assertEqual(cm.exception.orig.diag.constraint_name, "exercises_project_id_textbook_id_fkey")

    def test_ordering(self):
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="5.b", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="5.a", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="12", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="A12", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="A1", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="2", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="4", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="Some text", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="Some other text", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="Other text", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="1", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="Bob", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="10", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="Alice", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="03", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="2", instructions="", wording="", example="", clue="")

        with self.make_session() as session:
            self.assertEqual(
                [
                    (exercise.textbook_id is not None, exercise.textbook_page, exercise.number)
                    for (exercise,) in session.execute(sql.select(Exercise).order_by(Exercise.textbook_page, Exercise.number))
                ],
                [
                    (True, 1, "1"),
                    (True, 1, "2"),
                    (True, 1, "03"),
                    (True, 1, "10"),
                    (True, 1, "Alice"),
                    (True, 1, "Bob"),
                    (True, 5, "2"),
                    (True, 5, "5.a"),
                    (True, 5, "5.b"),
                    (True, 5, "12"),
                    (True, 5, "A1"),
                    (True, 5, "A12"),
                    (False, None, "4"),
                    (False, None, "Other text"),
                    (False, None, "Some other text"),
                    (False, None, "Some text"),
                ],
            )

    def test_delete_with_extraction_events(self):
        exercise = self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="5.b", instructions="", wording="", example="", clue="")
        self.create_model(ExtractionEvent, exercise=exercise, event="{}")
        self.create_model(ExtractionEvent, exercise=exercise, event="{}")

        self.delete_item(exercise)

        self.assertEqual(self.count_models(Exercise), 0)
        self.assertEqual(self.count_models(ExtractionEvent), 0)


class ExercisesResource:
    singular_name = "exercise"
    plural_name = "exercises"

    Model = api_models.Exercise

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    def create_item(
        self,
        project,
        textbook,
        textbook_page,
        number,
        instructions,
        wording,
        example,
        clue,
        wording_paragraphs_per_pagelet,
        rectangles,
        adaptation,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        # @todo Add logs when modifying all resources. Give them a unique request identifier to be able te regroup logs from the same batch request.
        return create_item(
            session, Exercise,
            project=project,
            textbook=textbook,
            textbook_page=textbook_page,
            number=number,
            instructions=instructions,
            wording=wording,
            example=example,
            clue=clue,
            wording_paragraphs_per_pagelet=wording_paragraphs_per_pagelet,
            rectangles=rectangles,
            adaptation=adaptation,
            created_by=authenticated_user,
            updated_by=authenticated_user,
        )

    def get_item(
        self,
        id,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        return get_item(session, Exercise, ExercisesResource.sqids.decode(id)[0])

    class Filters(PydanticBase):
        textbook: str | None
        textbook_page: int | None
        number: str | None

    def get_page(
        self,
        first_index,
        page_size,
        session: SessionDependable,
        filters: Annotated[Filters, make_filters(Filters)],
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        query = sql.select(Exercise).order_by(Exercise.textbook_id, Exercise.textbook_page, Exercise.number)
        if filters.textbook is not None:
            query = query.where(Exercise.textbook_id == TextbooksResource.sqids.decode(filters.textbook)[0])
        if filters.textbook_page is not None:
            query = query.where(Exercise.textbook_page == filters.textbook_page)
        if filters.number is not None:
            query = query.where(Exercise.number == filters.number)
        return get_page(session, query, first_index, page_size)

    @contextmanager
    def save_item(
        self,
        item,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        yield
        item.updated_by = authenticated_user
        save_item(session, item)

    def delete_item(
        self,
        item,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        delete_item(session, item)


set_wrapper(Exercise, orm_wrapper_with_sqids(ExercisesResource.sqids))


class ExtractionEvent(OrmBase, CreatedUpdatedByAtMixin):
    __tablename__ = "extraction_events"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    exercise_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Exercise.id , ondelete="CASCADE"))
    exercise: orm.Mapped[Exercise] = orm.relationship(back_populates="extraction_events")

    event: orm.Mapped[str]
