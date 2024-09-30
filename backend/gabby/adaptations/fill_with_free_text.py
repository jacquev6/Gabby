from typing import ClassVar, Literal

from .. import parsing
from .. import renderable
from mydantic import PydanticBase


class FillWithFreeTextAdaptation(PydanticBase):
    kind: Literal["fill-with-free-text"]

    placeholder: str

    def make_adapted_instructions(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.instructions)

    class WordingAdapter(parsing.WordingSectionAdapter):
        def placeholder_tag(self, args):
            return renderable.FreeTextInput()

    adapt_wording: ClassVar = parsing.WordingSectionParser({"placeholder": ""}, WordingAdapter())

    def make_adapted_wording(self, exercise):
        return self.adapt_wording(exercise.wording.replace(self.placeholder, "{placeholder}"))

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
