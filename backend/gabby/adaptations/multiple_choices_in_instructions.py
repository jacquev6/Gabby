from typing import ClassVar, Literal
import itertools
import os

from .. import exercise_delta
from .. import exercise_delta as d
from .. import parsing
from .. import renderable
from .. import renderable as r
from .testing import AdaptationTestCase
from mydantic import PydanticBase

if os.environ.get("GABBY_UNITTESTING", "false") == "true":
    from .. import exercises


class MultipleChoicesInInstructionsAdaptation(PydanticBase):
    kind: Literal["multiple-choices-in-instructions"]

    placeholder: str

    class InstructionsAdapter(parsing.InstructionsSectionAdapter):
        def choice_tag(self, args):
            assert len(args) == 1
            return renderable.BoxedText(text=args[0])

    instructions_tags: ClassVar = {"choice": r""" "|" STR """}

    adapt_instructions: ClassVar = parsing.InstructionsSectionParser(instructions_tags, InstructionsAdapter())

    def make_adapted_instructions(self, exercise):
        return self.adapt_instructions(exercise.instructions)

    class InstructionsDeltaMaker(parsing.InstructionsSectionDeltaMaker):
        def choice_tag(self, args):
            return exercise_delta.InsertOp(insert=args[0], attributes={"choice": True})

    make_instructions_delta_: ClassVar = parsing.InstructionsSectionParser(instructions_tags, InstructionsDeltaMaker())

    def make_instructions_delta(self, exercise):
        return self.make_instructions_delta_(exercise.instructions)

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

    gather_choices: ClassVar = parsing.InstructionsSectionParser(instructions_tags, ChoicesGatherer())

    class WordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, choices):
            self.choices = choices

        def placeholder_tag(self, args):
            return renderable.MultipleChoicesInput(choices=self.choices)

    def make_adapted_wording(self, exercise):
        choices = self.gather_choices(exercise.instructions)
        return parsing.parse_wording_section(
            {"placeholder": ""},
            self.WordingAdapter(choices),
            exercise.wording.replace(self.placeholder, "{placeholder}")
        )

    def make_wording_delta(self, exercise):
        return parsing.make_plain_wording_section_delta(exercise.wording)

    def make_adapted_example(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.example)

    def make_example_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.example)

    def make_adapted_clue(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.clue)

    def make_clue_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.clue)


class MultipleChoicesInInstructionsAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose {choice|a} or {choice|b}.",
            wording="A ... B ...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInInstructionsAdaptation(kind="multiple-choices-in-instructions", placeholder="..."),
        )

        self.do_test(
            exercise,
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
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose {choice|a} or {choice|b}.",
            wording="A @ B @",
            example="This {choice|is} the @ example.",
            clue="This is {choice|the} @ clue.",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInInstructionsAdaptation(kind="multiple-choices-in-instructions", placeholder="@"),
        )

        self.do_test(
            exercise,
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
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="{choice|a} # {choice|b}\n\n c #\nd.",
            wording="...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInInstructionsAdaptation(kind="multiple-choices-in-instructions", placeholder="..."),
        )

        self.do_test(
            exercise,
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
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions=" \t  Choose  \t\n  {choice|a}.   Or {choice|b} .   \t\n   ",
            wording="...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInInstructionsAdaptation(kind="multiple-choices-in-instructions", placeholder="..."),
        )

        self.do_test(
            exercise,
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
