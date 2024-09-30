from typing import ClassVar, Literal

from .. import parsing
from .. import renderable
from mydantic import PydanticBase


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
