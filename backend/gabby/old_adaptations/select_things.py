from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import exercise_delta as d
from .. import renderable as r
from ..exercises import Exercise
from ..testing import AdaptationTestCase
from .base import OldAdaptation


class SelectThingsAdaptation(OldAdaptation):
    def __init__(self, exercise: Exercise, colors, words, punctuation):
        super().__init__(exercise)
        self.colors = colors
        self.words = words
        self.punctuation = punctuation

    def to_new_adaptation(self):
        return api_models.SelectThingsAdaptation(
            kind="select-things",
            punctuation=self.punctuation,
            words=self.words,
            colors=self.colors,
        )


class SelectThingsAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="The wording of this exercise is a single sentence.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red", "blue"], words=True, punctuation=False)

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
                            r.SelectableText(text="The", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="wording", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="of", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="this", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="exercise", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="a", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="single", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="sentence", colors=["red", "blue"], boxed=False),
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
                    d.InsertOp(insert="The wording of this exercise is a single sentence."),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_sel_tags(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="{sel1|abc} {sel2|def} {sel3|ghi} {sel4|jkl}",
            wording="wording",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red", "green", "blue"], words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color="red"),
                            r.Whitespace(),
                            r.SelectedText(text="def", color="green"),
                            r.Whitespace(),
                            r.SelectedText(text="ghi", color="blue"),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="sel4"),
                            r.PlainText(text="|"),
                            r.PlainText(text="jkl"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red", "green", "blue"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="abc", attributes={"sel": 1}),
                    d.InsertOp(insert=" "),
                    d.InsertOp(insert="def", attributes={"sel": 2}),
                    d.InsertOp(insert=" "),
                    d.InsertOp(insert="ghi", attributes={"sel": 3}),
                    d.InsertOp(insert=" {sel4|jkl}"),
                ],
                wording=[
                    d.InsertOp(insert="wording"),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_single_color(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="{sel1|abc}",
            wording="wording",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red"], words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color="red"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="abc", attributes={"sel": 1}),
                ],
                wording=[
                    d.InsertOp(insert="wording"),
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
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red"], words=True, punctuation=False)

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
                            r.SelectableText(text="wording", colors=["red"], boxed=False),
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
            wording="wording is\n\non\n\nmultiple lines",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red"], words=True, punctuation=False)

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
                            r.SelectableText(text="wording", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=["red"], boxed=False),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="on", colors=["red"], boxed=False),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="multiple", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="lines", colors=["red"], boxed=False),
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
                    d.InsertOp(insert="wording is\n\non\n\nmultiple lines"),
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
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red"], words=True, punctuation=False)

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
                            r.SelectableText(text="tag", colors=["red"], boxed=False),
                            r.PlainText(text="|"),
                            r.SelectableText(text="def", colors=["red"], boxed=False),
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
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red"], words=True, punctuation=False)

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
                            r.SelectableText(text="def", colors=["red"], boxed=False),
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
            textbook_page=None,
            instructions="instructions",
            wording="wording",
            example="This is the example.",
            clue="This is the clue.",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red"], words=True, punctuation=False)

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
                            r.SelectableText(text="wording", colors=["red"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
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
                    d.InsertOp(insert="wording"),
                ],
                example=[
                    d.InsertOp(insert="This is the example."),
                ],
                clue=[
                    d.InsertOp(insert="This is the clue."),
                ],
            ),
        )

    def test_example_and_clue_with_sel_tags(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="wording",
            example="{sel1|abc} {sel2|def}",
            clue="{sel3|ghi} {sel4|jkl}",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red", "green", "blue"], words=True, punctuation=False)

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
                            r.SelectableText(text="wording", colors=["red", "green", "blue"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color="red"),
                            r.Whitespace(),
                            r.SelectedText(text="def", color="green"),
                        ]),
                    ]),
                ]),
                clue=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="ghi", color="blue"),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="sel4"),
                            r.PlainText(text="|"),
                            r.PlainText(text="jkl"),
                            r.PlainText(text="}"),
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
                    d.InsertOp(insert="wording"),
                ],
                example=[
                    d.InsertOp(insert="abc", attributes={"sel": 1}),
                    d.InsertOp(insert=" "),
                    d.InsertOp(insert="def", attributes={"sel": 2}),
                ],
                clue=[
                    d.InsertOp(insert="ghi", attributes={"sel": 3}),
                    d.InsertOp(insert=" {sel4|jkl}"),
                ],
            ),
        )
