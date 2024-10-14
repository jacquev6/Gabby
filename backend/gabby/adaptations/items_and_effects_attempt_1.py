from typing import ClassVar, Literal

from .. import exercise_delta
from .. import parsing
from .. import renderable
from mydantic import PydanticBase


class ItemsAndEffectsAttempt1Adaptation(PydanticBase):
    kind: Literal["items-and-effects-attempt-1"]

    class WordsItems(PydanticBase):
        kind: Literal["words"]
        punctuation: bool

    class SentencesItems(PydanticBase):
        kind: Literal["sentences"]

    class ManualItems(PydanticBase):
        kind: Literal["manual"]

    Items: ClassVar = WordsItems | SentencesItems | ManualItems

    items: Items

    class Effects(PydanticBase):
        class Selectable(PydanticBase):
            colors: list[str]

        selectable: Selectable | None
        boxed: bool

    effects: Effects

    @property
    def _color_indexes(self):
        if self.effects.selectable is None:
            return []
        else:
            return range(1, len(self.effects.selectable.colors) + 1)

    def _make_instructions_tags(self):
        tags = {}
        if self.effects.selectable is not None:
            tags.update({f"sel{color_index}": r""" "|" STR """ for color_index in self._color_indexes})
        return tags

    def _make_instructions_adapter_type(self):
        tag_functions = {}
        if self.effects.selectable is not None:
            colors = self.effects.selectable.colors
            tag_functions.update({
                f"sel{color_index}_tag": (lambda color: staticmethod(lambda args: renderable.SelectedText(text=args[0], color=color)))(colors[color_index - 1])
                for color_index in self._color_indexes
            })
        return type("InstructionsAdapter", (parsing.InstructionsSectionAdapter,), tag_functions)

    def _adapt_instructions(self, section):
        return parsing.InstructionsSectionParser(
            self._make_instructions_tags(),
            self._make_instructions_adapter_type()(),
        )(
            section,
        )

    def make_adapted_instructions(self, exercise):
        return self._adapt_instructions(exercise.instructions)

    class WordsItemsWordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, punctuation, colors, boxed):
            self.select_punctuation = punctuation
            self.colors = colors
            self.boxed = boxed

        def WORD(self, arg):
            return renderable.SelectableText(text=arg.value, colors=self.colors, boxed=self.boxed)

        def PUNCTUATION_IN_SENTENCE(self, arg):
            if self.select_punctuation:
                return renderable.SelectableText(text=arg.value, colors=self.colors, boxed=self.boxed)
            else:
                return renderable.PlainText(text=arg.value)

        PUNCTUATION_AT_END_OF_SENTENCE = PUNCTUATION_IN_SENTENCE
        PUNCTUATION_IN_LENIENT_PARAGRAPH = PUNCTUATION_IN_SENTENCE

    class ManualItemsWordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, colors, boxed):
            self.colors = colors
            self.boxed = boxed

        def selectable_tag(self, args):
            assert len(args) == 1
            return renderable.SelectableText(text=args[0], colors=self.colors, boxed=self.boxed)

    def make_adapted_wording(self, exercise):
        if self.effects.selectable is None:
            return parsing.adapt_plain_wording_section(exercise.wording)
        else:
            if self.items.kind == "words":
                return parsing.parse_wording_section(
                    {},
                    self.WordsItemsWordingAdapter(self.items.punctuation, self.effects.selectable.colors, self.effects.boxed),
                    exercise.wording,
                )
            elif self.items.kind == "manual":
                return parsing.parse_wording_section(
                    {"selectable": r""" "|" STR """},
                    self.ManualItemsWordingAdapter(self.effects.selectable.colors, self.effects.boxed),
                    exercise.wording,
                )
            else:
                assert False, f"Unknown items kind: {self.items.kind}"

    def make_adapted_example(self, exercise):
        return self._adapt_instructions(exercise.example)

    def make_adapted_clue(self, exercise):
        return self._adapt_instructions(exercise.clue)

    def _make_instructions_delta_maker_type(self):
        tag_functions = {}
        if self.effects.selectable is not None:
            tag_functions.update({
                f"sel{color_index}_tag": (lambda color_index: staticmethod(lambda args: exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": color_index})))(color_index)
                for color_index in self._color_indexes
            })
        return type("InstructionsDeltaMaker", (parsing.InstructionsSectionDeltaMaker,), tag_functions)

    def _make_instructions_delta(self, section):
        return parsing.InstructionsSectionParser(
            self._make_instructions_tags(),
            self._make_instructions_delta_maker_type()(),
        )(
            section,
        )

    def make_instructions_delta(self, exercise):
        return self._make_instructions_delta(exercise.instructions)

    class ManualItemsWordingDeltaMaker(parsing.WordingSectionDeltaMaker):
        def selectable_tag(self, args):
            assert len(args) == 1
            return exercise_delta.TextInsertOp(insert=args[0], attributes={"selectable": True})

    def make_wording_delta(self, exercise):
        if self.effects.selectable is None:
            return parsing.make_plain_wording_section_delta(exercise.wording)
        else:
            if self.items.kind == "words":
                return parsing.make_plain_wording_section_delta(exercise.wording)
            elif self.items.kind == "manual":
                return parsing.WordingSectionParser(
                    {"selectable": r""" "|" STR """},
                    self.ManualItemsWordingDeltaMaker(),
                )(
                    exercise.wording,
                )
            else:
                assert False, f"Unknown items kind: {self.items.kind}"

    def make_example_delta(self, exercise):
        return self._make_instructions_delta(exercise.example)

    def make_clue_delta(self, exercise):
        return self._make_instructions_delta(exercise.clue)
