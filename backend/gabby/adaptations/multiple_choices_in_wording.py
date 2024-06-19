from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import parsing
from .. import renderable
from .. import renderable as r
from .. import settings
from ..api_utils import make_item_creator, make_item_deleter, make_item_getter, make_item_saver
from ..exercises import Adaptation, Exercise
from ..testing import AdaptationTestCase
from ..wrapping import set_wrapper, make_sqids, orm_wrapper_with_sqids
from .cleanup import delete_previous_adaptation


class MultipleChoicesInWordingAdaptation(Adaptation):
    __tablename__ = "adaptations__mciw"
    __mapper_args__ = {
        "polymorphic_identity": "mciw",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)

    def make_adapted_instructions(self):
        return parsing.parse_plain_section(self.exercise.instructions)

    class WordingAdapter(parsing.SectionTransformer):
        def choices_tag(self, args):
            return renderable.MultipleChoicesInput(choices=[arg.value for arg in args])

    adapt_wording = parsing.SectionParser({"choices": r""" ("|" STR)+ """}, WordingAdapter())

    def make_adapted_wording(self):
        return self.adapt_wording(self.exercise.wording)

    def make_adapted_example(self):
        return parsing.parse_plain_section(self.exercise.example)

    def make_adapted_clue(self):
        return parsing.parse_plain_section(self.exercise.clue)


class MultipleChoicesInWordingAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices|a|b|c} B {choices|d|e}.",
            example="",
            clue="",
        )
        adaptation = MultipleChoicesInWordingAdaptation(exercise=exercise)

        self.do_test(
            adaptation,
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["d", "e"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
            ),
        )

    def test_example_and_clue(self):
        pass  # @todo Implement this test


class MultipleChoicesInWordingAdaptationsResource:
    singular_name = "multiple_choices_in_wording_adaptation"
    plural_name = "multiple_choices_in_wording_adaptations"

    Model = api_models.MultipleChoicesInWordingAdaptation

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    ItemCreator = make_item_creator(MultipleChoicesInWordingAdaptation, preprocess=delete_previous_adaptation)

    ItemGetter = make_item_getter(MultipleChoicesInWordingAdaptation, sqids=sqids)

    ItemSaver = make_item_saver()

    ItemDeleter = make_item_deleter()


set_wrapper(MultipleChoicesInWordingAdaptation, orm_wrapper_with_sqids(MultipleChoicesInWordingAdaptationsResource.sqids))
