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
                wording=[
                    d.TextInsertOp(insert="The wording.", attributes={"bold": True, "italic": True}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="The example.", attributes={"bold": True, "italic": True}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="The clue.", attributes={"bold": True, "italic": True}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                text_reference=[
                    d.TextInsertOp(insert="The reference.", attributes={"bold": True, "italic": True}),
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
                        instructions=r.Section(
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
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", bold=True, italic=True, text="The"),
                                        r.Whitespace(kind="whitespace", bold=True, italic=True),
                                        r.Text(kind="text", bold=True, italic=True, text="wording"),
                                        r.Text(kind="text", bold=True, italic=True, text="."),
                                    ]
                                )
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", bold=True, italic=True, text="The"),
                                        r.Whitespace(kind="whitespace", bold=True, italic=True),
                                        r.Text(kind="text", bold=True, italic=True, text="reference"),
                                        r.Text(kind="text", bold=True, italic=True, text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(paragraphs=[]),
                    ),
                ],
            ),
        )

    def test_sel_and_bold(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(insert="The instructions.", attributes={"bold": True, "sel": 1}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="The example.", attributes={"bold": True, "sel": 1}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="The clue.", attributes={"bold": True, "sel": 1}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
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
                        instructions=r.Section(
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
                            ]
                        ),
                        wording=r.Section(paragraphs=[]),
                    )
                ],
            ),
        )

    def test_sel_and_italic(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(insert="The instructions.", attributes={"italic": True, "sel": 1}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="The example.", attributes={"italic": True, "sel": 1}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="The clue.", attributes={"italic": True, "sel": 1}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
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
                        instructions=r.Section(
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
                            ]
                        ),
                        wording=r.Section(paragraphs=[]),
                    )
                ],
            ),
        )

    def test_bold_in_one_choice_in_choices2_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(
                        insert="alpha, b",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "..."}},
                    ),
                    d.TextInsertOp(
                        insert="rav",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "..."}, "bold": True},
                    ),
                    d.TextInsertOp(
                        insert="o ou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "..."}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="...\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
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
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(
                                            kind="whitespace",
                                        ),
                                        r.PassiveSequence(
                                            kind="passiveSequence",
                                            contents=[
                                                r.Text(kind="text", text="b"),
                                                r.Text(kind="text", bold=True, text="rav"),
                                                r.Text(kind="text", text="o"),
                                            ],
                                            boxed=True,
                                        ),
                                        r.Whitespace(
                                            kind="whitespace",
                                        ),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(
                                            kind="whitespace",
                                        ),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", bold=True, text="rav"),
                                                    r.Text(kind="text", text="o"),
                                                ],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                        )
                                    ]
                                )
                            ]
                        ),
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
                        insert="(alpha, b",
                        attributes={"choices2": {"start": "(", "separator1": ",", "separator2": "ou", "stop": ")", "placeholder": "..."}},
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
                        instructions=r.Section(paragraphs=[]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", bold=True, text="rav"),
                                                    r.Text(kind="text", text="o"),
                                                ],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                        )
                                    ]
                                )
                            ]
                        ),
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
                        insert="alpha, b",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(
                        insert="rav",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}, "bold": True},
                    ),
                    d.TextInsertOp(
                        insert="o ou charlie",
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
                        instructions=r.Section(paragraphs=[]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", bold=True, text="rav"),
                                                    r.Text(kind="text", text="o"),
                                                ],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                        )
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )
