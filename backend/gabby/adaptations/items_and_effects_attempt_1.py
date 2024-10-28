from typing import Literal
import os

from .. import exercise_delta as d
from .. import parsing
from .. import renderable as r
from .testing import AdaptationTestCase
from mydantic import PydanticBase

if os.environ.get("GABBY_UNITTESTING", "false") == "true":
    from .. import exercises


class ItemsAndEffectsAttempt1Adaptation(PydanticBase):
    kind: Literal["items-and-effects-attempt-1"]

    items: parsing.ItemsAndEffectsAttempt1.Items
    effects: parsing.ItemsAndEffectsAttempt1.Effects

    def make_effects(self):
        return [parsing.ItemsAndEffectsAttempt1(items=self.items, effects=self.effects)]


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
                            r.PlainText(text="jkl"),
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
                    d.TextInsertOp(insert=" jkl", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )
