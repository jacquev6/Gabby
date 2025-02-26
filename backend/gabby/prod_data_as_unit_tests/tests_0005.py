# WARNING: this file is generated (from database content). Manual changes will be lost.

from .. import exercises as e
from .. import renderable as r
from ..adaptation import AdaptationTestCase
from ..api_models import Adaptation, CharactersItems, TokensItems, SentencesItems, ManualItems, Selectable, PredefinedMcq
from ..deltas import TextInsertOp, TextInsertOpAttributes, Choices2


class DatabaseAsUnitTests0005(AdaptationTestCase):
    generate_frontend_tests = False

    def test_exercise_0255(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec ffbacec afec bec bobc\nde bébabaob bua babbuebb : ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="b’, be, ba",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1=",", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Eb cebbbe-fabbe, ob ... bboufe ... foabubec ... bâbabebbc bécebbc.\nb. Ce buabbaeb ... a fac ébé bébofé.\nc. Bec abbeubbec ... cobb fac becbaubéc.\nd. Ab ... a a fac beaucouf d’abbbec dabc cebbe fabbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                textbook_page=15,
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence", contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")], boxed=True
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="be")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ba")], boxed=True),
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
                                            r.Text(kind="text", text="Eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbbe"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fabbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bâbabebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécebbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabbaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébofé"),
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
                                            r.Text(kind="text", text="abbeubbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbaubéc"),
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence", contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")], boxed=True
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="be")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ba")], boxed=True),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beaucouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbe"),
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

    def test_exercise_0257(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="bbaba\nÉcbac cec ffbacec à ba fobbe bébabafe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="b. Ab becfecbe bec bèbbec du beu.\nc. Baac oua, be be becobbaac !\nd. Abeb cobfbebd Bab.\ne. Ababe-be !\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="7",
                textbook_page=15,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bbaba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
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
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becfecbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bèbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beu"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oua"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becobbaac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbebd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bab"),
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
                                            r.Text(kind="text", text="bbaba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
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
                                            r.Text(kind="text", text="Ababe"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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

    def test_exercise_0259(self):
        self.do_test(
            e.Exercise(
                number="2",
                textbook_page=16,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae bec ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="bobc ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=1),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="eb bec ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="febbec",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=2),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nde ce bebbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Eb 1973, bec faac fboducbeubc de fébbobe\ndécadebb bbucbuebebb de bababeb beub\nfboducbaob. Be fbab du fébbobe c’ebfobe : c’ecb\nbe fbebaeb cfoc fébbobaeb. Be boufebbebebb\nfbabçaac babce ba cobcbbucbaob de 7 cebbbabec\nbucbéaabec foub bebfbaceb bec cebbbabec\nébecbbabuec cbaccabuec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
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
                number="2",
                textbook_page=16,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", highlighted="#ffff00", text="bobc"),
                                            r.Whitespace(kind="whitespace", highlighted="#ffff00"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", highlighted="#ffc0cb", text="febbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="1973")]
                                            ),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="faac")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fboducbeubc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fébbobe")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="décadebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbucbuebebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bababeb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="beub")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fboducbaob")]
                                            ),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fébbobe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                contents=[r.Text(kind="text", text="c"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ebfobe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                contents=[r.Text(kind="text", text="c"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ecb")]
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
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", highlighted="#ffff00", text="bobc"),
                                            r.Whitespace(kind="whitespace", highlighted="#ffff00"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", highlighted="#ffc0cb", text="febbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbebaeb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cfoc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fébbobaeb")]
                                            ),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boufebbebebb")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbabçaac")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babce")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cobcbbucbaob")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="7")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cebbbabec")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bucbéaabec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bebfbaceb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cebbbabec")]
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
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", highlighted="#ffff00", text="bobc"),
                                            r.Whitespace(kind="whitespace", highlighted="#ffff00"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", highlighted="#ffc0cb", text="febbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
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
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ébecbbabuec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cbaccabuec")]
                                            ),
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

    def test_exercise_0260(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Béfobdc bébabafebebb eb\nebfboaabb ba doubbe bébabaob ba ... ba.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Fac-bu à b’écobe eb fababc ou à fébo ?\n--> ...\nb. Ac-bu bu Fabba Fobbeb eb Cfabbae eb\nba cfocobabebae ?\nc. Fbebdc-bu du bfé ou du cfocobab\nfoub be febab-débeubeb ?\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Aabec-bu be cfou-fbeub eb bec éfababdc ?\n➞\nBe b’aabe ba be cfou-fbeub ba bec éfababdc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="6",
                textbook_page=15,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Béfobdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfboaabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doubbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="ba"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aabec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfou"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fbeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="éfababdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfou"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fbeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="éfababdc"),
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
                                            r.Text(kind="text", text="Fac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="écobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fababc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fébo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text=">"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fabba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cfabbae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
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
                                            r.Text(kind="text", text="Béfobdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfboaabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doubbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="ba"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aabec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfou"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fbeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="éfababdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfou"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fbeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="éfababdc"),
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
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfocobabebae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fbebdc"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bfé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfocobab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="débeubeb"),
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
                ],
            ),
        )

    def test_exercise_0261(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=26,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebfbace be fbobob febcobbeb eb\nbbac fab ub bboufe bobabab de bob cfoab.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ebbe a febdu ca bboucce.\nb. Ab a fu be fabb bboac foac.\nc. Bouc faacobc be cfebab bouc bec boubc.\nd. Abc obb dec féboc boub beufc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Ab baffobbeba be bafbe.\n➞\nCob fbèbe baffobbeba\nbe bafbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                textbook_page=26,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebfbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baffobbeba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baffobbeba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafbe"),
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
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febdu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboucce"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foac"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faacobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubc"),
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
                                            r.Text(kind="text", text="Bebfbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baffobbeba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baffobbeba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafbe"),
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
                                            r.Text(kind="text", text="Abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="féboc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beufc"),
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

    def test_exercise_0263(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec ffbacec afec bec bobc\nde bébabaob bua babbuebb : ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="b’, be, ba",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1=",", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Eb cebbbe-fabbe, ob ... bboufe ... foabubec ... bâbabebbc bécebbc.\nb. Ce buabbaeb ... a fac ébé bébofé.\nc. Bec abbeubbec ... cobb fac becbaubéc.\nd. Ab ...a a fac beaucouf d’abbbec dabc cebbe fabbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                textbook_page=15,
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence", contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")], boxed=True
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="be")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ba")], boxed=True),
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
                                            r.Text(kind="text", text="Eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbbe"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fabbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bâbabebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécebbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabbaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébofé"),
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
                                            r.Text(kind="text", text="abbeubbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbaubéc"),
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence", contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")], boxed=True
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="be")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ba")], boxed=True),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                                    [r.Text(kind="text", text="be")],
                                                    [r.Text(kind="text", text="ba")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beaucouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbe"),
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

    def test_exercise_0264(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac cec ffbacec à ba fobbe bébabafe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be becobbaac-bu ?\nb. Fababe-b-ab eb fabbe ?\nc. Faebc-bu debaab ?\nd. Afec-fouc fboad ?\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                textbook_page=15,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
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
                                            r.Text(kind="text", text="becobbaac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fababe"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Faebc"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debaab"),
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
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
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
                                            r.Text(kind="text", text="Afec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fboad"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
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

    def test_exercise_0265(self):
        self.do_test(
            e.Exercise(
                number="3",
                textbook_page=31,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec ffbacec afec ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="au, aub,",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1=",", separator2="ou", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="du ou dec",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="ou", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Babab bebbbe ... bbafaab à 19 feubec.\nb. Beboîb fa ... babcfé bouc bec babdac.\nc. Be cfab ... foacabc ecb cub be babcob.\nd. Be boubec fac bbof fabe : febcec ... ebfabbc.\ne. Ce coab, bouc abbobc bouc ... cabéba.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="3",
                textbook_page=31,
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="au")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="aub")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="du")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="dec")], boxed=True),
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
                                            r.Text(kind="text", text="Babab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="au")], [r.Text(kind="text", text="aub")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="19"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feubec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Beboîb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="au")], [r.Text(kind="text", text="aub")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babcfé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babdac"),
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
                                            r.Text(kind="text", text="cfab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="au")], [r.Text(kind="text", text="aub")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foacabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babcob"),
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="au")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="aub")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="du")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="dec")], boxed=True),
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
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="au")], [r.Text(kind="text", text="aub")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabbc"),
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
                                            r.Text(kind="text", text="coab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="au")], [r.Text(kind="text", text="aub")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabéba"),
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

    def test_exercise_0266(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=35,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec ffbacec afec bec BB fbofocéc.\n\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="bouc bec ebfabbc de ba cbacce, ba dabe de cob abbafebcaabe,  bec feuabbec dec abbbec ou ba cebaabe fbocfaabe",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1=",", separator2="ou", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ... bobbebb à b’aubobbe.\nb. Cobbaac-bu ... ?\nc. Be befaebdbaa fouc foab ... .\nd. ... obb fabbacafé au cobcoubc de becbube.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="4",
                textbook_page=35,
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="BB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocéc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="bouc"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ebfabbc"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="de"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ba"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cbacce"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="ba"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="dabe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="de"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cob"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="abbafebcaabe"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="bec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="feuabbec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="dec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="abbbec"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="ba"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cebaabe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fbocfaabe"),
                                                ],
                                                boxed=True,
                                            ),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="Bouc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ebfabbc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cbacce"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="Ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="dabe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cob"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbafebcaabe"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="Bec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="feuabbec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="dec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbbec"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="Ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cebaabe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fbocfaabe"),
                                                    ],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aubobbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cobbaac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="bouc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ebfabbc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cbacce"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="dabe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cob"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbafebcaabe"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="bec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="feuabbec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="dec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbbec"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cebaabe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fbocfaabe"),
                                                    ],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befaebdbaa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="bouc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ebfabbc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cbacce"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="dabe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cob"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbafebcaabe"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="bec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="feuabbec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="dec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbbec"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cebaabe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fbocfaabe"),
                                                    ],
                                                ],
                                            ),
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
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="BB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocéc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="bouc"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ebfabbc"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="de"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ba"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cbacce"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="ba"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="dabe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="de"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cob"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="abbafebcaabe"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="bec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="feuabbec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="dec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="abbbec"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="ba"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cebaabe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fbocfaabe"),
                                                ],
                                                boxed=True,
                                            ),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="Bouc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ebfabbc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cbacce"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="Ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="dabe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cob"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbafebcaabe"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="Bec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="feuabbec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="dec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbbec"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="Ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cebaabe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fbocfaabe"),
                                                    ],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbacafé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobcoubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbube"),
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

    def test_exercise_0267(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=43,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae cfabue ffbace afec\nba fobbe du febbe bua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Auboubd’fua, be caeb ecb bbac eb ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(ab fbeub/ab fbeufaab/ab fbeufba)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="ou", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\nb. Faeb, ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(be cfebcfe/b’aa cfebcfé/be cfebcfebaa)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="ou", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" bob cfaeb febdabb ube feube.\nc. Ba fbocfaabe foac ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(be be cuac/be b’aa cuafa/be be cuafbaa)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="ou", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" foub be fac be febdbe.\nd. B’abbée fbocfaabe, ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(bu afaac/bu ac/bu aubac)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="ou", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" beuf abc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                textbook_page=43,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="Auboubd"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="fua"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ab"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="fbeub")],
                                                    [r.Text(kind="text", text="ab"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="fbeufaab")],
                                                    [r.Text(kind="text", text="ab"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="fbeufba")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Faeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="be"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cfebcfe")],
                                                    [
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="’"),
                                                        r.Text(kind="text", text="aa"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cfebcfé"),
                                                    ],
                                                    [r.Text(kind="text", text="be"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cfebcfebaa")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febdabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feube"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbocfaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="be"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="be"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cuac"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="be"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="’"),
                                                        r.Text(kind="text", text="aa"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cuafa"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="be"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="be"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cuafbaa"),
                                                    ],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febdbe"),
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
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="abbée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbocfaabe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="bu"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="afaac")],
                                                    [r.Text(kind="text", text="bu"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ac")],
                                                    [r.Text(kind="text", text="bu"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="aubac")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beuf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
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

    def test_exercise_0268(self):
        self.do_test(
            e.Exercise(
                number="2",
                textbook_page=144,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae bec bboufec bobabaub\ncuafabbc afec b’adbecbaf bua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. bec ... babbebebbc (fabaabc – bécfabb)\nb. dec babec ... (fabceub – daabobabuec)\nc. dec obbbec ... (boabec – bbabcfe)\nd. dec ebabebc ... (dubec – ebbuaeub)\ne. de ... boubbéec (bobbuec – abbebbababbe)\nf. bec ... fobbec (ébobbe – bboccec)\nb. de ... cfecbabeubc (bobbbeub – cfabeubeuce)\nf. dec cbaebbc ... (ebabeabbc – abfebbab)\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="2",
                textbook_page=144,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbebebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="fabaabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécfabb"),
                                            r.Text(kind="text", text=")"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="fabceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daabobabuec"),
                                            r.Text(kind="text", text=")"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="boabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabcfe"),
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
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebabebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="dubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbuaeub"),
                                            r.Text(kind="text", text=")"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubbéec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="bobbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbababbe"),
                                            r.Text(kind="text", text=")"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="ébobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboccec"),
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
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfecbabeubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="bobbbeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabeubeuce"),
                                            r.Text(kind="text", text=")"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbaebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="ebabeabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfebbab"),
                                            r.Text(kind="text", text=")"),
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

    def test_exercise_0269(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=21,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cfoacac be cubeb cobbecb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ba cababe/Bec cababec cfabbe.\nb. Be bouf eb b’abbeau/B’abbeau daccubebb.\nc. Ba baabaèbe/Ba baabaèbe eb be fob au baab bobbe.\nd. Be cobbeau/Bec cobbeaub aabebb be fbobabe.\ne. Be fébob /Bec fébobc c’affbocfe\nde ba bafaèbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Be baèfbe/Be baèfbe eb ba bobbue fobb ba coubce.\n➞\nBe baèfbe eb ba bobbue fobb ba coubce.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="7",
                textbook_page=21,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cfoacac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baèfbe"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baèfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubce"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baèfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubce"),
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
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cababe"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cababec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbe"),
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
                                            r.Text(kind="text", text="bouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbeau"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daccubebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baabaèbe"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baabaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
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
                                            r.Text(kind="text", text="Cfoacac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baèfbe"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baèfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubce"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baèfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubce"),
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
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbeau"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbeaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aabebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobabe"),
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
                                            r.Text(kind="text", text="fébob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fébobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affbocfe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafaèbe"),
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

    def test_exercise_0270(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac cec ffbacec à ba fobbe bébabafe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec fbeuc cobb baeb bobfbéc.*\n--> ...\nb. Bec cfbobec du fabecfoc bbabbebb au cobeab.\n--> ...\nc. Bec caèbec cobb cobfobbabbec.\n--> ...\nd. Bec ffabec écbaabebb baeb.\n--> ...\ne. Bec cbabbobabbc fobcbaobbebb.\n--> ...\nf. Ba foabube ecb baeb ebbbebebue.\n--> ...\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="9",
                textbook_page=15,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
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
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobfbéc"),
                                            r.Text(kind="text", text="."),
                                            r.Text(kind="text", text="*"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text=">"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfbobec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabecfoc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobeab"),
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
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
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
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text=">"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caèbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfobbabbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text=">"),
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
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
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
                                            r.Text(kind="text", text="ffabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbaabebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text=">"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbabbobabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbaobbebb"),
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
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
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
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text=">"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbebebue"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text=">"),
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
                ],
            ),
        )

    def test_exercise_0271(self):
        self.do_test(
            e.Exercise(
                number="1",
                textbook_page=16,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae bouc bec débebbababbc\nde ce bebbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Ube éobaebbe ecb ube cebbbabe ébecbbabue\ncobbe boubec bec aubbec : ube bubbabe (b’fébace)\necb bace eb bobabaob fab be febb ; ebbe ecb coufbée\nà ub abbebbabeub bua fboduab de b’ébecbbacabé.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
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
                number="1",
                textbook_page=16,
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
                                            r.Text(kind="text", text="débebbababbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="éobaebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cebbbabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébecbbabue")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boubec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aubbec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bubbabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fébace")]),
                                            r.Text(kind="text", text=")"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobabaob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coufbée")]),
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
                                            r.Text(kind="text", text="débebbababbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbebbabeub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bua")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fboduab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébecbbacabé")]),
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

    def test_exercise_0272(self):
        self.do_test(
            e.Exercise(
                number="1",
                textbook_page=1,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cfebcfe bec bobc cuafabbc dabc\nbe dacbaobbaabe eb abdabue beub cbacce.\nCobbaeb de cbaccec ac-bu bbouféec ?\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. cofae\nb. bu\nc. boube\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="1",
                textbook_page=1,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cfebcfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dacbaobbaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobbaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbaccec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbouféec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
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
                                            r.Text(kind="text", text="cofae"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
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

    def test_exercise_0273(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=7,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Béfobdc fab ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="fbaa ou faub",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="ou", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. coccabebbe ecb ub adbecbaf. → ...\nb. bûcfe ecb ub febbe. → ...\nc. cebbe ecb ub débebbababb. → ...\nd. debbaeb ecb ub febbe. → ...\ne. becfabeb ecb ub febbe. → ...\nf. acfababaob ecb ub bob. → ...\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=1,
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
                textbook_page=7,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Béfobdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fbaa")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="faub")], boxed=True),
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
                                            r.Text(kind="text", text="coccabebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="fbaa")], [r.Text(kind="text", text="faub")]]
                                            ),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="Béfobdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fbaa")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="faub")], boxed=True),
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
                                            r.Text(kind="text", text="bûcfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="fbaa")], [r.Text(kind="text", text="faub")]]
                                            ),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="Béfobdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fbaa")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="faub")], boxed=True),
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
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="fbaa")], [r.Text(kind="text", text="faub")]]
                                            ),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="Béfobdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fbaa")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="faub")], boxed=True),
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
                                            r.Text(kind="text", text="debbaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="fbaa")], [r.Text(kind="text", text="faub")]]
                                            ),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="Béfobdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fbaa")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="faub")], boxed=True),
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
                                            r.Text(kind="text", text="becfabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="fbaa")], [r.Text(kind="text", text="faub")]]
                                            ),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="Béfobdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fbaa")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="faub")], boxed=True),
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
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="acfababaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="fbaa")], [r.Text(kind="text", text="faub")]]
                                            ),
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

    def test_exercise_0274(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=7,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Aboube be cuffabe –eub aub febbec.\nAbdabue ba cbacce dec bobc fabbabuéc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="babeb ➞ ... \ncbacce : ...\nbbacbeb ➞ ... \ncbacce : ...\nbabbeb ➞ ... \ncbacce : ...\nabfebbeb ➞ ... \ncbacce : ...\nbafbeb ➞ ...\ncbacce : ...\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=2,
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
                textbook_page=7,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuffabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Text(kind="text", text="eub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbabuéc"),
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
                                            r.Text(kind="text", text="babeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cbacce"),
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
                                            r.Text(kind="text", text="Aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuffabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Text(kind="text", text="eub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbabuéc"),
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
                                            r.Text(kind="text", text="bbacbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cbacce"),
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
                                            r.Text(kind="text", text="Aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuffabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Text(kind="text", text="eub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbabuéc"),
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
                                            r.Text(kind="text", text="babbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cbacce"),
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
                                            r.Text(kind="text", text="Aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuffabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Text(kind="text", text="eub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbabuéc"),
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
                                            r.Text(kind="text", text="abfebbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cbacce"),
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
                                            r.Text(kind="text", text="Aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuffabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Text(kind="text", text="eub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbabuéc"),
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
                                            r.Text(kind="text", text="bafbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cbacce"),
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
                ],
            ),
        )

    def test_exercise_0275(self):
        self.do_test(
            e.Exercise(
                number="2",
                textbook_page=30,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae bec bobc accobfabbéc\nfab ub abbacbe défaba.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="B’abfebbaob du caboffobe bebobbe à 1843. Ebbe ecb due à Adobffe Cab (1814-1894), bua eb défoca be bbefeb eb Fbabce eb 1846. Ab fub ébèfe de cbababebbe au cobcebfaboabe de Bbubebbec eb, coufaababb febfecbaobbeb ba cbababebbe bacce, ab abfebba ub boufeb abcbbubebb bu’ab bafbaca caboffobe.\nBeab Baabbeb, Foubebbe, Bécfabeb, Cabfouebbe,\nCobb eb bec aubbec, © Édabaobc de b’Offobbub, 2010.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=1,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
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
                number="2",
                textbook_page=30,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobfabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défaba"),
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
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                contents=[r.Text(kind="text", text="B"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abfebbaob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="caboffobe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="1843")]),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="due")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Adobffe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="1814")]),
                                            r.Text(kind="text", text="-"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="1894")]),
                                            r.Text(kind="text", text=")"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bua")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="défoca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbefeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Fbabce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="1846")]),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébèfe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cbababebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="au")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobcebfaboabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bbubebbec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coufaababb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febfecbaobbeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cbababebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bacce")]),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abfebba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boufeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abcbbubebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                contents=[r.Text(kind="text", text="bu"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bafbaca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="caboffobe")]),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobfabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défaba"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Beab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Baabbeb")]),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Foubebbe")]),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bécfabeb")]),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cabfouebbe")]),
                                            r.Text(kind="text", text=","),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobfabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défaba"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cobb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aubbec")]),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="©"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Édabaobc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Offobbub")]),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="2010")]),
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

    def test_exercise_0276(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=31,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cebbe becebbe de cbêfec\nafec bec abbacbec babbuabbc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc ... cabadaeb, bebbec ... fababe eb ... ceb.\nCaccec ... œufc eb bébabbec afec ... cuabbèbe.\nAbcobfobec ... baab fboad eb ... beubbe fobdu.\nBabbec baeb ... fâbe babuade. Faabec cuabe ... cbêfec dabc ... foêbe bbèc cfaude.\nCaufoudbec afec ... feu de cucbe ou ébabec ... cobfabube.\nDacfocec dabc ... fbab.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="4",
                textbook_page=31,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbêfec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuabbc"),
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
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabadaeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fababe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Caccec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="œufc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuabbèbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abcobfobec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fboad"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beubbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobdu"),
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
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbêfec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuabbc"),
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
                                            r.Text(kind="text", text="Babbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fâbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuade"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Faabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbêfec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaude"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Caufoudbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cucbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfabube"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dacfocec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbab"),
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

    def test_exercise_0277(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe ba fab de cfabue ffbace\nafec be febbe bua cobfaebb.\n\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="obdobbe-b-ab. c’ébobbe-b-ab. debabda-b-ab.",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1=".", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Foubbuoa fabc-bu ca bôb ? ...\nb. Bec fobaabec dec bbaabc obb cfabbé, ...\nc. Oufbe ba febêbbe ! ...\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=1,
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
                textbook_page=17,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="obdobbe"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="ab"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="c"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="ébobbe"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="ab"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="debabda"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="ab"),
                                                ],
                                                boxed=True,
                                            ),
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
                                            r.Text(kind="text", text="Foubbuoa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bôb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="Obdobbe"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="ab"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="C"),
                                                        r.Text(kind="text", text="’"),
                                                        r.Text(kind="text", text="ébobbe"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="ab"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="Debabda"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="ab"),
                                                    ],
                                                ],
                                            ),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="obdobbe"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="ab"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="c"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="ébobbe"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="ab"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="debabda"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="ab"),
                                                ],
                                                boxed=True,
                                            ),
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobaabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbé"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="obdobbe"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="ab"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="c"),
                                                        r.Text(kind="text", text="’"),
                                                        r.Text(kind="text", text="ébobbe"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="ab"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="debabda"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="ab"),
                                                    ],
                                                ],
                                            ),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="obdobbe"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="ab"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="c"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="ébobbe"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="ab"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="debabda"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="ab"),
                                                ],
                                                boxed=True,
                                            ),
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
                                            r.Text(kind="text", text="Oufbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febêbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="Obdobbe"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="ab"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="C"),
                                                        r.Text(kind="text", text="’"),
                                                        r.Text(kind="text", text="ébobbe"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="ab"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="Debabda"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="-"),
                                                        r.Text(kind="text", text="ab"),
                                                    ],
                                                ],
                                            ),
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

    def test_exercise_0278(self):
        self.do_test(
            e.Exercise(
                number="2",
                textbook_page=120,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec bobc afec",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="b ou b",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="ou", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a...bebce ◆ a...bucbe ◆ ube ba...fe ◆ a...foba ◆\na...bobabe ◆ co...baeb ◆ ube fe...be ◆ ube\nba...be ◆ ub fo...faeb ◆ baa...bebabb ◆\nub e...fabb ◆ cefbe...bbe ◆ béa...boabc ◆\nube ba...be ◆ a...foccabbe ◆ ub co...be ◆\nub co...fbeub ◆ e...bébabeb ◆ ub ba...bbe ◆\nube o...bbe ◆ b’e...babbuebebb ◆ e...fab ◆\na...cobbu ◆ co...fbeb ◆ a...bebabbe\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="2",
                textbook_page=120,
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
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="bebce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="bucbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="fe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="foba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="bobabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="co"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fe"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ba"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fo"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="faeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baa"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="bebabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="fabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cefbe"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="bbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béa"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="boabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="foccabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="co"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="co"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="fbeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="bébabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="bbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
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
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="o"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="bbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="babbuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="cobbu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="co"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="fbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="bebabbe"),
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

    def test_exercise_0279(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=7,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae b’abbbuc bua ce cacfe dabc cfabue bacbe eb écbac ca cbacce.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. fabbobc ◆ badobc ◆ abbobc ◆ febdobc\nb. fadobc ◆ bebbobc ◆ babbobc ◆ cabobc\nc. foab ◆ abboabe ◆ couboab ◆ dobboab\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=1,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["#ffff00", "#ffc0cb"]),
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
                number="9",
                textbook_page=7,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
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
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="fabbobc")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="badobc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="abbobc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="febdobc")],
                                            ),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="fadobc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="bebbobc")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="babbobc")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="cabobc")]
                                            ),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="foab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="abboabe")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="couboab")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="dobboab")],
                                            ),
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

    def test_exercise_0280(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=120,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae bec ffbacec eb cobfbèbe\nba debbaèbe bebbbe dec bobc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Fa boueb defob....\nb. Bebc bob bobbeb, ab faab fboa....\nc. Ab b’ecb fac abbafé, ab ecb eb bebab....\nd. Ce fabb ecb bbo... bob....\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=None,
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
                number="7",
                textbook_page=120,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="defob"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fboa"),
                                            r.FreeTextInput(kind="freeTextInput"),
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbafé"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebab"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbo"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Text(kind="text", text="."),
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

    def test_exercise_0281(self):
        self.do_test(
            e.Exercise(
                number="Defababbue",
                textbook_page=127,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Befbace cobbecbebebb eb eb ecb dabc ce\ndaabobue. Abbebbaob, ube aubbe fobbe\nc’ecb bbaccée. Caubac-bu ba bebboufeb ?\n\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="– Bua ... bà ?\n– C’... boa !\n– Ebbbe ... eccuae bec cfefeub, bu ... boub bouabbé.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
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
                number="Defababbue",
                textbook_page=127,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Befbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecbebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daabobue"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abbebbaob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aubbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaccée"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Caubac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebboufeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
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
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bà"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="’"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eccuae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfefeub"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouabbé"),
                                            r.Text(kind="text", text="."),
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

    def test_exercise_0282(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=127,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec ffbacec du bebbe\nafec eb ou ecb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="be cobfc, dec febabc ... dec bboc.\n– C’... ube ébufbaob, dab babab.\n– Baac où ... be bubébo du docbeub ? dab fafa.\n– Ab ... cub be buffeb.\nFafa affebbe be docbeub, bua ... bà ube deba-feube afbèc.\n– C’... ba fabacebbe. Be fouc abbuaébec fac.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
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
                textbook_page=127,
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
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
                                            r.Text(kind="text", text="cobfc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="’"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébufbaob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babab"),
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
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
                                            r.Text(kind="text", text="Baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubébo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="docbeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fafa"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buffeb"),
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
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
                                            r.Text(kind="text", text="Fafa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="docbeub"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bà"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deba"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="feube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afbèc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="’"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabacebbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbuaébec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
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

    def test_exercise_0283(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=127,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe afec ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="eb ou ecb",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="ou", separator2="ou", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. be babdab ... bob fbèbe ◆ bob fbèbe ... boa\nb. ba buab ... be boub ◆ Be boub ... fbocfe.\nc. be cfaeb ... be cfab ◆ Be cfaeb ... b’ebbeba du cfab.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=1,
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
                textbook_page=127,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="eb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ecb")], boxed=True),
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
                                            r.Text(kind="text", text="babdab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="eb")], [r.Text(kind="text", text="ecb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="eb")], [r.Text(kind="text", text="ecb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boa"),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="eb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ecb")], boxed=True),
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
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="eb")], [r.Text(kind="text", text="ecb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="eb")], [r.Text(kind="text", text="ecb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbocfe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="eb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ecb")], boxed=True),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="eb")], [r.Text(kind="text", text="ecb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="eb")], [r.Text(kind="text", text="ecb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebbeba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfab"),
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

    def test_exercise_0284(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=26,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cfoacac be cubeb cobbecb foub cfabue ffbace.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(Bec ababaub caufabec / Ba fabbfèbe)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" fab dabc ba fobêb.\nb. ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(Be cfab / Bec cfabc)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" cobb dec fébabc de ba bêbe fababbe bue ba fabbfèbe.\nc. ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(Cec bbaffec / Cob febabe)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" ecb doub.\nd. Baac ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(cec bbaffec / cob febabe)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" cobb acébéec.\ne. Feubeucebebb c’",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(ab / abc)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="/", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" ecb ub féboce cfacceub, ab ecb cabc dabbeb foub b’Fobbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=1,
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
                textbook_page=26,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cfoacac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="Bec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ababaub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="caufabec"),
                                                    ],
                                                    [r.Text(kind="text", text="Ba"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="fabbfèbe")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobêb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="Cfoacac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Be"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cfab")],
                                                    [r.Text(kind="text", text="Bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cfabc")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fébabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fababbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbfèbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="Cfoacac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Cec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="bbaffec")],
                                                    [r.Text(kind="text", text="Cob"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="febabe")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="Cfoacac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
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
                                            r.Text(kind="text", text="Baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="cec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="bbaffec")],
                                                    [r.Text(kind="text", text="cob"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="febabe")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="acébéec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
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
                                            r.Text(kind="text", text="Cfoacac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
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
                                            r.Text(kind="text", text="Feubeucebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ab")], [r.Text(kind="text", text="abc")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="féboce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfacceub"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="Fobbe"),
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

    def test_exercise_0286(self):
        self.do_test(
            e.Exercise(
                number="1",
                textbook_page=18,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae bouc bec febbec cobbubuéc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec ébababec fboduacebb du fobbeb.\nb. Be facbab cobbaebb dec ofubec.\nc. Be febb bbabcfobbe be fobbeb.\nd. Afbèc fécobdabaob, bec ofubec ce bbabcfobbebb eb bbaabec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
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
                number="1",
                textbook_page=18,
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
                                            r.Text(kind="text", text="febbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbubuéc"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Bec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ébababec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fboduacebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fobbeb")]
                                            ),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="facbab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cobbaebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ofubec")]
                                            ),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="febb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbabcfobbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fobbeb")]
                                            ),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Afbèc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fécobdabaob")]
                                            ),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ofubec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbabcfobbebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbaabec")]
                                            ),
                                            r.Text(kind="text", text="."),
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

    def test_exercise_0287(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=25,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebbabe bec ffbacec afec be cobfbébebb bua cobfaebb. ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="à ube bobbe cboaccabce ◆ à b’ébabe ◆ dec fbabc éfacéc ◆ à ba buab",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="◆", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be boub cuccède ... .\nb. B’ebebcace ffacabue cobbbabue ... .\nc. Au becbaubabb, ob a boûbé ... .\nd. Ab faub fbebdbe b’accebceub foub accédeb ...\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
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
                number="7",
                textbook_page=25,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbébebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="à"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bobbe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cboaccabce"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="à"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="ébabe"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="dec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fbabc"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="éfacéc"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="à"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ba"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="buab"),
                                                ],
                                                boxed=True,
                                            ),
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
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuccède"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ube"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bobbe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cboaccabce"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="’"),
                                                        r.Text(kind="text", text="ébabe"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="dec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fbabc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="éfacéc"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="buab"),
                                                    ],
                                                ],
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
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebebcace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffacabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ube"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bobbe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cboaccabce"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="’"),
                                                        r.Text(kind="text", text="ébabe"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="dec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fbabc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="éfacéc"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="buab"),
                                                    ],
                                                ],
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
                                            r.Text(kind="text", text="Au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbaubabb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boûbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ube"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bobbe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cboaccabce"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="’"),
                                                        r.Text(kind="text", text="ébabe"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="dec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fbabc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="éfacéc"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="buab"),
                                                    ],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="accebceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accédeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ube"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bobbe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cboaccabce"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="’"),
                                                        r.Text(kind="text", text="ébabe"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="dec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fbabc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="éfacéc"),
                                                    ],
                                                    [
                                                        r.Text(kind="text", text="à"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="buab"),
                                                    ],
                                                ],
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

    def test_exercise_0288(self):
        self.do_test(
            e.Exercise(
                number="1",
                textbook_page=11,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ubabuebebb bec ffbacec bucbec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ba fobcbuabaob feub fabfoac bodafaeb be cebc d’ube ffbace.\nb. Bec babebc cobb ubabacéc dabc bec daabobuec.\nc. Ba fabbube feub êbbe fbacée à ba fab d’ube ffbace.\nd. Foub foceb ube buecbaob, ob ubabace ub foabb d’ebcbababaob.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
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
                number="1",
                textbook_page=11,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bucbec"),
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
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabfoac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bodafaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
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
                                            r.Text(kind="text", text="babebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabacéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daabobuec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="êbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbacée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buecbaob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebcbababaob"),
                                            r.Text(kind="text", text="."),
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

    def test_exercise_0289(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=64,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe ce bebbe afec bec cubebc de ba bacbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="Bec Bafobaac ◆ Ba baabbe de ceb ababab babab ◆ Bobubba ◆ Ab",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="◆", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Bobubba ecb ub ababab babab bua beccebbbe ub feu à ub bafab. ... fab dabc bec bebc cfaudec fbèc du Bafob. Ceb ébé, ube bode ecb affabue au Bafob. ... bebbebb dec ffoboc de ceb ébbabbe ababab cub Abbebbeb. .... fab cub bec bécafc de cobaub. Ab ce boubbab d’éfobbec. ... ecb bbèc béduabe, à feabe deub cebbabèbbec de bobb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
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
                number="7",
                textbook_page=64,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="Bec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="Bafobaac"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="Ba"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="baabbe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="de"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ceb"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ababab"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="babab"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="Bobubba")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="Ab")], boxed=True),
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
                                            r.Text(kind="text", text="Bobubba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beccebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafab"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="Bafobaac")],
                                                    [
                                                        r.Text(kind="text", text="Ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="baabbe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ceb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ababab"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="babab"),
                                                    ],
                                                    [r.Text(kind="text", text="Bobubba")],
                                                    [r.Text(kind="text", text="Ab")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaudec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bafob"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébé"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bode"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bafob"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="Bafobaac")],
                                                    [
                                                        r.Text(kind="text", text="Ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="baabbe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ceb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ababab"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="babab"),
                                                    ],
                                                    [r.Text(kind="text", text="Bobubba")],
                                                    [r.Text(kind="text", text="Ab")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffoboc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abbebbeb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="Bafobaac")],
                                                    [
                                                        r.Text(kind="text", text="Ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="baabbe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ceb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ababab"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="babab"),
                                                    ],
                                                    [r.Text(kind="text", text="Bobubba")],
                                                    [r.Text(kind="text", text="Ab")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobaub"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubbab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="éfobbec"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="Bafobaac")],
                                                    [
                                                        r.Text(kind="text", text="Ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="baabbe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="de"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ceb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ababab"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="babab"),
                                                    ],
                                                    [r.Text(kind="text", text="Bobubba")],
                                                    [r.Text(kind="text", text="Ab")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béduabe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbabèbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobb"),
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

    def test_exercise_0290(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=64,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Accocae cfabue cubeb au febbe bua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Febeb eb Abba ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="fabbacafobc abbec babcfe débébabebb ac",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nBe  ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="fabbacafobc abbec babcfe débébabebb ac",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nBouc  ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="fabbacafobc abbec babcfe débébabebb ac",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nBu  ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="fabbacafobc abbec babcfe débébabebb ac",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nFouc ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="fabbacafobc abbec babcfe débébabebb ac",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\n\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
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
                number="4",
                textbook_page=64,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Accocae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="Febeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="fabbacafobc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="babcfe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="débébabebb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ac"),
                                                    ]
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="fabbacafobc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="babcfe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="débébabebb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ac"),
                                                    ]
                                                ],
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
                                            r.Text(kind="text", text="Accocae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="Bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="fabbacafobc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="babcfe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="débébabebb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ac"),
                                                    ]
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="fabbacafobc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="babcfe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="débébabebb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ac"),
                                                    ]
                                                ],
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
                                            r.Text(kind="text", text="Accocae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="Fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="fabbacafobc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="babcfe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="débébabebb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ac"),
                                                    ]
                                                ],
                                            ),
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

    def test_exercise_0291(self):
        self.do_test(
            e.Exercise(
                number="2",
                textbook_page=146,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae bec bboufec bobabaub cuafabbc afec b’adbecbaf bua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. bec ... babbebebbc ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(fabaabc – bécfabb)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="-", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nb. dec babec ... ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(fabceub – daabobabuec)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="-", separator2="", stop=")", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nc. dec obbbec ... ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(boabec – bbabcfe)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="-", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nd. dec ebabebc ... ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(dubec – ebbuaeub)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="-", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\ne. de ... boubbéec ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(bobbuec – abbebbababbe)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="-", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nf. bec ... fobbec ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(ébobbe – bboccec)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="-", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nb. de ... cfecbabeubc ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(bobbbeub – cfabeubeuce)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="-", separator2="", stop=")", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nf. dec cbaebbc ... ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="(ebabeabbc – abfebbab)",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="-", separator2="", stop=")", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
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
                number="2",
                textbook_page=146,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbebebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="fabaabc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="–"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bécfabb"),
                                                    ]
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="fabceub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="–"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="daabobabuec"),
                                                    ]
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="boabec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="–"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bbabcfe"),
                                                    ]
                                                ],
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
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebabebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="dubec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="–"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="ebbuaeub"),
                                                    ]
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubbéec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="bobbuec"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="–"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abbebbababbe"),
                                                    ]
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="ébobbe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="–"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bboccec"),
                                                    ]
                                                ],
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
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
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
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfecbabeubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="bobbbeub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="–"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="cfabeubeuce"),
                                                    ]
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbaebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="ebabeabbc"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="–"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="abfebbab"),
                                                    ]
                                                ],
                                            ),
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

    def test_exercise_0292(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=23,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cfoacac be cubeb cobbecb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="Ba cababe/Bec cababec",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="/", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" cfabbe.\nb. ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="Be bouf eb b’abbeau/B’abbeau ",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="/", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="daccubebb.\nc.",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" Ba baabaèbe/Ba baabaèbe eb be fob au baab",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="/", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=" bobbe.\nd. Be cobbeau/Bec cobbeaub aabebb be fbobabe.\ne. Be fébob /Bec fébobc c’affbocfe de ba bafaèbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Be baèfbe/Be baèfbe eb ba bobbue fobb ba coubce. ➞ Be baèfbe eb ba bobbue fobb ba coubce.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
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
                number="7",
                textbook_page=23,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cfoacac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baèfbe"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baèfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubce"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baèfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubce"),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Ba"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cababe")],
                                                    [r.Text(kind="text", text="Bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cababec")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [
                                                        r.Text(kind="text", text="Be"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bouf"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="eb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="b"),
                                                        r.Text(kind="text", text="’"),
                                                        r.Text(kind="text", text="abbeau"),
                                                    ],
                                                    [r.Text(kind="text", text="B"), r.Text(kind="text", text="’"), r.Text(kind="text", text="abbeau")],
                                                ],
                                            ),
                                            r.Text(kind="text", text="daccubebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Ba"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="baabaèbe")],
                                                    [
                                                        r.Text(kind="text", text="Ba"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="baabaèbe"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="eb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="be"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fob"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="au"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="baab"),
                                                    ],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
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
                                            r.Text(kind="text", text="cobbeau"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbeaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aabebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobabe"),
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
                                            r.Text(kind="text", text="fébob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fébobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affbocfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafaèbe"),
                                            r.Text(kind="text", text="."),
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

    def test_exercise_0293(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=72,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec ffbacec afec ba fobbe febbabe bua cobfaebb au fubub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be ... be cfebab de dboabe. ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="fbebdbaa ◆ fbebaac ◆ fbebdc",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="◆", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nb. Bu ... faabe ub déboub foub cabueb ba bbabd-bèbe. ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="feub ◆ foudbac ◆ foudba",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="◆", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nc. Ob ... ce baabbeb dabc be bac. ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="foubbobb ◆ foubba ◆ foufaab",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="◆", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nd. Bouc ... bec féboc eb boc cacc à doc. fbebaobc ◆ fbebdbobc ◆ fbebdbobb\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
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
                number="6",
                textbook_page=72,
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fubub"),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="fbebdbaa")],
                                                    [r.Text(kind="text", text="fbebaac")],
                                                    [r.Text(kind="text", text="fbebdc")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dboabe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="feub")],
                                                    [r.Text(kind="text", text="foudbac")],
                                                    [r.Text(kind="text", text="foudba")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="déboub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bèbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="foubbobb")],
                                                    [r.Text(kind="text", text="foubba")],
                                                    [r.Text(kind="text", text="foufaab")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baabbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bac"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="féboc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doc"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebdbobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebdbobb"),
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

    def test_exercise_0294(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=127,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec ffbacec afec ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="ob ou obb",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="ou", separator2="ou", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ... ecb cacféc debbaèbe be badeau.\nb. Abc ... cûbebebb febbé ba fobbe à cbé.\nc. Abc ... baacob.\nd. ... fa bouc affobbeb boc fbabc.\ne. ... ecb cebbéc b’ub cobbbe b’aubbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
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
                number="8",
                textbook_page=127,
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ob")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="obb")], boxed=True),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="Ob")], [r.Text(kind="text", text="Obb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacféc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="badeau"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ob")], [r.Text(kind="text", text="obb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cûbebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbé"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="ob")], [r.Text(kind="text", text="obb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="Ob")], [r.Text(kind="text", text="Obb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="Ob")], [r.Text(kind="text", text="Obb")]]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aubbe"),
                                            r.Text(kind="text", text="."),
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

    def test_exercise_0295(self):
        self.do_test(
            e.Exercise(
                number="1",
                textbook_page=136,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Béfobdc fab fbaa ou faub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ca ub bob ecb baccubab, ab feub êbbe au fbubaeb ou au cabbubaeb.\nb. Ub bob ecb baccubab ou fébabab.\nc. Be bobbbe abdabue ca ub bob ecb au cabbubaeb ou au fbubaeb.\nd. Be bobbbe abdabue bue be bob ecb fobcébebb au fbubaeb.\ne. Be débebbababb abdabue be bebbe eb be bobbbe d’ub bob.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
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
                number="1",
                textbook_page=136,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Béfobdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbaa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faub"),
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
                                            r.Text(kind="text", text="Ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baccubab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="êbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbubaeb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baccubab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fébabab"),
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
                                            r.Text(kind="text", text="bobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbubaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
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
                                            r.Text(kind="text", text="bobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcébebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
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
                                            r.Text(kind="text", text="débebbababb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Text(kind="text", text="."),
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

    def test_exercise_0296(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=38,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bboufe b’abbbuc de cfabue bacbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ub  b’ bu  dec\nb. ba  bobbe  bouc  boc\nc. deub  dec  cebbe  ube\nd. be  ba  ub  ça\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["#ffff00", "#ffc0cb"]),
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
                number="5",
                textbook_page=38,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="ub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="bu")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="dec")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="ba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="bobbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="bouc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="boc")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="deub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="cebbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="ube")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="be")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="ba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="ub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], boxed=True, contents=[r.Text(kind="text", text="ça")]
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

    def test_exercise_0297(self):
        self.do_test(
            e.Exercise(
                number="3",
                textbook_page=1,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe afec : ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="be, ube, ub, dec, bu, ebbec, abc",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1=",", separator2="", stop="", placeholder="...", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert=".\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="... fade\n... fadebb\n... défebcec\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
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
                number="3",
                textbook_page=1,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="be")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ube")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ub")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="dec")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bu")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="ebbec")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="abc")], boxed=True),
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Be")],
                                                    [r.Text(kind="text", text="Ube")],
                                                    [r.Text(kind="text", text="Ub")],
                                                    [r.Text(kind="text", text="Dec")],
                                                    [r.Text(kind="text", text="Bu")],
                                                    [r.Text(kind="text", text="Ebbec")],
                                                    [r.Text(kind="text", text="Abc")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fade"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Be")],
                                                    [r.Text(kind="text", text="Ube")],
                                                    [r.Text(kind="text", text="Ub")],
                                                    [r.Text(kind="text", text="Dec")],
                                                    [r.Text(kind="text", text="Bu")],
                                                    [r.Text(kind="text", text="Ebbec")],
                                                    [r.Text(kind="text", text="Abc")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fadebb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Be")],
                                                    [r.Text(kind="text", text="Ube")],
                                                    [r.Text(kind="text", text="Ub")],
                                                    [r.Text(kind="text", text="Dec")],
                                                    [r.Text(kind="text", text="Bu")],
                                                    [r.Text(kind="text", text="Ebbec")],
                                                    [r.Text(kind="text", text="Abc")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défebcec"),
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

    def test_exercise_0299(self):
        self.do_test(
            e.Exercise(
                number="2",
                textbook_page=10,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ubabuebebb bec ffbacec ebacbec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ube ffbace ce bebbabe fab ub foabb, ub foabb d’ebcbababaob ou ub foabb d’abbebbobabaob.\nb. Ca ube cuabe de bobc b’a fac de cebc, baac bu’ebbe cobbebce fab ube babuccube eb ce bebbabe fab ub foabb, c’ecb ube ffbace.\nc. Ube ffbace cobbebce fab ube babuccube.\nd. Ube ffbace cobbebce fab ub foabb.\ne. Ube ffbace, c’ecb ba bêbe cfoce bu’ube babbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=SentencesItems(kind="sentences"),
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
                number="2",
                textbook_page=10,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebacbec"),
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
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                contents=[
                                                    r.Text(kind="text", text="Ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ffbace"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ce"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bebbabe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fab"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ub"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="foabb"),
                                                    r.Text(kind="text", text=","),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ub"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="foabb"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="d"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="ebcbababaob"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ou"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ub"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="foabb"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="d"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="abbebbobabaob"),
                                                    r.Text(kind="text", text="."),
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                contents=[
                                                    r.Text(kind="text", text="Ca"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cuabe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="de"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bobc"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="a"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fac"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="de"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cebc"),
                                                    r.Text(kind="text", text=","),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="baac"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bu"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="ebbe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cobbebce"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fab"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="babuccube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="eb"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ce"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bebbabe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fab"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ub"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="foabb"),
                                                    r.Text(kind="text", text=","),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="c"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="ecb"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ffbace"),
                                                    r.Text(kind="text", text="."),
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                contents=[
                                                    r.Text(kind="text", text="Ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ffbace"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cobbebce"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fab"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="babuccube"),
                                                    r.Text(kind="text", text="."),
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                contents=[
                                                    r.Text(kind="text", text="Ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ffbace"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cobbebce"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fab"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ub"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="foabb"),
                                                    r.Text(kind="text", text="."),
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb"],
                                                contents=[
                                                    r.Text(kind="text", text="Ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ffbace"),
                                                    r.Text(kind="text", text=","),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="c"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="ecb"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ba"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bêbe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cfoce"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bu"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="babbe"),
                                                    r.Text(kind="text", text="."),
                                                ],
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

    def test_exercise_0300(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=167,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Ebcadbe be badacab eb coubabbe be cuffabe dec adbecbafc cuafabbc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. feubeub ◆ febcaf ◆ ebceccaf ◆ babfeubeub\nb. babaabbe ◆ cbaabbaf ◆ bacabbe ◆ bafabbe\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=CharactersItems(kind="characters", letters=True),
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
                number="5",
                textbook_page=167,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ebcadbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="badacab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuffabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="f")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="e")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="u")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="e")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="u")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="f")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="e")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="c")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="f")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="e")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="c")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="e")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="c")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="c")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="f")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="f")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="e")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="u")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="e")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="u")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="e")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="c")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="f")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="c")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="e")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="◆"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="f")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="e")]),
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

    def test_exercise_0301(self):
        self.do_test(
            e.Exercise(
                number="2",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebèfe bec cabbec de fobcbuabaob du bebbe. Cbacce-bec dabc be babbeau.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Boub ! Babb ! Dec ebfbocaobc de bubaèbec eb de bbuabc ebfbaccebb be caeb : ce cobb bec feub d’abbaface, dec fboduabc cfababuec bua ebfbocebb eb fob. Afbèc b’abbubabe de ba fucée, ab faub ce bebbbe à b’abba !\nBa fbabbe bobbe be bobb de ba fucée eb ebfbabbe ba foudbe bua ce bboufe à b’abbébaeub. Ba foudbe ebfbocafe ecb bébabbée à dec fboduabc cfababuec, affebéc « éboabec », bua dobbebb ba coubeub décabée.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="Bob ebcacbofédae « Cobbebb ça babcfe ? » 6-9 abc, bbad. C. Bbabcfabd, © Édabaobc Babbababd Beubecce, 2010.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="2",
                textbook_page=13,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cbacce"),
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
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="Boub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="Babb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="Dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ebfbocaobc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="de")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bubaèbec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="eb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="de")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bbuabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ebfbaccebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="be")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="caeb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ce")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="cobb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="feub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="d"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="abbaface")]
                                            ),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="fboduabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="cfababuec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bua")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ebfbocebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="eb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="fob")]
                                            ),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="Afbèc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="abbubabe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="de")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="fucée")]
                                            ),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="faub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ce")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bebbbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="abba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="Ba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="fbabbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bobbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="be")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bobb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="de")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="fucée")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="eb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ebfbabbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="foudbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bua")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ce")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bboufe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                boxed=True,
                                                contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="abbébaeub")]
                                            ),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="Ba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="foudbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ebfbocafe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ecb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bébabbée")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="fboduabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="cfababuec")]
                                            ),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="affebéc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="«"),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="éboabec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="»"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="bua")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="dobbebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="ba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="coubeub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], boxed=True, contents=[r.Text(kind="text", text="décabée")]
                                            ),
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
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcacbofédae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="«"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ça"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babcfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="»"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="6"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="9"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbad"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bbabcfabd"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="©"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Édabaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babbababd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Beubecce"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="2010"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=False,
                                tricolored=False,
                            )
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0302(self):
        self.do_test(
            e.Exercise(
                number="1",
                textbook_page=14,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae ubabuebebb bec ffbacec bua cobb à ba fobbe ebcbababafe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. B’facboabe bue bu be bacobbec ecb abcboaabbe !\nb. Be b’aa babaac ebbebdu ube cfoce fabeabbe.\nc. Bu ebabèbec ub feu !\nd. Ce b'ecb fac fbaa.\ne. Buabd ac-bu affbac cebbe boufebbe ?\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=SentencesItems(kind="sentences"),
                    items_are_selectable=Selectable(colors=["#ffff00"]),
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
                number="1",
                textbook_page=14,
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcbababafe"),
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
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                boxed=True,
                                                contents=[
                                                    r.Text(kind="text", text="B"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="facboabe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bue"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bu"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="be"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bacobbec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ecb"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="abcboaabbe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="!"),
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                boxed=True,
                                                contents=[
                                                    r.Text(kind="text", text="Be"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="’"),
                                                    r.Text(kind="text", text="aa"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="babaac"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ebbebdu"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cfoce"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fabeabbe"),
                                                    r.Text(kind="text", text="."),
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                boxed=True,
                                                contents=[
                                                    r.Text(kind="text", text="Bu"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ebabèbec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ub"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="feu"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="!"),
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                boxed=True,
                                                contents=[
                                                    r.Text(kind="text", text="Ce"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="b"),
                                                    r.Text(kind="text", text="'"),
                                                    r.Text(kind="text", text="ecb"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fac"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="fbaa"),
                                                    r.Text(kind="text", text="."),
                                                ],
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                boxed=True,
                                                contents=[
                                                    r.Text(kind="text", text="Buabd"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="ac"),
                                                    r.Text(kind="text", text="-"),
                                                    r.Text(kind="text", text="bu"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="affbac"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="cebbe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="boufebbe"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="?"),
                                                ],
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

    def test_exercise_0303(self):
        self.do_test(
            e.Exercise(
                number="2",
                textbook_page=14,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Abdabue bec ffbacec bua cobb à ba fobbe bébabafe eb cobobae bec babbuec de ba bébabaob.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Cubboub, be dac baeb.\nCebbe ffbace ecb à ba fobbe bébabafe. → ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="Fbaa/Faub",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="/", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nb. Buabd befaebdbobc-bouc ?\nCebbe ffbace ecb à ba fobbe bébabafe. → ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="Fbaa/Faub",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="/", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nc. Be b’aabe fac bec éfababdc.\nCebbe ffbace ecb à ba fobbe bébabafe. → ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="Fbaa/Faub",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="/", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nd. Debaab, bouc abobc au cabéba.\nCebbe ffbace ecb à ba fobbe bébabafe. → ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="Fbaa/Faub",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="/", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\ne. Coufbe-boa afabb de cobbab !\nCebbe ffbace ecb à ba fobbe bébabafe. → ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="Fbaa/Faub",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="/", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\nf. Be coubc fac bbof fabe.\nCebbe ffbace ecb à ba fobbe bébabafe. → ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="Fbaa/Faub",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="", separator1="/", separator2="", stop="", placeholder="", mcq_field_uid=None),
                            mcq_placeholder=False,
                            manual_item=False,
                            sel=None,
                        ),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                text_reference=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
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
                number="2",
                textbook_page=14,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cubboub")]),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baeb")]),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ffbace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bébabafe")]),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="Fbaa")], [r.Text(kind="text", text="Faub")]]
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
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Buabd")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="befaebdbobc")]),
                                            r.Text(kind="text", text="-"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bouc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ffbace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bébabafe")]),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="Fbaa")], [r.Text(kind="text", text="Faub")]]
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
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="éfababdc")]),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ffbace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bébabafe")]),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="Fbaa")], [r.Text(kind="text", text="Faub")]]
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
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Debaab")]),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bouc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abobc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="au")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabéba")]),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ffbace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bébabafe")]),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="Fbaa")], [r.Text(kind="text", text="Faub")]]
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
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Coufbe")]),
                                            r.Text(kind="text", text="-"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boa")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ffbace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bébabafe")]),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="Fbaa")], [r.Text(kind="text", text="Faub")]]
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
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabaob"),
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
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coubc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbof")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabe")]),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ffbace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bébabafe")]),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="→"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="Fbaa")], [r.Text(kind="text", text="Faub")]]
                                            ),
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
