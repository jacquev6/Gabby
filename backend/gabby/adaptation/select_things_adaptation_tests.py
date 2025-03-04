from . import AdaptationTestCase
from .. import deltas as d
from .. import exercises as e
from .. import renderable as r
from ..api_models import Adaptation, TokensItems, Selectable, PredefinedMcq

# These tests follow a legacy organization, based on classes that have been deleted.
# There is some duplication because tests have been kept through refactoring.
# Tests above focus on specific features of the adaptation process.
# A reorganization would be beneficial, future me!


class SelectThingsAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="The wording of this exercise is a single sentence.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "blue"]),
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
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="The")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="wording")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="of")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="this")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="exercise")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="is")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="a")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="single")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="sentence")]),
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

    def test_sel_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(insert="abc", attributes={"sel": 1}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="def", attributes={"sel": 2}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="ghi", attributes={"sel": 3}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="jkl", attributes={"sel": 4}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="wording\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "green", "blue"]),
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
                                            r.Text(kind="text", highlighted="red", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", highlighted="green", text="def"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", highlighted="blue", text="ghi"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="jkl"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red", "green", "blue"], contents=[r.Text(kind="text", text="wording")]
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

    def test_single_color(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="abc", attributes={"sel": 1}), d.TextInsertOp(insert="\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
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
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", highlighted="red", text="abc")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="wording")])]
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

    def test_multiple_lines_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
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
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[r.Text(kind="text", text="instructions"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="are")]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="on")]),
                                    r.Paragraph(
                                        contents=[r.Text(kind="text", text="multiple"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="lines")]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="wording")])]
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

    def test_multiple_lines_in_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording is\n\non\n\nmultiple lines\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
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
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="wording")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="is")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="on")])]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="multiple")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="lines")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_unknown_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="{tag|abc}\n", attributes={})],
                wording=[d.TextInsertOp(insert="{tag|def}\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
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
                        sections=[
                            r.Section(
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
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="{"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="tag")]),
                                            r.Text(kind="text", text="|"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="def")]),
                                            r.Text(kind="text", text="}"),
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

    def test_strip_whitespace(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="   abc   \n", attributes={})],
                wording=[d.TextInsertOp(insert="   def   \n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
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
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="abc")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="def")])]
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

    def test_example_and_clue(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording\n", attributes={})],
                example=[d.TextInsertOp(insert="This is the example.\n", attributes={})],
                clue=[d.TextInsertOp(insert="This is the clue.\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
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
                                    r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="This"),
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
                                            r.Text(kind="text", text="is"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="the"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="clue"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="wording")])]
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

    def test_example_and_clue_with_sel_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording\n", attributes={})],
                example=[
                    d.TextInsertOp(insert="abc", attributes={"sel": 1}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="def", attributes={"sel": 2}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="ghi", attributes={"sel": 3}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="jkl", attributes={"sel": 4}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "green", "blue"]),
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
                                    r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", highlighted="red", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", highlighted="green", text="def"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", highlighted="blue", text="ghi"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="jkl"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red", "green", "blue"], contents=[r.Text(kind="text", text="wording")]
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

    def test_french_elision_of_articles__without_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="Selectionne les articles.\n", attributes={})],
                wording=[d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
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
                                            r.Text(kind="text", text="Selectionne"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="les"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="articles"),
                                            r.Text(kind="text", text="."),
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
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="La")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="maison")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="belle")]),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="'")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="école")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="fermée")]),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="’")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="automobile")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="verte")]),
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

    def test_french_elision_of_articles__punctuation_only(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="Selectionne les articles.\n", attributes={})],
                wording=[d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=False, punctuation=True),
                    items_are_selectable=Selectable(colors=["red"]),
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
                                            r.Text(kind="text", text="Selectionne"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="les"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="articles"),
                                            r.Text(kind="text", text="."),
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
                                            r.Text(kind="text", text="La"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="maison"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="est"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="belle"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="L"),
                                            r.Text(kind="text", text="'"),
                                            r.Text(kind="text", text="école"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="est"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fermée"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="L"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="automobile"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="est"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="verte"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
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

    def test_french_elision_of_articles__with_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="Selectionne les articles.\n", attributes={})],
                wording=[d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["red"]),
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
                                            r.Text(kind="text", text="Selectionne"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="les"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="articles"),
                                            r.Text(kind="text", text="."),
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
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="La")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="maison")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="belle")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="'")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="école")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="fermée")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="’")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="automobile")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="verte")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["red"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
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

    def test_french_elision_of_articles__without_punctuation__boxed_only(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="Selectionne les articles.\n", attributes={})],
                wording=[d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
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
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Selectionne"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="les"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="articles"),
                                            r.Text(kind="text", text="."),
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
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="La")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="maison")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="belle")], boxed=True),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence", contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="'")], boxed=True
                                            ),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="école")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fermée")], boxed=True),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence", contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="’")], boxed=True
                                            ),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="automobile")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="verte")], boxed=True),
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

    def test_french_elision_of_articles__punctuation_only__boxed_only(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="Selectionne les articles.\n", attributes={})],
                wording=[d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=False, punctuation=True),
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
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Selectionne"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="les"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="articles"),
                                            r.Text(kind="text", text="."),
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
                                            r.Text(kind="text", text="La"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="maison"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="est"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="belle"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="L"),
                                            r.Text(kind="text", text="'"),
                                            r.Text(kind="text", text="école"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="est"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fermée"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="L"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="automobile"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="est"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="verte"),
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

    def test_french_elision_of_articles__with_punctuation__boxed_only(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="Selectionne les articles.\n", attributes={})],
                wording=[d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
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
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Selectionne"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="les"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="articles"),
                                            r.Text(kind="text", text="."),
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
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="La")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="maison")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="belle")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence", contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="'")], boxed=True
                                            ),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="école")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fermée")], boxed=True),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence", contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="’")], boxed=True
                                            ),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="automobile")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="verte")], boxed=True),
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
