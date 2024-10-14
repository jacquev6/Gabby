from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import exercise_delta as d
from .. import renderable as r
from ..exercises import Exercise
from ..testing import AdaptationTestCase
from .base import OldAdaptation


class FillWithFreeTextAdaptation(OldAdaptation):
    def __init__(self, exercise: Exercise, placeholder: str):
        super().__init__(exercise)
        self.placeholder = placeholder

    def to_new_adaptation(self):
        return api_models.FillWithFreeTextAdaptation(
            kind="fill-with-free-text",
            placeholder=self.placeholder,
        )


class FillWithFreeTextAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="The wording of this ... is a ... sentence.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.do_test(
            adaptation,
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
                    d.InsertOp(insert="instructions"),
                ],
                wording=[
                    d.InsertOp(insert="The wording of this ... is a ... sentence."),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_start_and_end_with_placeholder(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="@ a @",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="@")

        self.do_test(
            adaptation,
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
                    d.InsertOp(insert="instructions"),
                ],
                wording=[
                    d.InsertOp(insert="@ a @"),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_multiple_lines_in_instructions(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions\nare\n\non\n\nmultiple\nlines",
            wording="wording",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.do_test(
            adaptation,
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
                    d.InsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines"),
                ],
                wording=[
                    d.InsertOp(insert="wording"),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_multiple_lines_in_wording(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="foo toto : ...\n\nbar : ...\n\nbaz : ...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.do_test(
            adaptation,
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
                    d.InsertOp(insert="instructions"),
                ],
                wording=[
                    d.InsertOp(insert="foo toto : ...\n\nbar : ...\n\nbaz : ..."),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_unknown_tags(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="{tag|abc}",
            wording="{tag|def}",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.do_test(
            adaptation,
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
                    d.InsertOp(insert="{tag|abc}"),
                ],
                wording=[
                    d.InsertOp(insert="{tag|def}"),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_strip_whitespace(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="   abc   ",
            wording="   def   ",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.do_test(
            adaptation,
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
                    d.InsertOp(insert="   abc   "),
                ],
                wording=[
                    d.InsertOp(insert="   def   "),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_example_and_clue(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="This @ is the wording.",
            example="This @ is the example.",
            clue="This @ is the clue.",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="@")

        self.do_test(
            adaptation,
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
                    d.InsertOp(insert="instructions"),
                ],
                wording=[
                    d.InsertOp(insert="This @ is the wording."),
                ],
                example=[
                    d.InsertOp(insert="This @ is the example."),
                ],
                clue=[
                    d.InsertOp(insert="This @ is the clue."),
                ],
            ),
        )
