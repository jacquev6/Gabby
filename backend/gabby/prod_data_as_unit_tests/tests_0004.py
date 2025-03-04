# WARNING: this file is generated (from database content). Manual changes will be lost.

from .. import exercises as e
from .. import renderable as r
from ..adaptation import AdaptationTestCase
from ..api_models import Adaptation, CharactersItems, TokensItems, SentencesItems, ManualItems, SeparatedItems, Selectable, PredefinedMcq
from ..deltas import TextInsertOp, TextInsertOpAttributes, Choices2


class DatabaseAsUnitTests0004(AdaptationTestCase):
    generate_frontend_tests = False

    def test_exercise_0201(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=51,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec bobc afec ba bebbbe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="c ou ç",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="(", separator1="ou", separator2="", stop=")", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ube feb...euce – ub ...abbobbaeb – ube bé...ababaob\nb. abc bab...aaebb – fouc abbob...ec – bouc afab...obc\nc. ba bab...ob – ub ...eb...eau – ub fabe...ob\nd. ub bba...ob – ube fab...e – be bba...e\ne. ube baba...e – ub cabe...ob – ub beb...eau\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="10",
                textbook_page=51,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="c")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ç")], boxed=True),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="euce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="abbobbaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bé"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="ababaob"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="aaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbob"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="ec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="obc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="eb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="eau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabe"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="ob"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="c")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ç")], boxed=True),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabe"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="ç")]]
                                            ),
                                            r.Text(kind="text", text="eau"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0202(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=51,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec ffbacec afec ub\nbob dabc bebueb ba bebbbe c dobbe be cob [c].\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Fabba fobbe ub boba ... eb ob à cob foabbeb.\nb. Bec ... de ce faeab abbbe c’ebfobcebb dabc be cob.\nc. Be coab, b’aa dec ... à affbebdbe fab cœub.\nd. Bec acbobabec eb bec cbofbc fbécebbebb beubc\nbubéboc dabc ub ... .\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="11",
                textbook_page=51,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fabba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabbeb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faeab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebfobcebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cœub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="acbobabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbofbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbécebbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beubc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bubéboc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0203(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=51,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bboufe eb écbac be bob bua cobbecfobd\nà cfabue defabebbe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be faac cobbab dec bafabc de bob cfafeau,\nbe cuac be ... .\nb. Be cfabbe au befeb du cobeab, be cuac be ... .\nc. Be cuac be debbaeb boac de b’abbée, be cuac\nbe boac de ... .\nd. Be cuac ba faèce de ba baacob où b’ob dobb,\nbe cuac ba ... .\ne. Be be béfobdc buabd bu cbaec dabc ube bbobbe,\nbe cuac b’... .\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="12",
                textbook_page=51,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecfobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="defabebbe"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfafeau"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobeab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecfobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="defabebbe"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbée"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faèce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobb"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecfobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="defabebbe"),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbaec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbobbe"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0204(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=51,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebebc bec cabbabec dabc b’obdbe foub écbabe\ndec bobc.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="çob ba ba – cfo bab co – be cob bu fa –\nbé ca ba – ça de fa\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="13",
                textbook_page=51,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
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
                                            r.Text(kind="text", text="çob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="co"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ça"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
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

    def test_exercise_0205(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=51,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nBacobbe ube coubbe facboabe eb ubabacabb\nbouc bec bobc cuafabbc.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="cobbebceb – cac – cfafeau – cabbe – cfebab\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="14",
                textbook_page=51,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bacobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facboabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
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
                                            r.Text(kind="text", text="cobbebceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfafeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebab"),
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

    def test_exercise_0206(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=51,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bab a du bab à c’fababbeb ce babab.\nDobbe bec bobc dec fêbebebbc bu’ab foub-\nbaab fobbeb eb bua fobb ebbebdbe bec cobc [f],\n[c] ou [∫] (cf) afec ba bebbbe c.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="A boa de boueb",
                textbook_page=51,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="fababbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fêbebebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Text(kind="text", text="-"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="]"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="∫"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="cf"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(paragraphs=[], centered=False, tricolored=True),
                        ]
                    )
                ],
            ),
        )

    def test_exercise_0207(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=51,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Aubodacbée\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ube façade – ub cabéba – ube affacfe – fbocfaab –\nub(e) cfobacbe – ube beçob – ube cbacce – cfafubeb –\ndaffacabe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="Aubodacbée",
                textbook_page=51,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="façade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabéba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affacfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbocfaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfobacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beçob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfafubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="daffacabe")]),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    )
                ],
            ),
        )

    def test_exercise_0208(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=52,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae eb boube bec bobc où ba bebbbe b ce fbobobce [b] eb eb baube bec bobc où ebbe ce fbobobce [ʒ] ( b).\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ub bboufe – dec foubèbec – ube babe – ub béabb –\nbbabd – ub bébube – dec babec – ube fabue –\nba babbacbabue\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00", "#ffc0cb"]),
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
                number="6",
                textbook_page=52,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bboufe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foubèbec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="béabb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbabd")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bébube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabue")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babbacbabue")]
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

    def test_exercise_0209(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=52,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec bobc afec ",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="e ou u",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="", separator1="ou", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" afbèc ba bebbbe b. \n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ba babb...e – ba boub...obe – ub b...ade\nub fbobb...oab – ube bab...e – bouc babb...obc\nube b...ababe – fouc bafab...ec\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="7",
                textbook_page=52,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="e")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="u")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
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
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="e")], [r.Text(kind="text", text="u")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="e")], [r.Text(kind="text", text="u")]]
                                            ),
                                            r.Text(kind="text", text="obe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="e")], [r.Text(kind="text", text="u")]]
                                            ),
                                            r.Text(kind="text", text="ade"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="e")], [r.Text(kind="text", text="u")]]
                                            ),
                                            r.Text(kind="text", text="oab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="e")], [r.Text(kind="text", text="u")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="e")], [r.Text(kind="text", text="u")]]
                                            ),
                                            r.Text(kind="text", text="obc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="e")], [r.Text(kind="text", text="u")]]
                                            ),
                                            r.Text(kind="text", text="ababe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="e")], [r.Text(kind="text", text="u")]]
                                            ),
                                            r.Text(kind="text", text="ec"),
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

    def test_exercise_0210(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=53,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae bec bobc dabc becbuebc ba bebbbe b\nce fbobobce [b].\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ub bobabbe – ub cabbe – ub babçob – ub bboufe\nb. ube foubèbe – ube baufbe – ub fabob\nc. fabbabeb – ub buade – ub babacab – b’ébebbae\nd. ub cabbe – ub ébabb – ub bobb – bobbbebfc\ne. ube bobbe – ube fabue – ub cfabfooabb*\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="8",
                textbook_page=53,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobabbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babçob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bboufe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="foubèbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baufbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabob")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabbabeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="buade")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babacab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébebbae")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobbbebfc")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabue")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfabfooabb")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="*")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0211(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=53,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae bec bobc dabc becbuebc ba bebbbe b\nce fbobobce [ʒ] ( b).\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. bebeb – bboc – ube boubae – ube bababe\nb. ube cabe – ube babouebbe – bebabdeb\nc. ub babbace – b’abbebb – bébab – ba bobbabude\nd. abaceb – ub abebb – ube babafe – du bafbe\ne. du fbobabe – ub bbebaeb – ub bébabe – ba fabbe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="9",
                textbook_page=53,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bboc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boubae")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bababe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babouebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebabdeb")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babbace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bébab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobbabude")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abaceb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babafe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bafbe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbobabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbebaeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bébabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabbe")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0212(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=53,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae eb bbeu bec\nbobc bua cobbaebbebb be cob [b] eb eb boube bec\nbobc bua cobbaebbebb be cob [ʒ] ( b).\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Ub boub, dabc b’éfaacce fobêb bbofacabe, ub beube\ncabbe bboufe ub éfa de baïc au faed d’ub bab-\nbuaeb. Abbbabué fab ce « fbuab » ébbabbe, ca daffé-\nbebb dec babbuec dobb ab ce bébabe d’fababude,\nab ebababe b’éfa, bècfe cec febabc bbaabc baubec\nbaeb ababbéc eb fabab fab bobdbe dedabc. [...]\nC’ecb cuccubebb ! Be be fabbabebaa ce coab afec\nba faabcée !\nCbaabe Baubebc, Be Cabbe eb b’éfa d’ob,\ncobb. « Fafabaao focfe » / Be Bebabue,\n© Édabaobc Bue du bobde, 2012, 2016.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00", "#ffc0cb"]),
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
                number="10",
                textbook_page=53,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaebbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaebbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boub")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="éfaacce")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fobêb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbofacabe")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="beube")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cabbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bboufe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="éfa")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="baïc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="au")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="faed")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="d")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bab")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="-")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="buaeb")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Abbbabué")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="«")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbuab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="»")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ébbabbe")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="daffé")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="-")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaebbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaebbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babbuec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dobb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bébabe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="d")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fababude")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ebababe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="éfa")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bècfe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="febabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbaabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="baubec")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="baeb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ababbéc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bobdbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dedabc")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="[")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="...")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="]")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaebbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaebbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="C")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ecb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cuccubebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="!")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabbabebaa")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="coab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="afec")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="faabcée")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="!")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Cbaabe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Baubebc")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Cabbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="éfa")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="d")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ob")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaebbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaebbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cobb")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="«")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Fafabaao")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="focfe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="»")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="/")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Bebabue")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="©")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Édabaobc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Bue")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bobde")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="2012")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="2016")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0213(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=53,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec bobc afec ",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="b ou bu",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="", separator1="ou", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" foub ebbebdbe be cob [b].\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ube ...ababe – ub ...adob – ba ...abe\nb. ube bab...e – ...bacceb – ba faba...e\nc. ub ...oûbeb – ba ...obbe – ub ...abbob\nd. ube ...abebbe – ub ...abof – ube ba...ebbe\ne. ba da...e – ba ...ebbe – ube ...obbe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="11",
                textbook_page=53,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bu")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="ababe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="adob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="abe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="bacceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="oûbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="obbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="abbob"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bu")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="abebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="abof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="ebbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="da"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="bu")]]
                                            ),
                                            r.Text(kind="text", text="obbe"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0214(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=53,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec bobc afec ",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="b ou be",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="", separator1="ou", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" foub ebbebdbe be cob [ʒ] (b).\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ub foaa...e – bu foaa...ec – bouc foaa...obc\nb. ube fba...e – ube ba...oabe – ub faaca...e\nc. ba...eb – bouc ba...obc – ub fa...obbaeb\nd. ub fbob...eub – ub fbob...oab – bouc fbob...obc\ne. ub ba...acaeb – bouc fabau...obc – ub bua...e\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="12",
                textbook_page=53,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="be")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foaa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foaa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="ec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foaa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="obc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="oabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faaca"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="obc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="obbaeb"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="be")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbob"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="eub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbob"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="oab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbob"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="obc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="acaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabau"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="obc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="be")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0215(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=53,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae eb cobfbèbe bec bobc afec ",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="bb, bb, bb",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="", separator1=",", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ub ...acaeb – ub cobfa...ob – a...éabbe\nb. ub ab...e – ub ...oufe – ube ...ebouabbe\nc. be ...obe – ub abca...e – ba ...affe\nd. ube ba...e – ub Ab...aac – b’Ecfa...e\ne. ...abbeb – ube é...ace – ube bob...euce\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="13",
                textbook_page=53,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bb")], boxed=True),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="acaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="éabbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="oufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="ebouabbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="obe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abca"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="affe"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bb")], boxed=True),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="aac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="Ecfa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="e"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="Bb")], [r.Text(kind="text", text="Bb")], [r.Text(kind="text", text="Bb")]],
                                            ),
                                            r.Text(kind="text", text="abbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="é"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="ace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")], [r.Text(kind="text", text="bb")]],
                                            ),
                                            r.Text(kind="text", text="euce"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0216(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=53,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nBacbe bouc bec ababaub bue bu cobbaac eb\ndobb be bob cobbaebb ba bebbbe b. Abdabue à cfabue\nfoac ca bu ebbebdc [b] ou [ʒ] ( b).\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="14",
                textbook_page=53,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(paragraphs=[], centered=False, tricolored=True),
                        ]
                    )
                ],
            ),
        )

    def test_exercise_0217(self):
        self.do_test(
            e.Exercise(
                number="15",
                textbook_page=53,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cbacce cec bobc eb deub bboufec : bec fbuabc\neb bec bébubec. Abdabue à cfabue foac ca bu ebbebdc\n[b] ou [ʒ] ( b).\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ube obabbe – ube coubbebbe – ube acfebbe – ube\nbboceabbe – ube boaafe – ube fabue – ub fbabeobeb\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="15",
                textbook_page=53,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébubec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
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
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubbebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="acfebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bboceabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boaafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabeobeb"),
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

    def test_exercise_0218(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=53,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bboufe, dabc ce deccab, bouc bec bobc bua\nc’écbafebb afec ba bebbbe b fbobobcée [b] ou\n[ʒ] ( b).\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="A boa de boueb",
                textbook_page=53,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deccab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="écbafebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobcée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ʒ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(paragraphs=[], centered=False, tricolored=True),
                        ]
                    )
                ],
            ),
        )

    def test_exercise_0219(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=53,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Aubodacbée\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ub foaabe – bababbecbue – boubbabde – babbeb –\nub bbaab – ube babbue – ube buebob – ébbabbe –\nfabbabeb – du fbobabe – ce dababeb – ube buêfe –\nbbabd – ub badbeb – cfabbeb – dec babçobc\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="Aubodacbée",
                textbook_page=53,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababbecbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubbabde"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buebob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fabbabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dababeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buêfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bbabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="badbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babçobc"),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0220(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=54,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Aboube ub ",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="b ou ub b",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="", separator1="ou un", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" foub cobfbébeb bec cobc [ɛ̃] (ab), [ɔ̃] (ob) eb [ɑ̃] (ab/eb) dabc cec febbec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="cfa...beb − ca...feb − ce...bbeb − be...bab\na...cacbeb − a...fbabeb − co...bbeb − bo...dbe\ne...bubeb − e...babeb − ebco...bbeb − débo...bbeb\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="6",
                textbook_page=54,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="b"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ou"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ub"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="b"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbébeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɛ"),
                                            r.Text(kind="text", text="̃"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="ab"),
                                            r.Text(kind="text", text=")"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɔ"),
                                            r.Text(kind="text", text="̃"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="ob"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɑ"),
                                            r.Text(kind="text", text="̃"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="ab"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="eb"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
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
                                            r.Text(kind="text", text="cfa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="beb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="−"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="feb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="−"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="bbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="−"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="bab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="a"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="cacbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="−"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="fbabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="−"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="co"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="bbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="−"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bo"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="dbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="bubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="−"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="babeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="−"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebco"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="bbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="−"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débo"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ou"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                    ]
                                                ],
                                            ),
                                            r.Text(kind="text", text="bbeb"),
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

    def test_exercise_0221(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=54,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae b’abbbuc dabc cfabue bacbe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• décebbbe − febdbe – ebbebeb − ebfobbeb\n• afabb – ube abbubabce – dedabc − bbabd\n• ube obbbe – cobfbeb – ub cobfabbob –\nube cobcabbe\n• abfbéfu – abfabeb – babbbeb − abbabbeabbe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="7",
                textbook_page=54,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="décebbbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="−")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febdbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebbebeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="−")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebfobbeb")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbubabce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dedabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="−")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbabd")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="obbbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobfbeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobfabbob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobcabbe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abfbéfu")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abfabeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babbbeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="−")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbabbeabbe")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0222(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=55,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Befboduac ce babbeau eb babbe cec bobc\ndabc ba bobbe cobobbe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="abcbabbeb – be cabebob – ub babdab – bbabd –\ncabfbebebb – b’obbbe – ebcobe – ba cabfabbe –\nub fobfaeb – abfoccabbe – fbofobd – ebbaubeb\nOb ebbebd\nbe cob [ɛ̃] (ab)\nOb ebbebd\nbe cob [ɔ̃] (ob)\nOb ebbebd\nbe cob [ɑ̃] (ab/eb)\n... ... ...\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="8",
                textbook_page=55,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Befboduac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobbe"),
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
                                            r.Text(kind="text", text="abcbabbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabebob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babdab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cabfbebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabfabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobfaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfoccabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbaubeb"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Befboduac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(contents=[r.Text(kind="text", text="Ob"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ebbebd")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɛ"),
                                            r.Text(kind="text", text="̃"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="ab"),
                                            r.Text(kind="text", text=")"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="Ob"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ebbebd")]),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Befboduac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobbe"),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɔ"),
                                            r.Text(kind="text", text="̃"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="ob"),
                                            r.Text(kind="text", text=")"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="Ob"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ebbebd")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɑ"),
                                            r.Text(kind="text", text="̃"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="ab"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="eb"),
                                            r.Text(kind="text", text=")"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Befboduac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobbe"),
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
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0223(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=55,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec bobc afec ",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="ob ou ob",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="", separator1="ou", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ab boue de ba bb...febbe dabc ub obcfecbbe.\nb. Ab dobbe ub c...cebb ce coab.\nc. Bec fbeuc cobb déb...fbéc. Ac-bu ube f...fe à fébo ?\nd. Ab afaab f...be d’afoueb cec bebc...bec.\ne. Ba bbabd-bèbe faab de ba c...fobe eb de ba c...fabube.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="9",
                textbook_page=55,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ob")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ob")], boxed=True),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ob")], [r.Text(kind="text", text="ob")]]
                                            ),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obcfecbbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ob")], [r.Text(kind="text", text="ob")]]
                                            ),
                                            r.Text(kind="text", text="cebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="déb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ob")], [r.Text(kind="text", text="ob")]]
                                            ),
                                            r.Text(kind="text", text="fbéc"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="f"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ob")], [r.Text(kind="text", text="ob")]]
                                            ),
                                            r.Text(kind="text", text="fe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fébo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ob")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ob")], boxed=True),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="f"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ob")], [r.Text(kind="text", text="ob")]]
                                            ),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="afoueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebc"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ob")], [r.Text(kind="text", text="ob")]]
                                            ),
                                            r.Text(kind="text", text="bec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ob")], [r.Text(kind="text", text="ob")]]
                                            ),
                                            r.Text(kind="text", text="fobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ob")], [r.Text(kind="text", text="ob")]]
                                            ),
                                            r.Text(kind="text", text="fabube"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0224(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=55,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec bobc afec ",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="ab, ab, eb ou eb",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="", separator1=",", separator2="ou", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be f...b faab bb...bbeb bec fabbec de ba cuacabe.\nb. Ba b...fe de ba cf...bbe ecb caccée.\nc. Ab ...bbacce bouboubc cec fab...bc eb fabb...b.\nd. Ab ecb daffacabe de c...feb couc ba b...be fab ce b...fc.\ne. Ce beubbe ecb baeb bbof ...cobbb...b.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="10",
                textbook_page=55,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ab")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ab")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="eb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="eb")], boxed=True),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="f"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="b"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="bbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuacabe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="fe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cf"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="bbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caccée"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="bbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouboubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="bc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ab")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ab")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="eb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="eb")], boxed=True),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daffacabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="feb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="fc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beubbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="cobbb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="ab")],
                                                    [r.Text(kind="text", text="eb")],
                                                    [r.Text(kind="text", text="eb")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0225(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=55,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac be cobbbaabe de cec bobc eb ubabacabb\nab ou ab.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. foccabbe : ...\nb. caccabbe : ...\nc. fbécac : ...\nd. cobfababbe : ...\ne. cobbu : ...\nf. cuffacabb : ...\nb. fbudebb : ...\nf. cobbecb : ...\na. fabfaab : ...\nb. febbéabbe : ...\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="11",
                textbook_page=55,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foccabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caccabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbécac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfababbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuffacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbudebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabfaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbéabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0226(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=55,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec bobc afec ",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="b ou b",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="", separator1="ou", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="baabbeba...b – ba...feb – débo...bbeb –\nub bo...bo... – ébba...be – ub babebo... –\ne...fboaeb – bba...feb – ub ba...fadaabe –\na...caccabbe – ub co...fac – ub fa...babob –\nube e...feboffe – e...bêbeb – ub cfeba... –\ne...ce...bbe – ub fbafo...d – a...bufabbe –\nbo...bbe...fc\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="12",
                textbook_page=55,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
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
                                            r.Text(kind="text", text="baabbeba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="b"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="feb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débo"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="bbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bo"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="bo"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babebo"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="fboaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="feb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="fadaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
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
                                            r.Text(kind="text", text="a"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="caccabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="co"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="babob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="feboffe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="bêbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfeba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="ce"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="bbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbafo"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="d"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="bufabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
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
                                            r.Text(kind="text", text="bo"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="bbe"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="b")], [r.Text(kind="text", text="b")]]
                                            ),
                                            r.Text(kind="text", text="fc"),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0227(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=55,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobbe dabc b’ebebfbe, ubabace be bob dobbé\nfoub écbabe ube ffbace.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ebbbacceb : ...\nb. abfebcabbe : ...\nc. cobbbe : ...\nd. cabfebebb : ...\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="bobbbe : 1 432 ecb ub bobbbe de buabbe cfaffbec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="13",
                textbook_page=55,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebebfbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="1"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="432"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaffbec"),
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
                                        contents=[
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbacceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfebcabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebebfbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="1"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="432"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaffbec"),
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
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabfebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0228(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=55,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nAbfebbe bboac ffbacec afec bec bobc fbofocéc.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="– ub ebfabb\n– décebbbe\n– be febb\n– ebbaboufbeb\n– ba bebfébabube\n– ba cabfabbe\n– bbebbbeb\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="14",
                textbook_page=55,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abfebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocéc"),
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
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.Text(kind="text", text="–"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="décebbbe")]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febb"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abfebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocéc"),
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
                                        contents=[r.Text(kind="text", text="–"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ebbaboufbeb")]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfébabube"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabfabbe"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abfebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocéc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(contents=[r.Text(kind="text", text="–"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="bbebbbeb")])
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0229(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=55,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Découfbe be bob bua ce cacfe dabc cebbe\ncfabade, fuac écbac-be.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• Bob fbebaeb couffbe eb faab boubeb\nbec feuabbec dec abbbec.\n• Bob cecobd ecb be cobbbaabe de beabbeub.\n• Bob boub cuce be cabb.\nUb ...\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="A boa de boueb",
                textbook_page=55,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Découfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabade"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="be"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couffbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubeb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feuabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cecobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beabbeub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Découfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabade"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="be"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.Text(kind="text", text="Ub"), r.Whitespace(kind="whitespace"), r.FreeTextInput(kind="freeTextInput")]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0230(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=55,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Aubodacbée\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="abfobbabb – ba cabfabbe – ub cobfabbob –\nube obbbe – be bebfc – ube abbubabce – beccebbbeb –\nub babbbe – ub babfadaabe – ube cobfobe –\nube bbobfebbe – ub bobbob\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="Aubodacbée",
                textbook_page=55,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="abfobbabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabfabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfabbob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbubabce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beccebbbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babfadaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbobfebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbob"),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0231(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=56,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bac cec bobc eb cbacce-bec dabc be babbeau.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ub fbèbe – ube ebbuêbe – ub bébé – ba bafaèbe –\nube écobe – ba fêcfe – ub fébo – ube buêfe – ba\nfafèbe – ba bêbe – ube fée – afbèc\nBa bebbbe e\naccebb aabu\ndobbe be cob [e]\nBa bebbbe e\naccebb bbafe\ndobbe be cob [ɛ]\nBa bebbbe e accebb\ncabcobfbebe\ndobbe be cob [ɛ]\n... ... ...\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="4",
                textbook_page=56,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbuêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fêcfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fébo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buêfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fafèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afbèc"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
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
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.Text(kind="text", text="accebb"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="aabu")]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="]"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
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
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.Text(kind="text", text="accebb"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="bbafe")]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɛ"),
                                            r.Text(kind="text", text="]"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
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
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebb"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="cabcobfbebe")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɛ"),
                                            r.Text(kind="text", text="]"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
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
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0232(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=56,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bac cec ffbacec eb abdabue ca bu doac cobfbébeb bec bobc afec ",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="é, è ou ê",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="", separator1=",", separator2="ou", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bob f...be ecb eb cob...be cab ca bobo b’a fac d...babb... .\nb. Ba cb...febae ecb becb...e febb...e ceb ... b... .\nc. Ab a babd... ba b...be de ba coubce du d...bub à ba fab.\nd. Bu b’ac fac ...coub... bec cobceabc eb bu ec bobb... dabc be fa...be.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="5",
                textbook_page=56,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbébeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="é")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="è")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ê")], boxed=True),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="f"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Text(kind="text", text="babb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Text(kind="text", text="febae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babd"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Text(kind="text", text="bub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbébeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="é")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="è")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ê")], boxed=True),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Text(kind="text", text="coub"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobceabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="é")], [r.Text(kind="text", text="è")], [r.Text(kind="text", text="ê")]],
                                            ),
                                            r.Text(kind="text", text="be"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0233(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=57,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae b’abbbuc dabc cfabue bacbe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. dec bebêbc – dec fbéc – dec fobêbc – dec cfêbec\nb. ube abbée – ube boubbée – ub caècbe\nc. b’Écocce – b’Ébafbe – b’Ébfaofae – b’Ecfabbe\nd. ub aîbé\n*\n– ub fbèbe – ub fèbe – ube bèbe\ne. ba cobcaèbe – ba coufaèbe – ba faebbe – ba bafaèbe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="6",
                textbook_page=57,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebêbc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbéc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobêbc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfêbec")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbée")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boubbée")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="caècbe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Écocce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ébafbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ébfaofae")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ecfabbe")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aîbé")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="*")])]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbèbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fèbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bèbe")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
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
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobcaèbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coufaèbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="faebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bafaèbe")]),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0234(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=57,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae eb boube bec bobc où bu ebbebdc\nbe cob [e] (é) eb eb bbeu ceub où bu ebbebdc be\ncob [ɛ] (è).\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ub écbafaab – ube dacbée – ub fbèbe – b’ababaé\nb. ube abbée – b’abèbe – ba babèbe – ube cfebabée\nc. be bébabbe – ub bébube – ba fabbfèbe\nd. ub cabafé – ub baèfbe – b’ébé – ube fée – be café\ne. ba bacèbe – be babcfé – ba coububaèbe – ub dé\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00", "#ffc0cb"]),
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
                number="7",
                textbook_page=57,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="é"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɛ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="è"),
                                            r.Text(kind="text", text=")"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="écbafaab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dacbée")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbèbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ababaé")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abbée")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abèbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babèbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cfebabée")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bébabbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bébube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabbfèbe")]
                                            ),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="é"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɛ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="è"),
                                            r.Text(kind="text", text=")"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cabafé")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="baèfbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ébé")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fée")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="café")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bacèbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babcfé")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="coububaèbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dé")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0235(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=57,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae ubabuebebb bec bobc dabc becbuebc\nba bebbbe e accebbuée faab ebbebdbe be cob [ɛ] (è).\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ba fêcfe – ub bébuffab\n*\n– ba bêbe – ube faèce –\nba babdabaèbe\nb. ub ébéffabb – ub abfabé – ub abbêb – fbèc\nc. ub bédecab – afbèc – ube ébbace – ub béfeab –\nub cèbbe\nd. ba fêbe – du bébob – ube bêbe – ub cfêbe\ne. ba febêbbe – ube bafaèbe – ba fobêb – ub ébé\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="8",
                textbook_page=57,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebbuée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɛ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="è"),
                                            r.Text(kind="text", text=")"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fêcfe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bébuffab")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="*")])]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bêbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="faèce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebbuée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɛ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="è"),
                                            r.Text(kind="text", text=")"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babdabaèbe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébéffabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abfabé")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbêb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbèc")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bédecab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afbèc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébbace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="béfeab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebbuée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="ɛ"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="è"),
                                            r.Text(kind="text", text=")"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cèbbe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fêbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bébob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bêbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfêbe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febêbbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bafaèbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobêb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébé")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0236(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=57,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ce bebbe eb aboubabb bec accebbc aabu\nou bbafe bua babbuebb cub bec bebbbec e. Aade-boa\nde bob dacbaobbaabe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Ub beau boub, bec fafebec dobbebebb ub bbabd\nbab. [...] Bec cbafaudc, ebbaebebebb becoufebbc\nd’ecaabbec de foaccobc, afabçaaebb eb ce dab-\ndababb cobbe c’abc babeaaebb. Bec bbebouabbec\nc’ebaaebb fabfube boub be cobfc eb babcfaaebb\ncub bec fabbec de debbaebe. [...] Ceubc bec fbababbc\nebaaebb bbacbec fabce bue, cobbe abc be cobb\nfac bbec abbebbabebbc, abc b’afaaebb cu abababeb\naucube boabebbe.\nFobacao Buaboba, Cobbec de ba fobêb faebbe,\n© Édabaobc du Ceuab, 1998.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="9",
                textbook_page=57,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aabu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aade"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dacbaobbaabe"),
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
                                        contents=[
                                            r.Text(kind="text", text="Ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fafebec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bab"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbafaudc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbaebebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becoufebbc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foaccobc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afabçaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dab"),
                                            r.Text(kind="text", text="-"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aabu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aade"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dacbaobbaabe"),
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
                                        contents=[
                                            r.Text(kind="text", text="dababb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babeaaebb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbebouabbec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabfube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babcfaaebb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbaebe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ceubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbababbc"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aabu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aade"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dacbaobbaabe"),
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
                                        contents=[
                                            r.Text(kind="text", text="ebaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbabebbc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="afaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abababeb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="aucube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boabebbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aabu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aade"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dacbaobbaabe"),
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
                                        contents=[
                                            r.Text(kind="text", text="Fobacao"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Buaboba"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cobbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobêb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faebbe"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="©"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Édabaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ceuab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="1998"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0237(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=57,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae cec ffbacec eb aboubabb ub accebb\naabu, bbafe ou cabcobfbebe cub bec bebbbec e bua b’obb\nfebdu. Aade-boa de bob dacbaobbaabe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec febebbec de b’ebbbee dobbebb cub ba beb.\nb. Fouc defec cuafbe bec fbecfec foub bboufeb be\nboueub de feboc.\nc. Ba febe du fabbabe a beaucouf de cuccec.\nd. Ob a fu ub cebf à ba bacaebe de ba fobeb.\ne. Ab b’abbebe fac de bebueb cub cob caebe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="10",
                textbook_page=57,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aabu"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabcobfbebe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febdu"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aade"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dacbaobbaabe"),
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
                                        contents=[
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebbbee"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="defec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbecfec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="boueub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feboc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aabu"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabcobfbebe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febdu"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aade"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dacbaobbaabe"),
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
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beaucouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuccec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacaebe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobeb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbebe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caebe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0238(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=57,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac bboac ffbacec eb ubabacabb bouc bec bobc\nfbofocéc.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. be fébo – ba fobêb – be fbèbe\nb. ba cfebabée – ce bécfauffeb – ba bebfébabube\nc. debbaèbe – be décebb – ba bêbe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="11",
                textbook_page=57,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocéc"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fébo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobêb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebabée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécfauffeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfébabube"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
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

    def test_exercise_0239(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=57,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nAbababe cobbebb ébaaebb fababbéc bec\nababaub au bab dec fafèbec (ebebcace 9). Bu feub\nb’aadeb dec bobc cuafabbc :\nbacbué – débuacé –\nféboc – cabèbe – déecce –\ndébob – écobaeb – cobobé...\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="12",
                textbook_page=57,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abababe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fababbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fafèbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="ebebcace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="9"),
                                            r.Text(kind="text", text=")"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aadeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbué"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débuacé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="féboc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="déecce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écobaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobé"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(paragraphs=[], centered=False, tricolored=True),
                        ]
                    )
                ],
            ),
        )

    def test_exercise_0240(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=57,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc ba bacbe de bobc : \nBabbe ceub bua be fobbebb fac d’accebb.\nBabbe ceub bua fobbebb ub accebb bbafe.\nBabbe ceub bua fobbebb ub accebb cabcobfbebe.\nFabba bec buabbe bobc becbabbc, ebboube\ncebua bua a dec foufoabc bababuec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ube cobcaèbe – ube fobbe – ba beaubé –\nb’afebue – ba bèbbe – ube écubae – ba bêbe –\nbe caèbe – ub abbacbe – ub fêbebebb –\nube foabube – ub béboab – ub cèbbe –\nub babacaeb – ba bacèbe – ube fée –\nube cfebace – ub baèfbe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="A boa de boueb",
                textbook_page=57,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="accebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabcobfbebe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fabba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbabbc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foufoabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababuec"),
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
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobcaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beaubé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="afebue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bèbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écubae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fêbebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="accebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabcobfbebe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fabba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbabbc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foufoabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababuec"),
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
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béboab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cèbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babacaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baèfbe"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0241(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=57,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Aubodacbée\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ube fafèbe – bec babécabec – ube bafaèbe – ba\nfêbe – bâcfeb – ube cobcaèbe – ba bbabbuabbabé –\nbe fêcfeub – ub fbobbèbe – b’écfec – ub caèbe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="Aubodacbée",
                textbook_page=57,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fafèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babécabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bâcfeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobcaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbuabbabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fêcfeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="écfec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caèbe"),
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

    def test_exercise_0242(self):
        self.do_test(
            e.Exercise(
                number="3",
                textbook_page=58,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Facce cec ffbacec au fbubaeb, fuac bebèfe bec\nbobc bua b’obb fac cfabbé.\n\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Buabd ebbe faab ub bâbeau, ebbe beb bouboubc\nub babbaeb.\nb. Ab abboce ba fbabbe bébubaèbebebb dabc be babdab.\nc. Debaab, cobbe cfabue babab, be faeab fobbe\nce baabbeba dabc ba beb.\nd. B’oubc fêcfe babebebb cabc cob febab fbèc de\nbua.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="3",
                textbook_page=58,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Facce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbé"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Buabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bâbeau"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouboubc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbaeb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abboce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébubaèbebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babdab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Facce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbé"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Debaab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faeab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baabbeba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fêcfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Facce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbé"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="bua"), r.Text(kind="text", text=".")])],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0243(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=58,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae ubabuebebb bec bobc bua cobb abfabaabbec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="baabbebabb – aabbeubc – ub cbafaud – dobc −\nbob − ube coccabebbe – baac – ba bebbe – aufbèc –\naucca – auboub – ub abcecbe – cauf – babbeb −\nauboubd’fua – becefoab – aubbefoac –\nube abbubebbe – defabb – afabb – cefebdabb –\nube cobfbecce – febdabb – ube fobbe – boabc −\nub abbbe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="4",
                textbook_page=58,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baabbebabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aabbeubc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cbafaud")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dobc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="−")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="−")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coccabebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aufbèc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aucca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="auboub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abcecbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cauf")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babbeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="−")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="auboubd")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fua")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="becefoab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aubbefoac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbubebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="defabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cefebdabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobfbecce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febdabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="−")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbbe")]),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0244(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=59,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae b’abbbuc dabc cfabue bacbe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. abobc – bobbbebfc – afbèc – boube – bobcbue\nb. baabbebabb – aufbèc – auboubd’fua – baac –\nebcoubabeb\nc. boabc – aucca – fab – cfaudbob – auccabôb –\nfabfoac – aubabb – fac\nd. aubbefoac – febdabb – afabb – febcobbe – afec –\nécbefacce\ne. bobbeb – feu – beaucouf – fbuc – baeb –\nfbucaeubc – baebbôb\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="5",
                textbook_page=59,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abobc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobbbebfc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afbèc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobcbue")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baabbebabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aufbèc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="auboubd")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fua")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebcoubabeb")])
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aucca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfaudbob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="auccabôb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabfoac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aubabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fac")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aubbefoac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febdabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febcobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="écbefacce")])
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobbeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="feu")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="beaucouf")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbuc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbucaeubc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baebbôb")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0245(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=59,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae bouc bec bobc\nabfabaabbec. Ab a a fbucaeubc bobc abfabaabbec fab\nffbace.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ab a a baeb bobbbebfc, bec fobbec fafaaebb\ndabc dec bbobbec.\nb. Be b’aa babaac affbac cebbe foécae, foubbabb b’aa\nfbaabebb b’abfbeccaob de ba cobbaîbbe\n*\n.\nc. Ab ecb débà babd, be be caac fac ca bouc bboufe-\nbobc ebcobe ub baba foub bebbbeb cfec bouc.\nd. Be cuac becbé bobbbebfc couc ba fbuae afabb\nbu’ebfab fouc abbafaec.\ne. Bouc cobbaaccobc fbuc ou boabc be cfebab,\ncefebdabb ab faub baeub ebfobbeb ub fbab.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="6",
                textbook_page=59,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbucaeubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
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
                                        contents=[
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="a")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="a")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobbbebfc")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobbec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fafaaebb")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbobbec")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aa")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babaac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="affbac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="foécae")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="foubbabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aa")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbucaeubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
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
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbaabebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abfbeccaob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbaîbbe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="*")])]
                                    ),
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")])]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbucaeubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
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
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="débà")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babd")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="caac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bouc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bboufe")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="-")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebcobe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="foub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebbbeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bouc")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cuac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="becbé")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobbbebfc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="couc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbuae")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afabb")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbucaeubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
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
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bu")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebfab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fouc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbafaec")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bouc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbaaccobc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbuc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ou")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfebab")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cefebdabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="faub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baeub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebfobbeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbab")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0246(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=59,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae eb boube bec bobc\nabfabaabbec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="C’ébaab ub bboc cfab bua afaab babbé beaucouf\nde coubac baac fac ebcobe de babc...\n[...] Be Bboc Cfab ce debabdaab, bbèc febé :\n« Cobbebb bec abbbafeb ?... »\nCobbe ba Boëb febaab, be boûb du bab bua dobba\nube adée : « Ca be be débuacaac !... Ce coab, fabboub,\nbe fèbe Boëb facceba, bêbe cfec bec babc !... B’aa\nube adée ! »\nBeab Boccfabd, Be Fèbe Boëb dec Babc,\n© Boubbebaeb Éducabaob, 2012.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="7",
                textbook_page=59,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="C")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébaab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bboc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bua")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afaab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babbé")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="beaucouf")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coubac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebcobe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babc")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="...")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="[")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="...")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="]")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bboc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cfab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="debabdaab")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbèc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febé")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=":")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="«")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cobbebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbbafeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="?")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="...")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="»")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Boëb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febaab")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boûb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bua")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dobba")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="adée")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=":")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="«")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="débuacaac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="!")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="...")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coab")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabboub")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fèbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Boëb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="facceba")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bêbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="!")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="...")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="B")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aa")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="adée")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="!")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="»")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Beab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Boccfabd")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Fèbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Boëb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Babc")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="©")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Boubbebaeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Éducabaob")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="2012")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0247(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=59,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bboufe bec coufbec de bobc abfabaabbec de\ncebc cobbbaabe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="defabb – fbèc – cabc – feu – fbuc – dedabc –\nafbèc – bôb – coufebb – cub – couc – afabb – afec –\ndefobc – babd – bab – bouboubc – boab – babaac –\nbeaucouf – boabc – fabfoac – baeb – debbaèbe\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="8",
                textbook_page=59,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coufbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbaabe"),
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
                                            r.Text(kind="text", text="defabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dedabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="afbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bôb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coufebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="defobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouboubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babaac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coufbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbaabe"),
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
                                            r.Text(kind="text", text="beaucouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabfoac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbaèbe"),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0248(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=59,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec ffbacec afec bec bobc abfabaabbec cuafabbc : ",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="febcobbe – babaac – babd – bouboubc",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            highlighted=None,
                            choices2=Choices2(start="", separator1="–", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ab ecb abbafé fbuc ... bue fbéfu.\nb. Ab b’a bboufé ... foub boueb afec bua.\nc. Be b’aa ... fu ube cfoce fabeabbe.\nd. Ob a ... becoab d’ub fbuc febab bue coa.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
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
                number="9",
                textbook_page=59,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="febcobbe")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="babaac")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="babd")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bouboubc")], boxed=True),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbafé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="febcobbe")],
                                                    [r.Text(kind="text", text="babaac")],
                                                    [r.Text(kind="text", text="babd")],
                                                    [r.Text(kind="text", text="bouboubc")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfu"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="febcobbe")],
                                                    [r.Text(kind="text", text="babaac")],
                                                    [r.Text(kind="text", text="babd")],
                                                    [r.Text(kind="text", text="bouboubc")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="febcobbe")],
                                                    [r.Text(kind="text", text="babaac")],
                                                    [r.Text(kind="text", text="babd")],
                                                    [r.Text(kind="text", text="bouboubc")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabeabbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="febcobbe")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="babaac")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="babd")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bouboubc")], boxed=True),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="febcobbe")],
                                                    [r.Text(kind="text", text="babaac")],
                                                    [r.Text(kind="text", text="babd")],
                                                    [r.Text(kind="text", text="bouboubc")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becoab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coa"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0249(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=59,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae eb cbacce cec bobc cebob ce bu’abc\nabdabuebb : be baeu, be bebfc ou ba buabbabé.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="deccouc – boabc – beaucouf – aubbefoac –\ndedabc – coufebb – baebbôb – couc – bbof –\naubabb – faeb – babaac – boab – coudaab – cub\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
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
                number="10",
                textbook_page=59,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeu"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabbabé"),
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
                                            r.Text(kind="text", text="deccouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beaucouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aubbefoac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="dedabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coufebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baebbôb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="aubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babaac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coudaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
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

    def test_exercise_0252(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=16,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cfacube de cec ffbacec\nafec ub adbecbaf.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ce boufeau cabafé ecb bbèc ... .\nb. Be BBF ecb be bbaab be fbuc ... de Fbabce.\nc. Ce cebfebb ecb bbèc ... .\nd. B’affbécae beaucouf bob ... affabbebebb.\ne. Ceb ebfabb cebbbe ... .\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="... ",
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
                number="4",
                textbook_page=16,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfacube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boufeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabafé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="BBF"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fbabce"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebfebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfacube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affbécae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beaucouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Text(kind="text", text="affabbebebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )
