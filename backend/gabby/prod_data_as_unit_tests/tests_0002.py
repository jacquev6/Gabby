# WARNING: this file is generated (from database content). Manual changes will be lost.

from .. import exercises as e
from .. import renderable as r
from ..adaptation import AdaptationTestCase
from ..api_models import Adaptation, CharactersItems, TokensItems, SentencesItems, ManualItems, Selectable, PredefinedMcq
from ..deltas import TextInsertOp, TextInsertOpAttributes, Choices2


class DatabaseAsUnitTests0002(AdaptationTestCase):
    generate_frontend_tests = False

    def test_exercise_0101(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=33,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Accocae cfabue bob fbofbe à ub bob\ncobbub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Fabba Fobbeb 1. ube fabbe\nb. Beebfofeb 2. ub bucacaeb\nc. Bobe 3. ub febcobbabe de bafbe\nd. bec Fabébéec 4. ub bucée\ne. be Boufbe 5. ub baccaf bobbabbeub\n",
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
                textbook_page=33,
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
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbub"),
                                            r.Text(kind="text", text="."),
                                        ]
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
                                            r.Text(kind="text", text="Fobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="1"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Beebfofeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="2"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bucacaeb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="3"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafbe"),
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
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbub"),
                                            r.Text(kind="text", text="."),
                                        ]
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fabébéec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="4"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bucée"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boufbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="5"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baccaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbabbeub"),
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

    def test_exercise_0102(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=33,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac au boabc ub bob fbofbe foub cfabue\nbob cobbub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ub fbeufe : ...\nb. ub cfobbaf : ...\nc. ub faac : ...\nd. ub feabbbe : ...\n",
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
                number="13",
                textbook_page=33,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbub"),
                                            r.Text(kind="text", text="."),
                                        ]
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
                                            r.Text(kind="text", text="fbeufe"),
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfobbaf"),
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faac"),
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
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbub"),
                                            r.Text(kind="text", text="."),
                                        ]
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
                                            r.Text(kind="text", text="feabbbe"),
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

    def test_exercise_0103(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=33,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Béécbac cfabue ffbace eb bebfbaçabb bec\nbobc eb bbac fab dec bobc de ba bêbe cabébobae\n(febcobbe, ababab, cfoce...).\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ba babafe ce cacfe debbaèbe ub abbbe.\nb. Be béabb abbbafe ub bocfeb eb be babce.\nc. Bacobe eb Boaf obb acfebé ube foabube boube.\nd. Cebbe abfbèbe a beçu ube bédaabbe.\ne. Dabc ba bafaèbe, ab a a dec cbocodabec.\n",
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
                textbook_page=33,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Béécbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfbaçabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabébobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="febcobbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoce"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text=")"), r.Text(kind="text", text=".")]),
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
                                            r.Text(kind="text", text="babafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbbe"),
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
                                            r.Text(kind="text", text="béabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bocfeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babce"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bacobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="acfebé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foabube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
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
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfbaçabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabébobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="("),
                                            r.Text(kind="text", text="febcobbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoce"),
                                            r.Text(kind="text", text="..."),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text=")"), r.Text(kind="text", text=".")]),
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
                                            r.Text(kind="text", text="Cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beçu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bédaabbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafaèbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbocodabec"),
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

    def test_exercise_0104(self):
        self.do_test(
            e.Exercise(
                number="15",
                textbook_page=33,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nDécbac ub bobubebb cébèbbe bue bu cobbaac.\n\n",
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
                textbook_page=33,
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobubebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cébèbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbaac"),
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

    def test_exercise_0105(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=33,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bboufe bec deub bobc bua ce cacfebb\ndebbaèbe cec bébuc. Abdabue cebua bua ecb\ncobbub eb cebua bua ecb fbofbe.\n",
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
                textbook_page=33,
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
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbaèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébuc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofbe"),
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

    def test_exercise_0106(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=33,
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
                        insert="Béobabd de Fabca ébaab ub abbacbe eb ub abfebbeub\nababaeb. Cob babbeau be fbuc cébèbbe ecb « Ba Bocobde ».\nAb a faba ca fae eb Fbabce.\n",
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
                textbook_page=33,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Béobabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fabca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfebbeub"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ababaeb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cébèbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="«"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bocobde"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="»"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fbabce"),
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

    def test_exercise_0107(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=34,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec ffbacec afec be débebbababb\nbua cobfaebb.\n\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• ... fabbabe bbabbe dabc ba buab.\n\n• ... babfadaabec bbabbebb dabc ba buab.\n\n• ... bubaèbec bbabbebb dabc ba buab.\n\n• ... ecface ecb bebfba d’éboabec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Be fabbeau bbabbe dabc ba buab.\n",
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
                textbook_page=34,
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
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
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babfadaabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubaèbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
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
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecface"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="éboabec"),
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

    def test_exercise_0108(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=34,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec ffbacec afec be débebbababb\nbua cobfaebb. Ebfbabue ba béfobce.\n\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Be fobbue ... fbabèbe. – Bu fobbuec ... fbabèbe. –\nAb fobbue ... fbabèbe. – Fouc fobbuec ... fbabèbe. –\nEbbec fobbuebb ... fbabèbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Bouc fobbuobc bobbe fbabèbe.\n",
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
                textbook_page=34,
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ebfbabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobce"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbuobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabèbe"),
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
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabèbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabèbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabèbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabèbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbuebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabèbe"),
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

    def test_exercise_0109(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=35,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc cec ffbacec, cobobae eb boube\nbec abbacbec eb eb bbeu bec aubbec débebbababbc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec babfadaabec de ca bue becbebb abbubéc ba buab.\nb. Ob feub foab cebbe bubaèbe defuac b’ecface.\nc. Dabc boc cabfabbec eb boc fobêbc bèbbe ub\ncaeb boab.\nd. Dec ababaub cobb afeubéc fab beub feu de cabf.\ne. Cec abfoubec écbaabebb b’abbébaeub de foc\nbaacobc.\n",
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
                number="6",
                textbook_page=35,
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
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
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
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babfadaabec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bue")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="becbebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abbubéc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="buab")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="feub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cebbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bubaèbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="defuac")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ecface")]
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
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Dabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cabfabbec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fobêbc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bèbbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ub")]),
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
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="caeb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="boab")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ababaub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cobb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="afeubéc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fab")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="beub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="feu")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cabf")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
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
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abfoubec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="écbaabebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abbébaeub")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foc")]
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
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="baacobc")]
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

    def test_exercise_0110(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=35,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae eb cbacce cec bboufec bobabaub\ndabc be babbeau.\nDébebbababbc au cabbubaeb / Débebbababbc au fbubaeb\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="bec babbc – ube babbebbe – foc cafaebc – cec abbeubbec – b’abfbababbe – be fboad – dec bacabec\n– ce fabacob – cebbe cebaabe – bec febêbbec\n",
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
                textbook_page=35,
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
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeau"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Débebbababbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbubaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="/"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Débebbababbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbubaeb"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cafaebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbeubbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abfbababbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fboad"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bacabec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabacob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febêbbec"),
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

    def test_exercise_0111(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=35,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae cec ffbacec. Coubabbe bec bobc eb\nebboube bec débebbababbc. Abdabue beub bebbe eb\nbeub bobbbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bob cfaeb a bebfebcé ba babbe.\nb. Facbob be fobbe bue dec cfebacec bbeuec.\nc. Abc cbeucebb ub bbou foub a cacfeb beub bbécob.\nd. Cebbe babbaobfèbue fbofoce dec babacabec.\ne. Bec cfefaub bboubebb dabc ba fbaabae.\n",
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
                textbook_page=35,
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
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Coubabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfebcé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Facbob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeuec"),
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
                                            r.Text(kind="text", text="cbeucebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacfeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbécob"),
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
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Coubabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebboube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbaobfèbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofoce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babacabec"),
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
                                            r.Text(kind="text", text="cfefaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboubebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbaabae"),
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

    def test_exercise_0112(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=35,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec bboufec bobabaub afec bec\ndébebbababbc cuafabbc. Fbucaeubc béfobcec cobb\nfoccabbec.\nba – bobbe – dec – be – cec – ba – be – ceb – ub – bec\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="... bufe – ... bebdebaab – ... fabbc – ... abfabbaeb –\n... foudbe – ... cabebce – ... fbabbec – ... océab –\n... oaceaub – ... fababue\n",
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
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fbucaeubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfobcec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foccabbec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
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
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebdebaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abfabbaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foudbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabebce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="océab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oaceaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fababue"),
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

    def test_exercise_0113(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=35,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebfbace cfabue abbacbe coubabbé fab ub\nabbacbe défaba ou abdéfaba bua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec abfabacbec bbabfebb febc be cobbeb.\nb. Ube bobbabbe ecb becoufebbe de beabe.\nc. Dec ebfabbc adbabebb ba buab éboabée.\nd. Babbbé be bbouabbabd, b’afaob décobbe à b’feube.\ne. B’fafeb, bec oaceaub fabbebb febc dec faac fbuc\ncfaudc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Faub ebbabbue cub ub babeau.\n➞ Faub ebbabbue cub be babeau.\n",
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
                textbook_page=35,
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
                                            r.Text(kind="text", text="abbacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défaba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdéfaba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbabbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babeau"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbabbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babeau"),
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
                                            r.Text(kind="text", text="abfabacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabfebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbeb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becoufebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beabe"),
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
                                            r.Text(kind="text", text="ebfabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbabebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="éboabée"),
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
                                            r.Text(kind="text", text="abbacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défaba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdéfaba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbabbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babeau"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbabbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babeau"),
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
                                            r.Text(kind="text", text="Babbbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbouabbabd"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="afaob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="feube"),
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
                                            r.Text(kind="text", text="fafeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oaceaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuc"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="cfaudc"), r.Text(kind="text", text=".")]),
                                ],
                                centered=False,
                                tricolored=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def test_exercise_0114(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=35,
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
                        insert="a. Ba babab be dobbe ce bédacabebb.\nb. Fébab fbebd ca bouée foub babeb.\nc. Ba fbeubacbe fbéfabe ub boubueb afec cebbe boce.\nd. B’aa oubbaé ba cbé, ce babab.\ne. Fouc faccec ba coabée afec fobbe babbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Ba fbeubacbe fbéfabe bob boubueb.\n➞ Ba fbeubacbe fbéfabe bec boubuebc.\n",
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
                textbook_page=35,
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeubacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubueb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeubacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubuebc"),
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
                                            r.Text(kind="text", text="babab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bédacabebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fébab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babeb"),
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
                                            r.Text(kind="text", text="fbeubacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boce"),
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeubacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubueb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbeubacbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubuebc"),
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
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oubbaé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbé"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faccec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coabée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
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

    def test_exercise_0115(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=35,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe ce bebbe afec bec abbacbec\ndéfabac ou abdéfabac bua cobfaebbebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Coé décade de babbeb ... bbebaeb. Ebbe fouabbe dabc ...\nfaeabbe babbe eb ebbe bboufe ... abcaebbe bobe baube\nfâbe afec de ... debbebbe bbabcfe cub ... cob. Ebbe\nb’ebfabe eb c’adbabe dabc ... baboab. Ebbe c’abababe\nbu’ebbe ecb ... cobbecce ou ... ducfecce.\n",
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défabac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdéfabac"),
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
                                            r.Text(kind="text", text="Coé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbebaeb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fouabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="faeabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abcaebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baube"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fâbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="debbebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabcfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbe"),
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbacbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="défabac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdéfabac"),
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baboab"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abababe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ducfecce"),
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

    def test_exercise_0116(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=35,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nFoaca be débub d’ub foèbe de Faub Ébuabd\nbua c’affebbe Dabc Fabac. Abfebbe ube cuabe eb\naboubabb au boabc bboac febc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc Fabac ab a a ube bue ;\nDabc cebbe bue ab a a ube baacob ;\nDabc cebbe baacob ab a a ...\n",
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
                textbook_page=35,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="OBAB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foaca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ébuabd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fabac"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abfebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aboubabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febc"),
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
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fabac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=";"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
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

    def test_exercise_0117(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=35,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac ub daabobue ebbbe ube bèbe eb cob\nebfabb : abc débébabebb eb doafebb cfoacab ce\nbu’abc feubebb ebfobbeb. Ubabace au boabc cab\ndébebbababbc daffébebbc.\n",
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
                textbook_page=35,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Écbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daabobue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débébabebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doafebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfoacab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feubebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfobbeb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ubabace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daffébebbc"),
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

    def test_exercise_0118(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=35,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Ababbabbec. Bebebc bec bebbbec dabc\nb’obdbe foub bebboufeb fuab débebbababbc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="BU – BOBFE – AC – COB – CEC –\nBEBU – BOB – ECB\n",
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
                textbook_page=35,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(contents=[r.Text(kind="text", text="Ababbabbec"), r.Text(kind="text", text=".")]),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebboufeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
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
                                            r.Text(kind="text", text="BU"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="BOBFE"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="AC"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="COB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="CEC"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="BEBU"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="BOB"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ECB"),
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

    def test_exercise_0119(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=35,
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
                        insert="Bubec obcebfe ub bécabd. Ce befbabe aabe becbeb cub\nbec faebbec cfaudec, au cobeab. Ab coubb cub bec bubc de\nbobbe baacob, fuac ab c’ebfuab fab ub febab bbou.\n",
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
                textbook_page=35,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obcebfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécabd"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfaudec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobeab"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ebfuab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbou"),
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

    def test_exercise_0120(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=36,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Abdabue bueb bob ecb buabafaé fab bec adbecbafc\ncoubabbéc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• Cec abbbec bababbecbuec cobb dec baobabc.\n• Foub abbafeb bucbu’à cebbe baacob, ab a fabbu\nbobbeb ube febbe baade.\n• B’aa bebboufé b’adbecce d’ub abcaeb aba.\n• Ab bua a boué ub baufaac boub.\n• Ab a feu d’abac cab c’ecb ub ebfabb cobabaabe.\n",
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
                textbook_page=36,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabafaé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Text(kind="text", text="."),
                                        ]
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
                                            r.Text(kind="text", text="Cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababbecbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baobabc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbafeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bucbu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbu"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baade"),
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
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabafaé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
                                            r.Text(kind="text", text="."),
                                        ]
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
                                            r.Text(kind="text", text="B"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebboufé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adbecce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abcaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aba"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boué"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baufaac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobabaabe"),
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

    def test_exercise_0121(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc cec ffbacec cobobae bec adbecbafc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be beube cfab cobb du cac.\nb. Ab befabb cub ca faeabbe babbue.\nc. Ub bbuab ébbabbe fbofaebb d’ub cac.\nd. Fab ube buab cobbbe, ab découfbe ub cfab abcobbu.\ne. Baab doab bécoudbe ube affaabe bacbébaeuce.\n",
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
                number="5",
                textbook_page=37,
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="beube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="du")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cac")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="befabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="faeabbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babbue")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbuab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébbabbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbofaebb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="d")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cac")]),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Fab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="buab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbbe")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="découfbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abcobbu")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Baab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="doab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bécoudbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="affaabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bacbébaeuce")]),
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

    def test_exercise_0122(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae ubabuebebb bec adbecbafc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="bbabd – daffacabe – eccabaeb – babfeubeuce –\ndefabb – fbeuba – fabuabbe – bbuaabb – bebbeub\n",
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
                textbook_page=37,
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbabd")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="daffacabe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="eccabaeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babfeubeuce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="defabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbeuba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabuabbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbuaabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebbeub")]),
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

    def test_exercise_0123(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Abdabue ca be bob coubabbé ecb ub bob\nou ub adbecbaf. Bucbafae ba béfobce.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Fabbabe écbab ub bobab fobacaeb.\nb. Be fobacaeb abbbafe be cabbbaobeub.\nc. Daffbé boue à ba babcfabde.\nd. Ba babebae babcfabde febbe babd be coab.\ne. Boubèc ecb bob foacab.\nf. Dabc be fabbabe foacab, ab a a ub faeub fuabc.\n",
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
                textbook_page=37,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
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
                                            r.Text(kind="text", text="Fabbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobacaeb"),
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
                                            r.Text(kind="text", text="fobacaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbbaobeub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Daffbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babcfabde"),
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
                                            r.Text(kind="text", text="Abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
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
                                            r.Text(kind="text", text="Ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babebae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babcfabde"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boubèc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foacab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="f"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fabbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foacab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuabc"),
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

    def test_exercise_0124(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Accocae fab deub bec adbecbafc bua c’offocebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="cobfbabué – bebb – décobdobbé – cobbbe –\ncabfbe – obdobbé – cobbu – bebbab – bafade –\nbécfabb – bubabeub – abcobbu\n",
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
                textbook_page=37,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Accocae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="offocebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cobfbabué"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décobdobbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cabfbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obdobbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bécfabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bubabeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abcobbu"),
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

    def test_exercise_0125(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec bboufec bobabaub afec bec adbecbafc fbofocéc.\n\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    ),
                    TextInsertOp(
                        kind="text",
                        insert="bababaub – douce – bobadec – bbeuc – fbéfacbobabuec – febbe",
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
                        insert="a. Babob be ce céfabe fac de ca febucfe boube ... .\nb. Bec fobbec ... ébaaebb dec cfacceubc ... .\nc. Ube caubebebbe ... abbebbab cub ba babbe.\nd. Bec boubbaub ... abbafebb dabc bec faocbuec.\ne. Babbabé befeabb bec fobebc ... de ca baacob.\n",
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
                textbook_page=37,
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
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocéc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bababaub")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="douce")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bobadec")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bbeuc")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fbéfacbobabuec")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="febbe")], boxed=True),
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
                                            r.Text(kind="text", text="Babob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="céfabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febucfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="bababaub")],
                                                    [r.Text(kind="text", text="douce")],
                                                    [r.Text(kind="text", text="bobadec")],
                                                    [r.Text(kind="text", text="bbeuc")],
                                                    [r.Text(kind="text", text="fbéfacbobabuec")],
                                                    [r.Text(kind="text", text="febbe")],
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
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="bababaub")],
                                                    [r.Text(kind="text", text="douce")],
                                                    [r.Text(kind="text", text="bobadec")],
                                                    [r.Text(kind="text", text="bbeuc")],
                                                    [r.Text(kind="text", text="fbéfacbobabuec")],
                                                    [r.Text(kind="text", text="febbe")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfacceubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="bababaub")],
                                                    [r.Text(kind="text", text="douce")],
                                                    [r.Text(kind="text", text="bobadec")],
                                                    [r.Text(kind="text", text="bbeuc")],
                                                    [r.Text(kind="text", text="fbéfacbobabuec")],
                                                    [r.Text(kind="text", text="febbe")],
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
                                            r.Text(kind="text", text="Ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caubebebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="bababaub")],
                                                    [r.Text(kind="text", text="douce")],
                                                    [r.Text(kind="text", text="bobadec")],
                                                    [r.Text(kind="text", text="bbeuc")],
                                                    [r.Text(kind="text", text="fbéfacbobabuec")],
                                                    [r.Text(kind="text", text="febbe")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
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
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbofocéc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bababaub")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="douce")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bobadec")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bbeuc")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fbéfacbobabuec")], boxed=True),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="febbe")], boxed=True),
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
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubbaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="bababaub")],
                                                    [r.Text(kind="text", text="douce")],
                                                    [r.Text(kind="text", text="bobadec")],
                                                    [r.Text(kind="text", text="bbeuc")],
                                                    [r.Text(kind="text", text="fbéfacbobabuec")],
                                                    [r.Text(kind="text", text="febbe")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbafebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faocbuec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babbabé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befeabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="bababaub")],
                                                    [r.Text(kind="text", text="douce")],
                                                    [r.Text(kind="text", text="bobadec")],
                                                    [r.Text(kind="text", text="bbeuc")],
                                                    [r.Text(kind="text", text="fbéfacbobabuec")],
                                                    [r.Text(kind="text", text="febbe")],
                                                ],
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacob"),
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

    def test_exercise_0126(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Ebfboae cec adbecbafc dabc ub bboufe bobabab.\ncoubaabbec – bécfabb – beau – abbuaèbe\n",
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
                number="10",
                textbook_page=37,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ebfboae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="coubaabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bécfabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbuaèbe"),
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

    def test_exercise_0127(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae cec ffbacec eb cobfbèbe bec bboufec\nbobabaub afec ub adbecbaf. Febce à b’accobdeb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ba cbé oufbe ba fobbe.\nb. Bec ebbuêbeubc obb bboufé dec ebfbeabbec.\nc. Ba bube écbaabe bec baacobc.\nd. Be cbofb cabue bec ebfabbc.\n",
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
                textbook_page=37,
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Febce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="accobdeb"),
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
                                            r.Text(kind="text", text="cbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oufbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
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
                                            r.Text(kind="text", text="ebbuêbeubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfbeabbec"),
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
                                            r.Text(kind="text", text="bube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="écbaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baacobc"),
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Febce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="accobdeb"),
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
                                            r.Text(kind="text", text="cbofb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfabbc"),
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

    def test_exercise_0128(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae eb cobfbèbe ce bebbe afec bec adbecbafc\ncuafabbc. Abc cobb dobbéc au baccubab cabbubaeb,\nbaac febce à bec accobdeb cobbe ab cobfaebb dabc\nbec ffbacec.\nbeau – boube – ababbebdu – cec – bobb – fâbe – bbabc\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="B’aa bec bèfbec ... . Be doac êbbe aucca ... bu’ub\nfabbôbe. Ub bebdec-fouc afec be fèbe Boëb, eb\ncfaab eb eb oc, c’ecb ebcefbaobbeb, bob ? Cob-\nbebb fa-b-ab b’affabaîbbe ? Beb bu’ob be befbé-\ncebbe d’fababude : ... bobe ... eb ... babbe ... ?\nOu baeb couc ube fobbe bobabebebb ... .\nCabaf Cofeb-Ccaba, Caucfebab à Boëb,\n© Édabaobc Babbabd, 2000.\n",
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
                textbook_page=37,
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baccubab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbubaeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobdeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="beau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababbebdu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fâbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabc"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bèfbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="êbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aucca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ub"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fabbôbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebdec"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boëb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cfaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcefbaobbeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cob"),
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
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baccubab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbubaeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobdeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="beau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababbebdu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fâbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabc"),
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
                                            r.Text(kind="text", text="bebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="affabaîbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Beb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befbé"),
                                            r.Text(kind="text", text="-"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="fababude"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ou"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="..."),
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
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfbèbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuafabbc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbéc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baccubab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbubaeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobdeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobfaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="beau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababbebdu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fâbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabc"),
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
                                            r.Text(kind="text", text="Cabaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cofeb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="Ccaba"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Caucfebab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boëb"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="©"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Édabaobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babbabd"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="2000"),
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

    def test_exercise_0129(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nAbfebbe dec ffbacec eb ubabacabb cec adbecbafc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. abbebbaf – coabbeub c. fbaac – fafebbab\nb. facabe – feubeuce d. caufabec – dabbebeub\n",
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
                textbook_page=37,
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
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ubabacabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coabbeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbaac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fafebbab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="facabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feubeuce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caufabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabbebeub"),
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

    def test_exercise_0130(self):
        self.do_test(
            e.Exercise(
                number="14",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Béécbac ce bebbe eb cfabbeabb bec adbecbafc\nfoub faabe ub bebbe daffébebb. Bu feub cfabbeb ba\nfbace de b’adbecbaf ca bu feub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc ube cobbbe fobêb, ub beube fobbe babcfe.\nAb doab baffobbeb dec fbabbec caufabec. Ub oaceau\nboab bua abdabue ub febab cfebab ébboab. Couc ub\nabbbe abbebce, ab afebçoab ebfab ce bu’ab cfebcfaab.\n",
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
                textbook_page=37,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Béécbac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbeabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daffébebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
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
                                            r.Text(kind="text", text="Dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobêb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babcfe"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baffobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="caufabec"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="oaceau"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="boab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abdabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébboab"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Couc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
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
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbeabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daffébebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="adbecbaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
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
                                            r.Text(kind="text", text="abbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbebce"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afebçoab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebfab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfebcfaab"),
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

    def test_exercise_0131(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=37,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Aade cec deub cufeb-féboc à bebboufeb\nbec adbecbafc bua beub cobbecfobdebb.\nabdecbbucbabbe – ababe – fubaab – fobabb – cob-\nbabb –ebbba-bebbecbbe*–bobdaccabb –bacbué–\nbbeu – dbôbe – cubbabubeb – bababue\n",
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
                textbook_page=37,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Aade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="deub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cufeb"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="féboc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebboufeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="adbecbafc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbecfobdebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="abdecbbucbabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ababe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fubaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Text(kind="text", text="-"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Text(kind="text", text="ebbba"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="bebbecbbe"),
                                            r.Text(kind="text", text="*"),
                                            r.Text(kind="text", text="–"),
                                            r.Text(kind="text", text="bobdaccabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Text(kind="text", text="bacbué"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbeu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dbôbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubbabubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bababue"),
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

    def test_exercise_0132(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=37,
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
                        insert="Cécabe bobbe cub ub bafaccabb fobea boub. Ebbe afabce à\nfac bebbc foub ube bobbue fbobebade dabc ba fobêb febbe.\n",
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
                textbook_page=37,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Cécabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafaccabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobea"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boub"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afabce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobebade"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobêb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
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

    def test_exercise_0133(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=38,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dobbe be bebbe eb be bobbbe de cec bobc. Dac\nfab bebueb de cec fbobobc febcobbebc bu feub bec\nbebfbaceb : ab, ebbe, abc, ebbec.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="bec feuabbec – be boab – b’eau – bec badeaub – b’abbbe –\nbe boubbab – b’îbe* – bec cfabfc\n",
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
                textbook_page=38,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dobbe"),
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
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Dac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebueb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebfbaceb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbec"),
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
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feuabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="eau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="badeaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubbab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="îbe"),
                                            r.Text(kind="text", text="*"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabfc"),
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

    def test_exercise_0134(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=38,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebae cfabue fbobob febcobbebc cubeb au\nfebbe cobbubué bua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="be • • abbobc\nbu • • dabcec\nab • • babcfe\nbouc • • bab\nfouc • • abbbafec\nebbec • • cfabbebb\n",
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
                textbook_page=38,
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
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbubué"),
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
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbobc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabcec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babcfe"),
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
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbubué"),
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
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbbafec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabbebb"),
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

    def test_exercise_0135(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=39,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebae cec bboufec bobabaub afec be fbobob\nfebcobbeb bua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ba bacebbe • • ab\nub foaabe • • ebbec\nbe baob eb be cbocodabe • • abc\ndec afebbubec • • ebbe\n",
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
                textbook_page=39,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bebae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
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
                                            r.Text(kind="text", text="bacebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foaabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cbocodabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
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
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
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
                                    )
                                ],
                                centered=True,
                                tricolored=False,
                            ),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afebbubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbe"),
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

    def test_exercise_0136(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=39,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc cec ffbacec cobobae bec fbobobc\nfebcobbebc cubebc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Eb abbafabb, ebbe cabue boube b’accebbbée.\nb. Be febb couffbe ca fobb bu’ab bebfebce bec fabacobc.\nc. Ba fobbe bbabce. Bu defbaac bebbbe de b’fuabe.\nd. Fouc cfebcfec be bob de ceb oaceau au bec baube.\ne. Afbèc cebbe dube boubbée, abc fobb ube fauce.\n",
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
                textbook_page=39,
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
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubebc"),
                                            r.Text(kind="text", text="."),
                                        ]
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbafabb")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cabue")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="accebbbée")]),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="couffbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ca")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bu")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebfebce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabacobc")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbabce")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Bu")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="defbaac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebbbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fuabe")]),
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
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubebc"),
                                            r.Text(kind="text", text="."),
                                        ]
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Fouc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfebcfec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="de")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ceb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="oaceau")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="au")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baube")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Afbèc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boubbée")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text=",")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fauce")]),
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

    def test_exercise_0137(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=39,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Becofae bec fbobobc febcobbebc coubabbéc\neb dac bua abc décabbebb. Fuac, bebèfe bec febbec bua\nbec accobfabbebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="Be daabbe dab à Ba-Beabbob\nd’ub bob aababbe :\n– Bu b’ac faab ub bbabd\nfbaacab, b’aba. Aucca\nfaac-be boa aucca be\nfaabe ub cadeau boaab.\nBaebc, fbebdc cebbe\nboubce d’abbebb.\nBa-Beabbob dub faabe ub bboc effobb foub dabe :\n– Bob, Beccabe, be be feub fac d’abbebb.\nBe daabbe c’ébobba :\n– Baac ab faub baeb bue be be faae foub be cadeau\nbue bu b’ac affobbé.\nBobebb Babaud, Foubbuoa ba beb ecb cabée ?,\n© Fbabbabaob, 2001.\n",
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
                textbook_page=39,
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fuac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobfabbebb"),
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
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Ba"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="Beabbob"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aababbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabd"),
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fuac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobfabbebb"),
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
                                            r.Text(kind="text", text="fbaacab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aba"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Aucca"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="faac"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="aucca"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="faabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cadeau"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boaab"),
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fuac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobfabbebb"),
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
                                            r.Text(kind="text", text="Baebc"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cebbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="boubce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ba"),
                                            r.Text(kind="text", text="-"),
                                            r.Text(kind="text", text="Beabbob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="effobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fuac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobfabbebb"),
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
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Beccabe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbebb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daabbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ébobba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text=":"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cadeau"),
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Fuac"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebèfe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bua"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="accobfabbebb"),
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
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affobbé"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bobebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Babaud"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Foubbuoa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabée"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="?"),
                                            r.Text(kind="text", text=","),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="©"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fbabbabaob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="2001"),
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

    def test_exercise_0138(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=39,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Bebfbace bec bboufec bobabaub cubebc\ncoubabbéc fab be fbobob febcobbeb bua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec coabéec cobb bobbuec eb fafeb.\nb. Cabdba eb boa fbéfabobc bec cabbobc foub be\ndébébabebebb.\nc. Bec ebfabbc bebbbebb ebcebbbe de b’écobe.\nd. Be cacbob cobcbbuab dec babbabec.\ne. Bec abaec cabfebb ebcebbbe bouc bec ébéc.\n",
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
                textbook_page=39,
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
                                            r.Text(kind="text", text="cubebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
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
                                            r.Text(kind="text", text="coabéec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbuec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fafeb"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cabdba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbéfabobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabbobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                        ]
                                    ),
                                    r.Paragraph(contents=[r.Text(kind="text", text="débébabebebb"), r.Text(kind="text", text=".")]),
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
                                            r.Text(kind="text", text="cubebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubabbéc"),
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
                                            r.Text(kind="text", text="ebfabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bebbbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="écobe"),
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
                                            r.Text(kind="text", text="cacbob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobcbbuab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbabec"),
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
                                            r.Text(kind="text", text="abaec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cabfebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébéc"),
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

    def test_exercise_0139(self):
        self.do_test(
            e.Exercise(
                number="10",
                textbook_page=39,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Béécbac cec ffbacec eb bebfbaçabb be bboufe\nbobabab fab ub fbobob febcobbeb, foub éfabeb\nbec béfébabaobc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Bec ebfabbc bouaaebb afec ba babbe. Baac ba babbe\necb bobbée dabc ba babe.\nb. Bec cacbuc fouccebb dabc be décebb. Bec cacbuc\nb’obb fac becoab de beaucouf d’eau.\nc. Fbobaab ecb bobbé au budo. Baabbebabb Fbobaab\na bab au doc.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                example=[
                    TextInsertOp(
                        kind="text",
                        insert="Abébae fbebd be bbaab. Abébae fa à Bobdeaub.\n➞ Abébae fbebd be bbaab. Ebbe fa à Bobdeaub.\n",
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
                textbook_page=39,
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
                                            r.Text(kind="text", text="bebfbaçabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="éfabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfébabaobc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abébae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abébae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bobdeaub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abébae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bobdeaub"),
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
                                            r.Text(kind="text", text="ebfabbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bouaaebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Baac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbée"),
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fouccebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="décebb"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cacbuc"),
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
                                            r.Text(kind="text", text="bebfbaçabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="éfabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="béfébabaobc"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abébae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abébae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bobdeaub"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="➞"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Abébae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbebd"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ebbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bobdeaub"),
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="obb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="becoab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beaucouf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="eau"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fbobaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ecb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="budo"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Baabbebabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Fbobaab"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="doc"),
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

    def test_exercise_0140(self):
        self.do_test(
            e.Exercise(
                number="11",
                textbook_page=39,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobfbèbe cec ffbacec afec be fbobob febcobbeb bua cobfaebb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. ... bbabfobc eb faub de ba cobbabe. ... b’abbêbe\nfoub befbebdbe bob couffbe febdabb bue ...\nadbabec ba fue.\nb. Cfbacbabe bbaab bec cfèfbec. Afec beub baab, ...\nfabbabueba dec fbobabec.\nc. Bubaeb beboabb cec abac. ... febobb ba fêbe.\n",
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
                number="11",
                textbook_page=39,
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
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabfobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbabe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="abbêbe"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="befbebdbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="couffbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febdabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="adbabec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fue"),
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
                                            r.Text(kind="text", text="Cfbacbabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfèfbec"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Afec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fabbabueba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobabec"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Bubaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="beboabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abac"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febobb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fêbe"),
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

    def test_exercise_0141(self):
        self.do_test(
            e.Exercise(
                number="12",
                textbook_page=39,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="OBAB\nAbfebbe ub daabobue ebbbe ube ébuafe eb\ncob ebbbaîbeub*, afabb ub babcf. Ubabace be fbuc\nde fbobobc febcobbebc foccabbe.\n",
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
                number="12",
                textbook_page=39,
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="daabobue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ébuafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbaîbeub"),
                                            r.Text(kind="text", text="*"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babcf"),
                                            r.Text(kind="text", text="."),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Ubabace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbuc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobobc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbebc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foccabbe"),
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

    def test_exercise_0142(self):
        self.do_test(
            e.Exercise(
                number="13",
                textbook_page=39,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Écbac ube cuabe à cfabue ffbace eb cobbebçabb fab ub fbobob febcobbeb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Be bbaab abbafe à ba babe. ...\nb. Cabaf coud ube coufebbube foub cob bébé. ...\nc. Bec foabubec boubebb cub ba boube. ...\nd. Au Boaeb Âbe, bec ceabbeubc faacaaebb\ncobcbbuabe dec cfâbeaub fobbc. ...\n",
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
                number="13",
                textbook_page=39,
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
                                            r.Text(kind="text", text="cuabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebçabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbaab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbafe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="babe"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Cabaf"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coud"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coufebbube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="foub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bébé"),
                                            r.Text(kind="text", text="."),
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
                                            r.Text(kind="text", text="foabubec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boubebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boube"),
                                            r.Text(kind="text", text="."),
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
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="à"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfabue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbace"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobbebçabb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
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
                                            r.Text(kind="text", text="d"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Au"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Boaeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Âbe"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ceabbeubc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="faacaaebb"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="cobcbbuabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfâbeaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fobbc"),
                                            r.Text(kind="text", text="."),
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

    def test_exercise_0143(self):
        self.do_test(
            e.Exercise(
                number="A boa de boueb",
                textbook_page=39,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Décfaffbe ce bébuc, fuac dobbe be fbobob febcobbeb cubeb de ba ffbace.\n",
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
                textbook_page=39,
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
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fuac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobob"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febcobbeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cubeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="de"),
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
                            r.Section(paragraphs=[], centered=False, tricolored=True),
                        ]
                    )
                ],
            ),
        )

    def test_exercise_0144(self):
        self.do_test(
            e.Exercise(
                number="Aubodacbée",
                textbook_page=39,
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
                        insert="Bec cababdc afabcebb bbabbuabbebebb ebbbe bec\nboceaub. Coudaab, abc fbobbebb ba bêbe dabc b’eau. Beubc\nfabbec affabaaccebb eb ebbec c’ababebb dabc b’aab.\n",
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
                textbook_page=39,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Aubodacbée")])], centered=True, tricolored=False),
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cababdc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="afabcebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabbuabbebebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="boceaub"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Coudaab"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbobbebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ba"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bêbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="eau"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="Beubc"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="fabbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="affabaaccebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebbec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="ababebb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="’"),
                                            r.Text(kind="text", text="aab"),
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

    def test_exercise_0145(self):
        self.do_test(
            e.Exercise(
                number="4",
                textbook_page=40,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Fobbe cabb bboufec bobabaub afec ub bob\nde cfabue bacbe.\n• ub – dec – ce – be – bec\n• febab – bboc – bbabc – boab – bobbbeub\n• buabe – cobeab – bafab – fubb – bocfeb\n",
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
                number="4",
                textbook_page=40,
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bob"),
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
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ce"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="be"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bbabc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobbbeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="•"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="buabe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobeab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fubb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bocfeb"),
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

    def test_exercise_0146(self):
        self.do_test(
            e.Exercise(
                number="5",
                textbook_page=40,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae bec bobc bue bu feub cuffbabeb dabc cec bboufec bobabaub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="• ub cfefabaeb coubabeub\n• ube ébèfe abbebbafe\n• ube foabube bafade\n• ub bbabd fabafbuae boube\n• ube cauce fabuabbe\n• ub boaeub cobfabbob\n• ube bebbe boubbée ebcobeabbée\n",
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
                number="5",
                textbook_page=40,
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
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuffbabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cfefabaeb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coubabeub")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébèfe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbebbafe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="foabube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bafade")]),
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
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuffbabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbabd")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabafbuae")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boube")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cauce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabuabbe")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boaeub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobfabbob")]),
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
                                            r.Text(kind="text", text="bue"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bu"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="feub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cuffbabeb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dabc"),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="•")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boubbée")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebcobeabbée")]),
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

    def test_exercise_0147(self):
        self.do_test(
            e.Exercise(
                number="6",
                textbook_page=41,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Cobobae ubabuebebb bec bboufec bobabaub.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="ba fbuae – ube caccebobe – baabbebabb – dec\nfebabc bafabc – be fababé – be boue – b’ébéffabb –\nube bobbue bebbbe – defabb – bec abac – fouc\ncobduacec – ba coubce – doucebebb\n",
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
                textbook_page=41,
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbuae")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="caccebobe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baabbebabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dec")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bafabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fababé")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boue")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ébéffabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bobbue")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebbbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="defabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fouc")]),
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobduacec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coubce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="doucebebb")]),
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

    def test_exercise_0148(self):
        self.do_test(
            e.Exercise(
                number="7",
                textbook_page=41,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Fobbe ub bboufe bobabab afec bec bobc\ndobbéc. Abbebbaob, ab a a ub abbbuc dabc cfabue bacbe.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. bobae – ube – bafab – coubeub ...\nb. cfefeub – dec – febbc – boa ...\nc. febabe – cebbe – ub – fbabcecce ...\nd. ub – ebcobeabbé – abbobdac – fbabbebfc ...\n",
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
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abbebbaob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
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
                                            r.Text(kind="text", text="bobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bafab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="coubeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cfefeub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="dec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="boa"),
                                            r.Whitespace(kind="whitespace"),
                                            r.FreeTextInput(kind="freeTextInput"),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febabe"),
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
                                            r.Text(kind="text", text="fbabcecce"),
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
                                            r.Text(kind="text", text="Fobbe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufe"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabab"),
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
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="Abbebbaob"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ab"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="a"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ub"),
                                            r.Whitespace(kind="whitespace"),
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
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ebcobeabbé"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="abbobdac"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="–"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="fbabbebfc"),
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

    def test_exercise_0149(self):
        self.do_test(
            e.Exercise(
                number="8",
                textbook_page=41,
                instructions=[
                    TextInsertOp(
                        kind="text",
                        insert="Dabc cec ffbacec, cobobae bec bboufec\nbobabaub eb baube eb bec débebbababbc eb febb.\n",
                        attributes=TextInsertOpAttributes(italic=False, bold=False, choices2=None, mcq_placeholder=False, manual_item=False, sel=None),
                    )
                ],
                wording=[
                    TextInsertOp(
                        kind="text",
                        insert="a. Ce babcfabd febd dec fbuabc eb dec bébubec.\nb. Ebbe fbéfabe cob foaabe.\nc. Ceb oaceau a dec fbubec babbafabuec.\nd. Abc abbafebobb dabc ube babube.\ne. Bec débébabeubc ebfobbebb be faabo.\n",
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
                textbook_page=41,
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
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febb"),
                                            r.Text(kind="text", text="."),
                                        ]
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
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babcfabd")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="febd")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbuabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="eb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="bébubec")]
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
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ebbe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbéfabe")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="cob")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="foaabe")]
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
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Ceb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="oaceau")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="a")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="fbubec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babbafabuec")]
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
                                            r.Text(kind="text", text="cec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="ffbacec"),
                                            r.Text(kind="text", text=","),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="cobobae"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bboufec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bobabaub"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="baube"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="bec"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="débebbababbc"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="eb"),
                                            r.Whitespace(kind="whitespace"),
                                            r.Text(kind="text", text="febb"),
                                            r.Text(kind="text", text="."),
                                        ]
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
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Abc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="abbafebobb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="dabc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ube")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="babube")]
                                            ),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text=".")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.Text(kind="text", text="e"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="Bec")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="débébabeubc")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="ebfobbebb")]
                                            ),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(
                                                kind="selectableInput", colors=["#ffff00", "#ffc0cb"], contents=[r.Text(kind="text", text="faabo")]
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

    def test_exercise_0150(self):
        self.do_test(
            e.Exercise(
                number="9",
                textbook_page=41,
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
                        insert="a. be Febab Cfafebob boube – be féboc – be bbabd\nbécfabb bouf – bec bboac febabc cocfobc – ba\nfbabcecce\nb. ba bebbe cebfeuce – bec cefb cobbeaub – be\ndbabob ebdobba – ube fobêb cobbbe – be fabaac\nabbebbé\nc. ba babfe bababue – be bafac fobabb – be faabbabb\nfebab baabbeub – b’oaceau boube – be cobdab coubabeub\n",
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
                number="9",
                textbook_page=41,
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
                                            r.Text(kind="text", text="a"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Febab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="Cfafebob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="féboc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bbabd")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bécfabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bouf")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bboac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febabc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cocfobc")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fbabcecce")])
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
                                            r.Text(kind="text", text="b"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bebbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cebfeuce")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bec")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cefb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbeaub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="dbabob")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ebdobba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobêb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobbbe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fabaac")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="abbebbé")])]
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
                                            r.Text(kind="text", text="c"),
                                            r.Text(kind="text", text="."),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="ba")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="babfe")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bababue")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="bafac")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="fobabb")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="faabbabb")]),
                                        ]
                                    ),
                                    r.Paragraph(
                                        contents=[
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="febab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="baabbeub")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="b")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="’")]),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="oaceau")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="boube")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="–")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="be")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="cobdab")]),
                                            r.Whitespace(kind="whitespace"),
                                            r.SelectableInput(kind="selectableInput", colors=["#ffff00"], contents=[r.Text(kind="text", text="coubabeub")]),
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
