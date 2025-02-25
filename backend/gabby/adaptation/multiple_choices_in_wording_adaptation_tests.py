from . import AdaptationTestCase
from .. import deltas as d
from .. import exercises as e
from .. import renderable as r
from ..api_models import Adaptation, PredefinedMcq

# These tests follow a legacy organization, based on classes that have been deleted.
# There is some duplication because tests have been kept through refactoring.
# Tests above focus on specific features of the adaptation process.
# A reorganization would be beneficial, future me!


class MultipleChoicesInWordingAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(insert="a/b/c", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.TextInsertOp(insert=" B ", attributes={}),
                    d.TextInsertOp(insert="d#e", attributes={"choices2": {"start": "", "separator1": "#", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")], [r.Text(kind="text", text="c")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="d")], [r.Text(kind="text", text="e")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_without_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="(blah/blih)", attributes={"choices2": {"start": "(", "separator1": "/", "separator2": "", "stop": ")", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blah")], [r.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_spaces(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="  (  blah  /  blih  )  ",
                        attributes={"choices2": {"start": "(", "separator1": "/", "separator2": "", "stop": ")", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blah")], [r.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_empty_start_and_stop(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="blah/blih", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blah")], [r.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_empty_separator(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="blah / blih", attributes={"choices2": {"start": "", "separator1": "", "separator2": "", "stop": "", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [
                                                    r.Text(kind="text", text="blah"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="/"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="blih"),
                                                ]
                                            ],
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_longer_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="((blah//blih))", attributes={"choices2": {"start": "((", "separator1": "//", "separator2": "", "stop": "))", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blah")], [r.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_escaped_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="{blah|blih}", attributes={"choices2": {"start": "{", "separator1": "|", "separator2": "", "stop": "}", "placeholder": ""}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blah")], [r.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_placeholder_before(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="The sky is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)", attributes={"choices2": {"start": "(", "separator1": "/", "separator2": "", "stop": ")", "placeholder": "@@"}}
                    ),
                    d.TextInsertOp(insert=" \n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_placeholder_after(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/red)", attributes={"choices2": {"start": "(", "separator1": "/", "separator2": "", "stop": ")", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=" The sky is ....\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_two_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/yellow)", attributes={"choices2": {"start": "(", "separator1": "/", "separator2": "", "stop": ")", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=" The sky is ..., the sun is ....\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sun"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_two_choices2_with_matching_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/red)", attributes={"choices2": {"start": "(", "separator1": "/", "separator2": "", "stop": ")", "placeholder": "@1"}}
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(
                        insert="[green*yellow]", attributes={"choices2": {"start": "[", "separator1": "*", "separator2": "", "stop": "]", "placeholder": "@2"}}
                    ),
                    d.TextInsertOp(insert=" The sky is @1, the sun is @2.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sun"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="green")], [r.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_two_choices2_with_identical_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="The sky is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)", attributes={"choices2": {"start": "(", "separator1": "/", "separator2": "", "stop": ")", "placeholder": "@@"}}
                    ),
                    d.TextInsertOp(insert="\n\nThe sun is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(green/yellow)", attributes={"choices2": {"start": "(", "separator1": "/", "separator2": "", "stop": ")", "placeholder": "@@"}}
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sun"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="green")], [r.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_two_choices2_with_spaces_between_them(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Choose wisely.\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="The sky is @1, ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)", attributes={"choices2": {"start": "(", "separator1": "/", "separator2": "", "stop": ")", "placeholder": "@1"}}
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(
                        insert="[green*yellow]", attributes={"choices2": {"start": "[", "separator1": "*", "separator2": "", "stop": "]", "placeholder": "@2"}}
                    ),
                    d.TextInsertOp(insert=" the sun is @2.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sun"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="green")], [r.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )
