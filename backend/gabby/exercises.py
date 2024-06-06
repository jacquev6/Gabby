from contextlib import contextmanager

from sqlalchemy import orm
import sqlalchemy as sql

from . import api_models
from . import parsing
from . import renderable
from . import settings
from .database_utils import OrmBase, SessionDependent, make_item_creator, make_item_deleter, make_item_getter, make_item_saver, make_page_getter
from .projects import Project
from .testing import TransactionTestCase
from .textbooks import Textbook, TextbooksResource
from .wrapping import wrap, unwrap, set_wrapper, make_sqids, orm_wrapper_with_sqids


class Adaptation(OrmBase):
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


class Exercise(OrmBase):
    __tablename__ = "exercises"

    __table_args__ = (
        sql.UniqueConstraint("textbook_id", "textbook_page", "number"),
        sql.CheckConstraint("(textbook_id IS NULL) = (textbook_page IS NULL)", name="textbook_id_textbook_page_consistently_null"),
    )

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    project_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Project.id))
    project: orm.Mapped[Project] = orm.relationship(back_populates="exercises")

    textbook_id: orm.Mapped[int | None] = orm.mapped_column(sql.ForeignKey(Textbook.id))
    textbook: orm.Mapped[Textbook | None] = orm.relationship(back_populates="exercises")
    textbook_page: orm.Mapped[int | None]
    bounding_rectangle: orm.Mapped[dict | None] = orm.mapped_column(sql.JSON)

    number: orm.Mapped[str]  # @todo Custom collation: https://dba.stackexchange.com/a/285230
    instructions: orm.Mapped[str]
    wording: orm.Mapped[str]
    example: orm.Mapped[str]
    clue: orm.Mapped[str]

    adaptation_id: orm.Mapped[int | None] = orm.mapped_column(sql.ForeignKey(Adaptation.id), unique=True)
    adaptation: orm.Mapped[Adaptation | None] = orm.relationship(back_populates="exercise")

    extraction_events: orm.Mapped[list["ExtractionEvent"]] = orm.relationship(back_populates="exercise")


# @todo Enable all tests in this class
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
        with self.assertRaises(sql.exc.IntegrityError) as cm:
            self.create_model(Exercise, project=None, textbook=self.textbook, textbook_page=5, number="5", instructions="", wording="", example="", clue="")
        self.assertEqual(cm.exception.orig.diag.column_name, "project_id")

    # def test_create_with_inconsistent_project(self):
    #     other_project = self.create_model(Project, title="Other project")
    #     # Implemented using a "fat" foreign key added outside Django's ORM, in 'migrations/0003_initial_patch.py'
    #     with self.assertRaises(sql.exc.IntegrityError) as cm:
    #         self.create_model(Exercise, project=other_project, textbook=self.textbook, textbook_page=5, number="5", instructions="", wording="", example="", clue="")
    #     self.assertEqual(cm.exception.orig.diag.constraint_name, "")

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
    #     self.assertEqual(
    #         [
    #             (bool(exercise.textbook), exercise.textbook_page, exercise.number)
    #             for exercise in Exercise.objects.order_by("textbook_page", "number")
    #         ],
    #         [
    #             (True, 1, "1"),
    #             (True, 1, "2"),
    #             (True, 1, "03"),
    #             (True, 1, "10"),
    #             (True, 1, "Alice"),
    #             (True, 1, "Bob"),
    #             (True, 5, "2"),
    #             (True, 5, "5.a"),
    #             (True, 5, "5.b"),
    #             (True, 5, "12"),
    #             (True, 5, "A1"),
    #             (True, 5, "A12"),
    #             (False, None, "4"),
    #             (False, None, "Other text"),
    #             (False, None, "Some other text"),
    #             (False, None, "Some text"),
    #         ],
    #     )

#     def test_share_adaptation(self):
#         project = self.create_model(Project, title="Project", description="")
#         exercise_1 = self.create_model(Exercise, project=project, number="Exercise 1", instructions="", wording="", example="", clue="")
#         exercise_2 = self.create_model(Exercise, project=project, number="Exercise 2", instructions="", wording="", example="", clue="")
#         adaptation = self.create_model(GenericAdaptation)

#         exercise_1.adaptation = adaptation
#         self.session.commit()

#         exercise_2.adaptation = adaptation
#         with self.assertRaises(sql.exc.IntegrityError) as cm:
#             self.session.commit()
#         self.assertEqual(cm.exception.orig.diag.constraint_name, "")

#         # self.assertIs(exercise_1.adaptation, exercise_2.adaptation)


class ExercisesResource:
    singular_name = "exercise"
    plural_name = "exercises"

    Model = api_models.Exercise

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    ItemCreator = make_item_creator(
        Exercise,
        preprocess=lambda bounding_rectangle, **kwargs: {
            "bounding_rectangle": None if bounding_rectangle is None else bounding_rectangle.model_dump(),
            **kwargs,
        },
    )

    ItemGetter = make_item_getter(Exercise, sqids=sqids)

    PageGetter = make_page_getter(
        Exercise,
        default_sort=["textbook_id", "textbook_page", "number"],
        filter_functions={
            "textbook_page": lambda q, textbook_page: q.where(Exercise.textbook_page == textbook_page),
            "textbook": lambda q, textbook: q.where(Exercise.textbook_id == TextbooksResource.sqids.decode(textbook)[0]),
            "number": lambda q, number: q.where(Exercise.number == number),
        },
    )

    class ItemSaver(SessionDependent):
        @contextmanager
        def __call__(self, item):
            previous_adaptation = item.adaptation
            previous_bounding_rectangle = item.bounding_rectangle
            yield
            if item.bounding_rectangle is not previous_bounding_rectangle and item.bounding_rectangle is not None:
                item.bounding_rectangle = item.bounding_rectangle.model_dump()
            if previous_adaptation is not None and unwrap(item.adaptation) != unwrap(previous_adaptation):
                self.session.delete(previous_adaptation)

    ItemDeleter = make_item_deleter()


set_wrapper(Exercise, orm_wrapper_with_sqids(ExercisesResource.sqids))


class ExtractionEvent(OrmBase):
    __tablename__ = "extraction_events"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    exercise_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Exercise.id))
    exercise: orm.Mapped[Exercise] = orm.relationship(back_populates="extraction_events")

    event: orm.Mapped[str]


class ExtractionEventsResource:
    singular_name = "extraction_event"
    plural_name = "extraction_events"

    Model = api_models.ExtractionEvent

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    ItemCreator = make_item_creator(ExtractionEvent)

    ItemGetter = make_item_getter(ExtractionEvent, sqids=sqids)

    PageGetter = make_page_getter(ExtractionEvent)

    ItemSaver = make_item_saver()

    ItemDeleter = make_item_deleter()


set_wrapper(ExtractionEvent, orm_wrapper_with_sqids(ExtractionEventsResource.sqids))
