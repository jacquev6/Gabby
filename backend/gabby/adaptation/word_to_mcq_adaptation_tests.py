from . import AdaptationTestCase
from .. import deltas as d
from .. import exercises as e
from .. import renderable as r
from ..api_models import Adaptation, PredefinedMcq


class WordToMcqAdaptationTestCase(AdaptationTestCase):
    def test_words_in_sentences(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo ou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="a. Firsta ", attributes={}),
                    d.TextInsertOp(insert="firstb", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert=" firstc\nb. ", attributes={}),
                    d.TextInsertOp(insert="Seconda", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert=" secondb secondc\nc. Thirda thirdb ", attributes={}),
                    d.TextInsertOp(insert="thirdc", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.AnySequence(
                                                kind="sequence",
                                                contents=[
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="Firsta"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="firstb", highlighted="#ffff00"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="firstc"),
                                                        ],
                                                    ),
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="→"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="Firsta"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.MultipleChoicesInput(
                                                                kind="multipleChoicesInput",
                                                                choices=[
                                                                    [r.Text(kind="text", text="alpha")],
                                                                    [r.Text(kind="text", text="bravo")],
                                                                    [r.Text(kind="text", text="charlie")],
                                                                ],
                                                            ),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="firstc"),
                                                        ],
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
                                                            r.Text(kind="text", text="Seconda", highlighted="#ffff00"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="secondb"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="secondc"),
                                                        ],
                                                    ),
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="→"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.MultipleChoicesInput(
                                                                kind="multipleChoicesInput",
                                                                choices=[
                                                                    [r.Text(kind="text", text="alpha")],
                                                                    [r.Text(kind="text", text="bravo")],
                                                                    [r.Text(kind="text", text="charlie")],
                                                                ],
                                                            ),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="secondb"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="secondc"),
                                                        ],
                                                    ),
                                                ],
                                                vertical=True,
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.AnySequence(
                                                kind="sequence",
                                                contents=[
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="Thirda"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="thirdb"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="thirdc", highlighted="#ffff00"),
                                                        ],
                                                    ),
                                                    r.AnySequence(
                                                        kind="sequence",
                                                        contents=[
                                                            r.Text(kind="text", text="→"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="Thirda"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.Text(kind="text", text="thirdb"),
                                                            r.Whitespace(kind="whitespace"),
                                                            r.MultipleChoicesInput(
                                                                kind="multipleChoicesInput",
                                                                choices=[
                                                                    [r.Text(kind="text", text="alpha")],
                                                                    [r.Text(kind="text", text="bravo")],
                                                                    [r.Text(kind="text", text="charlie")],
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                vertical=True,
                                            ),
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
