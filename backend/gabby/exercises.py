from contextlib import contextmanager
from typing import Annotated

from sqlalchemy import orm
import sqlalchemy as sql

from fastjsonapi import make_filters

from . import adaptation
from . import api_models
from . import deltas
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

    # Custom collation: https://dba.stackexchange.com/a/285230
    number: orm.Mapped[str] = orm.mapped_column(sql.String(None, collation="exercise_number"))

    _instructions_text: orm.Mapped[str] = orm.mapped_column(name="instructions_text", nullable=True)
    _instructions_deltas: orm.Mapped[list] = orm.mapped_column(sql.JSON, name="instructions", default=deltas.empty_as_list, server_default=deltas.empty_as_string)

    @property
    def instructions(self) -> deltas.Deltas:
        if self._instructions_deltas is None:  # Before the first flush to DB if not set in constructor.
            self._instructions_deltas = deltas.empty_as_list
        return [deltas.InsertOp(**delta) for delta in self._instructions_deltas]

    @instructions.setter
    def instructions(self, instructions: deltas.Deltas):
        self._instructions_deltas = [delta.model_dump() for delta in instructions]

    _wording_text: orm.Mapped[str] = orm.mapped_column(name="wording_text", nullable=True)
    _wording_deltas: orm.Mapped[list] = orm.mapped_column(sql.JSON, name="wording", default=deltas.empty_as_list, server_default=deltas.empty_as_string)

    @property
    def wording(self) -> deltas.Deltas:
        if self._wording_deltas is None:  # Before the first flush to DB if not set in constructor.
            self._wording_deltas = deltas.empty_as_list
        return [deltas.InsertOp(**delta) for delta in self._wording_deltas]

    @wording.setter
    def wording(self, wording: deltas.Deltas):
        self._wording_deltas = [delta.model_dump() for delta in wording]

    _example_text: orm.Mapped[str] = orm.mapped_column(name="example_text", nullable=True)
    _example_deltas: orm.Mapped[list] = orm.mapped_column(sql.JSON, name="example", default=deltas.empty_as_list, server_default=deltas.empty_as_string)

    @property
    def example(self) -> deltas.Deltas:
        if self._example_deltas is None:  # Before the first flush to DB if not set in constructor.
            self._example_deltas = deltas.empty_as_list
        return [deltas.InsertOp(**delta) for delta in self._example_deltas]

    @example.setter
    def example(self, example: str | deltas.Deltas):
        self._example_deltas = [delta.model_dump() for delta in example]

    _clue_text: orm.Mapped[str] = orm.mapped_column(name="clue_text", nullable=True)
    _clue_deltas: orm.Mapped[list] = orm.mapped_column(sql.JSON, name="clue", default=deltas.empty_as_list, server_default=deltas.empty_as_string)

    @property
    def clue(self) -> deltas.Deltas:
        if self._clue_deltas is None:  # Before the first flush to DB if not set in constructor.
            self._clue_deltas = deltas.empty_as_list
        return [deltas.InsertOp(**delta) for delta in self._clue_deltas]

    @clue.setter
    def clue(self, clue: deltas.Deltas):
        self._clue_deltas = [delta.model_dump() for delta in clue]

    _text_reference: orm.Mapped[list] = orm.mapped_column(sql.JSON, name="text_reference", default=deltas.empty_as_list, server_default=deltas.empty_as_string)

    @property
    def text_reference(self) -> deltas.Deltas:
        if self._text_reference is None:  # Before the first flush to DB if not set in constructor.
            self._text_reference = deltas.empty_as_list
        return [deltas.InsertOp(**delta) for delta in self._text_reference]

    @text_reference.setter
    def text_reference(self, text_reference: deltas.Deltas):
        self._text_reference = [delta.model_dump() for delta in text_reference]

    wording_paragraphs_per_pagelet: orm.Mapped[int | None] = orm.mapped_column(nullable=True)

    _rectangles: orm.Mapped[list] = orm.mapped_column(sql.JSON, name="rectangles", default=[], server_default="[]")

    @property
    def rectangles(self) -> list[api_models.PdfRectangle]:
        return [api_models.PdfRectangle(**rectangle) for rectangle in self._rectangles]

    @rectangles.setter
    def rectangles(self, rectangles: list[api_models.PdfRectangle]):
        self._rectangles = [rectangle.model_dump() for rectangle in rectangles]

    _adaptation: orm.Mapped[dict] = orm.mapped_column(sql.JSON, name="adaptation", default={"format": 0}, server_default="{\"format\": 0}")

    @property
    def adaptation(self) -> api_models.AdaptationV2:
        if self._adaptation is None:  # Before the first flush to DB if not set in constructor.
            self._adaptation = {"format": 0}

        match self._adaptation["format"]:
            case 0:
                return api_models.AdaptationV2(kind="generic", effects=[])
            case 2:
                return api_models.AdaptationV2(**self._adaptation["settings"])
            case format:
                raise ValueError(f"Unknown adaptation format {format}")

    @adaptation.setter
    def adaptation(self, adaptation: api_models.AdaptationV2):
        self._adaptation = {
            "format": 2,
            "settings": adaptation.model_dump(),
        }

    def make_adapted(self):
        return adaptation.adapt(self)


class ExerciseTestCase(TransactionTestCase):
    def setUp(self):
        super().setUp()
        self.project = self.create_model(Project, title="Project", description="")
        self.textbook = self.create_model(Textbook, project=self.project, title="Textbook")

    def test_create__with_textbook(self):
        e = self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="5", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.assertEqual(e.project, self.project)
        self.assertEqual(e.textbook, self.textbook)
        self.assertEqual(e.textbook_page, 5)
        self.assertEqual(e.number, "5")

    def test_create__without_textbook(self):
        e = self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="5", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.assertEqual(e.project, self.project)
        self.assertIsNone(e.textbook)
        self.assertIsNone(e.textbook_page)
        self.assertEqual(e.number, "5")

    def test_create_duplicate(self):
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="5", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        with self.assertRaises(sql.exc.IntegrityError) as cm:
            self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="5", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.assertEqual(cm.exception.orig.diag.constraint_name, "exercises_textbook_id_textbook_page_number_key")

    def test_create_near_duplicates(self):
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="A", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="a", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

    def test_create_with_textbook_but_without_textbook_page(self):
        with self.assertRaises(sql.exc.IntegrityError) as cm:
            self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=None, number="5", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.assertEqual(cm.exception.orig.diag.constraint_name, "textbook_id_textbook_page_consistently_null")

    def test_create_with_textbook_page_but_without_textbook(self):
        with self.assertRaises(sql.exc.IntegrityError) as cm:
            self.create_model(Exercise, project=self.project, textbook=None, textbook_page=5, number="5", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.assertEqual(cm.exception.orig.diag.constraint_name, "textbook_id_textbook_page_consistently_null")

    def test_create_without_project__without_orm(self):
        with self.make_session() as session:
            with self.assertRaises(sql.exc.IntegrityError) as cm:
                session.execute(sql.insert(Exercise).values(
                    project_id=None,
                    textbook_id=self.textbook.id,
                    textbook_page=5,
                    number="5",
                ))
        self.assertEqual(cm.exception.orig.diag.column_name, "project_id")

    def test_create_without_project__with_orm(self):
        with self.make_session() as session:
            session.add(Exercise(
                project=None,
                textbook=session.get(Textbook, self.textbook.id),
                textbook_page=5,
                number="5",
                instructions=deltas.empty,
                wording=deltas.empty,
                example=deltas.empty,
                clue=deltas.empty,
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
                instructions=deltas.empty,
                wording=deltas.empty,
                example=deltas.empty,
                clue=deltas.empty,
                created_by_id=self.user_for_create.id,
                updated_by_id=self.user_for_create.id,
            ))
            with self.assertRaises(sql.exc.IntegrityError) as cm:
                session.flush()
        self.assertEqual(cm.exception.orig.diag.constraint_name, "exercises_project_id_textbook_id_fkey")

    def test_ordering(self):
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="5.b", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="5.a", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="12", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="A12", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="A1", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=5, number="2", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="4", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="Some text", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="Some other text", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="Other text", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="1", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="Bob", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="10", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="Alice", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="03", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.project, textbook=self.textbook, textbook_page=1, number="2", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

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
        text_reference,
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
            text_reference=text_reference,
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
