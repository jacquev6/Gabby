from . import exercise_delta as d
from . import exercises as e
from . import parsing as p
from . import renderable as r
from .adaptations.testing import AdaptationTestCase
from .api_models import AdaptationV2


class FillWithFreeTextAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions",
                wording="The wording of this ... is a ... sentence.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[p.FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions",
                wording="@ a @",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[p.FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="@")]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions\nare\n\non\n\nmultiple\nlines",
                wording="wording",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[p.FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions",
                wording="foo toto : ...\n\nbar : ...\n\nbaz : ...",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[p.FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="{tag|abc}",
                wording="{tag|def}",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[p.FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="   abc   ",
                wording="   def   ",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[p.FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions",
                wording="This @ is the wording.",
                example="This @ is the example.",
                clue="This @ is the clue.",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[p.FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="@")]),
            ),
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


class ItemsAndEffectsAttempt1AdaptationTestCase(AdaptationTestCase):
    def test_selectable_words__plain(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions",
                wording="This is, the wording.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="items-and-effects-attempt-1", effects=[p.ItemsAndEffectsAttempt1AdaptationEffect(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "words", "punctuation": False},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": False},
                )]),
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
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions",
                wording="This is, the wording.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="items-and-effects-attempt-1", effects=[p.ItemsAndEffectsAttempt1AdaptationEffect(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "words", "punctuation": True},
                    effects={"selectable": {"colors": ["green", "yellow", "orange"]}, "boxed": False},
                )]),
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
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions",
                wording="This is, the wording.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="items-and-effects-attempt-1", effects=[p.ItemsAndEffectsAttempt1AdaptationEffect(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "words", "punctuation": False},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": True},
                )]),
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
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions",
                wording="This {selectable|is}{selectable|,} {selectable|the} wording.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="items-and-effects-attempt-1", effects=[p.ItemsAndEffectsAttempt1AdaptationEffect(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "manual"},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": False},
                )]),
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
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions",
                wording="This {selectable|is}{selectable|,} {selectable|the} wording.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="items-and-effects-attempt-1", effects=[p.ItemsAndEffectsAttempt1AdaptationEffect(
                    kind="items-and-effects-attempt-1",
                    items={"kind": "manual"},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": True},
                )]),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="{sel1|abc} {sel2|def} {sel3|ghi} {sel4|jkl}",
                wording="wording",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                    adaptation=AdaptationV2(kind="items-and-effects-attempt-1", effects=[p.ItemsAndEffectsAttempt1AdaptationEffect(
                        kind="items-and-effects-attempt-1",
                        items={"kind": "words", "punctuation": False},
                        effects={"selectable": {"colors": ["red", "green", "blue"]}, "boxed": False},
                    )]),
            ),
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


class MultipleChoicesInInstructionsAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choice|a} or {choice|b}.",
                wording="A ... B ...",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices-in-instructions", effects=[p.MultipleChoicesInInstructionsAdaptationEffect(kind="multiple-choices-in-instructions", placeholder="...")]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choice|a} or {choice|b}.",
                wording="A @ B @",
                example="This {choice|is} the @ example.",
                clue="This is {choice|the} @ clue.",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices-in-instructions", effects=[p.MultipleChoicesInInstructionsAdaptationEffect(kind="multiple-choices-in-instructions", placeholder="@")]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="{choice|a} # {choice|b}\n\n c #\nd.",
                wording="...",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices-in-instructions", effects=[p.MultipleChoicesInInstructionsAdaptationEffect(kind="multiple-choices-in-instructions", placeholder="...")]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=" \t  Choose  \t\n  {choice|a}.   Or {choice|b} .   \t\n   ",
                wording="...",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices-in-instructions", effects=[p.MultipleChoicesInInstructionsAdaptationEffect(kind="multiple-choices-in-instructions", placeholder="...")]),
            ),
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

    def test_choices2(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||or|||...|a or b}.",
                wording="A ... B ...",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices-in-instructions", effects=[]),
            ),
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
                    d.TextInsertOp(insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_two_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||,|or||...|a, b, c or d}.",
                wording="A ... B ...",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices-in-instructions", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.BoxedText(text="c"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="d"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c", "d"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c", "d"]),
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
                    d.TextInsertOp(insert="a, b, c or d", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "or", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_oxford_comma(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||,|or||...|a, b, c, or d}.",
                wording="A ... B ...",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices-in-instructions", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.BoxedText(text="c"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="d"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c", "d"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c", "d"]),
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
                    d.TextInsertOp(insert="a, b, c, or d", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "or", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_successive_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||/|||...|a / b // c}.",
                wording="A ... B ...",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices-in-instructions", effects=[]),
            ),
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
                            r.PlainText(text="/"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.Whitespace(),
                            r.PlainText(text="/"),
                            r.Whitespace(),
                            r.BoxedText(text="c"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c"]),
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
                    d.TextInsertOp(insert="a / b // c", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_start_and_stop(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2|(|or||)|...|(a or b)}.",
                wording="A ... B ...",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices-in-instructions", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="("),
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text=")"),
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
                    d.TextInsertOp(insert="(a or b)", attributes={"choices2": {"start": "(", "separator1": "or", "separator2": "", "stop": ")", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_two_choices2(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||or|||...|a or b} and {choices2||or|||@@@|c or d}.",
                wording="A ... @@@\nB ... @@@",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices-in-instructions", effects=[]),
            ),
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
                            r.Whitespace(),
                            r.PlainText(text="and"),
                            r.Whitespace(),
                            r.BoxedText(text="c"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="d"),
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
                            r.MultipleChoicesInput(choices=["c", "d"]),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["c", "d"]),
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
                    d.TextInsertOp(insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=" and ", attributes={}),
                    d.TextInsertOp(insert="c or d", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "@@@"}}),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... @@@\nB ... @@@", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )


class MultipleChoicesInWordingAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="A {choices|a|b|c} B {choices|d|e}.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["d", "e"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A {choices|a|b|c} B {choices|d|e}.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_without_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="A {choices2|(|/||)||(blah/blih)}.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="(blah/blih)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_spaces(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="A {choices2|(|/||)||  (  blah  /  blih  )  }.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="  (  blah  /  blih  )  ",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_empty_start_and_stop(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="A {choices2||/||||blah/blih}.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="blah/blih",
                        attributes={
                            "choices2": {
                                "start": "",
                                "separator1": "/",
                                "separator2": "",
                                "stop": "",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_empty_separator(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="A {choices2||||||blah / blih}.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah / blih"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="blah / blih",
                        attributes={
                            "choices2": {
                                "start": "",
                                "separator1": "",
                                "separator2": "",
                                "stop": "",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_longer_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="A {choices2|((|//||))||((blah//blih))}.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="((blah//blih))",
                        attributes={
                            "choices2": {
                                "start": "((",
                                "separator1": "//",
                                "separator2": "",
                                "stop": "))",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_escaped_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording=r"A {choices2|\{|\|||\}||\{blah\|blih\}}.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="{blah|blih}",
                        attributes={
                            "choices2": {
                                "start": "{",
                                "separator1": "|",
                                "separator2": "",
                                "stop": "}",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_placeholder_before(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="The sky is @@. {choices2|(|/||)|@@|(blue/red)} ",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_placeholder_after(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="{choices2|(|/||)|...|(blue/red)} The sky is ....",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "...",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is ....", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_two_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="{choices2|(|/||)|...|(blue/yellow)} The sky is ..., the sun is ....",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "yellow"]),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "yellow"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/yellow)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "...",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is ..., the sun is ....", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_two_choices2_with_matching_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="{choices2|(|/||)|@1|(blue/red)} {choices2|[|*||]|@2|[green*yellow]} The sky is @1, the sun is @2.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["green", "yellow"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "@1",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(
                        insert="[green*yellow]",
                        attributes={
                            "choices2": {
                                "start": "[",
                                "separator1": "*",
                                "separator2": "",
                                "stop": "]",
                                "placeholder": "@2",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is @1, the sun is @2.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_two_choices2_with_identical_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="The sky is @@. {choices2|(|/||)|@@|(blue/red)}\n\nThe sun is @@. {choices2|(|/||)|@@|(green/yellow)}",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["green", "yellow"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                    d.TextInsertOp(insert="\n\nThe sun is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(green/yellow)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_two_choices2_with_spaces_between_them(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.",
                wording="The sky is @1, {choices2|(|/||)|@1|(blue/red)} {choices2|[|*||]|@2|[green*yellow]} the sun is @2.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["green", "yellow"]),
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
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @1, ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "@1",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(
                        insert="[green*yellow]",
                        attributes={
                            "choices2": {
                                "start": "[",
                                "separator1": "*",
                                "separator2": "",
                                "stop": "]",
                                "placeholder": "@2",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" the sun is @2.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )


class SelectThingsAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions",
                wording="The wording of this exercise is a single sentence.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="select-things", effects=[p.SelectThingsAdaptationEffect(kind="select-things", colors=["red", "blue"], words=True, punctuation=False)]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="{sel1|abc} {sel2|def} {sel3|ghi} {sel4|jkl}",
                wording="wording",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="select-things", effects=[p.SelectThingsAdaptationEffect(kind="select-things", colors=["red", "green", "blue"], words=True, punctuation=False)]),
            ),
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

    def test_single_color(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="{sel1|abc}",
                wording="wording",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="select-things", effects=[p.SelectThingsAdaptationEffect(kind="select-things", colors=["red"], words=True, punctuation=False)]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions\nare\n\non\n\nmultiple\nlines",
                wording="wording",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="select-things", effects=[p.SelectThingsAdaptationEffect(kind="select-things", colors=["red"], words=True, punctuation=False)]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions",
                wording="wording is\n\non\n\nmultiple lines",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="select-things", effects=[p.SelectThingsAdaptationEffect(kind="select-things", colors=["red"], words=True, punctuation=False)]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="{tag|abc}",
                wording="{tag|def}",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="select-things", effects=[p.SelectThingsAdaptationEffect(kind="select-things", colors=["red"], words=True, punctuation=False)]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="   abc   ",
                wording="   def   ",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="select-things", effects=[p.SelectThingsAdaptationEffect(kind="select-things", colors=["red"], words=True, punctuation=False)]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions",
                wording="wording",
                example="This is the example.",
                clue="This is the clue.",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="select-things", effects=[p.SelectThingsAdaptationEffect(kind="select-things", colors=["red"], words=True, punctuation=False)]),
            ),
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
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions",
                wording="wording",
                example="{sel1|abc} {sel2|def}",
                clue="{sel3|ghi} {sel4|jkl}",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="select-things", effects=[p.SelectThingsAdaptationEffect(kind="select-things", colors=["red", "green", "blue"], words=True, punctuation=False)]),
            ),
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
                            r.PlainText(text="jkl"),
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
                    d.TextInsertOp(insert=" jkl", attributes={}),
                ],
            ),
        )



class MultipleAdaptationEffectsTestCase(AdaptationTestCase):
    def test_fill_with_free_text_and_multiple_choices_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions {choice|short} {choice|long}",
                wording="The wording of this ... is a @@@ sentence.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind=None, effects=[
                    p.FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="..."),
                    p.MultipleChoicesInInstructionsAdaptationEffect(kind="multiple-choices-in-instructions", placeholder="@@@"),
                ]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                            r.Whitespace(),
                            r.BoxedText(text="short"),
                            r.Whitespace(),
                            r.BoxedText(text="long"),
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
                            r.MultipleChoicesInput(choices=["short", "long"]),
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
                    d.TextInsertOp(insert="instructions ", attributes={}),
                    d.TextInsertOp(insert="short", attributes={"choice": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="long", attributes={"choice": True}),
                ],
                wording=[
                    d.TextInsertOp(insert="The wording of this ... is a @@@ sentence.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_multiple_choices_in_instructions_and_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely {choice|alpha} {choice|bravo}.",
                wording="A {choices|a|b|c} B {choices|d|e} C @@@.",
                example="",
                clue="",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind=None, effects=[
                    p.MultipleChoicesInInstructionsAdaptationEffect(kind="multiple-choices-in-instructions", placeholder="@@@"),
                ]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.Whitespace(),
                            r.BoxedText(text="alpha"),
                            r.Whitespace(),
                            r.BoxedText(text="bravo"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["d", "e"]),
                            r.Whitespace(),
                            r.PlainText(text="C"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["alpha", "bravo"]),
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
                    d.TextInsertOp(insert="Choose wisely ", attributes={}),
                    d.TextInsertOp(insert="alpha", attributes={"choice": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="bravo", attributes={"choice": True}),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A {choices|a|b|c} B {choices|d|e} C @@@.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )
