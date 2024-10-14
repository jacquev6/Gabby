from typing import Literal
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


class SelectThingsAdaptation(PydanticBase):
    kind: Literal["select-things"]

    colors: list[str]
    words: bool
    punctuation: bool

    @property
    def _color_indexes(self):
        return range(1, len(self.colors) + 1)

    def _make_tags(self):
        return {f"sel{color_index}": r""" "|" STR """ for color_index in self._color_indexes}

    def _make_adapter_type(self):
        return type("InstructionsAdapter", (parsing.InstructionsSectionAdapter,), {
            f"sel{color_index}_tag": (lambda color_index: staticmethod(lambda args: renderable.SelectedText(text=args[0], color=self.colors[color_index - 1])))(color_index)
            for color_index in self._color_indexes
        })

    def _adapt_instructions(self, section):
        return parsing.InstructionsSectionParser(
            self._make_tags(),
            self._make_adapter_type()(),
        )(
            section,
        )

    def make_adapted_instructions(self, exercise):
        return self._adapt_instructions(exercise.instructions)

    class WordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, words, punctuation, colors):
            self.select_words = words
            self.select_punctuation = punctuation
            self.colors = colors

        def WORD(self, arg):
            if self.select_words:
                return renderable.SelectableText(text=arg.value, colors=self.colors, boxed=False)
            else:
                return renderable.PlainText(text=arg.value)

        def PUNCTUATION_IN_SENTENCE(self, arg):
            if self.select_punctuation:
                return renderable.SelectableText(text=arg.value, colors=self.colors, boxed=False)
            else:
                return renderable.PlainText(text=arg.value)

        PUNCTUATION_AT_END_OF_SENTENCE = PUNCTUATION_IN_SENTENCE
        PUNCTUATION_IN_LENIENT_PARAGRAPH = PUNCTUATION_IN_SENTENCE

    def make_adapted_wording(self, exercise):
        return parsing.parse_wording_section(
            {},
            self.WordingAdapter(self.words, self.punctuation, self.colors),
            exercise.wording,
        )

    def make_adapted_example(self, exercise):
        return self._adapt_instructions(exercise.example)

    def make_adapted_clue(self, exercise):
        return self._adapt_instructions(exercise.clue)

    def _make_delta_maker_type(self):
        return type("InstructionsDeltaMaker", (parsing.InstructionsSectionDeltaMaker,), {
            f"sel{color_index}_tag": (lambda color: staticmethod(lambda args: exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": color})))(color_index)
            for color_index in self._color_indexes
        })

    def _make_instructions_delta(self, section):
        return parsing.InstructionsSectionParser(
            self._make_tags(),
            self._make_delta_maker_type()(),
        )(
            section,
        )

    def make_instructions_delta(self, exercise):
        return self._make_instructions_delta(exercise.instructions)

    def make_wording_delta(self, exercise):
        return parsing.make_plain_wording_section_delta(exercise.wording)

    def make_example_delta(self, exercise):
        return self._make_instructions_delta(exercise.example)

    def make_clue_delta(self, exercise):
        return self._make_instructions_delta(exercise.clue)


class SelectThingsAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="The wording of this exercise is a single sentence.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=SelectThingsAdaptation(kind="select-things", colors=["red", "blue"], words=True, punctuation=False),
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
                    d.TextInsertOp(insert="instructions", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The wording of this exercise is a single sentence.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_sel_tags(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=None,
            instructions="{sel1|abc} {sel2|def} {sel3|ghi} {sel4|jkl}",
            wording="wording",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=SelectThingsAdaptation(kind="select-things", colors=["red", "green", "blue"], words=True, punctuation=False),
        )

        self.do_test(
            exercise,
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
                    d.TextInsertOp(insert="abc", attributes={"sel": 1}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="def", attributes={"sel": 2}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="ghi", attributes={"sel": 3}),
                    d.TextInsertOp(insert=" {sel4|jkl}", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_single_color(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=None,
            instructions="{sel1|abc}",
            wording="wording",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=SelectThingsAdaptation(kind="select-things", colors=["red"], words=True, punctuation=False),
        )

        self.do_test(
            exercise,
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
                    d.TextInsertOp(insert="abc", attributes={"sel": 1}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording", attributes={}),
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
            adaptation=SelectThingsAdaptation(kind="select-things", colors=["red"], words=True, punctuation=False),
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
            wording="wording is\n\non\n\nmultiple lines",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=SelectThingsAdaptation(kind="select-things", colors=["red"], words=True, punctuation=False),
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
                    d.TextInsertOp(insert="instructions", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording is\n\non\n\nmultiple lines", attributes={}),
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
            adaptation=SelectThingsAdaptation(kind="select-things", colors=["red"], words=True, punctuation=False),
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
            adaptation=SelectThingsAdaptation(kind="select-things", colors=["red"], words=True, punctuation=False),
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
            textbook_page=None,
            instructions="instructions",
            wording="wording",
            example="This is the example.",
            clue="This is the clue.",
            wording_paragraphs_per_pagelet=3,
            adaptation=SelectThingsAdaptation(kind="select-things", colors=["red"], words=True, punctuation=False),
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
                    d.TextInsertOp(insert="instructions", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="This is the example.", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="This is the clue.", attributes={}),
                ],
            ),
        )

    def test_example_and_clue_with_sel_tags(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="wording",
            example="{sel1|abc} {sel2|def}",
            clue="{sel3|ghi} {sel4|jkl}",
            wording_paragraphs_per_pagelet=3,
            adaptation=SelectThingsAdaptation(kind="select-things", colors=["red", "green", "blue"], words=True, punctuation=False),
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
                    d.TextInsertOp(insert="instructions", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="abc", attributes={"sel": 1}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="def", attributes={"sel": 2}),
                ],
                clue=[
                    d.TextInsertOp(insert="ghi", attributes={"sel": 3}),
                    d.TextInsertOp(insert=" {sel4|jkl}", attributes={}),
                ],
            ),
        )
