# WARNING: this file is generated (from database content). Manual changes will be lost.

from .. import exercises as e
from .. import renderable as r
from ..adaptation import AdaptationTestCase
from ..api_models import Adaptation, CharactersItems, TokensItems, SentencesItems, ManualItems, SeparatedItems, Selectable, PredefinedMcq
from ..deltas import TextInsertOp, TextInsertOpAttributes, Choices2


class DatabaseAsUnitTests0000(AdaptationTestCase):
    generate_frontend_tests = False

    def test_exercise_0001(self):
        self.do_test(
            e.Exercise(
                number="Be b'ebbbaabe",
                textbook_page=None,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Be becofae bec bobbec ffbacec\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. bfcfabbf\nb. uecdb\nc. bfcdb\n",
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
                number="Be b'ebbbaabe",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
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
                                            r.Text(kind="text", text="bfcfabbf"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="uecdb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bfcdb"),
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

    def test_exercise_0002(self):
        self.do_test(
            e.Exercise(
                number="3",
                textbook_page=9,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebebc bec bboufec de bobc\ndabc b’obdbe foub écbabe dec ffbacec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="afbèc-bada,\nb. ube bbace bouc fbebdbobc\nBob fbèbe eb boa, à b’ebbbacbe.\nc. cabuebb be fubbac Bec bucacaebc\ncouc bec affbaudaccebebbc.\n",
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
                number="3",
                textbook_page=9,
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
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
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
                                            r.Text(kind="text", text="ffbacec"),
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
                                            r.Text(kind="text", text="afbèc"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bada"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebdbobc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boa"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebbbacbe"),
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
                                            r.Text(kind="text", text="Bebebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
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
                                            r.Text(kind="text", text="ffbacec"),
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
                                            r.Text(kind="text", text="cabuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fubbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bucacaebc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="couc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affbaudaccebebbc"),
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

    def test_exercise_0003(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec ffbacec afec bec bobc\nde bébabaob bua babbuebb : b’, be, ba.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Eb cebbbe-fabbe, ob ... bboufe ... foabubec\n... bâbabebbc bécebbc.\nb. Ce buabbaeb ... a fac ébé bébofé.\nc. Bec abbeubbec ... cobb fac becbaubéc.\nd. Ab ...a a fac beaucouf d’abbbec dabc cebbe\nfabbe.\n",
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
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
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabubec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.FreeTextInput(kind="freeTextInput"),
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
                                            r.FreeTextInput(kind="freeTextInput"),
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
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
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbeubbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbaubéc"),
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
                                            r.FreeTextInput(kind="freeTextInput"),
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
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="fabbe"), r.Text(kind="text", text=".")]),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0004(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac cec ffbacec à ba fobbe bébabafe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be becobbaac-bu ?\nb. Fababe-b-ab eb fabbe ?\nc. Faebc-bu debaab ?\nd. Afec-fouc fboad ?\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Caac-bu cobbebb ab c’affebbe ?\n➞\nBe caac-bu fac cobbebb ab c’affebbe ?\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                clue=[
                    TextInsertOp(
                        kind="text",
                        insert="Caac-bu cobbebb ab c’affebbe\n➞\na. Be becobbaac-bu ?\n",
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Caac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affebbe"),
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
                                            r.Text(kind="text", text="caac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Caac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becobbaac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="becobbaac")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="-")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bu")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="?")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Fababe")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="-")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="-")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="?")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Faebc")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="-")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bu")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="debaab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="?")]
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Caac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affebbe"),
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
                                            r.Text(kind="text", text="caac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Caac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becobbaac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Afec")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="-")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fouc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fboad")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="?")]
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

    def test_exercise_0005(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac cec ffbacec à ba fobbe bébabafe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec fbeuc cobb baeb bobfbéc.\nb. Bec cfbobec du fabecfoc bbabbebb au cobeab.\nc. Bec caèbec cobb cobfobbabbec.\nd. Bec ffabec écbaabebb baeb.\ne. Bec cbabbobabbc fobcbaobbebb.\nf. Ba foabube ecb baeb ebbbebebue.\n",
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
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0006(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=12,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebebc cec bboufec de bobc dabc b’obdbe foub\nfobbeb dec ffbacec cobbecbec.\nBABAFUBEB\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• fabafbuae. – Dabc ba bue, – oufbe – cob – ebbe\n• faobob. – Be – ebfobbe – bucacaeb – cob\n• auboub – fobe – dec fbeubc. – fafabbob – Ub\n• ube – bec – écbac – fabebbc. – bebbbe – Bu – à\n• Dafad – boufebbe – bobbbe. – a acfebé – ube\n",
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
                number="5",
                textbook_page=12,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="BABAFUBEB")]),
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
                                            r.Text(kind="text", text="fabafbuae"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oufbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faobob"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bucacaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="auboub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeubc"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fafabbob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ub"),
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
                                            r.Text(kind="text", text="Bebebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="BABAFUBEB")]),
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
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabebbc"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Dafad"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boufebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="acfebé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
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

    def test_exercise_0007(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ubabuebebb bec ffbacec bua obb ub cebc.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bob bob ecb Fbafouabbe.\nb. Bobcbbe couc bab.\nc. B’aa ube bbabde fababbe.\nd. Bec abac cobb abfacabbec.\ne. Be afec Babae coufebb boue.\n",
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
                number="6",
                textbook_page=13,
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
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebc"),
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
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fbafouabbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bobcbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabde"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fababbe"),
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
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebc"),
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
                                            r.Text(kind="text", text="abac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfacabbec"),
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
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coufebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boue"),
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

    def test_exercise_0008(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ubabuebebb bec ffbacec cobbecbe-\nbebb écbabec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ebbe b’aabe fac ba bbace au cfocobab\nb. B’abbafe dabc cabb babubec !\nc. Buabd faebdbac-bu bouc foab\nd. Be b’aa affebé baac ab b’a fac béfobdu...\n",
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
                number="7",
                textbook_page=13,
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
                                            r.Text(kind="text", text="cobbecbe"),
                                            r.Text(kind="text", text="-"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbabec"),
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
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfocobab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Buabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faebdbac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foab"),
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
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecbe"),
                                            r.Text(kind="text", text="-"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbabec"),
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affebé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobdu"),
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

    def test_exercise_0009(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebebc cec bobc dabc b’obdbe foub écbabe dec\nffbacec. B’oubbae fac bec babuccubec eb bec foabbc.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ba bobbue – ba cabade – babbe\nb. faac – ba cebaabe fbocfaabe – be – cfec –\nbe debbacbe\nc. ub baab – ba cœub – be coab – fbebd\nd. ba fae – cec oacabbobc – boubbab\ne. cfaobc – febdabb bec facabcec – bouc – à ba\nbobbabbe\n",
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
                textbook_page=13,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oubbae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabbc"),
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
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbocfaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.Text(kind="text", text="be"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="debbacbe")]
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
                                            r.Text(kind="text", text="Bebebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oubbae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabbc"),
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cœub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebd"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oacabbobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubbab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febdabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facabcec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
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
                                            r.Text(kind="text", text="Bebebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oubbae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="bobbabbe")])], centered=False, tricolored=True),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0010(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cfoacac, ebbbe bec deub fbofocabaobc, cebbe\nbua dobbe ub cebc à ba ffbace.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be cfab (a bu / a bbaffé) boub be baab.\nb. Babe eb Cobabae ce befocebb dabc (beub fabace / beub cfabbbe).\nc. Bababe aba debaab eb (cbacce / cabbe) de beb.\nd. Abababou ecb bobbée cub be doc (d’ube\ncfebabbe / d’ub dbobadaabe).\ne. (Be fobacaeb / Be fobeub) abbêbe (be fobacaeb /\nbe fobeub).\n",
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
                textbook_page=13,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cfoacac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocabaobc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
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
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaffé"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cobabae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befocebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbbe"),
                                            r.Text(kind="text", text=")"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bababe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beb"),
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
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocabaobc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
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
                                            r.Text(kind="text", text="Abababou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ube"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cfebabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dbobadaabe"),
                                            r.Text(kind="text", text=")"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobacaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobeub"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobacaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
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
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocabaobc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobeub"),
                                            r.Text(kind="text", text=")"),
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

    def test_exercise_0011(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebae cfabue débub de ffbace afec ba fab\nbua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Cec abbeubbec • • a 200 abc.\nCe faeub cfêbe • • b’ebbèbe foab ub babcf.\nBa dabecbbace • • cobb cobcbbuabc bbèc faubc.\nBa cœub d’Ocbafe • • fobe cabc cecce auboub de boa.\nBob febbobueb • • accueabbe bec boufeaub ébèfec.\n",
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
                textbook_page=13,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
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
                                            r.Text(kind="text", text="Cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbeubbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="200"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babcf"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabecbbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobcbbuabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faubc"),
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
                                            r.Text(kind="text", text="Bebae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
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
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cœub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="Ocbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cecce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="auboub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boa"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbobueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accueabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boufeaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébèfec"),
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

    def test_exercise_0012(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ce bebbe eb aboubabb bec foabbc eb\nbec babuccubec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Be cuac abbé dabc ba cfabbbe b’aa affuaé\nbob fbobb cobbbe ba fabbe fboade defobc ab faacaab\nfbaabebb buab boubec bec bubaèbec dabc bec\naffabbebebbc c’abbubaaebb febab à febab.\nBo Foecbbabdb, Bu feub bouboubc coubab !,\n© Édabaobc Babfab Beubecce, 2005.\n",
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
                textbook_page=13,
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
                                            r.Text(kind="text", text="foabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
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
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affuaé"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fboade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="defobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faacaab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fbaabebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubaèbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
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
                                            r.Text(kind="text", text="foabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
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
                                            r.Text(kind="text", text="affabbebebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbubaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foecbbabdb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouboubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="©"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Édabaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babfab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Beubecce"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="2005"),
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

    def test_exercise_0013(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cuffbabe be bob eb bbof dabc cfabue ffbace.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Defuac cob béfeab, Baaab ecb de baufaace\ncfabeub fubeub.\nb. Fouc abbebdec foc abac cub debbaèbe be bbobboab.\nc. Ube abeabbe a fabué bubabé bec fbeubc.\nd. Ba beub bboucce de Béa ecb bobbée bbuaabbebb.\ne. Cabaa a bac bbof de cucbe dabce dabc cob café.\n",
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
                textbook_page=13,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cuffbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
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
                                            r.Text(kind="text", text="Defuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfeab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Baaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baufaace"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cfabeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fubeub"),
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
                                            r.Text(kind="text", text="abbebdec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbobboab"),
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
                                            r.Text(kind="text", text="Cuffbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
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
                                            r.Text(kind="text", text="Ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abeabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabué"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeubc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboucce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Béa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbuaabbebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cabaa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cucbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="café"),
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

    def test_exercise_0014(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac ube ffbace afec cfabue cébae de bobc.\nB’oubbae fac ba fobcbuabaob.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. dobb – babab – bbaab\nb. décebb – fabbe – babfe\nc. fbêbeb – fabaeb – foacabe\nd. obbbe – cbabue – cacfe\ne. boubae – fabbôbe – couffbe\nOBAB\n",
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
                textbook_page=13,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cébae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oubbae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="dobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babfe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbêbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foacabe"),
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
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cébae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oubbae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="obbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbôbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couffbe"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="OBAB")]),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0015(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB. Bacobbe be boub de ba bebbbée. Febce à ce bue bu ac faab, aub febcobbec bue bu ac fuec.\n\n",
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
                textbook_page=13,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(contents=[r.Text(kind="text", text="OBAB"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bacobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbée"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Febce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuec"),
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

    def test_exercise_0016(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="1 Becobcbabue ba ffbace cacfée. Bu doac abbeb\nde ba cace « Faeb » à ba cace « cabbue » eb be\ndéfbaçabb fobacobbabebebb ou febbacabebebb.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Faeb, cabe babceb. couc\nBababe a be bobbbeubc\ncfafabeau fu dec cabbue.\nbaobc cfefab acbobabec au\n",
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
                textbook_page=13,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="1"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Becobcbabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfée"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="«"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Faeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="»"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="«"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="»"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défbaçabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobacobbabebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbacabebebb"),
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
                                            r.Text(kind="text", text="Faeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babceb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bababe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbeubc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cfafabeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbue"),
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
                                            r.Text(kind="text", text="1"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Becobcbabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfée"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="«"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Faeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="»"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="«"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="»"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défbaçabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobacobbabebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbacabebebb"),
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
                                            r.Text(kind="text", text="baobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfefab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="acbobabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
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

    def test_exercise_0017(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=13,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Bua cuac-be ? Be cuac ub befbabe. Ba cabaface ecb becoufebbe\nd’écaabbec. Foub fobdbe bec œufc, be beboubbe cub ba\nfbabe où be cuac bée. Be feub fafbe fbuc de cebb abc !\n",
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
                textbook_page=13,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befbabe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabaface"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becoufebbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="écaabbec"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="œufc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beboubbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bée"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fafbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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

    def test_exercise_0018(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=14,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cfoacac be cabbe de fobcbuabaob bua cobfaebb.\n\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• Debaab , : bec ebfabbc b’abobb fac à b’écobe ? .\n• Foubbuoa ec-bu cobbebb ... ?\n• B’adobe cebbe cfabcob , !\n• Afec ce cfafeau ... ? bu ec fbaabebb dbôbe . :\n",
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
                textbook_page=14,
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
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Debaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="écobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foubbuoa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabcob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfafeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbaabebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dbôbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
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

    def test_exercise_0019(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="ì\nEbboube bec cabbec de fobcbuabaob.\n",
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
                        insert="a. B’afaabeub ecb febdu.\nb. Babfeubeucebebb, cob afaob ecb eb fabbe !\nc. Ab ce bebboufe ceub au babaeu du décebb.\nd. Febdabb ba buab, ab a eu bbèc fboad.\ne. Cobbebb fa-b-ab deccabeb ce boubob ?\n",
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
                number="6",
                textbook_page=15,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ì"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="a"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="afaabeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febdu"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Babfeubeucebebb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="c"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babaeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="d"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Febdabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fboad"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="e"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deccabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
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

    def test_exercise_0020(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cfoacac be foabb bua cobfaebb foub fabab cec\nffbacec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ce bafbe ecb faccaobbabb . ! ?\nb. À bua affabbaebb ce cbabo . ! ?\nc. Cébacbaeb a febdu ube debb de baab . ! ?\nd. Bocabae, faac boabc de bbuab . ! ?\ne. Buebbec cfauccubec cfoacac-bu . ! ?\n",
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
                textbook_page=15,
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
                                            r.Text(kind="text", text="foabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
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
                                            r.Text(kind="text", text="bafbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faccaobbabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="À"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affabbaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbabo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cébacbaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febdu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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
                                            r.Text(kind="text", text="Cfoacac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
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
                                            r.Text(kind="text", text="Bocabae"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbuab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Buebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfauccubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoacac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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

    def test_exercise_0021(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ce bebbe eb ebboubabb bec cabbec du daabobue.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc ba coub, Ébace eb Aouccef ce dacfubebb :\n« Dobbe-boa ce babbob, bécbabe Aouccef.\n− Bob, be be babde ! Ob fa faabe ube fabbae de bacfeb,\nbéfobd Ébace.\n− Bu b’ac bu’à eb fbebdbe ub aubbe.\n− Baac c’ecb be debbaeb bu’ab becbe. »\n",
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
                textbook_page=15,
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
                                            r.Text(kind="text", text="ebboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daabobue"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Dabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coub")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=",")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ébace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Aouccef")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dacfubebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=":")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="«")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Dobbe")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="-")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boa")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babbob")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=",")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bécbabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Aouccef")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="−")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bob")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=",")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babde")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="!")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fa")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="faabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabbae")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bacfeb")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=",")]
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daabobue"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="béfobd")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ébace")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="−")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bu")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                contents=[r.Text(kind="text", text="b"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                contents=[r.Text(kind="text", text="bu"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbebdbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aubbe")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="−")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Baac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                contents=[r.Text(kind="text", text="c"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="debbaeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00"],
                                                contents=[r.Text(kind="text", text="bu"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="becbe")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="»")]
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

    def test_exercise_0022(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ce daabobue eb be fbécebbabb cobbecbebebb. Abbebbaob, ab babbue ub cabbe de\nfobcbuabaob !\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Eb ebbbabb dabc ba fababade, be fbofecceub bubbube à cob accacbabb : Fouc b’afec fac oubbaé ba babfe, b’ecfèbe. – Be fouc abbuaébec fac, b’aa boub\nce bu’ab faub. – Bouc aubobc aucca becoab d’ub\naffabeab ffobo, aboube-b-ab. – Ab ecb dabc bob cac.\nB’aa fbac aucca ube bouccobe eb ub coubeau.\n",
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
                textbook_page=15,
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
                                            r.Text(kind="text", text="daabobue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbécebbabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecbebebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abbebbaob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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
                                            r.Text(kind="text", text="Eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fababade"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofecceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubbube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accacbabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oubbaé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babfe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecfèbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbuaébec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faub"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aubobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aucca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becoab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ub"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="affabeab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffobo"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboube"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ab"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cac"),
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
                                            r.Text(kind="text", text="daabobue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbécebbabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecbebebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abbebbaob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aucca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouccobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubeau"),
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

    def test_exercise_0023(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Béécbac cec ffbacec eb aboubabb bec babuccubec eb ba fobcbuabaob.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. cobbaeb coûbe\n*\nce boubueb\nb. cec cabbec cobb bbof dbôbec\nc. fabaa débébabe ba cebaabe fbocfaabe\nd. feub-bu febab be cfebcfeb\n",
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
                textbook_page=15,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Béécbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="cobbaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coûbe"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="*")]),
                                    r.Paragraph(
                                        contents=[r.Text(kind="text", text="ce"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="boubueb")]
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
                                            r.Text(kind="text", text="Béécbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dbôbec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabaa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débébabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbocfaabe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebcfeb"),
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

    def test_exercise_0024(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Céfabe bec ffbacec, eb aboube bec babuccubec\neb ba fobcbuabaob.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="foub cob abbafebcaabe Babfab a abfabé bouc cec\nabac abc cobb d’abobd abbéc boueb dabc be fabc\nebcuabe abc obb bouc couffbé cub bec boubaec du\nbâbeau boub be bobde a beaucouf ba\n",
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
                textbook_page=15,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Céfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbafebcaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babfab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="abac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ebcuabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couffbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubaec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
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
                                            r.Text(kind="text", text="Céfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="bâbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobde"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beaucouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
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

    def test_exercise_0025(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ce bebbe eb cfoacaccabb be cabbe de\nfobcbuabaob bua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Bua ce cacfe debbaèbe Bobcaeub Babbabbe ... ,\nfeabbbe cubbéabacbe ! ? Babbabbe ecb ub febab\nbobcaeub obdabaabe eb cocbube-cbafabe-cfafeau\nbebob , . baac afec ube ababababaob ebbbaobda-\nbaabe ! ? « Boub ce bue b’ob foab cacfe buebbue\ncfoce » dacaab-ab ? . Ube bebbe ebfocabaob cub cob\nœufbe faebb d’oufbab au Cebbbe Fobfadou , .\nBe Febab Béobabd b°217, © Édabaobc Fabob, ocbobbe 2016.\n",
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
                textbook_page=15,
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
                                            r.Text(kind="text", text="cfoacaccabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="Bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bobcaeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="feabbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubbéabacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bobcaeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obdabaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cocbube"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="cbafabe"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="cfafeau"),
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
                                            r.Text(kind="text", text="cfoacaccabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="bebob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababababaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbaobda"),
                                            r.Text(kind="text", text="-"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="baabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="«"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buebbue"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cfoce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="»"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dacaab"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfocabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
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
                                            r.Text(kind="text", text="cfoacaccabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
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
                                            r.Text(kind="text", text="œufbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oufbab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fobfadou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Béobabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="°"),
                                            r.Text(kind="text", text="217"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="©"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Édabaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fabob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ocbobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="2016"),
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

    def test_exercise_0026(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Abababe ce bue feufebb ce dabe be bobcbbe\neb ba fabbe.\nOBAB\n",
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
                number="13",
                textbook_page=15,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abababe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feufebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobcbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="OBAB")]),
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

    def test_exercise_0027(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac ba cuabe du daabobue ebbbe b’afaabeub\neb be Febab Fbabce.\n",
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
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daabobue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="afaabeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fbabce"),
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

    def test_exercise_0028(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Boube ba fobcbuabaob c’ecb bébabbée !\nBéécbac eb bebebbabb cfabue cabbe de\nfobcbuabaob à ba bobbe fbace.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Bouc bec cabedac ! Fabbo fa aadeb ca, babae\nDabc be babdab ab. abboce bec bocec. bec bubafec\neb bec abac Ab abbacfe. aucca bec baufaacec\nfebbec, Bueb bbafaab,\n",
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
                textbook_page=15,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabbée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Béécbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebebbabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbace"),
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
                                            r.Text(kind="text", text="Bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabedac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fabbo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aadeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babae"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babdab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abboce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bocec"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubafec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacfe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aucca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baufaacec"),
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
                                            r.Text(kind="text", text="Boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébabbée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Béécbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebebbabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbuabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbace"),
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
                                            r.Text(kind="text", text="febbec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafaab"),
                                            r.Text(kind="text", text=","),
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

    def test_exercise_0029(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=15,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Debbaèbe ub bub de faebbec, ub beube fobbe découfbe\nube baacob ababdobbée. Ba fobbe eb bec fabbec cobb\ncaccéec. Bua feub baeb fababeb aca ?\n",
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
                textbook_page=15,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Debbaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faebbec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="découfbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababdobbée"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="caccéec"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fababeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
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

    def test_exercise_0030(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=16,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Buebbec ffbacec dobbebb ub obdbe ? Fab buebc\nfoabbc ce bebbabebb-ebbec ?\n\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• Feub-bu fobbeb cebbe babebbe ?\n• Fobbe cebbe babebbe !\n• Ebbe b’a fac foubu fobbeb cebbe babebbe.\n• Ca bu cobc, fobbe cebbe babebbe à ba bbabd-bèbe.\n",
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
                textbook_page=16,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Buebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbabebb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ebbec"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Feub"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foubu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babebbe"),
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
                                            r.Text(kind="text", text="Buebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbabebb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ebbec"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bèbe"),
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

    def test_exercise_0031(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=16,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Buebbe ffbace feub ce bebbabeb fab ub foabb\nd’abbebbobabaob ?\n\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• Écoube ba cobcabbe... • Ac-bu faab...\n• B’aa acfebé dec fobbec...\n",
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
                number="5",
                textbook_page=16,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Buebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbebbobabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
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
                                            r.Text(kind="text", text="Écoube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobcabbe"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="acfebé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbec"),
                                            r.Text(kind="text", text="..."),
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

    def test_exercise_0032(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=16,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Buebbe ffbace dobbe ube abfobbabaob ?\n\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• Ecb-ce bue bu ebbebdc ? • Cobc de bà !\n• Be buc facce defabb ba babe.\n",
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
                number="6",
                textbook_page=16,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Buebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfobbabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
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
                                            r.Text(kind="text", text="Ecb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbebdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bà"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="defabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babe"),
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

    def test_exercise_0033(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ubabuebebb bec ffbacec décbababafec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ba beabe ecb bobbée boube ba bababée.\nb. Foce bob babbeau cub cebbe cfaace !\nc. Bouc fêbebobc bob abbafebcaabe debaab coab.\nd. Foubec-fouc babe ce boubbab ?\n",
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
                number="7",
                textbook_page=17,
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
                                            r.Text(kind="text", text="décbababafec"),
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
                                            r.Text(kind="text", text="beabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababée"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fêbebobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbafebcaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coab"),
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
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbababafec"),
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
                                            r.Text(kind="text", text="Foubec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubbab"),
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

    def test_exercise_0034(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ubabuebebb bec ffbacec abbebbobabafec eb aboube beub foabb.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Cobbebb fobcbaobbe cebbe babbebbe...\nb. Be babbec babaac bec fbuabc de ceb abbucbe...\nc. Cebbe foabube ecb-ebbe ba fôbbe...\nd. Defuac be débub du boac, ba bafaèbe ecb eb cbue...\n",
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
                textbook_page=17,
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
                                            r.Text(kind="text", text="abbebbobabafec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabb"),
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
                                            r.Text(kind="text", text="Cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobcbaobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbebbe"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babaac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbucbe"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fôbbe"),
                                            r.Text(kind="text", text="..."),
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
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabb"),
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
                                            r.Text(kind="text", text="Defuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbue"),
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

    def test_exercise_0035(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ubabuebebb bec ffbacec abfébabafec\neb aboube beub foabb.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be fobbe fac de cfabbe bbof boubde...\nb. A-b-ab febbé ba febêbbe...\nc. Foub buébab ba boub, ab faub fbebdbe du cabof...\nd. Abbêbe d’ebbuaeb ba cœub...\n",
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
                textbook_page=17,
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
                                            r.Text(kind="text", text="abfébabafec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabb"),
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
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubde"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="A"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febêbbe"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buébab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabof"),
                                            r.Text(kind="text", text="..."),
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
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfébabafec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabb"),
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
                                            r.Text(kind="text", text="Abbêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebbuaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cœub"),
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

    def test_exercise_0036(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac bec ffbacec décbababafec bua béfobdebb\nà cec ffbacec abbebbobabafec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Buebbe feube ecb-ab ?\nb. Foubbuoa ebfobbec-fouc ub fabafbuae ?\nc. Aabec-bu ba bababaob ?\nd. Bua ecb Cebdbabbob ?\ne. Où feub-ob acfebeb du faab ?\n",
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
                textbook_page=17,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbababafec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobdebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafec"),
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
                                            r.Text(kind="text", text="Buebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foubbuoa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfobbec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabafbuae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Aabec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababaob"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbababafec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobdebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafec"),
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
                                            r.Text(kind="text", text="Bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cebdbabbob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="acfebeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
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

    def test_exercise_0037(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac bec ffbacec abbebbobabafec aubbuebbec\nbéfobdebb cec ffbacec décbababafec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be febb faebb du cud.\nb. Ebbe c’affebbe Boacebbe.\nc. Bob bebca, be b’aa fbuc coaf.\nd. Bouc be bebboufobc fac boc cbéc.\ne. Boïc b’affbécae fac ce deccab ababé.\n",
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
                textbook_page=17,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aubbuebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobdebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbababafec"),
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
                                            r.Text(kind="text", text="febb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cud"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boacebbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebca"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coaf"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aubbuebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobdebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbababafec"),
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
                                            r.Text(kind="text", text="Bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebboufobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbéc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boïc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affbécae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deccab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababé"),
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

    def test_exercise_0038(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bbabcfobbe cec ffbacec eb ffbacec abfébabafec, cobbe dabc b’ebebfbe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bu doac bua bebdbe cob babbob.\nb. Ab faub bue bouc febaobc afec fouc.\nc. Foufec-fouc fabbeb boabc fabe ?\nd. Feub-bu be dobbeb be ceb ?\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Bu doac fbebdbe ce cabof. ➞ Fbebdc ce cabof !\n",
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
                textbook_page=17,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bbabcfobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfébabafec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebebfbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabof"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fbebdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbob"),
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
                                            r.Text(kind="text", text="faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foufec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabe"),
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
                                            r.Text(kind="text", text="Bbabcfobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfébabafec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebebfbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabof"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fbebdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabof"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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
                                            r.Text(kind="text", text="Feub"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceb"),
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

    def test_exercise_0039(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Accocae ba ffbace abfébabafe bua cobbecfobd\nà ba ffbace décbababafe.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ba boube ecb bbaccabbe.\nb. Ce cfocobab ecb bbèc cfaud.\nc. Ba beb bobbe.\nd. Be cobeab bbûbe* ba feau.\ne. Bob bbaab fabb à obce feubec.\n1. Bebc de ba cbèbe fbobecbbace.\n2. Défêcfe-boa, bu fac be babeb !\n3. Abbebdec ub feu afabb de be boabe !\n4. Boubec doucebebb !\n5. Buabbobc bafadebebb ba fbabe.\n",
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
                textbook_page=17,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Accocae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecfobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbababafe"),
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
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaccabbe"),
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
                                            r.Text(kind="text", text="cfocobab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaud"),
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
                                            r.Text(kind="text", text="beb"),
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
                                            r.Text(kind="text", text="Accocae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecfobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbababafe"),
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
                                            r.Text(kind="text", text="cobeab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbûbe"),
                                            r.Text(kind="text", text="*"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feau"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feubec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="1"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobecbbace"),
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
                                            r.Text(kind="text", text="Accocae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecfobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbababafe"),
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
                                            r.Text(kind="text", text="2"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Défêcfe"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="boa"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="3"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abbebdec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="4"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doucebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecfobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbababafe"),
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
                                            r.Text(kind="text", text="5"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Buabbobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafadebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabe"),
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

    def test_exercise_0040(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nBebebc cec bobc dabc b’obdbe foub faabe dec\nffbacec, fuac dobbe beub bafe.\n\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. be fbuc coubb. – a fbac – Be bouf – be cfebab\nb. cebbe fecbe – fobbec-fouc – fobbabbe ? – Foubbuoa\nc. fac – fabbe – ba boucfe fbeabe ! – Be\n",
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
                textbook_page=17,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bebebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafe"),
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
                                            r.Text(kind="text", text="fbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fecbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foubbuoa"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boucfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
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

    def test_exercise_0041(self):
        self.do_test(
            e.Exercise(
                number="15",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB. Obcebfe cebbe ababe, fuac écbac bboac ffbacec :\ndécbababafe, abbebbobabafe eb abfébabafe. Ubabace\nbec febbec : abbebdbe, bebabdeb, bbafebceb.\n\n",
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
                number="15",
                textbook_page=17,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(contents=[r.Text(kind="text", text="OBAB"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Obcebfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbababafe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfébabafe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ubabace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebdbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebabdeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafebceb"),
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

    def test_exercise_0042(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Décfaffbe ce bébuc eb dac au babçob de\nb’ebebcace 15 ce bu’ab be doab fac faabe.\n",
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
                textbook_page=17,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Décfaffbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babçob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebebcace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="15"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabe"),
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

    def test_exercise_0043(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=17,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="– Cobbebb be bobbec-bu ?\n– Bob bob ecb Febcobbe.\n– Be bebc fac !\n– Ca ob be cfebcfe, dac bue bu ac fu Febcobbe !\n",
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
                textbook_page=17,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Febcobbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
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
                            r.Section(paragraphs=[], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebcfe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Febcobbe"),
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

    def test_exercise_0044(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=18,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bbabcfobbe cec ffbacec eb ffbacec abbebbobabafec.\n\n\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• Fouc bboufec be bob cfebab.\n• Ab faab beau.\n• Ebbe affbebd baeb cob bôbe.\n• Bu befaebdbac baebbôb.\n• Fouc cebec bà foub be feef-ebd*.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Bu ec cobbebb.\n➞ Ec-bu cobbebb ? / Ecb-ce bue bu ec cobbebb ?\n",
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
                textbook_page=18,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bbabcfobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ecb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beau"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affbebd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bôbe"),
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
                                            r.Text(kind="text", text="Bbabcfobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ecb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befaebdbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baebbôb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bà"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feef"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ebd"),
                                            r.Text(kind="text", text="*"),
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

    def test_exercise_0045(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=19,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ubabuebebb bec ffbacec abbebbobabafec.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Fbabçoac-bubab ecb dabc be babbace.\nb. A-b-ab abfbeccaobbé cec cababadec ?\nc. Caab-ab aucca bbabfeb à ba cobde ?\nd. Bueb ébbabbe febab-débeubeb !\ne. Be fbéfèbe-b-ab fac ube babbabe de cobfabube ?\n",
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
                number="5",
                textbook_page=19,
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
                                            r.Text(kind="text", text="abbebbobabafec"),
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
                                            r.Text(kind="text", text="Fbabçoac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bubab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="A"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfbeccaobbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cababadec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Caab"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aucca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabfeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobde"),
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
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafec"),
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
                                            r.Text(kind="text", text="Bueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="débeubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="!"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfèbe"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfabube"),
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

    def test_exercise_0046(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=19,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae eb cbacce cec ffbacec abbebbobabafec,\ncebob ba babaèbe dobb ebbec cobb cobcbbuabec.\nFebbe + cubeb ... ? Ecb-ce bue + cubeb +\nfebbe ... ?\n\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ecb-ce bue be buéfabd coubb fabe ?\nb. Fac-bu béfabeb be boab de ba baacob ?\nc. Ecb-ce bue bec ebfabbc cobb cabec ?\nd. Cfabbebb-abc ebcebbbe dabc ube cfobabe ?\ne. Debabdec-fouc ba febbaccaob foub cobbab ?\n",
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
                number="6",
                textbook_page=19,
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobcbbuabec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="?")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ecb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="?")]),
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
                                            r.Text(kind="text", text="Ecb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buéfabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ecb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabec"),
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
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabafec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobcbbuabec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="?")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ecb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="?")]),
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
                                            r.Text(kind="text", text="Cfabbebb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfobabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Debabdec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbaccaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbab"),
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

    def test_exercise_0047(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=19,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae cec ffbacec eb écbafabb be bob\nabbebbobabaf eb boube. Ebboube be febbe eb cou-\nbabbe be cubeb.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Foubbuoa fbeubec-bu ?\nb. Où ce bboufe b’fôbeb ?\nc. Buabd abfebbebec-fouc ba bacfabe à bebobbeb\nbe bebfc ?\nd. Cobbebb ce défbaçaaebb bec fobbec au\nBoaeb Âbe ?\ne. Bue febce Cabdba de cebbe facboabe ?\n",
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
                number="7",
                textbook_page=19,
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
                                            r.Text(kind="text", text="écbafabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cou"),
                                            r.Text(kind="text", text="-"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
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
                                            r.Text(kind="text", text="Foubbuoa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeubec"),
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
                                            r.Text(kind="text", text="Où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="fôbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Buabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfebbebec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebobbeb"),
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
                                            r.Text(kind="text", text="écbafabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cou"),
                                            r.Text(kind="text", text="-"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défbaçaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Boaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Âbe"),
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
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbafabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbobabaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cou"),
                                            r.Text(kind="text", text="-"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
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
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cabdba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facboabe"),
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

    def test_exercise_0048(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=29,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc bec ffbacec, cobobae bec cobfbébebbc.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bouc acfebobc dec fbuabc fbaac.\nb. Ba cœub ecb abbobbée cub be cabbe.\nc. À bada boub bucbe, be débeubebaa !\nd. Faebdbobb-abc eb buc ?\ne. B’aa écbab à ba coucabe.\n",
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
                textbook_page=29,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbébebbc"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bouc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="acfebobc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbuabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbaac")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cœub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ecb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbobbée")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabbe")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="À")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bada")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bucbe")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=",")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="débeubebaa")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="!")]
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
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbébebbc"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Faebdbobb")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="-")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="buc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text="?")]
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
                                                contents=[r.Text(kind="text", text="B"), r.Text(kind="text", text="’")],
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aa")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="écbab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coucabe")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00"], padding=(16.0, 3.2), contents=[r.Text(kind="text", text=".")]
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

    def test_exercise_0049(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=29,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec ffbacec afec bec\ncobfbébebbc de bob cfoab.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Babab bbacobe ... foub ba febabe cœub.\n\nb. Bec aubobobabec boubebb bbèc fabe ... .\n\nc. ... , bouc cfaobc cub bec facbec ebbeabéec.\n\nd. Beaucouf de boubacbec foaabebb ... .\n\ne. B’ebfoae ube cabbe focbabe ... .\n",
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
                number="13",
                textbook_page=29,
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
                                            r.Text(kind="text", text="cobfbébebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoab"),
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
                                            r.Text(kind="text", text="bbacobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cœub"),
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
                                            r.Text(kind="text", text="aubobobabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbeabéec"),
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
                                            r.Text(kind="text", text="cobfbébebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoab"),
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
                                            r.Text(kind="text", text="Beaucouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foaabebb"),
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
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebfoae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="focbabe"),
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

    def test_exercise_0050(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=19,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Accocae cfabue buecbaob à ca béfobce.\n",
                        attributes=TextInsertOpAttributes(
                            italic=False, bold=False, highlighted=None, choices2=None, mcq_placeholder=False, manual_item=False, sel=None
                        ),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Où fabc-bu ?\nb. Buabd fabc-bu ?\nc. Foubbuoa fabc-bu ?\nd. Cobbebb fabc-bu ?\ne. Afec bua fabc-bu ?\n1. Be fabc ba cebaabe\nfbocfaabe.\n2. Be fabc afec bob\nabae Faobaabe.\n3. Be fabc eb bbaab.\n4. Be fabc au Fobbubab.\n5. Be fabc cab b’affbebdc\nbe fobbubaac.\n",
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
                textbook_page=19,
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
                                            r.Text(kind="text", text="buecbaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobce"),
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
                                            r.Text(kind="text", text="Où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
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
                                            r.Text(kind="text", text="Buabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foubbuoa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
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
                                            r.Text(kind="text", text="Accocae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buecbaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobce"),
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
                                            r.Text(kind="text", text="Cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="1"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebaabe"),
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
                                            r.Text(kind="text", text="buecbaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobce"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(contents=[r.Text(kind="text", text="fbocfaabe"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="2"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="abae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Faobaabe"),
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
                                            r.Text(kind="text", text="Accocae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buecbaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobce"),
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
                                            r.Text(kind="text", text="3"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="4"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fobbubab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="5"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affbebdc"),
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
                                            r.Text(kind="text", text="buecbaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobce"),
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
                                            r.Text(kind="text", text="fobbubaac"),
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
