from . import AdaptationTestCase
from .. import deltas as d
from .. import exercises as e
from .. import renderable as r
from ..api_models import Adaptation, PredefinedMcq

# These tests follow a legacy organization, based on classes that have been deleted.
# There is some duplication because tests have been kept through refactoring.
# Tests above focus on specific features of the adaptation process.
# A reorganization would be beneficial, future me!


class FillWithFreeTextAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The wording of this ... is a ... sentence.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="of"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sentence"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_start_and_end_with_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="@ a @\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="@",
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_multiple_lines_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[r.Text(kind="text", text="instructions"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="are")]
                                ),
                                r.Paragraph(contents=[r.Text(kind="text", text="on")]),
                                r.Paragraph(
                                    contents=[r.Text(kind="text", text="multiple"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="lines")]
                                ),
                            ]
                        ),
                        wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="wording")])]),
                    )
                ],
            ),
        )

    def test_multiple_lines_in_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="foo toto : ...\n\nbar : ...\n\nbaz : ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="foo"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="toto"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text=":"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="bar"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text=":"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="baz"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text=":"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_unknown_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="{tag|abc}\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="{tag|def}\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="{"),
                                        r.Text(kind="text", text="tag"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="abc"),
                                        r.Text(kind="text", text="}"),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="{"),
                                        r.Text(kind="text", text="tag"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="def"),
                                        r.Text(kind="text", text="}"),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_strip_whitespace(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="   abc   \n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="   def   \n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="abc")])]),
                        wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="def")])]),
                    )
                ],
            ),
        )

    def test_example_and_clue(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This @ is the wording.\n", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="This @ is the example.\n", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="This @ is the clue.\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="@",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="@"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="example"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="@"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="clue"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )
