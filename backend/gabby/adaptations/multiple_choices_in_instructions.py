from contextlib import contextmanager

import itertools
from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import parsing
from .. import renderable
from .. import renderable as r
from .. import settings
from ..api_utils import create_item, get_item, save_item, delete_item
from ..database_utils import SessionDependable
from ..exercises import Adaptation
from ..exercises import Adaptation, Exercise
from ..testing import AdaptationTestCase
from ..users import MandatoryAuthBearerDependable
from ..wrapping import set_wrapper, make_sqids, orm_wrapper_with_sqids


class MultipleChoicesInInstructionsAdaptation(Adaptation):
    __tablename__ = "adaptations__mcii"
    __mapper_args__ = {
        "polymorphic_identity": "mcii",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)

    placeholder: orm.Mapped[str]

    class InstructionsAdapter(parsing.InstructionsSectionAdapter):
        def choice_tag(self, args):
            return renderable.BoxedText(text=args[0])

    adapt_instructions = parsing.InstructionsSectionParser({"choice": r""" "|" STR """}, InstructionsAdapter())

    def make_adapted_instructions(self):
        return self.adapt_instructions(self.exercise.instructions)

    class ChoicesGatherer(parsing.InstructionsSectionAdapter):
        def section(self, choices):
            return list(itertools.chain.from_iterable(choices))

        def paragraph(self, choices):
            return list(itertools.chain.from_iterable(choices))

        def strict_paragraph(self, choices):
            return list(itertools.chain.from_iterable(choices))

        def strict_sentence(self, choices):
            return list(itertools.chain.from_iterable(choices))

        def in_sentence_punctuation(self, args):
            return []

        def end_of_sentence_punctuation(self, args):
            return []

        def lenient_paragraph(self, choices):
            return list(itertools.chain.from_iterable(choices))

        def word(self, args):
            return []

        def whitespace(self, args):
            return []

        def punctuation(self, args):
            return []

        def choice_tag(self, args):
            return [args[0].value]

    gather_choices = parsing.InstructionsSectionParser({"choice": r""" "|" STR """}, ChoicesGatherer())

    class WordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, choices):
            self.choices = choices

        def placeholder_tag(self, args):
            return renderable.MultipleChoicesInput(choices=self.choices)

    def make_adapted_wording(self):
        choices = self.gather_choices(self.exercise.instructions)
        return parsing.parse_wording_section(
            {"placeholder": ""},
            self.WordingAdapter(choices),
            self.exercise.wording.replace(self.placeholder, "{placeholder}")
        )

    def make_adapted_example(self):
        return parsing.adapt_plain_instructions_section(self.exercise.example)

    def make_adapted_clue(self):
        return parsing.adapt_plain_instructions_section(self.exercise.clue)


class MultipleChoicesInInstructionsAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose {choice|a} or {choice|b}.",
            wording="A ... B ...",
            example="",
            clue="",
        )
        adaptation = MultipleChoicesInInstructionsAdaptation(exercise=exercise, placeholder="...")

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
            ),
        )

    def test_example_and_clue(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose {choice|a} or {choice|b}.",
            wording="A @ B @",
            example="This {choice|is} the @ example.",
            clue="This is {choice|the} @ clue.",
        )
        adaptation = MultipleChoicesInInstructionsAdaptation(exercise=exercise, placeholder="@")

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="choice"),
                            r.PlainText(text="|"),
                            r.PlainText(text="is"),
                            r.PlainText(text="}"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="@"),
                            r.Whitespace(),
                            r.PlainText(text="example"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                clue=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="choice"),
                            r.PlainText(text="|"),
                            r.PlainText(text="the"),
                            r.PlainText(text="}"),
                            r.Whitespace(),
                            r.PlainText(text="@"),
                            r.Whitespace(),
                            r.PlainText(text="clue"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
            ),
        )


class MultipleChoicesInInstructionsAdaptationsResource:
    singular_name = "multiple_choices_in_instructions_adaptation"
    plural_name = "multiple_choices_in_instructions_adaptations"

    Model = api_models.MultipleChoicesInInstructionsAdaptation

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    def create_item(
        self,
        exercise,
        placeholder,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        if exercise.adaptation is not None:
            session.delete(exercise.adaptation)
        return create_item(
            session, MultipleChoicesInInstructionsAdaptation,
            exercise=exercise,
            placeholder=placeholder,
            created_by=authenticated_user,
            updated_by=authenticated_user,
        )

    def get_item(
        self,
        id,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        return get_item(session, MultipleChoicesInInstructionsAdaptation, MultipleChoicesInInstructionsAdaptationsResource.sqids.decode(id)[0])

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


set_wrapper(MultipleChoicesInInstructionsAdaptation, orm_wrapper_with_sqids(MultipleChoicesInInstructionsAdaptationsResource.sqids))
