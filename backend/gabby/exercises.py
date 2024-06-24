from contextlib import contextmanager
from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy import orm
import sqlalchemy as sql

from fastjsonapi import make_filters

from . import api_models
from . import parsing
from . import renderable
from . import settings
from .database_utils import OrmBase, SessionDependable
from .api_utils import create_item, get_item, get_page, save_item, delete_item
from .projects import Project
from .testing import TransactionTestCase
from .textbooks import Textbook, TextbooksResource
from .users import MandatoryAuthBearerDependable
from .users.mixins import CreatedUpdatedByAtMixin
from .wrapping import unwrap, set_wrapper, make_sqids, orm_wrapper_with_sqids


class Adaptation(OrmBase, CreatedUpdatedByAtMixin):
    __tablename__ = "adaptations"

    __mapper_args__ = {
        "polymorphic_on": "kind",
    }

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    kind: orm.Mapped[str] = orm.mapped_column(sql.String(16))

    exercise: orm.Mapped["Exercise"] = orm.relationship(back_populates="adaptation")

    def make_adapted(self):
        return renderable.AdaptedExercise(
            number=self.exercise.number,
            textbook_page=self.exercise.textbook_page,
            instructions=self.make_adapted_instructions(),
            wording=self.make_adapted_wording(),
            example=self.make_adapted_example(),
            clue=self.make_adapted_clue(),
        )

    def to_generic_adaptation(self):
        return GenericAdaptation(
            exercise=Exercise(
                project=None,
                textbook=self.exercise.textbook,
                textbook_page=self.exercise.textbook_page,
                number=self.exercise.number,
                instructions=self.make_adapted_instructions().to_generic(),
                wording=self.make_adapted_wording().to_generic(),
                example=example.to_generic() if (example := self.make_adapted_example()) else "",
                clue=clue.to_generic() if (clue := self.make_adapted_clue()) else "",
            ),
        )


class GenericAdaptation(Adaptation):
    __tablename__ = "adaptations__g"
    __mapper_args__ = {
        "polymorphic_identity": "g",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)

    def make_adapted_instructions(self):
        return parsing.parse_generic_section(self.exercise.instructions)

    def make_adapted_wording(self):
        return parsing.parse_generic_section(self.exercise.wording)

    def make_adapted_example(self):
        return parsing.parse_generic_section(self.exercise.example)

    def make_adapted_clue(self):
        return parsing.parse_generic_section(self.exercise.clue)


