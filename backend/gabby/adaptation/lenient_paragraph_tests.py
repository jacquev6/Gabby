from . import AdaptationTestCase
from .. import deltas as d
from .. import exercises as e
from .. import renderable as r
from ..api_models import Adaptation, TokensItems, Selectable, PredefinedMcq

# These tests follow a legacy organization, based on classes that have been deleted.
# There is some duplication because tests have been kept through refactoring.
# Tests above focus on specific features of the adaptation process.
# A reorganization would be beneficial, future me!


class LenientParagraphTestCase(AdaptationTestCase):
    def test_bold_and_italic(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(insert="This is a ", attributes={}),
                    d.TextInsertOp(insert="strict", attributes={"bold": True}),
                    d.TextInsertOp(insert=" instructions ", attributes={}),
                    d.TextInsertOp(insert="paragraph", attributes={"italic": True}),
                    d.TextInsertOp(insert=".\n\nAnd this is a ", attributes={}),
                    d.TextInsertOp(insert="lenient", attributes={"bold": True}),
                    d.TextInsertOp(insert=" instructions ", attributes={}),
                    d.TextInsertOp(insert="paragraph", attributes={"italic": True}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a ", attributes={}),
                    d.TextInsertOp(insert="strict", attributes={"bold": True}),
                    d.TextInsertOp(insert=" wording ", attributes={}),
                    d.TextInsertOp(insert="paragraph", attributes={"italic": True}),
                    d.TextInsertOp(insert=".\nAnd this is a ", attributes={}),
                    d.TextInsertOp(insert="lenient", attributes={"bold": True}),
                    d.TextInsertOp(insert=" wording ", attributes={}),
                    d.TextInsertOp(insert="paragraph", attributes={"italic": True}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
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
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", bold=True, text="strict"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", italic=True, text="paragraph"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="And"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", bold=True, text="lenient"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", italic=True, text="paragraph"),
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
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", bold=True, text="strict"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", italic=True, text="paragraph"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="And"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", bold=True, text="lenient"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", italic=True, text="paragraph"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_select_words_without_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This is a strict paragraph, with... some punctuation.\n\nAnd this, is a... lenient paragraph\n", attributes={})
                ],
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="This")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="is")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="a")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="strict")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="paragraph")]),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="with")]),
                                        r.Text(kind="text", text="..."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="some")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="punctuation")]),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="And")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="this")]),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="is")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="a")]),
                                        r.Text(kind="text", text="..."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="lenient")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="paragraph")]),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_select_words_with_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This is a strict paragraph, with... some punctuation.\n\nAnd this, is a... lenient paragraph\n", attributes={})
                ],
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
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="This")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="is")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="a")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="strict")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="paragraph")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="with")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="...")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="some")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="punctuation")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="And")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="this")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="is")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="a")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="...")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="lenient")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="paragraph")]),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_fill_with_free_text(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This is a ... strict paragraph. With some punctuation.\n\nAnd this, is a ... lenient paragraph\n", attributes={})
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
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
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="strict"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="paragraph"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="With"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="some"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="punctuation"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="And"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="lenient"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="paragraph"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_multiple_choices(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a ... strict paragraph. With some punctuation.\n\nAnd this, is a ... lenient paragraph\n", attributes={})
                ],
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
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Text(kind="text", text="."),
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
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="strict"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="paragraph"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="With"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="some"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="punctuation"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="And"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="lenient"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="paragraph"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )
