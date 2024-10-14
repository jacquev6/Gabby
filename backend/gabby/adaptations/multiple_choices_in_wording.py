from typing import ClassVar, Literal
import os

from .. import parsing
from .. import renderable
from .. import renderable as r
from .testing import AdaptationTestCase
from mydantic import PydanticBase

if os.environ.get("GABBY_UNITTESTING", "false") == "true":
    from .. import exercises


class MultipleChoicesInWordingAdaptation(PydanticBase):
    kind: Literal["multiple-choices-in-wording"]

    def make_adapted_instructions(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.instructions)

    class WordingAdapter(parsing.WordingSectionAdapter):
        def choices_tag(self, args):
            return renderable.MultipleChoicesInput(choices=[arg for arg in args])

    adapt_wording: ClassVar = parsing.WordingSectionParser({"choices": r""" ("|" STR)+ """}, WordingAdapter())

    def make_adapted_wording(self, exercise):
        return self.adapt_wording(exercise.wording)

    def make_adapted_example(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.example)

    def make_adapted_clue(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.clue)

    def make_instructions_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.instructions)

    def make_wording_delta(self, exercise):
        return parsing.make_plain_wording_section_delta(exercise.wording)

    def make_example_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.example)

    def make_clue_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.clue)


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
        )

    def test_example_and_clue(self):
        pass  # @todo Implement this test
