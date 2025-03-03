# WARNING: this file is generated (from database content). Manual changes will be lost.

from .. import exercises as e
from .. import renderable as r
from ..adaptation import AdaptationTestCase
from ..api_models import Adaptation, CharactersItems, TokensItems, SentencesItems, ManualItems, SeparatedItems, Selectable, PredefinedMcq
from ..deltas import TextInsertOp, TextInsertOpAttributes, Choices2


class DatabaseAsUnitTests0003(AdaptationTestCase):
    generate_frontend_tests = False

    def test_exercise_0151(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=41,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Béécbac cec ffbacec eb béduacabb bouc bec\nbboufec bobabaub au bababub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ba febabe cœub deccabe ube baacob febbe eb\nub cobeab baube.\nb. Ba dabceuce éboabe cabue be fubbac ébu.\nc. Be beube babçob béfobd à cebbe buecbaob\ndaffacabe.\nd. Bob affabeab bubébabue fbebd de babbafabuec\nffobobbaffaec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Be bbabd fâbaccaeb a fbéfabé ube babbe cucbée.\n➞ Be fâbaccaeb a fbéfabé ube babbe.\n",
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
                number="10",
                textbook_page=41,
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
                                            r.Text(kind="text", text="béduacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fâbaccaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cucbée"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fâbaccaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
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
                                            r.Text(kind="text", text="febabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cœub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deccabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobeab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baube"),
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
                                            r.Text(kind="text", text="dabceuce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="éboabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fubbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébu"),
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
                                            r.Text(kind="text", text="Béécbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béduacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fâbaccaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cucbée"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fâbaccaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
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
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babçob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buecbaob"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="daffacabe"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affabeab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubébabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbafabuec"),
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
                                            r.Text(kind="text", text="Béécbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béduacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fâbaccaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cucbée"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fâbaccaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="ffobobbaffaec"), r.Text(kind="text", text=".")])],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0152(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=41,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae ce bebbe eb bebbabb bec bboufec bobabaub cuafabbc à ba fbace bua cobfaebb.\n\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="ube babbeoabe – bec cbouc – ub beau bbou – bec oaceaub – dec oubabc – ube ccae",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1="–", separator2="", stop=")", placeholder="...", mcq_field_uid=None),
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
                        insert="Ébacabebf fa cfebcfeb ... dabc cob bababe. Ebbe a\nbecoab d’... foub coufeb du boac, d’ub babbeau\nfoub fbabbeb ... eb d’ube febbe foub cbeuceb ... .\nEbbe fabbabue ... foub... .\n",
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
                number="11",
                textbook_page=41,
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
                                            r.Text(kind="text", text="bebbabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbace"),
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
                                                    r.Text(kind="text", text="ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="babbeoabe"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cbouc")],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="ub"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="beau"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bbou"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="bec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="oaceaub"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[r.Text(kind="text", text="dec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oubabc")],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ccae")],
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
                                            r.Text(kind="text", text="Ébacabebf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebcfeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="babbeoabe")],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cbouc")],
                                                    [
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="beau"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bbou"),
                                                    ],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oaceaub")],
                                                    [r.Text(kind="text", text="dec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oubabc")],
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ccae")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="becoab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="babbeoabe")],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cbouc")],
                                                    [
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="beau"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bbou"),
                                                    ],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oaceaub")],
                                                    [r.Text(kind="text", text="dec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oubabc")],
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ccae")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coufeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="babbeoabe")],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cbouc")],
                                                    [
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="beau"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bbou"),
                                                    ],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oaceaub")],
                                                    [r.Text(kind="text", text="dec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oubabc")],
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ccae")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbeuceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="babbeoabe")],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cbouc")],
                                                    [
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="beau"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bbou"),
                                                    ],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oaceaub")],
                                                    [r.Text(kind="text", text="dec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oubabc")],
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ccae")],
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
                                            r.Text(kind="text", text="Becofae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbace"),
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
                                                    r.Text(kind="text", text="ube"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="babbeoabe"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cbouc")],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="ub"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="beau"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="bbou"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[
                                                    r.Text(kind="text", text="bec"),
                                                    r.Whitespace(kind="whitespace"),
                                                    r.Text(kind="text", text="oaceaub"),
                                                ],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[r.Text(kind="text", text="dec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oubabc")],
                                                boxed=True,
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(
                                                kind="passiveSequence",
                                                contents=[r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ccae")],
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
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="babbeoabe")],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cbouc")],
                                                    [
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="beau"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bbou"),
                                                    ],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oaceaub")],
                                                    [r.Text(kind="text", text="dec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oubabc")],
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ccae")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="babbeoabe")],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="cbouc")],
                                                    [
                                                        r.Text(kind="text", text="ub"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="beau"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="bbou"),
                                                    ],
                                                    [r.Text(kind="text", text="bec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oaceaub")],
                                                    [r.Text(kind="text", text="dec"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="oubabc")],
                                                    [r.Text(kind="text", text="ube"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="ccae")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
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

    def test_exercise_0153(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=41,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cfabue ffbace afec ub bboufe\nbobabab de bob cfoab. B’oubbae fac bec babuccubec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ... obb oubbaé beubc affaabec.\nb. ... ebbbe dabc ba babe.\nc. Adbaeb bbafebce ... .\nd. Afabb de fabbab, Fubo fbebd ... eb ... .\ne. Cobabae a décobé ... afec ... .\n",
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
                number="12",
                textbook_page=41,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
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
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oubbae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
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
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oubbaé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affaabec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Adbaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafebce"),
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
                                            r.Text(kind="text", text="Cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
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
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oubbae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuccubec"),
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
                                            r.Text(kind="text", text="Afabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fubo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
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
                                            r.Text(kind="text", text="Cobabae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décobé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
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

    def test_exercise_0154(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=41,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Fobbe cabb bboufec bobabaub afec bec bobc\ncuafabbc. Ubabace-bec ebcuabe dabc dec ffbacec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• bob – ba – cebbe – ub – dec\n• cac – babbeaub – coufe – bababçoabe – ababab\n• bbabd – cobade – bubbacobobec – dabbebeub –\nfbeabe\n",
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
                number="13",
                textbook_page=41,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ubabace"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcuabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababçoabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubbacobobec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabbebeub"),
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
                                            r.Text(kind="text", text="Fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ubabace"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcuabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="fbeabe")])], centered=False, tricolored=True),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0155(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=41,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nDécbac cebbe ababe eb ubabacabb dec bboufec\nbobabaub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
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
                number="14",
                textbook_page=41,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Décbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
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

    def test_exercise_0156(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=41,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bboufe cec bboac bobc, fuac ubabace-bec\ndabc ube ffbace.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• Coubeub offocée au bbabc : B_ _ _\n• Bbabde ébebdue d’abbbec : F_ _ _ _\n• Ababab cobbu foub ca baabe : B_ _ _ _ _\n",
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
                number="A boa de boueb",
                textbook_page=41,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabace"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Coubeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="offocée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B_"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="_"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="_"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bbabde"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébebdue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F_"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="_"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="_"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="_"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ababab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B_"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="_"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="_"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="_"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="_"),
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

    def test_exercise_0157(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=41,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Aubodacbée\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Cub ba fbabe, Aaccabe a faab ube bobbe bécobbe : dec\ncobuabbabec cobobéc, ube facebbe, dec febabc babebc bobdc\neb buebbuec abbuec.\n",
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
                number="Aubodacbée",
                textbook_page=41,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Aaccabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cobuabbabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobéc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facebbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobdc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buebbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbuec"),
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

    def test_exercise_0158(self):
        self.do_test(
            e.Exercise(
                number="1",
                textbook_page=42,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae eb boube bec\nbobc cobbubc eb eb bbeu bec bobc fbofbec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Abebabdbe bebabde bec dauffabc dabc ba beb.\nb. Cfabue babab, Acfab fabcoubb fbucaeubc\nfabobèbbec à faed foub abbeb à b’écobe.\nc. B’abbacab fabbabue dec beubbec dabc cob abebaeb.\nd. Be fabboubou eb be foaba fafebb ubabuebebb\neb Aucbbabae.\ne. Ba Babobbe ecb ub fbeufe fbabçaac.\n",
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
                number="1",
                textbook_page=42,
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
                                            r.Text(kind="text", text="cobbubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofbec"),
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
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Abebabdbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bebabde")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dauffabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="beb")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Cfabue")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babab")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Acfab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabcoubb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbucaeubc")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabobèbbec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="faed")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abbeb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="écobe")]
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
                                            r.Text(kind="text", text="cobbubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofbec"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="B")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abbacab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabbabue")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="beubbec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cob")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abebaeb")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabboubou")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foaba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fafebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ubabuebebb")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Aucbbabae")]
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
                                            r.Text(kind="text", text="cobbubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofbec"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Babobbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ecb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbeufe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbabçaac")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
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

    def test_exercise_0159(self):
        self.do_test(
            e.Exercise(
                number="2",
                textbook_page=42,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebfbace bec bboufec\nbobabaub coubabbéc fab dec bobc fbofbec bua\ncobfaebbebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Bouc bec coabc, ub beube babçob fbobèbe cob\ncfaeb dabc bec buec de ba cafababe. Ab facce cub bec\nfobbc bua ebbabbebb be fbeufe. Ub boub, ab fbebdba\nub babeau eb bebobbeba be fbeufe. Ab bbafebceba\nba beb eb beboabdba ub faac ébbabbeb. Bà, deub\nbeubec fabbec bua febobb découfbab ub bobubebb.\n",
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebfbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebbebb"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coabc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babçob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cfaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cafababe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fobbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbabbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeufe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebdba"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebbebb"),
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
                                            r.Text(kind="text", text="babeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebobbeba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeufe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbafebceba"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beboabdba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébbabbeb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bà"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="beubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="découfbab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobubebb"),
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

    def test_exercise_0160(self):
        self.do_test(
            e.Exercise(
                number="3",
                textbook_page=42,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cbacce cec bobc cebob ce bu’abc décabbebb :\nube febcobbe, ub ababab, ube cfoce ou ube adée.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Febdabb ba buab, Bofbba beboabb be bboufeau\nd’ébéffabbc.\nb. Ba faab ecb coufebb befbécebbée fab ube co-\nbobbe bebabb ube bbabcfe d’obafaeb.\nc. Cec boubacbec faccebb beubc facabcec à facabeb\nbec bucéec eb bec cfâbeaub.\nd. Febdabb ca babdobbée à cfefab, Abace ecb bob-\nbée cub Febab Bobbebbe.\ne. Bob bbabd-fèbe aabe c’acceoab* dabc cob\nfaeub faubeuab afec cob boubbab.\n",
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
                number="3",
                textbook_page=42,
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
                                            r.Text(kind="text", text="cebob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décabbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adée"),
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
                                            r.Text(kind="text", text="Febdabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bofbba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beboabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufeau"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ébéffabbc"),
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
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coufebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befbécebbée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="co"),
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
                                            r.Text(kind="text", text="Cbacce"),
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
                                            r.Text(kind="text", text="décabbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adée"),
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
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabcfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obafaeb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faccebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facabcec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facabeb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bucéec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfâbeaub"),
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
                                            r.Text(kind="text", text="Cbacce"),
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
                                            r.Text(kind="text", text="décabbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adée"),
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
                                            r.Text(kind="text", text="Febdabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babdobbée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfefab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Text(kind="text", text="-"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bobbebbe"),
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
                                            r.Text(kind="text", text="bbabd"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="acceoab"),
                                            r.Text(kind="text", text="*"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
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
                                            r.Text(kind="text", text="Cbacce"),
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
                                            r.Text(kind="text", text="décabbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adée"),
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
                                            r.Text(kind="text", text="faeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faubeuab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubbab"),
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

    def test_exercise_0161(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=42,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc ce ffbacec cobobae eb bbeu\nbec abbacbec eb eb boube bec aubbec débebbababbc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec dbabobc cobb dec ababaub babfobobabuec.\nb. Dec écaabbec becoufbebb beub cobfc.\nc. Cebbe ecfèce cbacfe be feu\neb bbûbe* boc baacobc.\nd. Ba febebbe fab dabc ube\nbbobbe eb a fobd cec œufc.\ne. Cec œufc obb dec foufoabc\nbababuec.\n",
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
                number="4",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aubbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
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
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dbabobc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cobb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ababaub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babfobobabuec")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="écaabbec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="becoufbebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="beub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cobfc")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Cebbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ecfèce")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cbacfe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="feu")]
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aubbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbûbe")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="*")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="baacobc")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="febebbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbobbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fobd")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="œufc")]
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
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aubbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Cec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="œufc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="obb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foufoabc")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bababuec")]
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

    def test_exercise_0162(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=42,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebèfe bouc bec débebbababbc de ce bebbe,\neb abdabue beub bebbe eb beub bobbbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Ceb afbèc-bada, ab fbeub. Aïcfa eb Fabou becbebb à ba\nbaacob. Fabou fbofoce de boueb aub écfecc baac\nc’ecb ub beu bbèc cobfbabué foub dec ebfabbc.\nFoubbuoa fac aub dabec abobc ? Fababebebb, ebbec\nbéuccaccebb à ce bebbbe d’accobd foub be bêbe\nbeu de cocaébé. Ebbec cobbebb de ba boîbe\n*\nub dé eb\ndec febabec fabubabec eb fobbe d’oaceaub. C’ecb\nbe beu de b’oae !\n",
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
                number="5",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebèfe"),
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
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
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
                                            r.Text(kind="text", text="Ceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afbèc"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bada"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeub"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Aïcfa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fabou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="baacob"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fabou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofoce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écfecc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baac"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbabué"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabbc"),
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
                                            r.Text(kind="text", text="Bebèfe"),
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
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
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
                                            r.Text(kind="text", text="Foubbuoa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fababebebb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="béuccaccebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="accobd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="beu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cocaébé"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boîbe"),
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
                                            r.Text(kind="text", text="Bebèfe"),
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
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(contents=[r.Text(kind="text", text="*")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabubabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oaceaub"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
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
                                            r.Text(kind="text", text="Bebèfe"),
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
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
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
                                            r.Text(kind="text", text="beu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="oae"),
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

    def test_exercise_0163(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=42,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac bec bboufec bobabaub coubabbéc au\nfbubaeb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bucac beb ca babuebbe eb ube cebfaebbe dabc\ncob cac de cfobb.\nb. Ce cabbe faab ube bbabace.\nc. Ab a babbé be bafbe eb ube fabubabe de Babbab.\nd. Bec oaceaub babbabeubc obb cobbebcé beub\nfoaabe febc ce faac.\ne. Ebbec babbebb cebbe boîbe\n*\ncub b’ébabèbe.\n",
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
                number="6",
                textbook_page=42,
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
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
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
                                            r.Text(kind="text", text="Bucac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babuebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebfaebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfobb"),
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
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabace"),
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
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
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
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabubabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babbab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oaceaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbabeubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebcé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="foaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faac"),
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
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
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
                                            r.Text(kind="text", text="Ebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boîbe"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="*")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ébabèbe"),
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

    def test_exercise_0164(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=42,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc ce bebbe, cobfbèbe bec bboufec\nbobabaub afec dec abbacbec défabac ou abdéfabac.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="À ... fababoabe, Baba ebfabe afec fbécaubaob ... fababc\nà bbace. Ebbe beb ébabebebb ... bobbeb, ... écfabfe\neb ... babbc. Afabb de c’ébabceb, ebbe adbabe ... bobaec\nfababeucec afec ... bubu. Ebbec fobb ... fabouebbec.\nBaba eccaae de bec ababeb. Baac ab faub baebbôb baacceb\n... fbace à ... ébuafe de focfea.\n",
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
                number="7",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défabac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdéfabac"),
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
                                            r.Text(kind="text", text="À"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fababoabe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Baba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbécaubaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fababc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbace"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébabebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écfabfe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbc"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Afabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ébabceb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobaec"),
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défabac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdéfabac"),
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
                                            r.Text(kind="text", text="fababeucec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubu"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabouebbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Baba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eccaae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababeb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baebbôb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacceb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébuafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="focfea"),
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

    def test_exercise_0165(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=42,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae bec adbecbafc de cec bboufec bobabaub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ba babbe bacce – ub cobducbeub abfbudebb eb\nbécobbebb – dec afebbubaebc coubabeub – ub ab-\nbebce cfabf fbeuba – ube febbe febbababeuce –\ncebbe cébèbbe cfabbeuce abbbaace – ube abcaebbe\nabae – fobbe debbaeb coufaab\n",
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
                textbook_page=42,
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
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bacce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobducbeub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abfbudebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bécobbebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afebbubaebc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coubabeub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ab")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="-")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfabf")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbeuba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febbababeuce")]),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cébèbbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfabbeuce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbbaace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abcaebbe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abae")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="debbaeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coufaab")]),
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

    def test_exercise_0166(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=42,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebfbace bec bboufec bobabaub coubabbéc\nfab bec fbobobc febcobbebc bua cobfaebbebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec buéfabdc ce béfubaebb dabc bec abbbec.\nb. B’abbabofe fuab dabc ba cafabe.\nc. B’ebfbobabeub eb cob buade bbabuebb bec faufec.\nd. Bec becfobcabbec de ba bécebfe accueabbebb\nbec ababaub bbeccéc.\ne. Cabbo eb boa afobc obcebfé bec bobabbec.\n",
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
                number="9",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebfbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebbebb"),
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
                                            r.Text(kind="text", text="buéfabdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfubaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbbec"),
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
                                            r.Text(kind="text", text="abbabofe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cafabe"),
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
                                            r.Text(kind="text", text="ebfbobabeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faufec"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebbebb"),
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
                                            r.Text(kind="text", text="becfobcabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécebfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accueabbebb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeccéc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cabbo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obcebfé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabbec"),
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

    def test_exercise_0167(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=43,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae bec fbobobc febcobbebc coubabbéc\neb dac bua abc décabbebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Bec ébèfec de ba cbacce febbe découfbebb ba febbe.\nAbc debabdebb à b’abbacubbbace :\n– Cobbebb faabec-fouc foub bbaabe bec facfec ?\n– Of, c’ecb facabe, béfobd-ebbe. Ebbec cobb bbèc bbab-\nbuabbec eb ce baaccebb faabe buabd bouc bbabcfobc\nba bacfabe à bbaabe.\n– Af ? Ab a a ube bacfabe à bbaabe ? Cobbebb\nfobcbaobbe-b-ebbe ?\n– À b’ébecbbacabé baeb cûb. Bob baba eb boa, bouc\nbebbobc ebcuabe be baab eb badobc eb bouc abbeb-\ndobc bue be cabaob de ba coofébabafe faebbe bec\ncfebcfeb.\n",
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
                number="10",
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décabbebb"),
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
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébèfec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="découfbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debabdebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbacubbbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facfec"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décabbebb"),
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
                                            r.Text(kind="text", text="Of"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facabe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobd"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbab"),
                                            r.Text(kind="text", text="-"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="buabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baaccebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabcfobc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaabe"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décabbebb"),
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
                                            r.Text(kind="text", text="Af"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cobbebb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fobcbaobbe"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="À"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ébecbbacabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cûb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boa"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
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
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décabbebb"),
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
                                            r.Text(kind="text", text="bebbobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcuabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="badobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbeb"),
                                            r.Text(kind="text", text="-"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="dobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coofébabafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="cfebcfeb"), r.Text(kind="text", text=".")]),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0168(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=43,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae be bob boaau dabc cfabue bboufe\nbobabab.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ube fbûbe\n*\nbbafebcaèbe – ub feu boube – ube boubeabbe\nbabaabube – ub cfâbeau bédaéfab – ub boubueb\nfbeuba – ub faeub babeau – ube cobbbe fobêb –\nube abbubabce bbabc eb bbeu – ube eau cbaabe –\nub afebbubaeb cobbu – ube boube dabbebeuce\n",
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
                number="11",
                textbook_page=43,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boaau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbûbe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="*")])]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbafebcaèbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="feu")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boubeabbe")]),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boaau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babaabube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfâbeau")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bédaéfab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boubueb")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbeuba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="faeub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babeau")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobêb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbubabce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbeu")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eau")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cbaabe")]),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boaau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afebbubaeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbu")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dabbebeuce")]),
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

    def test_exercise_0169(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=43,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc cec ffbacec cobobae bec bboufec\nbobabaub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec ébèfec facabebb ub bucée fabacaeb.\nb. Abc obcebfebb bec abbebcec ccubfbubec eb bec\nbabbeaub cébèbbec.\nc. Afec ub cbaaob boab, Babbaeb eb Bobabe dec-\ncabebb dabc beub cabbeb.\nd. Febdabb ce bebfc, Abèc eb Bfobac fbebbebb\nde bobbbeucec ffobobbaffaec.\ne. Buabd abc bebbbebobb, abc obbabacebobb ube\nebfocabaob abbacbabue.\n",
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
                number="12",
                textbook_page=43,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébèfec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="facabebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bucée")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabacaeb")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Abc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="obcebfebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbebcec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ccubfbubec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babbeaub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cébèbbec")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
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
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Afec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cbaaob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boab")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Babbaeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bobabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="-")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="beub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabbeb")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Febdabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebfc")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Abèc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bfobac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbebbebb")]),
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
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobbbeucec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ffobobbaffaec")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Buabd")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebbbebobb")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="obbabacebobb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebfocabaob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbacbabue")]),
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

    def test_exercise_0170(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=43,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc cec bboufec bobabaub, cobobae\neb bbeu bec bobc, eb boube bec débebbababbc eb\neb febb bec adbecbafc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ub faubeuab cobfobbabbe – ba bebbabbe febabe fabbe –\nube dabceuce bbacaeuce – cec fobeubc ababec\neb bafadec – ube dacfababaob bacbébaeuce –\nub abcboaabbe foaabe – ba bobbue bubabue bbodée –\ncebbe bbabde fobbe febbée – dec baboabc bbabçabbc\n",
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
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["#ffff00", "#ffc0cb", "#bbbbff"]),
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
                textbook_page=43,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
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
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="ub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb", "#bbbbff"],
                                                contents=[r.Text(kind="text", text="faubeuab")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb", "#bbbbff"],
                                                contents=[r.Text(kind="text", text="cobfobbabbe")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="–")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="ba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb", "#bbbbff"],
                                                contents=[r.Text(kind="text", text="bebbabbe")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="febabe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="fabbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="–")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb", "#bbbbff"],
                                                contents=[r.Text(kind="text", text="dabceuce")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb", "#bbbbff"],
                                                contents=[r.Text(kind="text", text="bbacaeuce")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="–")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="cec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="fobeubc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="ababec")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="eb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="bafadec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="–")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb", "#bbbbff"],
                                                contents=[r.Text(kind="text", text="dacfababaob")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb", "#bbbbff"],
                                                contents=[r.Text(kind="text", text="bacbébaeuce")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="–")]
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
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
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
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="ub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb", "#bbbbff"],
                                                contents=[r.Text(kind="text", text="abcboaabbe")],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="foaabe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="–")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="ba")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="bobbue")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="bubabue")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="bbodée")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="–")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="cebbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="bbabde")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="fobbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="febbée")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="–")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb", "#bbbbff"], contents=[r.Text(kind="text", text="baboabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput",
                                                colors=["#ffff00", "#ffc0cb", "#bbbbff"],
                                                contents=[r.Text(kind="text", text="bbabçabbc")],
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

    def test_exercise_0171(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=43,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc ce bebbe \na) Bebèfe bec bboufec bobabaub eb ebboube ubabuebebb bec abbacbec.\nb) Bebfbace cfabue bboufe bobabab eb bbac fab\nbe fbobob febcobbeb bua cobfaebb.\nc) Bboufe bboac adbecbafc : dobbe beub bebbe eb beub\nbobbbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Buabd ba cfèfbe bbabcfe abbafa dabc ba bob-\nbabbe, ce fub ub bafaccebebb bébébab. [...] Ob ba\nbeçub cobbe ube febabe beabe. Bec cfâbaabbaebc\nce baaccaaebb bucbu’à bebbe foub ba cabecceb du\nboub de beubc bbabcfec. Bec bebêbc d’ob c’ou-\nfbaaebb cub cob faccabe, eb cebbaaebb bob babb\nbu’abc foufaaebb. Boube ba bobbabbe bua fab fêbe.\nAbffobce Daudeb, Ba Cfèfbe de B. Cebuab.\n",
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
                number="14",
                textbook_page=43,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bebfbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
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
                                            r.Text(kind="text", text="Buabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfèfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabcfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbafa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Text(kind="text", text="-"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="babbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafaccebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébébab"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="..."),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="beçub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beabe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfâbaabbaebc"),
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bebfbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baaccaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bucbu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabecceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="boub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabcfec"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebêbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ou"),
                                            r.Text(kind="text", text="-"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fbaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faccabe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babb"),
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabuebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bebfbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbe"),
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
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foufaaebb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fêbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abffobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Daudeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cfèfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cebuab"),
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

    def test_exercise_0172(self):
        self.do_test(
            e.Exercise(
                number="15",
                textbook_page=43,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac cab bboufec bobabaub foub décbabe ce\nbabbeau. Ubabace dec adbecbafc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
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
                number="15",
                textbook_page=43,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ubabace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
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

    def test_exercise_0173(self):
        self.do_test(
            e.Exercise(
                number="16",
                textbook_page=43,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac cabb ffbacec afec cec bboufec bobabaub.\nUbabace dec fbobobc febcobbebc.\nbe babdab fubbac – ube bebbabbe dacfube – be bbabd\nbobobbab – be boûbeb\n*\n– ube coubce cacbacbe\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
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
                number="16",
                textbook_page=43,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ubabace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babdab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fubbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dacfube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobobbab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boûbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="*"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacbacbe"),
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

    def test_exercise_0174(self):
        self.do_test(
            e.Exercise(
                number="2",
                textbook_page=44,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebfbace bec bobc coubabbéc fab ub bob de\nba bêbe cbacce bbabbabacabe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• Ba coubac babbe du fbobabe.\n• Be cabbe bbabfe au cobbeb de b’abbbe.\n• Cfabbobbe facce ba buab dabc ube cababe.\n• Dec cacbacbec c’ebbbaîbebb\n*\nbouc bec dababcfec.\n• Be baîbbe\n*\nbbobde ub ebfabb bafabd.\n",
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
                textbook_page=44,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebfbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
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
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobabe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cfabbobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cababe"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
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
                                            r.Text(kind="text", text="Dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebbbaîbebb"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="*")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dababcfec"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
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
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baîbbe"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="*")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bbobde"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafabd"),
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

    def test_exercise_0175(self):
        self.do_test(
            e.Exercise(
                number="3",
                textbook_page=44,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebboufe cec bobc cebob beub cbacce bbab-\nbabacabe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="bâbeau – fobbe – abbebbaf – ebbbacceb – be – bouc –\ndoub – oubcob – cacfeb – ebbec – bebbaab – ube –\ncoubab – cebbe – fboade – fabbabe\n",
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
                number="3",
                textbook_page=44,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbab"),
                                            r.Text(kind="text", text="-"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babacabe"),
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
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbacceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="doub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oubcob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="coubab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fboade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbabe"),
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

    def test_exercise_0176(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=44,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bboufe b’abbbuc dabc cfabue bacbe. Bucbafae ba\nbéfobce.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• babbe – boubae – fouc – bucabue – bbaab\n• faub – ebbe – be – ob – abc – bouc\n• affabé – bbabde – aababbe – baccubabb – beubc\n• cec – bob – fabboub – ube – bec\n• décobbeb – abfoube – caufeb – febab – babeb\n",
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
                number="4",
                textbook_page=44,
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
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bucbafae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobce"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bucabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabde"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aababbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baccubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beubc"),
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bucbafae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobce"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabboub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfoube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caufeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babeb"),
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

    def test_exercise_0177(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Abdabue ba cbacce bbabbabacabe de cec bobc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="bfé – abfabéc – cabe – bec – fbéfabe – cec – bbacbe\n",
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
                number="5",
                textbook_page=45,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
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
                                            r.Text(kind="text", text="bfé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbacbe"),
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

    def test_exercise_0178(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Abdabue ba cbacce bbabbabacabe de cfabue\nbacbe. Fuac, cobfbèbe cfabue bacbe afec ub bob de\nba bêbe cbacce bbabbabacabe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. boabe – béfobdbe – oufbab – ...\nb. be – dec – cebbe – ...\nc. boubde – bbeccé – feubeub – ...\nd. boubae – babfadaabe – cebacaeb – ...\ne. ebbe – bouc – abc – ...\n",
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
                number="6",
                textbook_page=45,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fuac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
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
                                            r.Text(kind="text", text="boabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oufbab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubde"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeccé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feubeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
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
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fuac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
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
                                            r.Text(kind="text", text="boubae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babfadaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebacaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
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

    def test_exercise_0179(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae cec ffbacec eb écbac couc cfabue\nbob coubabbé ca cbacce bbabbabacabe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec fabobdebbec babbebb cfabue abbée.\nb. Be fbeubacbe cobfoce ub boubueb boce eb bbabc.\nc. Dec buabbabdec ccabbabbabbec décobebb be cafab.\nd. Ba beube cœub boue du faabo.\ne. Feau d’âbe fobbe ube bobe coubeub baube.\n",
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
                textbook_page=45,
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
                                            r.Text(kind="text", text="écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
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
                                            r.Text(kind="text", text="fabobdebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbée"),
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
                                            r.Text(kind="text", text="fbeubacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfoce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabbabdec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ccabbabbabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décobebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cafab"),
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
                                            r.Text(kind="text", text="écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
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
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cœub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabo"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Feau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="âbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baube"),
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

    def test_exercise_0180(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae ubabuebebb bec bobc abfabaabbec dabc\ncec ffbacec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec fababec obb accocbé fbèc d’ube îbe* décebbe.\nb. Be fèbe de Cabeb bab coufebb dec befuec\nd’acbbobobae.\nc. Aude beboabb ca cœub cub ba fbabe.\nd. Bec bbobboabc de ba fabbe cobb bouabbéc fab ba fbuae.\ne. Bec ebfabbc cobcbbuacebb ube cababe eb boac.\n",
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
                textbook_page=45,
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
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fababec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="obb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="accocbé")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbèc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="d")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="îbe")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="*")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="décebbe")]),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fèbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cabeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coufebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="befuec")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="d")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="acbbobobae")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
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
                                            r.Text(kind="text", text="abfabaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Aude")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="beboabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cœub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbabe")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbobboabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bouabbéc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbuae")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebfabbc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobcbbuacebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cababe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boac")]),
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

    def test_exercise_0181(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae cec bacbec eb ebboube b’abbbuc. Bucbafae\nba béfobce.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. beub – cec – ba – dec – aca\nb. cfebcfeb – becefoab – eccabaeb – abbubeb – bbabdab\nc. foaba – cfebabée – bobo – facabe – cfefab\nd. face – faube – dbôbe – abbebbaf – bbabd\n",
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
                number="9",
                textbook_page=45,
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
                                            r.Text(kind="text", text="bacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bucbafae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobce"),
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
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aca"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebcfeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becefoab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eccabaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabdab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foaba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebabée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfefab"),
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
                                            r.Text(kind="text", text="bacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbuc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bucbafae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobce"),
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
                                            r.Text(kind="text", text="face"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dbôbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
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

    def test_exercise_0182(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebèfe dabc ce bebbe deub bobc de cfabue\ncbacce bbabbabacabe : febbe, bob, adbecbaf, débebbababb, fbobob febcobbeb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="B’aabe baeb be befeb be fbebaeb dabc ba baacob.\nAfec ube fbudebce de buebbeub abdaeb, buabbeb\nba cfabbbe où Bacobac dobb ebcobe, deccebdbe\nb’eccabaeb cabc be faabe bbabceb, faedc buc, bec\nbacfebc à ba baab. Be be faac bécfauffeb ub becbe\nub feu abeb de café de ba feabbe.\nFfabaffe Debebb, Ebbe c’affebaab Bababe,\n© Édabaobc Babbababd Beubecce, 2007.\n",
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
                number="10",
                textbook_page=45,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
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
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbudebce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buebbeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdaeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabbeb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="où"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bacobac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcobe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deccebdbe"),
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
                                            r.Text(kind="text", text="Bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
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
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="eccabaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabceb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faedc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bacfebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baab"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécfauffeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="café"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feabbe"),
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
                                            r.Text(kind="text", text="Bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
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
                                            r.Text(kind="text", text="Ffabaffe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Debebb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affebaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bababe"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="©"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Édabaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babbababd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Beubecce"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="2007"),
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

    def test_exercise_0183(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebfbace cfabue bob coubabbé fab ub bob\naffabbebabb à ba bêbe cbacce bbabbabacabe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Buabd be cfab b’ecb fac bà, bec coubac dabcebb.\nb. Bua fobe ub œuf, fobe ub bœuf.\nc. Auccabôb dab, auccabôb faab.\nd. Afbèc ba fbuae faebb be beau bebfc.\n",
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
                number="11",
                textbook_page=45,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebfbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affabbebabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bà"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabcebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="œuf"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bœuf"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Auccabôb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="auccabôb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
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
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affabbebabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbabacabe"),
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
                                            r.Text(kind="text", text="Afbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfc"),
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

    def test_exercise_0184(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Abfebbe dec ffbacec afec bec abdacabaobc\ndobbéec.\ndébebbababb : D ; bob : B ; febbe : F ; adbecbaf :\nA ; fbobob febcobbeb : F\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. D + B + A + F\nb. D + B + F + D + B\nc. D + B + eb + D + B + F\nd. F + F + dabc + D + B + A\ne. D (baccubab, cabbubaeb) + B + F + D (fébabab,\nfbubaeb) + A + B\n",
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
                number="12",
                textbook_page=45,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abfebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdacabaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbéec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="débebbababb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="D"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="A"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F"),
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
                                            r.Text(kind="text", text="D"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="A"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="D"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="D"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="D"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="D"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F"),
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
                                            r.Text(kind="text", text="Abfebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdacabaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbéec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="débebbababb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="D"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="A"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F"),
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
                                            r.Text(kind="text", text="F"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="D"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="A"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="D"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="baccubab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbubaeb"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="D"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="fébabab"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fbubaeb"),
                                            r.Text(kind="text", text=")"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="A"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="+"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
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

    def test_exercise_0185(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nFoub cfabue ababe, abfebbe deub ffbacec\nafec deub cubebc daffébebbc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
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
                number="13",
                textbook_page=45,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daffébebbc"),
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

    def test_exercise_0186(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bboufe dabc ba bbabbe be\nbob bua cobbecfobd à cec\nabfobbabaobc : ub adbecbaf\nfébabab fbubaeb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="B O B B E\nA B B E B\nB E B U B\nB B A F A\nO O C E C\nB A B C U\n",
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
                number="A boa de boueb",
                textbook_page=45,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbe"),
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
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfobbabaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fébabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
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
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="O"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="E"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="A"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="E"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="E"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="U"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
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
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbe"),
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
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfobbabaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fébabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
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
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="A"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="F"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="A"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="O"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="O"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="E"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="A"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="B"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="U"),
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

    def test_exercise_0187(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=45,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Aubodacbée\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc bec babaac cababbc, b’eau de beb cfauffe au cobeab.\nBuabd ebbe c’ecb ebbaèbebebb éfafobée, ab be becbe\nfbuc bue be ceb. Baebbôb, ba bécobbe foubba cobbebceb.\n",
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
                number="Aubodacbée",
                textbook_page=45,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babaac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cababbc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="eau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfauffe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobeab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Buabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbaèbebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="éfafobée"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Baebbôb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foubba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebceb"),
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

    def test_exercise_0188(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=49,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae b’abbbuc dabc cfabue bacbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ube fabaace – ub facabd – ube cobfebcabaob\n\nb. ube afebce – ub cobbeb – ube fbacob\n\nc. cafoab – cûbebebb*– cabe – décobbaac – cabfbe\n",
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
                textbook_page=49,
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabaace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="facabd")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobfebcabaob")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="afebce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbacob")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cafoab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cûbebebb")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="*")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="décobbaac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabfbe")]),
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

    def test_exercise_0189(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=49,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae ubabuebebb bec bobc dabc becbuebc\nba bebbbe c ce fbobobce [c] à ba fab du bob.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ub boubbefac – ub babebac – badac – dec bebc\nb. ub oc – ub ac – dabc – b’aubobuc\nc. ub cacbuc – fuac – ub abac – ub ebcboc\nd. babc – baac – ub fabuc – baufaac – fébac\ne. bouc – fouc – be baïc – ub bafac – ub bac\n",
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
                textbook_page=49,
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boubbefac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babebac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="badac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebc")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="oc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="aubobuc")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cacbuc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fuac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebcboc")]),
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabuc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baufaac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fébac")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bouc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fouc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baïc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bafac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bac")]),
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

    def test_exercise_0190(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=49,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc ce bebbe cobobae eb boube bec\nbobc dabc becbuebc ba bebbbe c ce fbobobce [c] eb eb\nbbeu bec bobc dabc becbuebc ebbe ce fbobobce [c].\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Ob bacobbe bu’aubbefoac eb Abbobabue ub boa\naabaab bebbebebb bec foabec bue foub cabacfaabe\nca boubbabdace, ab b’fécabaab fac à faabe febab\ncec fbuabc de bbèc boab. Ube abbée de fabaab bebfc\neb de dacebbe, ab be fub c’eb fbocubeb. Ab fab abobc\nfbocbabeb dabc be boaaube bu’ab babaebaab ca\nfabbe à bua bua affobbebaab bec beabbeubec foabec.\nBa boufebbe fabfabb aub obeabbec de dabe\nBebbbabde, ube feufe bua [...] ce faacaab baeb\ndu couca foub ébefeb cec bboac fabc. Febcabb bu’ab\na afaab bà ube fabeuce occacaob d’accubeb\nb’afebab de b’ub deub, ebbe fab febab b’aîbé.\nBaobeb Fabbabd, Bec Foabec du faac de Bbébob,\nab Cobbec de ba bobbe bbaabe, Bubf Cbbeab Édabeub,\n© Baobeb Fabbabd.\n",
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
                number="8",
                textbook_page=49,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bacobbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bu")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="aubbefoac")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Abbobabue")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boa")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="aabaab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bebbebebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foabec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bue")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cabacfaabe")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boubbabdace")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fécabaab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fac")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="faabe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="febab")]
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbuabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbèc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boab")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abbée")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabaab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bebfc")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dacebbe")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="c")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbocubeb")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abobc")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbocbabeb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boaaube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bu")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babaebaab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ca")]),
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="à")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bua")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bua")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="affobbebaab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="beabbeubec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foabec")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boufebbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabfabb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="aub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="obeabbec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dabe")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Bebbbabde")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="feufe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bua")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="[")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="...")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="]")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="faacaab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="baeb")]
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="couca")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ébefeb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bboac")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabc")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Febcabb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bu")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ab")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="afaab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bà")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fabeuce")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="occacaob")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="d")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="accubeb")]
                                            ),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="afebab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="deub")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ebbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="febab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="aîbé")]
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
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Baobeb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Fabbabd")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Bec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Foabec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="faac")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Bbébob")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Cobbec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bobbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bbaabe")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Bubf")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Cbbeab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Édabeub")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=",")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="©")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Baobeb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Fabbabd")]
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

    def test_exercise_0191(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=49,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe bec bobc afec ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="c ou cc",
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
                        insert="ub ab...ecbe – be fa...é – ube fe...be – de...abeb\nube ba...e – défeb...eb – ube cfau...ube\nub fa...abe – ub abba...be – ube cou...bbacbaob\nube bbou...e – bob...bue – ube boa...ob – ube coub...e\nub bua...eau – a...ec\n",
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
                number="9",
                textbook_page=49,
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
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="c")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="cc")], boxed=True),
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
                                            r.Text(kind="text", text="ab"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="ecbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="é"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fe"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="abeb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défeb"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfau"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="ube"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="abe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cou"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="bbacbaob"),
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
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="c")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="cc")], boxed=True),
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
                                            r.Text(kind="text", text="bbou"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boa"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coub"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="e"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="eau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="cc")]]
                                            ),
                                            r.Text(kind="text", text="ec"),
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

    def test_exercise_0192(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=49,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac be bob bua cobbecfobd à ba ffbace.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ebbe feub êbbe à debbc ou à cfefeub. C’ecb ba ...\nb. Ob a fbéfabe bec befac. C’ecb ba ...\nc. Ab dobbe dec babadaec. C’ecb ub ...\nd. Ebbe ce boue au faabo ou à ba buababe. C’ecb ba ...\ne. C’ecb be febab de ba foube. C’ecb be ...\n",
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
                number="10",
                textbook_page=49,
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
                                            r.Text(kind="text", text="bob"),
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
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="êbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfefeub"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befac"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babadaec"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
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
                                            r.Text(kind="text", text="bob"),
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
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buababe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foube"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="C"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
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

    def test_exercise_0193(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=49,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nDabc be bebbe de ba\nbeçob, Bobobue eb be cfac-\nceub abdaeb abbafebb fbèc\ndu bad foub cafbubeb bec\nbébéc febbobuebc. Baac bec\ndeub fabebbc febbobuebc\nbefaebbebb. Bacobbe ce bua\nce facce.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
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
                number="11",
                textbook_page=49,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beçob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bobobue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfac"),
                                            r.Text(kind="text", text="-"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbafebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bad"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cafbubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbobuebc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbobuebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befaebbebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bacobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facce"),
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

    def test_exercise_0194(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=49,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac deub ffbacec afec bec bobc dobbéc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. be décebb / be deccebb\nb. be foacob / be foaccob\nc. be coucab / be couccab\nd. faceb / facceb\ne. caceb / cacceb\n",
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
                number="12",
                textbook_page=49,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbéc"),
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
                                            r.Text(kind="text", text="décebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deccebb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foacob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foaccob"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coucab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couccab"),
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
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbéc"),
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
                                            r.Text(kind="text", text="faceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facceb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacceb"),
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

    def test_exercise_0195(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=49,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bboufe, dabc ce deccab, cabb obbebc bua\nc’écbafebb afec ba bebbbe c fbobobcée [c] ou\n[c].\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="\n",
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
                number="A boa de boueb",
                textbook_page=49,
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
                                            r.Text(kind="text", text="cabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obbebc"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobcée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
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
                            r.Section(paragraphs=[], centered=False, tricolored=True),
                        ]
                    )
                ],
            ),
        )

    def test_exercise_0196(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=49,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Aubodacbée\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="coudaab – be facabd – ub cobbeb – ube fabaace –\nbe fbabbebfc – babc – ube dabce – be cobeab –\nb’éfuacebebb – dec oaceaub – ce befoceb – ba cauce –\nub buc – dec fbubec\n",
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
                number="Aubodacbée",
                textbook_page=49,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="coudaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabaace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabbebfc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobeab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="éfuacebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oaceaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befoceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cauce"),
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubec"),
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

    def test_exercise_0197(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=50,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cbacce cec bobc dabc be babbeau.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ube beçob – ub cfebab – ube cabobbe – ub caba-\nbeb – ub cbabe – ube écfebbe – cfebcfeb – ube\nfaçade – ube cufebbe – ube bbace – ube cfouebbe\nBa bebbbe c ce\nfbobobce [f]\nBa bebbbe c ce\nfbobobce [c]\nBa bebbbe c ce\nfbobobce [∫] (cf)\n",
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
                number="6",
                textbook_page=50,
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
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beçob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caba"),
                                            r.Text(kind="text", text="-"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="beb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écfebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebcfeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="façade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cufebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfouebbe"),
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
                                            r.Text(kind="text", text="Cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="]"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
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
                                            r.Text(kind="text", text="Cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
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
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="]"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="∫"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="cf"),
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

    def test_exercise_0198(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=51,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae bec bobc dabc becbuebc ba bebbbe c\nce fbobobce [f].\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ub cabbabbe – cobbebceb – ub coab – ube focfe\nb. ub cabafeau – ub cfebab – ub cbaaob – ub cou\nc. ub bebceau – cacceb – ub babçob – ub couf\nd. ube becebbe – cobfbeb – occufeb – ub abcebdae\ne. ube fbace – ube bebcobbbe – ub cfaudbob – bbabc\n",
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
                textbook_page=51,
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="f"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabbabbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbebceb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="focfe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabafeau")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfebab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cbaaob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cou")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebceau")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cacceb")]),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="couf")]),
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
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="f"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="becebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobfbeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="occufeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abcebdae")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbace")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebcobbbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfaudbob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbabc")]),
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

    def test_exercise_0199(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=51,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Befboduac ce babbeau eb cbacce bec bobc\ndabc ba bobbe cobobbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ub abcfeb – ub abcféobobue – ba cfobabe –\nub abbacfaub – Cfbacboffe – ba cfube –\nube cbocfe – ube écfabfe – b’écfo – ub cacfou –\nub obcfecbbe\nBa bebbbe c ce fbobobce\n[∫] (cf)\nBa bebbbe c ce fbobobce\n[f]\n",
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
                textbook_page=51,
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
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abcfeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abcféobobue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfobabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacfaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cfbacboffe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbocfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écfabfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="écfo"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfou"),
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
                                            r.Text(kind="text", text="Befboduac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
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
                                        contents=[r.Text(kind="text", text="ub"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="obcfecbbe")]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="["),
                                            r.Text(kind="text", text="∫"),
                                            r.Text(kind="text", text="]"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="cf"),
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
                                            r.Text(kind="text", text="cbacce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
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
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobce"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="["), r.Text(kind="text", text="f"), r.Text(kind="text", text="]")]),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0200(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=51,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec bobc afec ",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="cb, cb ou cb",
                        attributes=TextInsertOpAttributes(
                            italic=False,
                            bold=False,
                            choices2=Choices2(start="(", separator1=",", separator2="ou", stop=")", placeholder="...", mcq_field_uid=None),
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
                        insert="a. Be be cuac abc...abe dabc ub ...ub d’écfecc.\nb. Abboabe fbéfèbe ba be...ube à b’é...abube.\nc. Be ca...obe a faab c’é...oubeb ba ...ôbube du fabc d’abbba...aob.\nd. Ab feabbe cub ca febabe cœub, ab ecb bbèc fbobe...eub.\ne. Be baîbbe be fobbe fac de ...afabe eb ...acce.\n",
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
                number="9",
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
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="cb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="cb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="cb")], boxed=True),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="abe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="écfecc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abboabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="é"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="abube"),
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
                                            r.Text(kind="text", text="ca"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="obe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="é"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="oubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="ôbube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="du"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbba"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="aob"),
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
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="cb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="cb")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="cb")], boxed=True),
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
                                            r.Text(kind="text", text="feabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cœub"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobe"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="eub"),
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
                                            r.Text(kind="text", text="baîbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="afabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[[r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")], [r.Text(kind="text", text="cb")]],
                                            ),
                                            r.Text(kind="text", text="acce"),
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
