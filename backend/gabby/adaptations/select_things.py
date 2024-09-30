from typing import Literal

from .. import exercise_delta
from .. import parsing
from .. import renderable
from mydantic import PydanticBase


class SelectThingsAdaptation(PydanticBase):
    kind: Literal["select-things"]

    colors: list[str]
    words: bool
    punctuation: bool

    @property
    def _color_indexes(self):
        return range(1, len(self.colors) + 1)

    def _make_tags(self):
        return {f"sel{color_index}": r""" "|" STR """ for color_index in self._color_indexes}

    def _make_adapter_type(self):
        return type("InstructionsAdapter", (parsing.InstructionsSectionAdapter,), {
            f"sel{color_index}_tag": (lambda color_index: staticmethod(lambda args: renderable.SelectedText(text=args[0], color=self.colors[color_index - 1])))(color_index)
            for color_index in self._color_indexes
        })

    def _adapt_instructions(self, section):
        return parsing.InstructionsSectionParser(
            self._make_tags(),
            self._make_adapter_type()(),
        )(
            section,
        )

    def make_adapted_instructions(self, exercise):
        return self._adapt_instructions(exercise.instructions)

    class WordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, words, punctuation, colors):
            self.select_words = words
            self.select_punctuation = punctuation
            self.colors = colors

        def WORD(self, arg):
            if self.select_words:
                return renderable.SelectableText(text=arg.value, colors=self.colors, boxed=False)
            else:
                return renderable.PlainText(text=arg.value)

        def PUNCTUATION_IN_SENTENCE(self, arg):
            if self.select_punctuation:
                return renderable.SelectableText(text=arg.value, colors=self.colors, boxed=False)
            else:
                return renderable.PlainText(text=arg.value)

        PUNCTUATION_AT_END_OF_SENTENCE = PUNCTUATION_IN_SENTENCE
        PUNCTUATION_IN_LENIENT_PARAGRAPH = PUNCTUATION_IN_SENTENCE

    def make_adapted_wording(self, exercise):
        return parsing.parse_wording_section(
            {},
            self.WordingAdapter(self.words, self.punctuation, self.colors),
            exercise.wording,
        )

    def make_adapted_example(self, exercise):
        return self._adapt_instructions(exercise.example)

    def make_adapted_clue(self, exercise):
        return self._adapt_instructions(exercise.clue)

    def _make_delta_maker_type(self):
        return type("InstructionsDeltaMaker", (parsing.InstructionsSectionDeltaMaker,), {
            f"sel{color_index}_tag": (lambda color: staticmethod(lambda args: exercise_delta.InsertOp(insert=args[0], attributes={"sel": color})))(color_index)
            for color_index in self._color_indexes
        })

    def _make_instructions_delta(self, section):
        return parsing.InstructionsSectionParser(
            self._make_tags(),
            self._make_delta_maker_type()(),
        )(
            section,
        )

    def make_instructions_delta(self, exercise):
        return self._make_instructions_delta(exercise.instructions)

    def make_wording_delta(self, exercise):
        return parsing.make_plain_wording_section_delta(exercise.wording)

    def make_example_delta(self, exercise):
        return self._make_instructions_delta(exercise.example)

    def make_clue_delta(self, exercise):
        return self._make_instructions_delta(exercise.clue)
