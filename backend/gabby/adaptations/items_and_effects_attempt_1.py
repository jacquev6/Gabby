from typing import ClassVar, Literal
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


class ItemsAndEffectsAttempt1Adaptation(PydanticBase):
    kind: Literal["items-and-effects-attempt-1"]

    class WordsItems(PydanticBase):
        kind: Literal["words"]
        punctuation: bool

    class SentencesItems(PydanticBase):
        kind: Literal["sentences"]

    class ManualItems(PydanticBase):
        kind: Literal["manual"]

    Items: ClassVar = WordsItems | SentencesItems | ManualItems

    items: Items

    class Effects(PydanticBase):
        class Selectable(PydanticBase):
            colors: list[str]

        selectable: Selectable | None
        boxed: bool

    effects: Effects

    @property
    def _color_indexes(self):
        if self.effects.selectable is None:
            return []
        else:
            return range(1, len(self.effects.selectable.colors) + 1)

    def _make_instructions_tags(self):
        tags = {}
        if self.effects.selectable is not None:
            tags.update({f"sel{color_index}": r""" "|" STR """ for color_index in self._color_indexes})
        return tags

    def _make_instructions_adapter_type(self):
        tag_functions = {}
        if self.effects.selectable is not None:
            colors = self.effects.selectable.colors
            tag_functions.update({
                f"sel{color_index}_tag": (lambda color: staticmethod(lambda args: renderable.SelectedText(text=args[0], color=color)))(colors[color_index - 1])
                for color_index in self._color_indexes
            })
        return type("InstructionsAdapter", (parsing.InstructionsSectionAdapter,), tag_functions)

    def _adapt_instructions(self, section):
        return parsing.InstructionsSectionParser(
            self._make_instructions_tags(),
            self._make_instructions_adapter_type()(),
        )(
            section,
        )

    def make_adapted_instructions(self, exercise):
        return self._adapt_instructions(exercise.instructions)

    class WordsItemsWordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, punctuation, colors, boxed):
            self.select_punctuation = punctuation
            self.colors = colors
            self.boxed = boxed

        def WORD(self, arg):
            return renderable.SelectableText(text=arg.value, colors=self.colors, boxed=self.boxed)

        def PUNCTUATION_IN_SENTENCE(self, arg):
            if self.select_punctuation:
                return renderable.SelectableText(text=arg.value, colors=self.colors, boxed=self.boxed)
            else:
                return renderable.PlainText(text=arg.value)

        PUNCTUATION_AT_END_OF_SENTENCE = PUNCTUATION_IN_SENTENCE
        PUNCTUATION_IN_LENIENT_PARAGRAPH = PUNCTUATION_IN_SENTENCE

    class ManualItemsWordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, colors, boxed):
            self.colors = colors
            self.boxed = boxed

        def selectable_tag(self, args):
            assert len(args) == 1
            return renderable.SelectableText(text=args[0], colors=self.colors, boxed=self.boxed)

    def make_adapted_wording(self, exercise):
        if self.effects.selectable is None:
            return parsing.adapt_plain_wording_section(exercise.wording)
        else:
            if self.items.kind == "words":
                return parsing.parse_wording_section(
                    {},
                    self.WordsItemsWordingAdapter(self.items.punctuation, self.effects.selectable.colors, self.effects.boxed),
                    exercise.wording,
                )
            elif self.items.kind == "manual":
                return parsing.parse_wording_section(
                    {"selectable": r""" "|" STR """},
                    self.ManualItemsWordingAdapter(self.effects.selectable.colors, self.effects.boxed),
                    exercise.wording,
                )
            else:
                assert False, f"Unknown items kind: {self.items.kind}"

    def make_adapted_example(self, exercise):
        return self._adapt_instructions(exercise.example)

    def make_adapted_clue(self, exercise):
        return self._adapt_instructions(exercise.clue)

    def _make_instructions_delta_maker_type(self):
        tag_functions = {}
        if self.effects.selectable is not None:
            tag_functions.update({
                f"sel{color_index}_tag": (lambda color_index: staticmethod(lambda args: exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": color_index})))(color_index)
                for color_index in self._color_indexes
            })
        return type("InstructionsDeltaMaker", (parsing.InstructionsSectionDeltaMaker,), tag_functions)

    def _make_instructions_delta(self, section):
        return parsing.InstructionsSectionParser(
            self._make_instructions_tags(),
            self._make_instructions_delta_maker_type()(),
        )(
            section,
        )

    def make_instructions_delta(self, exercise):
        return self._make_instructions_delta(exercise.instructions)

    class ManualItemsWordingDeltaMaker(parsing.WordingSectionDeltaMaker):
        def selectable_tag(self, args):
            assert len(args) == 1
            return exercise_delta.TextInsertOp(insert=args[0], attributes={"selectable": True})

    def make_wording_delta(self, exercise):
        if self.effects.selectable is None:
            return parsing.make_plain_wording_section_delta(exercise.wording)
        else:
            if self.items.kind == "words":
                return parsing.make_plain_wording_section_delta(exercise.wording)
            elif self.items.kind == "manual":
                return parsing.WordingSectionParser(
                    {"selectable": r""" "|" STR """},
                    self.ManualItemsWordingDeltaMaker(),
                )(
                    exercise.wording,
                )
            else:
                assert False, f"Unknown items kind: {self.items.kind}"

    def make_example_delta(self, exercise):
        return self._make_instructions_delta(exercise.example)

    def make_clue_delta(self, exercise):
        return self._make_instructions_delta(exercise.clue)


class ItemsAndEffectsAttempt1AdaptationTestCase(AdaptationTestCase):
    def test_selectable_words__plain(self):
        self.do_test(
            exercises.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions",
                wording="This is, the wording.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=ItemsAndEffectsAttempt1Adaptation(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "words", "punctuation": False},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": False},
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[r.Paragraph(sentences=[r.Sentence(tokens=[
                    r.SelectableText(text="This", colors=["red", "blue"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="is", colors=["red", "blue"], boxed=False),
                    r.PlainText(text=","),
                    r.Whitespace(),
                    r.SelectableText(text="the", colors=["red", "blue"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="wording", colors=["red", "blue"], boxed=False),
                    r.PlainText(text="."),
                ])])]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[d.TextInsertOp(insert="Instructions", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.", attributes={})],
                example=[],
                clue=[],
            ),
        )

    def test_selectable_words_and_punctuation(self):
        self.do_test(
            exercises.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions",
                wording="This is, the wording.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=ItemsAndEffectsAttempt1Adaptation(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "words", "punctuation": True},
                    effects={"selectable": {"colors": ["green", "yellow", "orange"]}, "boxed": False},
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[r.Paragraph(sentences=[r.Sentence(tokens=[
                    r.SelectableText(text="This", colors=["green", "yellow", "orange"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="is", colors=["green", "yellow", "orange"], boxed=False),
                    r.SelectableText(text=",", colors=["green", "yellow", "orange"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="the", colors=["green", "yellow", "orange"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="wording", colors=["green", "yellow", "orange"], boxed=False),
                    r.SelectableText(text=".", colors=["green", "yellow", "orange"], boxed=False),
                ])])]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[d.TextInsertOp(insert="Instructions", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.", attributes={})],
                example=[],
                clue=[],
            ),
        )

    def test_selectable_words__boxed(self):
        self.do_test(
            exercises.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions",
                wording="This is, the wording.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=ItemsAndEffectsAttempt1Adaptation(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "words", "punctuation": False},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": True},
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[r.Paragraph(sentences=[r.Sentence(tokens=[
                    r.SelectableText(text="This", colors=["red", "blue"], boxed=True),
                    r.Whitespace(),
                    r.SelectableText(text="is", colors=["red", "blue"], boxed=True),
                    r.PlainText(text=","),
                    r.Whitespace(),
                    r.SelectableText(text="the", colors=["red", "blue"], boxed=True),
                    r.Whitespace(),
                    r.SelectableText(text="wording", colors=["red", "blue"], boxed=True),
                    r.PlainText(text="."),
                ])])]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[d.TextInsertOp(insert="Instructions", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.", attributes={})],
                example=[],
                clue=[],
            ),
        )

    def test_selectable_manual_items__plain(self):
        self.do_test(
            exercises.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions",
                wording="This {selectable|is}{selectable|,} {selectable|the} wording.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=ItemsAndEffectsAttempt1Adaptation(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "manual"},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": False},
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[r.Paragraph(sentences=[r.Sentence(tokens=[
                    r.PlainText(text="This"),
                    r.Whitespace(),
                    r.SelectableText(text="is", colors=["red", "blue"], boxed=False),
                    r.SelectableText(text=",", colors=["red", "blue"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="the", colors=["red", "blue"], boxed=False),
                    r.Whitespace(),
                    r.PlainText(text="wording"),
                    r.PlainText(text="."),
                ])])]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[d.TextInsertOp(insert="Instructions", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is,", attributes={"selectable": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"selectable": True}),
                    d.TextInsertOp(insert=" wording.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_selectable_manual_items__boxed(self):
        self.do_test(
            exercises.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions",
                wording="This {selectable|is}{selectable|,} {selectable|the} wording.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=ItemsAndEffectsAttempt1Adaptation(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "manual"},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": True},
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[r.Paragraph(sentences=[r.Sentence(tokens=[
                    r.PlainText(text="This"),
                    r.Whitespace(),
                    r.SelectableText(text="is", colors=["red", "blue"], boxed=True),
                    r.SelectableText(text=",", colors=["red", "blue"], boxed=True),
                    r.Whitespace(),
                    r.SelectableText(text="the", colors=["red", "blue"], boxed=True),
                    r.Whitespace(),
                    r.PlainText(text="wording"),
                    r.PlainText(text="."),
                ])])]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[d.TextInsertOp(insert="Instructions", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is,", attributes={"selectable": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"selectable": True}),
                    d.TextInsertOp(insert=" wording.", attributes={}),
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
                adaptation=ItemsAndEffectsAttempt1Adaptation(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "words", "punctuation": False},
                    effects={"selectable": {"colors": ["red", "green", "blue"]}, "boxed": False},
                ),
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
