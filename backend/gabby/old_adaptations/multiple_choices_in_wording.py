from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import renderable as r
from ..exercises import Exercise
from ..testing import AdaptationTestCase
from .base import OldAdaptation


class MultipleChoicesInWordingAdaptation(OldAdaptation):
    def to_new_adaptation(self):
        return api_models.MultipleChoicesInWordingAdaptation(
            kind="multiple-choices-in-wording",
        )


class MultipleChoicesInWordingAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices|a|b|c} B {choices|d|e}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = MultipleChoicesInWordingAdaptation(exercise=exercise)

        self.do_test(
            adaptation,
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
        )

    def test_example_and_clue(self):
        pass  # @todo Implement this test
