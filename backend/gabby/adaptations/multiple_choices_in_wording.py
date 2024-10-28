from typing import Literal
import os

from .. import exercise_delta as d
from .. import renderable as r
from .testing import AdaptationTestCase
from mydantic import PydanticBase

if os.environ.get("GABBY_UNITTESTING", "false") == "true":
    from .. import exercises


class MultipleChoicesInWordingAdaptation(PydanticBase):
    kind: Literal["multiple-choices-in-wording"]

    def make_effects(self):
        return []


class MultipleChoicesInWordingAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices|a|b|c} B {choices|d|e}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["d", "e"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A {choices|a|b|c} B {choices|d|e}.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_without_placeholder(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices2|(|/|)||(blah/blih)}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="(blah/blih)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_spaces(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices2|(|/|)||  (  blah  /  blih  )  }.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="  (  blah  /  blih  )  ",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_empty_start_and_stop(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices2||/|||blah/blih}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="blah/blih",
                        attributes={
                            "choices2": {
                                "start": "",
                                "separator": "/",
                                "stop": "",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_empty_separator(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices2|||||blah / blih}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah / blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="blah / blih",
                        attributes={
                            "choices2": {
                                "start": "",
                                "separator": "",
                                "stop": "",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_longer_separators(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices2|((|//|))||((blah//blih))}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="((blah//blih))",
                        attributes={
                            "choices2": {
                                "start": "((",
                                "separator": "//",
                                "stop": "))",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_escaped_separators(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording=r"A {choices2|\{|\||\}||\{blah\|blih\}}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="{blah|blih}",
                        attributes={
                            "choices2": {
                                "start": "{",
                                "separator": "|",
                                "stop": "}",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_placeholder_before(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="The sky is @@. {choices2|(|/|)|@@|(blue/red)} ",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_placeholder_after(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="{choices2|(|/|)|...|(blue/red)} The sky is ....",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "...",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is ....", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_two_placeholders(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="{choices2|(|/|)|...|(blue/yellow)} The sky is ..., the sun is ....",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "yellow"]),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "yellow"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/yellow)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "...",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is ..., the sun is ....", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_two_choices2_with_matching_placeholders(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="{choices2|(|/|)|@1|(blue/red)} {choices2|[|*|]|@2|[green*yellow]} The sky is @1, the sun is @2.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["green", "yellow"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "@1",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(
                        insert="[green*yellow]",
                        attributes={
                            "choices2": {
                                "start": "[",
                                "separator": "*",
                                "stop": "]",
                                "placeholder": "@2",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is @1, the sun is @2.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_two_choices2_with_identical_placeholders(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="The sky is @@. {choices2|(|/|)|@@|(blue/red)}\n\nThe sun is @@. {choices2|(|/|)|@@|(green/yellow)}",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["green", "yellow"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                    d.TextInsertOp(insert="\n\nThe sun is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(green/yellow)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_two_choices2_with_spaces_between_them(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="The sky is @1, {choices2|(|/|)|@1|(blue/red)} {choices2|[|*|]|@2|[green*yellow]} the sun is @2.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["green", "yellow"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @1, ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "@1",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(
                        insert="[green*yellow]",
                        attributes={
                            "choices2": {
                                "start": "[",
                                "separator": "*",
                                "stop": "]",
                                "placeholder": "@2",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" the sun is @2.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )
