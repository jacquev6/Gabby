from . import AdaptationTestCase
from .. import deltas as d
from .. import exercises as e
from .. import renderable as r
from ..api_models import Adaptation, PredefinedMcq


class ManualMcqFieldsAdaptationTestCase(AdaptationTestCase):
    def test_simplest(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(
                        insert="alpha, bravo ou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "", "mcqFieldUid": "f34d6"}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.EmbedInsertOp(insert={"mcq-field": "f34d6"}), d.TextInsertOp(insert="\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
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
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        sections=[
                            r.Section(
                                paragraphs=[
                                    r.Paragraph(
                                        contents=[
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
                                            r.MultipleChoicesInput(
                                                kind="multipleChoicesInput",
                                                choices=[
                                                    [r.Text(kind="text", text="Alpha")],
                                                    [r.Text(kind="text", text="Bravo")],
                                                    [r.Text(kind="text", text="Charlie")],
                                                ],
                                            )
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