class Exercise(OrmBase, CreatedUpdatedByAtMixin):
    __tablename__ = "exercises"

    __table_args__ = (
        sql.UniqueConstraint("textbook_id", "textbook_page", "number"),
        sql.CheckConstraint("(textbook_id IS NULL) = (textbook_page IS NULL)", name="textbook_id_textbook_page_consistently_null"),
        sql.ForeignKeyConstraint(["project_id", "textbook_id"], ["textbooks.project_id", "textbooks.id"]),
    )

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    project_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Project.id))
    project: orm.Mapped[Project] = orm.relationship(back_populates="exercises", overlaps="exercises")

    textbook_id: orm.Mapped[int | None]
    textbook: orm.Mapped[Textbook | None] = orm.relationship(back_populates="exercises", overlaps="exercises,project")
    textbook_page: orm.Mapped[int | None]
    bounding_rectangle: orm.Mapped[dict | None] = orm.mapped_column(sql.JSON)

    # Custom collation: https://dba.stackexchange.com/a/285230
    number: orm.Mapped[str] = orm.mapped_column(sql.String(None, collation="exercise_number"))
    instructions: orm.Mapped[str]
    wording: orm.Mapped[str]
    example: orm.Mapped[str]
    clue: orm.Mapped[str]

    adaptation_id: orm.Mapped[int | None] = orm.mapped_column(sql.ForeignKey(Adaptation.id), unique=True)
    adaptation: orm.Mapped[Adaptation | None] = orm.relationship(back_populates="exercise")

    extraction_events: orm.Mapped[list["ExtractionEvent"]] = orm.relationship(back_populates="exercise", cascade="all, delete-orphan")


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

    def test_create_without_project(self):
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

    def test_create_without_project__fixed_by_orm(self):
        exercise = self.create_model(Exercise, project=None, textbook=self.textbook, textbook_page=5, number="5", instructions="", wording="", example="", clue="")
        self.assertEqual(exercise.project, self.project)

    def test_create_with_inconsistent_project(self):
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

    def test_create_with_inconsistent_project__fixed_by_orm(self):
        other_project = self.create_model(Project, title="Other project", description="")
        exercise = self.create_model(Exercise, project=other_project, textbook=self.textbook, textbook_page=5, number="5", instructions="", wording="", example="", clue="")
        self.assertEqual(exercise.project, self.project)

    def test_create_without_textbook__broken_by_orm(self):
        with self.make_session() as session:
            session.add(project1 := Project(title='Premier projet de test', description="Ce projet contient des exercices d'un seul manuel.", created_by=self.user_for_create, updated_by=self.user_for_create))
            session.add(project2 := Project(title='Deuxième projet de test', description='Ce projet contient des exercices originaux.', created_by=self.user_for_create, updated_by=self.user_for_create))
            session.flush()
            session.add(Textbook(project=project1, title='Français CE2', publisher='Slabeuf', year=2021, isbn='1234567890123', created_by=self.user_for_create, updated_by=self.user_for_create))
            # session.flush()  # This flush would avoid the IntegrityError
            # The exercise is created with 'project=None', probably because of the ORM warning silenced by the 'overlaps=' arguments in the relationships
            session.add(exercise4 := Exercise(project=project2, textbook=None, textbook_page=None, number='L1', instructions='Faire des choses intelligentes.', example='', clue='', wording='', created_by=self.user_for_create, updated_by=self.user_for_create))
            with self.assertRaises(sql.exc.IntegrityError) as cm:
                session.flush()
        self.assertEqual(cm.exception.orig.diag.column_name, "project_id")

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

    def test_share_adaptation(self):
        project = self.create_model(Project, title="Project", description="")
        adaptation = self.create_model(GenericAdaptation)
        exercise_1 = self.create_model(Exercise, project=project, number="Exercise 1", instructions="", wording="", example="", clue="", adaptation=adaptation)
        exercise_2 = self.create_model(Exercise, project=project, number="Exercise 2", instructions="", wording="", example="", clue="")

        with self.make_session() as session:
            with self.assertRaises(sql.exc.IntegrityError) as cm:
                session.execute(sql.update(Exercise).where(Exercise.id == exercise_2.id).values(adaptation_id=adaptation.id))
        self.assertEqual(cm.exception.orig.diag.constraint_name, "exercises_adaptation_id_key")

    def test_share_adaptation__fixed_by_orm(self):
        with self.make_session() as session:
            session.add(project := Project(title="Project", description="", created_by=self.user_for_create, updated_by=self.user_for_create))
            session.add(adaptation := GenericAdaptation(created_by=self.user_for_create, updated_by=self.user_for_create))
            session.flush()
            session.add(exercise_1 := Exercise(project=project, number="Exercise 1", instructions="", wording="", example="", clue="", adaptation=adaptation, created_by=self.user_for_create, updated_by=self.user_for_create))
            session.flush()
            session.add(exercise_2 := Exercise(project=project, number="Exercise 2", instructions="", wording="", example="", clue="", adaptation=adaptation, created_by=self.user_for_create, updated_by=self.user_for_create))
            session.flush()

            self.assertIs(exercise_1.adaptation, exercise_2.adaptation)

            session.refresh(exercise_1)

            self.assertIsNone(exercise_1.adaptation)

    def test_share_adaptation__not_fixed_by_orm(self):
        with self.make_session() as session:
            session.add(project := Project(title="Project", description="", created_by=self.user_for_create, updated_by=self.user_for_create))
            session.add(adaptation := GenericAdaptation(created_by=self.user_for_create, updated_by=self.user_for_create))
            session.flush()
            session.add(Exercise(project=project, number="Exercise 1", instructions="", wording="", example="", clue="", adaptation=adaptation, created_by=self.user_for_create, updated_by=self.user_for_create))
            session.add(Exercise(project=project, number="Exercise 2", instructions="", wording="", example="", clue="", adaptation=adaptation, created_by=self.user_for_create, updated_by=self.user_for_create))

            with self.assertRaises(sql.exc.IntegrityError) as cm:
                session.flush()
        self.assertEqual(cm.exception.orig.diag.constraint_name, "exercises_adaptation_id_key")

    def test_delete_with_extraction_events(self):
        exercise = self.create_model(Exercise, project=self.project, textbook=None, textbook_page=None, number="5.b", instructions="", wording="", example="", clue="")
        self.create_model(ExtractionEvent, exercise=exercise, event="{}")
        self.create_model(ExtractionEvent, exercise=exercise, event="{}")

        with self.make_session() as session:
            session.delete(exercise)
            session.flush()
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
        bounding_rectangle,
        number,
        instructions,
        wording,
        example,
        clue,
        adaptation,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        bounding_rectangle = None if bounding_rectangle is None else bounding_rectangle.model_dump()
        return create_item(
            session, Exercise,
            project=project,
            textbook=textbook,
            textbook_page=textbook_page,
            bounding_rectangle=bounding_rectangle,
            number=number,
            instructions=instructions,
            wording=wording,
            example=example,
            clue=clue,
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

    class Filters(BaseModel):
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
        previous_adaptation = item.adaptation
        previous_bounding_rectangle = item.bounding_rectangle
        yield
        if item.bounding_rectangle is not previous_bounding_rectangle and item.bounding_rectangle is not None:
            item.bounding_rectangle = item.bounding_rectangle.model_dump()
        if previous_adaptation is not None and unwrap(item.adaptation) != unwrap(previous_adaptation):
            session.delete(previous_adaptation)
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


class ExtractionEventsResource:
    singular_name = "extraction_event"
    plural_name = "extraction_events"

    Model = api_models.ExtractionEvent

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    def create_item(
        self,
        exercise,
        event,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        return create_item(
            session, ExtractionEvent,
            exercise=exercise,
            event=event,
            created_by=authenticated_user,
            updated_by=authenticated_user,
        )

    def get_item(
        self,
        id,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        return get_item(session, ExtractionEvent, ExtractionEventsResource.sqids.decode(id)[0])

    def get_page(
        self,
        first_index,
        page_size,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        query = sql.select(ExtractionEvent)
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


set_wrapper(ExtractionEvent, orm_wrapper_with_sqids(ExtractionEventsResource.sqids))
