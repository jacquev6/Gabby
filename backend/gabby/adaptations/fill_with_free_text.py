from typing import Literal
import os

from .. import exercise_delta as d
from .. import parsing
from .. import renderable as r
from .testing import AdaptationTestCase
from mydantic import PydanticBase

if os.environ.get("GABBY_UNITTESTING", "false") == "true":
    from .. import exercises


class FillWithFreeTextAdaptation(PydanticBase):
    kind: Literal["fill-with-free-text"]

    placeholder: str

    def make_effects(self):
        return [parsing.FillWithFreeText(placeholder=self.placeholder)]


class FillWithFreeTextAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="The wording of this ... is a ... sentence.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=FillWithFreeTextAdaptation(kind="fill-with-free-text", placeholder="..."),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="wording"),
                            r.Whitespace(),
                            r.PlainText(text="of"),
                            r.Whitespace(),
                            r.PlainText(text="this"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="sentence"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The wording of this ... is a ... sentence.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_start_and_end_with_placeholder(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="@ a @",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=FillWithFreeTextAdaptation(kind="fill-with-free-text", placeholder="@"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="@ a @", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_multiple_lines_in_instructions(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions\nare\n\non\n\nmultiple\nlines",
            wording="wording",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=FillWithFreeTextAdaptation(kind="fill-with-free-text", placeholder="..."),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                            r.Whitespace(),
                            r.PlainText(text="are"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="on"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="multiple"),
                            r.Whitespace(),
                            r.PlainText(text="lines"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="wording"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_multiple_lines_in_wording(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="foo toto : ...\n\nbar : ...\n\nbaz : ...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=FillWithFreeTextAdaptation(kind="fill-with-free-text", placeholder="..."),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="foo"),
                            r.Whitespace(),
                            r.PlainText(text="toto"),
                            r.Whitespace(),
                            r.PlainText(text=":"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="bar"),
                            r.Whitespace(),
                            r.PlainText(text=":"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="baz"),
                            r.Whitespace(),
                            r.PlainText(text=":"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="foo toto : ...\n\nbar : ...\n\nbaz : ...", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_unknown_tags(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="{tag|abc}",
            wording="{tag|def}",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=FillWithFreeTextAdaptation(kind="fill-with-free-text", placeholder="..."),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{"),
                            r.PlainText(text="tag"),
                            r.PlainText(text="|"),
                            r.PlainText(text="abc"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{"),
                            r.PlainText(text="tag"),
                            r.PlainText(text="|"),
                            r.PlainText(text="def"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="{tag|abc}", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="{tag|def}", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_strip_whitespace(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="   abc   ",
            wording="   def   ",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=FillWithFreeTextAdaptation(kind="fill-with-free-text", placeholder="..."),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="abc"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="def"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="   abc   ", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="   def   ", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_example_and_clue(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="This @ is the wording.",
            example="This @ is the example.",
            clue="This @ is the clue.",
            wording_paragraphs_per_pagelet=3,
            adaptation=FillWithFreeTextAdaptation(kind="fill-with-free-text", placeholder="@"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="wording"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="@"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
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
                            r.PlainText(text="@"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
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
                    d.TextInsertOp(insert="instructions", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This @ is the wording.", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="This @ is the example.", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="This @ is the clue.", attributes={}),
                ],
            ),
        )
