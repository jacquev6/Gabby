from . import AdaptationTestCase
from .. import deltas as d
from .. import exercises as e
from .. import renderable as r
from ..api_models import Adaptation, PredefinedMcq


class FormattingCompatibilityTestCase(AdaptationTestCase):
    def test_bold_and_italic(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(insert="The instructions.", attributes={"bold": True, "italic": True}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="The wording.", attributes={"bold": True, "italic": True}), d.TextInsertOp(insert="\n", attributes={})],
                example=[d.TextInsertOp(insert="The example.", attributes={"bold": True, "italic": True}), d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="The clue.", attributes={"bold": True, "italic": True}), d.TextInsertOp(insert="\n", attributes={})],
                text_reference=[d.TextInsertOp(insert="The reference.", attributes={"bold": True, "italic": True}), d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", bold=True, italic=True, text="The"),
                                            r.Whitespace(kind="whitespace", bold=True, italic=True),
                                            r.Text(kind="text", bold=True, italic=True, text="instructions"),
                                            r.Text(kind="text", bold=True, italic=True, text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", bold=True, italic=True, text="The"),
                                            r.Whitespace(kind="whitespace", bold=True, italic=True),
                                            r.Text(kind="text", bold=True, italic=True, text="example"),
                                            r.Text(kind="text", bold=True, italic=True, text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", bold=True, italic=True, text="The"),
                                            r.Whitespace(kind="whitespace", bold=True, italic=True),
                                            r.Text(kind="text", bold=True, italic=True, text="clue"),
                                            r.Text(kind="text", bold=True, italic=True, text="."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", bold=True, italic=True, text="The"),
                                            r.Whitespace(kind="whitespace", bold=True, italic=True),
                                            r.Text(kind="text", bold=True, italic=True, text="wording"),
                                            r.Text(kind="text", bold=True, italic=True, text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", bold=True, italic=True, text="The"),
                                            r.Whitespace(kind="whitespace", bold=True, italic=True),
                                            r.Text(kind="text", bold=True, italic=True, text="reference"),
                                            r.Text(kind="text", bold=True, italic=True, text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=False,
                            )
                        ]
                    ),
                ],
            ),
        )

    def test_bold_and_highlighted(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(insert="Before ", attributes={}),
                    d.TextInsertOp(insert="the instructions", attributes={"bold": True, "highlighted": "lightblue"}),
                    d.TextInsertOp(insert=" after\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="Before ", attributes={}),
                    d.TextInsertOp(insert="the wording", attributes={"bold": True, "highlighted": "lightblue"}),
                    d.TextInsertOp(insert=" after\n", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="Before ", attributes={}),
                    d.TextInsertOp(insert="the example", attributes={"bold": True, "highlighted": "lightblue"}),
                    d.TextInsertOp(insert=" after\n", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="Before ", attributes={}),
                    d.TextInsertOp(insert="the clue", attributes={"bold": True, "highlighted": "lightblue"}),
                    d.TextInsertOp(insert=" after\n", attributes={}),
                ],
                text_reference=[
                    d.TextInsertOp(insert="Before ", attributes={}),
                    d.TextInsertOp(insert="the reference", attributes={"bold": True, "highlighted": "lightblue"}),
                    d.TextInsertOp(insert=" after\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Before"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", bold=True, highlighted="lightblue", text="the"),
                                            r.Whitespace(kind="whitespace", bold=True, highlighted="lightblue"),
                                            r.Text(kind="text", bold=True, highlighted="lightblue", text="instructions"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="after"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Before"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", bold=True, highlighted="lightblue", text="the"),
                                            r.Whitespace(kind="whitespace", bold=True, highlighted="lightblue"),
                                            r.Text(kind="text", bold=True, highlighted="lightblue", text="example"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="after"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Before"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", bold=True, highlighted="lightblue", text="the"),
                                            r.Whitespace(kind="whitespace", bold=True, highlighted="lightblue"),
                                            r.Text(kind="text", bold=True, highlighted="lightblue", text="clue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="after"),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Before"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", bold=True, highlighted="lightblue", text="the"),
                                            r.Whitespace(kind="whitespace", bold=True, highlighted="lightblue"),
                                            r.Text(kind="text", bold=True, highlighted="lightblue", text="wording"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="after"),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Before"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", bold=True, highlighted="lightblue", text="the"),
                                            r.Whitespace(kind="whitespace", bold=True, highlighted="lightblue"),
                                            r.Text(kind="text", bold=True, highlighted="lightblue", text="reference"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="after"),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=False,
                            )
                        ]
                    ),
                ],
            ),
        )

    def test_fully_highlighted(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="The instructions.", attributes={"highlighted": "lightblue"}), d.TextInsertOp(insert="\n", attributes={})],
                wording=[d.TextInsertOp(insert="The wording.", attributes={"highlighted": "lightblue"}), d.TextInsertOp(insert="\n", attributes={})],
                example=[d.TextInsertOp(insert="The example.", attributes={"highlighted": "lightblue"}), d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="The clue.", attributes={"highlighted": "lightblue"}), d.TextInsertOp(insert="\n", attributes={})],
                text_reference=[d.TextInsertOp(insert="The reference.", attributes={"highlighted": "lightblue"}), d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", highlighted="lightblue", text="The"),
                                            r.Whitespace(kind="whitespace", highlighted="lightblue"),
                                            r.Text(kind="text", highlighted="lightblue", text="instructions"),
                                            r.Text(kind="text", highlighted="lightblue", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", highlighted="lightblue", text="The"),
                                            r.Whitespace(kind="whitespace", highlighted="lightblue"),
                                            r.Text(kind="text", highlighted="lightblue", text="example"),
                                            r.Text(kind="text", highlighted="lightblue", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", highlighted="lightblue", text="The"),
                                            r.Whitespace(kind="whitespace", highlighted="lightblue"),
                                            r.Text(kind="text", highlighted="lightblue", text="clue"),
                                            r.Text(kind="text", highlighted="lightblue", text="."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", highlighted="lightblue", text="The"),
                                            r.Whitespace(kind="whitespace", highlighted="lightblue"),
                                            r.Text(kind="text", highlighted="lightblue", text="wording"),
                                            r.Text(kind="text", highlighted="lightblue", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", highlighted="lightblue", text="The"),
                                            r.Whitespace(kind="whitespace", highlighted="lightblue"),
                                            r.Text(kind="text", highlighted="lightblue", text="reference"),
                                            r.Text(kind="text", highlighted="lightblue", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=False,
                            )
                        ]
                    ),
                ],
            ),
        )

    def test_sel_and_bold(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="The instructions.", attributes={"bold": True, "sel": 1}), d.TextInsertOp(insert="\n", attributes={})],
                example=[d.TextInsertOp(insert="The example.", attributes={"bold": True, "sel": 1}), d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="The clue.", attributes={"bold": True, "sel": 1}), d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["lightgreen", "lightblue"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", bold=True, highlighted="lightgreen", text="The"),
                                            r.Whitespace(kind="whitespace", bold=True, highlighted="lightgreen"),
                                            r.Text(kind="text", bold=True, highlighted="lightgreen", text="instructions"),
                                            r.Text(kind="text", bold=True, highlighted="lightgreen", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", bold=True, highlighted="lightgreen", text="The"),
                                            r.Whitespace(kind="whitespace", bold=True, highlighted="lightgreen"),
                                            r.Text(kind="text", bold=True, highlighted="lightgreen", text="example"),
                                            r.Text(kind="text", bold=True, highlighted="lightgreen", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", bold=True, highlighted="lightgreen", text="The"),
                                            r.Whitespace(kind="whitespace", bold=True, highlighted="lightgreen"),
                                            r.Text(kind="text", bold=True, highlighted="lightgreen", text="clue"),
                                            r.Text(kind="text", bold=True, highlighted="lightgreen", text="."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(paragraphs=[], centered=False, tricolored=True),
                        ]
                    )
                ],
            ),
        )

    def test_sel_and_italic(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="The instructions.", attributes={"italic": True, "sel": 1}), d.TextInsertOp(insert="\n", attributes={})],
                example=[d.TextInsertOp(insert="The example.", attributes={"italic": True, "sel": 1}), d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="The clue.", attributes={"italic": True, "sel": 1}), d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["lightgreen", "lightblue"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", italic=True, highlighted="lightgreen", text="The"),
                                            r.Whitespace(kind="whitespace", italic=True, highlighted="lightgreen"),
                                            r.Text(kind="text", italic=True, highlighted="lightgreen", text="instructions"),
                                            r.Text(kind="text", italic=True, highlighted="lightgreen", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", italic=True, highlighted="lightgreen", text="The"),
                                            r.Whitespace(kind="whitespace", italic=True, highlighted="lightgreen"),
                                            r.Text(kind="text", italic=True, highlighted="lightgreen", text="example"),
                                            r.Text(kind="text", italic=True, highlighted="lightgreen", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", italic=True, highlighted="lightgreen", text="The"),
                                            r.Whitespace(kind="whitespace", italic=True, highlighted="lightgreen"),
                                            r.Text(kind="text", italic=True, highlighted="lightgreen", text="clue"),
                                            r.Text(kind="text", italic=True, highlighted="lightgreen", text="."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(paragraphs=[], centered=False, tricolored=True),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_one_choice_in_choices2_in_instructions_with_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(
                        insert="alpha, b", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(
                        insert="rav",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "..."}, "bold": True},
                    ),
                    d.TextInsertOp(
                        insert="o ou charlie", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="...\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", bold=True, text="rav"),
                                                    r.Text(kind="text", text="o"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Alpha")],
                                                    [r.Text(kind="text", text="B"), r.Text(kind="text", bold=True, text="rav"), r.Text(kind="text", text="o")],
                                                    [r.Text(kind="text", text="Charlie")],
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_one_choice_in_choices2_in_instructions_with_mcq_beside_words(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(
                        insert="alpha, b", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}}
                    ),
                    d.TextInsertOp(
                        insert="rav", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}, "bold": True}
                    ),
                    d.TextInsertOp(
                        insert="o ou charlie", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="blah\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", bold=True, text="rav"),
                                                    r.Text(kind="text", text="o"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="blah"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="alpha")],
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", bold=True, text="rav"), r.Text(kind="text", text="o")],
                                                    [r.Text(kind="text", text="charlie")],
                                                ],
                                            ),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_one_choice_in_choices2_in_wording_with_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(insert="... ", attributes={}),
                    d.TextInsertOp(
                        insert="(alpha, b", attributes={"choices2": {"start": "(", "separator1": ",", "separator2": "ou", "stop": ")", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(
                        insert="rav",
                        attributes={"choices2": {"start": "(", "separator1": ",", "separator2": "ou", "stop": ")", "placeholder": "..."}, "bold": True},
                    ),
                    d.TextInsertOp(
                        insert="o ou charlie)",
                        attributes={"choices2": {"start": "(", "separator1": ",", "separator2": "ou", "stop": ")", "placeholder": "..."}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Alpha")],
                                                    [r.Text(kind="text", text="B"), r.Text(kind="text", bold=True, text="rav"), r.Text(kind="text", text="o")],
                                                    [r.Text(kind="text", text="Charlie")],
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_one_choice_in_choices2_in_wording_without_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(
                        insert="alpha, b", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}}
                    ),
                    d.TextInsertOp(
                        insert="rav", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}, "bold": True}
                    ),
                    d.TextInsertOp(
                        insert="o ou charlie", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="alpha")],
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", bold=True, text="rav"), r.Text(kind="text", text="o")],
                                                    [r.Text(kind="text", text="charlie")],
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_mcq_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha ou bravo", attributes={"choices2": {"start": "", "separator1": "ou", "separator2": "", "stop": "", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="Blah ", attributes={}),
                    d.TextInsertOp(insert="b", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert="la", attributes={"mcq-placeholder": True, "bold": True}),
                    d.TextInsertOp(insert="h", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,  # {"kind": "sentences"} is implied by items_are_repeated_with_mcq (for now?)
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=True,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Instructions"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.AnySequence(
                                                kind="sequence",
                                                contents=[
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="Blah"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", highlighted="#ffff00", text="b"),
                                                            r.Text(kind="text", highlighted="#ffff00", bold=True, text="la"),
                                                            r.Text(kind="text", highlighted="#ffff00", text="h"),
                                                            r.Text(kind="text", text="."),
                                                        ],
                                                    ),
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="→"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="Blah"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.MultipleChoicesInput(
                                                                kind="multipleChoicesInput",
                                                                choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                                            ),
                                                            r.Text(kind="text", text="."),
                                                        ],
                                                    ),
                                                ],
                                                vertical=True,
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_automated_items__letters(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(insert="Blah b", attributes={}),
                    d.TextInsertOp(insert="la", attributes={"bold": True}),
                    d.TextInsertOp(insert="h blah.\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="B")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="l")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="h")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", bold=True, text="l")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", bold=True, text="a")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="h")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="l")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="h")], boxed=True),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_automated_items__words(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(insert="Blah b", attributes={}),
                    d.TextInsertOp(insert="la", attributes={"bold": True}),
                    d.TextInsertOp(insert="h blah.\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="Blah")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", bold=True, text="la"),
                                                    r.Text(kind="text", text="h"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="blah")], boxed=True),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_automated_items__punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(insert="Blah", attributes={}),
                    d.TextInsertOp(insert=",", attributes={"bold": True}),
                    d.TextInsertOp(insert=" blah.\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Blah"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", bold=True, text=",")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="blah"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_automated_items__sentences(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(insert="Blah b", attributes={}),
                    d.TextInsertOp(insert="la", attributes={"bold": True}),
                    d.TextInsertOp(insert="h. Blah.\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="Blah"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", bold=True, text="la"),
                                                    r.Text(kind="text", text="h"),
                                                    r.Text(kind="text", text="."),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence", contents=[r.Text(kind="text", text="Blah"), r.Text(kind="text", text=".")], boxed=True
                                            ),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_automated_items__separated(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(insert="Blah b", attributes={}),
                    d.TextInsertOp(insert="la", attributes={"bold": True}),
                    d.TextInsertOp(insert="h / blah.\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "separated", "separator": "/"},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="Blah"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", bold=True, text="la"),
                                                    r.Text(kind="text", text="h"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence", contents=[r.Text(kind="text", text="blah"), r.Text(kind="text", text=".")], boxed=True
                                            ),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_bold_in_manual_items(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(insert="Blah ", attributes={}),
                    d.TextInsertOp(insert="b", attributes={"manual-item": True}),
                    d.TextInsertOp(insert="la", attributes={"manual-item": True, "bold": True}),
                    d.TextInsertOp(insert="h", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" blah.\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Blah"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", bold=True, text="la"),
                                                    r.Text(kind="text", text="h"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="blah"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_manual_item_with_one_line_end(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(insert="Blah ", attributes={}),
                    d.TextInsertOp(insert="bl\nah", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" blah.\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Blah"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[r.Text(kind="text", text="bl"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ah")],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="blah"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_manual_item_with_two_line_ends(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(insert="Blah ", attributes={}),
                    d.TextInsertOp(insert="bl\n\nah", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" blah.\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Blah"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[r.Text(kind="text", text="bl"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ah")],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="blah"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_manual_item_with_three_line_ends(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(insert="Blah ", attributes={}),
                    d.TextInsertOp(insert="bl\n\n\nah", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" blah.\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Blah"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[r.Text(kind="text", text="bl"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ah")],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="blah"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_choices2_with_one_line_end_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(
                        insert="alpha,\nbravo\nou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "..."}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="...\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Alpha")],
                                                    [r.Text(kind="text", text="Bravo")],
                                                    [r.Text(kind="text", text="Charlie")],
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_choices2_with_two_line_ends_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(
                        insert="alpha,\n\nbravo\n\nou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "..."}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="...\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Alpha")],
                                                    [r.Text(kind="text", text="Bravo")],
                                                    [r.Text(kind="text", text="Charlie")],
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_choices2_with_three_line_ends_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(
                        insert="alpha,\n\n\nbravo\n\n\nou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "..."}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="...\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Alpha")],
                                                    [r.Text(kind="text", text="Bravo")],
                                                    [r.Text(kind="text", text="Charlie")],
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_choices2_with_one_line_end_in_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(
                        insert="alpha,\nbravo\nou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="alpha")],
                                                    [r.Text(kind="text", text="bravo")],
                                                    [r.Text(kind="text", text="charlie")],
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_choices2_with_two_line_ends_in_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(
                        insert="alpha,\n\nbravo\n\nou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="alpha")],
                                                    [r.Text(kind="text", text="bravo")],
                                                    [r.Text(kind="text", text="charlie")],
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_choices2_with_three_line_ends_in_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                wording=[
                    d.TextInsertOp(
                        insert="alpha,\n\n\nbravo\n\n\nou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="alpha")],
                                                    [r.Text(kind="text", text="bravo")],
                                                    [r.Text(kind="text", text="charlie")],
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_mcq_placeholder_with_one_line_end(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha ou bravo", attributes={"choices2": {"start": "", "separator1": "ou", "separator2": "", "stop": "", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="Blah ", attributes={}),
                    d.TextInsertOp(insert="bl\nah", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,  # {"kind": "sentences"} is implied by items_are_repeated_with_mcq (for now?)
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=True,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Instructions"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.AnySequence(
                                                kind="sequence",
                                                contents=[
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="Blah"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", highlighted="#ffff00", text="bl"),
                                                            r.Whitespace(kind="whitespace", highlighted="#ffff00"),
                                                            r.Text(kind="text", highlighted="#ffff00", text="ah"),
                                                            r.Text(kind="text", text="."),
                                                        ],
                                                    ),
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="→"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="Blah"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.MultipleChoicesInput(
                                                                kind="multipleChoicesInput",
                                                                choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                                            ),
                                                            r.Text(kind="text", text="."),
                                                        ],
                                                    ),
                                                ],
                                                vertical=True,
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_mcq_placeholder_with_two_line_ends(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha ou bravo", attributes={"choices2": {"start": "", "separator1": "ou", "separator2": "", "stop": "", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="Blah ", attributes={}),
                    d.TextInsertOp(insert="bl\n\nah", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,  # {"kind": "sentences"} is implied by items_are_repeated_with_mcq (for now?)
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=True,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Instructions"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.AnySequence(
                                                kind="sequence",
                                                contents=[
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="Blah"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", highlighted="#ffff00", text="bl"),
                                                            r.Whitespace(kind="whitespace", highlighted="#ffff00"),
                                                            r.Text(kind="text", highlighted="#ffff00", text="ah"),
                                                            r.Text(kind="text", text="."),
                                                        ],
                                                    ),
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="→"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="Blah"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.MultipleChoicesInput(
                                                                kind="multipleChoicesInput",
                                                                choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                                            ),
                                                            r.Text(kind="text", text="."),
                                                        ],
                                                    ),
                                                ],
                                                vertical=True,
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_mcq_placeholder_with_three_line_ends(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha ou bravo", attributes={"choices2": {"start": "", "separator1": "ou", "separator2": "", "stop": "", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="Blah ", attributes={}),
                    d.TextInsertOp(insert="bl\n\n\nah", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,  # {"kind": "sentences"} is implied by items_are_repeated_with_mcq (for now?)
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=True,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Instructions"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.AnySequence(
                                                kind="sequence",
                                                contents=[
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="Blah"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", highlighted="#ffff00", text="bl"),
                                                            r.Whitespace(kind="whitespace", highlighted="#ffff00"),
                                                            r.Text(kind="text", highlighted="#ffff00", text="ah"),
                                                            r.Text(kind="text", text="."),
                                                        ],
                                                    ),
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="→"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="Blah"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.MultipleChoicesInput(
                                                                kind="multipleChoicesInput",
                                                                choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                                            ),
                                                            r.Text(kind="text", text="."),
                                                        ],
                                                    ),
                                                ],
                                                vertical=True,
                                            )
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )
