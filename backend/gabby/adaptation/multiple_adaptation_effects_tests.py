from . import AdaptationTestCase
from .. import deltas as d
from .. import exercises as e
from .. import renderable as r
from ..api_models import Adaptation, TokensItems, Selectable, PredefinedMcq

# These tests follow a legacy organization, based on classes that have been deleted.
# There is some duplication because tests have been kept through refactoring.
# Tests above focus on specific features of the adaptation process.
# A reorganization would be beneficial, future me!


class MultipleAdaptationEffectsTestCase(AdaptationTestCase):
    def test_fill_with_free_text_and_multiple_choices_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="short/long", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="The wording of this ... is a @@@ sentence.\n", attributes={})],
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
                textbook_page=42,
                pagelets=[
                    r.LegacyPagelet(
                        instructions=r.LegacySection(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="short")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="long")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.LegacySection(
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
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="short")], [r.Text(kind="text", text="long")]],
                                            show_choices_by_default=False,
                                        ),
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

    def test_multiple_choices_in_instructions_and_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Choose wisely ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(insert="a/b/c", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.TextInsertOp(insert=" B ", attributes={}),
                    d.TextInsertOp(insert="d/e", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.TextInsertOp(insert=" C @@@.\n", attributes={}),
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
                textbook_page=42,
                pagelets=[
                    r.LegacyPagelet(
                        instructions=r.LegacySection(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
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
                        wording=r.LegacySection(
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
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="C"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
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

    def test_many_adaptations_in_same_exercise(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.TextInsertOp(insert="Choose wisely ", attributes={}),
                    # Multiple choices in instructions
                    d.TextInsertOp(
                        insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}
                    ),
                ],
                wording=[
                    d.TextInsertOp(insert="Hello @@@ $$$ ....", attributes={}),
                    # Multiple choices in wording
                    d.TextInsertOp(
                        insert="(charlie|delta)",
                        attributes={"choices2": {"start": "(", "separator1": "|", "separator2": "", "stop": ")", "placeholder": "$$$"}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "yellow"]),
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
                    r.LegacyPagelet(
                        instructions=r.LegacySection(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.LegacySection(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "yellow"], boxed=True, contents=[r.Text(kind="text", text="Hello")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="charlie")], [r.Text(kind="text", text="delta")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )
