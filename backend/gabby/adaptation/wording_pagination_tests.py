from . import AdaptationTestCase
from .. import deltas as d
from .. import exercises as e
from .. import renderable as r
from ..api_models import Adaptation, PredefinedMcq


class WordingPaginationTestCase(AdaptationTestCase):
    def test_empty(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="\n", attributes={})],
                wording=[d.TextInsertOp(insert="\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
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
            r.Exercise(number="number", textbook_page=None, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[]), wording=r.Section(paragraphs=[]))]),
        )

    def test_single_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
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
                        instructions=r.Section(paragraphs=[]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="wording")])])
                    )
                ],
            ),
        )

    def test_full_pagelet(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording 1\nwording 2\nwording 3\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
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
                        instructions=r.Section(paragraphs=[]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="1")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="2")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="3")]),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_single_paragraph_on_second_page(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording 1\nwording 2\nwording 3\n", attributes={})],
                example=[d.TextInsertOp(insert="example\n", attributes={})],
                clue=[d.TextInsertOp(insert="clue\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="1")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="2")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="3")])
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_no_pagination(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording 1\nwording 2\nwording 3\nwording 4\nwording 5\nwording 6\n", attributes={})],
                example=[d.TextInsertOp(insert="example\n", attributes={})],
                clue=[d.TextInsertOp(insert="clue\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="1")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="2")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="3")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="4")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="5")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="6")]),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_only_manual_pagination(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording 1\n\nwording 2\n\n\nwording 3\n\nwording 4\n\nwording 5\n\nwording 6\n\n", attributes={})],
                example=[d.TextInsertOp(insert="example\n", attributes={})],
                clue=[d.TextInsertOp(insert="clue\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="1")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="2")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="3")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="4")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="5")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="6")]),
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_manual_and_automated_pagination(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording 1\n\nwording 2\n\n\nwording 3\n\nwording 4\n\nwording 5\n\nwording 6\n\n", attributes={})],
                example=[d.TextInsertOp(insert="example\n", attributes={})],
                clue=[d.TextInsertOp(insert="clue\n", attributes={})],
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="1")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="2")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="3")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="4")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="5")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="6")])
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_one_letter_per_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="a b c d\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
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
                                r.Paragraph(contents=[r.Text(kind="text", text="a")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="b")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="c")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="d")]),
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_one_word_per_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="a. worda wordb\nb. wordc wordd\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
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
                                        r.Text(kind="text", text="a"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="worda"),
                                    ]
                                ),
                                r.Paragraph(contents=[r.Text(kind="text", text="wordb")]),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="b"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wordc"),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wordd")]),
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_one_punctuation_per_paragraph(self):
        # This is probably not an actual use case. But this behavior is consistent with the others, so we capture it with a test.
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="a. word, word\nb. word! word\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
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
                                        r.Text(kind="text", text="a"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="word"),
                                        r.Text(kind="text", text=","),
                                    ]
                                ),
                                r.Paragraph(contents=[r.Text(kind="text", text="word")]),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="b"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="word"),
                                        r.Text(kind="text", text="!"),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="word")])]),
                    ),
                ],
            ),
        )

    def test_one_sentence_per_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="Il fait beau. Il fait chaud. Il ne pleut pas.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
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
                                        r.Text(kind="text", text="Il"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="fait"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="beau"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Il"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="fait"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="chaud"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Il"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ne"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="pleut"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="pas"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_one_manual_item_per_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                    ],
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="the"),
                                    ],
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="wording"),
                                        r.Text(kind="text", text="."),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )
