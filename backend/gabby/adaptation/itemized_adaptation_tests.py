from . import AdaptationTestCase
from .. import deltas as d
from .. import exercises as e
from .. import renderable as r
from ..api_models import Adaptation, PredefinedMcq

# These tests follow a legacy organization, based on classes that have been deleted.
# There is some duplication because tests have been kept through refactoring.
# Tests above focus on specific features of the adaptation process.
# A reorganization would be beneficial, future me!


class ItemizedAdaptationTestCase(AdaptationTestCase):
    def test_selectable_letters(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
                    items_are_selectable={"colors": ["red"]},
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="T")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="h")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="i")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="s")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="i")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="s")]),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="t")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="h")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="e")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="w")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="o")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="r")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="d")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="i")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="n")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="g")]),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_words__plain(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["red", "blue"]},
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="This")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="is")]),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="the")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="wording")]),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_words_and_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["green", "yellow", "orange"]},
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text="This")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text="is")]
                                        ),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text=",")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text="the")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text="wording")]
                                        ),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text=".")]
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_punctuation_only(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
                    items_are_selectable={"colors": ["green", "yellow", "orange"]},
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text=",")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text=".")]
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_words__boxed(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["red", "blue"]},
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="This")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="is")]
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="the")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="wording")]
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

    def test_selectable_tokens__in_lettered_list(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="a. First list element.\nb. Second element, still in list.\nc. Third element. The last one!", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["red"]},
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="a"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="First")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="b"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Second")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="still")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="in")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="c"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Third")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="The")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="last")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="one")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="!")]),
                                    ]
                                )
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_selectable_tokens__in_numbered_list(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="1) First list element.\n2) Second element, still in list.\n3) Third element. The last one!", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["red"]},
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="1"),
                                        r.Text(kind="text", text=")"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="First")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="2"),
                                        r.Text(kind="text", text=")"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Second")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="still")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="in")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="3"),
                                        r.Text(kind="text", text=")"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Third")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="The")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="last")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="one")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="!")]),
                                    ]
                                )
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_selectable_tokens__in_bullet_list(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="◆ First list element.\n◆ Second element, still in list.\n◆ Third element. The last one!", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["red"]},
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="◆"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="First")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="◆"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Second")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="still")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="in")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="◆"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Third")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="The")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="last")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="one")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="!")]),
                                    ]
                                )
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_selectable_sentences(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(
                        insert="Affirmative sentence. Exclamative sentence! Phrase exclamative ! Interrogative sentence? Phrase interrogative ? Suspens...\n",
                        attributes={},
                    )
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
                    items_are_selectable={"colors": ["red", "blue"]},
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                r.Text(kind="text", text="Affirmative"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="sentence"),
                                                r.Text(kind="text", text="."),
                                            ],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                r.Text(kind="text", text="Exclamative"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="sentence"),
                                                r.Text(kind="text", text="!"),
                                            ],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                r.Text(kind="text", text="Phrase"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="exclamative"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="!"),
                                            ],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                r.Text(kind="text", text="Interrogative"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="sentence"),
                                                r.Text(kind="text", text="?"),
                                            ],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                r.Text(kind="text", text="Phrase"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="interrogative"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="?"),
                                            ],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[r.Text(kind="text", text="Suspens"), r.Text(kind="text", text="...")],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_manual_items__plain(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is,", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable={"colors": ["red", "blue"]},
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            contents=[r.Text(kind="text", text="is"), r.Text(kind="text", text=",")],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="the")]),
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

    def test_selectable_manual_items__boxed(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is,", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable={"colors": ["red", "blue"]},
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[r.Text(kind="text", text="is"), r.Text(kind="text", text=",")],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="the")]
                                        ),
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

    def test_boxed_words(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="This")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="is")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="the")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="wording")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
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
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["red", "green", "blue"]},
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
                                        r.Text(kind="text", highlighted="red", text="abc"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", highlighted="green", text="def"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", highlighted="blue", text="ghi"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="jkl"),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "green", "blue"], contents=[r.Text(kind="text", text="wording")]
                                        )
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_letters(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="Abcd\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
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
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="b"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="c"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="d"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_words(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
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

    def test_mcq_beside_words_and_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_sentences(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="Affirmative sentence. Exclamative sentence! Phrase exclamative ! Interrogative sentence? Phrase interrogative ? Suspens...\n",
                        attributes={},
                    )
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Affirmative"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sentence"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="Exclamative"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sentence"),
                                        r.Text(kind="text", text="!"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="Phrase"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="exclamative"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="!"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="Interrogative"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sentence"),
                                        r.Text(kind="text", text="?"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="Phrase"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="interrogative"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="?"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="Suspens"),
                                        r.Text(kind="text", text="..."),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_manual_items(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=", ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
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

    def test_mcq_below_letters(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="Abcd\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
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
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="A"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="b"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="c"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="d"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_words(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
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
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="This"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="is"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="the"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="wording"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
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

    def test_mcq_below_words_and_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
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
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="This"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="is"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text=","),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="the"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="wording"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="."),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
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
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text=","),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="."),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_sentences(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="Affirmative sentence. Exclamative sentence! Phrase exclamative ! Interrogative sentence? Phrase interrogative ? Suspens...\n",
                        attributes={},
                    )
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
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
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Affirmative"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="sentence"),
                                                        r.Text(kind="text", text="."),
                                                    ],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Exclamative"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="sentence"),
                                                        r.Text(kind="text", text="!"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Phrase"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="exclamative"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="!"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Interrogative"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="sentence"),
                                                        r.Text(kind="text", text="?"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Phrase"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="interrogative"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="?"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[r.Text(kind="text", text="Suspens"), r.Text(kind="text", text="...")],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_manual_items(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=", ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
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
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="is"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="the"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
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

    def test_mcq_below_separated_items(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Indique le genre de chacun de ces groupes nominaux (", attributes={}),
                    d.TextInsertOp(
                        insert="singulier ou pluriel",
                        attributes={"choices2": {"start": "", "separator1": "ou", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert=")\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="a. les tables / les chaises / les fauteuils\nb. les enfants / les personnes âgées / les adultes\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "separated", "separator": "/"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
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
                                        r.Text(kind="text", text="Indique"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="le"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="genre"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="de"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="chacun"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="de"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ces"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="groupes"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="nominaux"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="("),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="singulier")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="pluriel")], boxed=True),
                                        r.Text(kind="text", text=")"),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="a"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="tables"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="chaises"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fauteuils"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="b"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="enfants"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="personnes"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="âgées"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="adultes"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_gender_mcq(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="alpha bravo charlie\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
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
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=True, grammatical_number=False),
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="alpha"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="bravo"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="charlie"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_number_mcq(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="alpha bravo charlie\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
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
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=True),
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="alpha"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="bravo"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="charlie"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_gender_and_number_mcq(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="alpha bravo charlie\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=True, grammatical_number=True),
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="alpha"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="bravo"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="charlie"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_gender_and_number_mcq__single_item_per_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="alpha bravo charlie\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=True, grammatical_number=True),
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="alpha"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="bravo"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="charlie"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )
