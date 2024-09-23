from contextlib import contextmanager
import itertools

from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import exercise_delta
from .. import exercise_delta as d
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
            assert len(args) == 1
            return renderable.BoxedText(text=args[0])

    instructions_tags = {"choice": r""" "|" STR """}

    adapt_instructions = parsing.InstructionsSectionParser(instructions_tags, InstructionsAdapter())

    def make_adapted_instructions(self):
        return self.adapt_instructions(self.exercise.instructions)

    class InstructionsDeltaMaker(parsing.InstructionsSectionDeltaMaker):
        def choice_tag(self, args):
            return exercise_delta.InsertOp(insert=args[0], attributes={"choice": True})

    make_instructions_delta_ = parsing.InstructionsSectionParser(instructions_tags, InstructionsDeltaMaker())

    def make_instructions_delta(self):
        return self.make_instructions_delta_(self.exercise.instructions)

    class ChoicesGatherer(parsing.Transformer):
        def section(self, args):
            return list(itertools.chain(*args))

        def strict_paragraph(self, args):
            return list(itertools.chain(*args))

        def sentence(self, args):
            return list(itertools.chain(*args))

        def lenient_paragraph(self, args):
            return list(itertools.chain(*args))

        def choice_tag(self, args):
            assert len(args) == 1
            return [args[0]]

        def WORD(self, arg):
            return []

        def LEADING_WHITESPACE(self, arg):
            return []

        def TRAILING_WHITESPACE(self, arg):
            return []

        def PARAGRAPH_SEPARATOR(self, arg):
            return []

        def SENTENCE_SEPARATOR(self, arg):
            return []

        def WHITESPACE_IN_SENTENCE(self, arg):
            return []

        def PUNCTUATION_IN_SENTENCE(self, arg):
            return []

        def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
            return []

        def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
            return []

        def INT(self, arg):
            return None

        def STR(self, arg):
            return arg.value

        def bold_tag(self, args):
            return []

        def italic_tag(self, args):
            return []

    gather_choices = parsing.InstructionsSectionParser(instructions_tags, ChoicesGatherer())

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

    def make_wording_delta(self):
        return parsing.make_plain_wording_section_delta(self.exercise.wording)

    def make_adapted_example(self):
        return parsing.adapt_plain_instructions_section(self.exercise.example)

    def make_example_delta(self):
        return parsing.make_plain_instructions_section_delta(self.exercise.example)

    def make_adapted_clue(self):
        return parsing.adapt_plain_instructions_section(self.exercise.clue)

    def make_clue_delta(self):
        return parsing.make_plain_instructions_section_delta(self.exercise.clue)


class MultipleChoicesInInstructionsAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose {choice|a} or {choice|b}.",
            wording="A ... B ...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
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
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="Choose "),
                    d.InsertOp(insert="a", attributes={"choice": True}),
                    d.InsertOp(insert=" or "),
                    d.InsertOp(insert="b", attributes={"choice": True}),
                    d.InsertOp(insert="."),
                ],
                wording=[
                    d.InsertOp(insert="A ... B ..."),
                ],
                example=[],
                clue=[],
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
            wording_paragraphs_per_pagelet=3,
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
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="Choose "),
                    d.InsertOp(insert="a", attributes={"choice": True}),
                    d.InsertOp(insert=" or "),
                    d.InsertOp(insert="b", attributes={"choice": True}),
                    d.InsertOp(insert="."),
                ],
                wording=[
                    d.InsertOp(insert="A @ B @"),
                ],
                example=[
                    d.InsertOp(insert="This {choice|is} the @ example."),
                ],
                clue=[
                    d.InsertOp(insert="This is {choice|the} @ clue."),
                ],
            ),
        )

    def test_lenient_paragraphs(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="{choice|a} # {choice|b}\n\n c #\nd.",
            wording="...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
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
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="#"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="c"),
                            r.Whitespace(),
                            r.PlainText(text="#"),
                            r.Whitespace(),
                            r.PlainText(text="d"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="a", attributes={"choice": True}),
                    d.InsertOp(insert=" # "),
                    d.InsertOp(insert="b", attributes={"choice": True}),
                    d.InsertOp(insert="\n\n c #\nd."),
                ],
                wording=[
                    d.InsertOp(insert="..."),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_whitespace(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions=" \t  Choose  \t\n  {choice|a}.   Or {choice|b} .   \t\n   ",
            wording="...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
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
                            r.PlainText(text="."),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.Whitespace(),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert=" \t  Choose  \t\n  "),
                    d.InsertOp(insert="a", attributes={"choice": True}),
                    d.InsertOp(insert=".   Or "),
                    d.InsertOp(insert="b", attributes={"choice": True}),
                    d.InsertOp(insert=" .   \t\n   "),
                ],
                wording=[
                    d.InsertOp(insert="..."),
                ],
                example=[],
                clue=[],
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
