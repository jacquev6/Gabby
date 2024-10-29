from typing import Literal
import os

from .. import exercise_delta as d
from .. import parsing
from .. import renderable as r
from .testing import AdaptationTestCase
from mydantic import PydanticBase

if os.environ.get("GABBY_UNITTESTING", "false") == "true":
    from .. import exercises


class MultipleChoicesInInstructionsAdaptation(PydanticBase):
    kind: Literal["multiple-choices-in-instructions"]

    placeholder: str

    def make_effects(self):
        return [parsing.MultipleChoicesInInstructionsAdaptationEffect(
            kind="multiple-choices-in-instructions",
            placeholder=self.placeholder,
        )]


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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="a", attributes={"choice": True}),
                    d.TextInsertOp(insert=" or ", attributes={}),
                    d.TextInsertOp(insert="b", attributes={"choice": True}),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...", attributes={}),
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="a", attributes={"choice": True}),
                    d.TextInsertOp(insert=" or ", attributes={}),
                    d.TextInsertOp(insert="b", attributes={"choice": True}),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A @ B @", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="This {choice|is} the @ example.", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="This is {choice|the} @ clue.", attributes={}),
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
                    d.TextInsertOp(insert="a", attributes={"choice": True}),
                    d.TextInsertOp(insert=" # ", attributes={}),
                    d.TextInsertOp(insert="b", attributes={"choice": True}),
                    d.TextInsertOp(insert="\n\n c #\nd.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="...", attributes={}),
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
                    d.TextInsertOp(insert=" \t  Choose  \t\n  ", attributes={}),
                    d.TextInsertOp(insert="a", attributes={"choice": True}),
                    d.TextInsertOp(insert=".   Or ", attributes={}),
                    d.TextInsertOp(insert="b", attributes={"choice": True}),
                    d.TextInsertOp(insert=" .   \t\n   ", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="...", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )
