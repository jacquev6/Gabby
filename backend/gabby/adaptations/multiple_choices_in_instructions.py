from typing import ClassVar, Literal
import itertools

from .. import exercise_delta
from .. import parsing
from .. import renderable
from mydantic import PydanticBase


class MultipleChoicesInInstructionsAdaptation(PydanticBase):
    kind: Literal["multiple-choices-in-instructions"]

    placeholder: str

    class InstructionsAdapter(parsing.InstructionsSectionAdapter):
        def choice_tag(self, args):
            assert len(args) == 1
            return renderable.BoxedText(text=args[0])

    instructions_tags: ClassVar = {"choice": r""" "|" STR """}

    adapt_instructions: ClassVar = parsing.InstructionsSectionParser(instructions_tags, InstructionsAdapter())

    def make_adapted_instructions(self, exercise):
        return self.adapt_instructions(exercise.instructions)

    class InstructionsDeltaMaker(parsing.InstructionsSectionDeltaMaker):
        def choice_tag(self, args):
            return exercise_delta.InsertOp(insert=args[0], attributes={"choice": True})

    make_instructions_delta_: ClassVar = parsing.InstructionsSectionParser(instructions_tags, InstructionsDeltaMaker())

    def make_instructions_delta(self, exercise):
        return self.make_instructions_delta_(exercise.instructions)

    class ChoicesGatherer(parsing.Transformer):
        def section(self, args):
            return list(itertools.chain(*args))

        def strict_paragraph(self, args):
            return list(itertools.chain(*args))

        def sentence(self, args):
            return list(itertools.chain(*args))

        def lenient_paragraph(self, args):
            return list(itertools.chain(*args))

        def choice_tag(self, args):
            assert len(args) == 1
            return [args[0]]

        def WORD(self, arg):
            return []

        def LEADING_WHITESPACE(self, arg):
            return []

        def TRAILING_WHITESPACE(self, arg):
            return []

        def PARAGRAPH_SEPARATOR(self, arg):
            return []

        def SENTENCE_SEPARATOR(self, arg):
            return []

        def WHITESPACE_IN_SENTENCE(self, arg):
            return []

        def PUNCTUATION_IN_SENTENCE(self, arg):
            return []

        def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
            return []

        def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
            return []

        def INT(self, arg):
            return None

        def STR(self, arg):
            return arg.value

        def bold_tag(self, args):
            return []

        def italic_tag(self, args):
            return []

    gather_choices: ClassVar = parsing.InstructionsSectionParser(instructions_tags, ChoicesGatherer())

    class WordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, choices):
            self.choices = choices

        def placeholder_tag(self, args):
            return renderable.MultipleChoicesInput(choices=self.choices)

    def make_adapted_wording(self, exercise):
        choices = self.gather_choices(exercise.instructions)
        return parsing.parse_wording_section(
            {"placeholder": ""},
            self.WordingAdapter(choices),
            exercise.wording.replace(self.placeholder, "{placeholder}")
        )

    def make_wording_delta(self, exercise):
        return parsing.make_plain_wording_section_delta(exercise.wording)

    def make_adapted_example(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.example)

    def make_example_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.example)

    def make_adapted_clue(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.clue)

    def make_clue_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.clue)
