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
