from __future__ import annotations
import itertools
from typing import Annotated, ClassVar, Literal, TypeAlias
import datetime

from fastjsonapi import Constant, Computed, Secret, WriteOnly
import pydantic

from . import exercise_delta
from . import renderable
from . import parsing
from mydantic import PydanticBase


class CreatedByAtMixin:
    created_at: Annotated[datetime.datetime, Computed()]
    created_by: Annotated[User, Computed()]

class UpdatedByAtMixin:
    updated_at: Annotated[datetime.datetime, Computed()]
    updated_by: Annotated[User, Computed()]

class CreatedUpdatedByAtMixin(CreatedByAtMixin, UpdatedByAtMixin):
    pass

class OptionalCreatedByAtMixin:
    created_at: Annotated[datetime.datetime, Computed()]
    created_by: Annotated[User | None, Computed()] = None

class OptionalUpdatedByAtMixin:
    updated_at: Annotated[datetime.datetime, Computed()]
    updated_by: Annotated[User | None, Computed()] = None

class OptionalCreatedUpdatedByAtMixin(OptionalCreatedByAtMixin, OptionalUpdatedByAtMixin):
    pass


class User(PydanticBase, CreatedUpdatedByAtMixin):
    username: str | None
    clear_text_password: Annotated[str, Secret()]


class RecoveryEmailRequest(PydanticBase):
    address: Annotated[str, WriteOnly()]
    language: Annotated[str, WriteOnly()]


class Ping(PydanticBase, OptionalCreatedUpdatedByAtMixin):
    message: str | None = None
    prev: Ping | None = None
    next: list[Ping] = []


class PdfFile(PydanticBase, CreatedByAtMixin):
    sha256: Annotated[str, Constant()]
    bytes_count: Annotated[int, Constant()]
    pages_count: Annotated[int, Constant()]
    namings: Annotated[list[PdfFileNaming], Computed()] = []
    sections: Annotated[list[Section], Computed()] = []


class PdfFileNaming(PydanticBase, CreatedByAtMixin):
    name: Annotated[str, Constant()]
    pdf_file: Annotated[PdfFile, Constant()]


class Project(PydanticBase, CreatedUpdatedByAtMixin):
    title: str
    description: str = ""
    textbooks: Annotated[list[Textbook], Computed()] = []
    exercises: Annotated[list[Exercise], Computed()] = []


class Textbook(PydanticBase, CreatedUpdatedByAtMixin):
    title: str
    publisher: str | None = None
    year: int | None = None
    isbn: str | None = None
    project: Annotated[Project, Constant()]
    exercises: Annotated[list[Exercise], Computed()] = []
    sections: Annotated[list[Section], Computed()] = []


class Section(PydanticBase, CreatedUpdatedByAtMixin):
    textbook_start_page: int
    pdf_file_start_page: int
    pages_count: int
    textbook: Annotated[Textbook, Constant()]
    pdf_file: Annotated[PdfFile, Constant()]


class Point(PydanticBase):
    x: float
    y: float

class PdfRectangle(PydanticBase):
    pdf_sha256: str
    pdf_page: int
    # @todo Migrate all coordinates to "relative"
    coordinates: Literal[
        "pdfjs",  # As returned by PdfJs
        "relative",  # To the size of the page, in the range [0, 1], with (0, 0) at the top-left corner.
    ]
    start: Point
    stop: Point
    text: str | None
    role: Literal["bounding", "instructions", "wording", "example", "clue"]

# @todo Move These 'Adaptation' classes near the 'Exercise' class.
# They have two responsibilities: API and behavior. Not SOLID, but so convenient for now.

class FillWithFreeTextAdaptation_(PydanticBase):
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

class ItemsAndEffectsAttempt1Adaptation_(PydanticBase):
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
                f"sel{color_index}_tag": (lambda color_index: staticmethod(lambda args: exercise_delta.InsertOp(insert=args[0], attributes={"sel": color_index})))(color_index)
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
            return exercise_delta.InsertOp(insert=args[0], attributes={"selectable": True})

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

class MultipleChoicesInInstructionsAdaptation_(PydanticBase):
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

class MultipleChoicesInWordingAdaptation_(PydanticBase):
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

class NullAdaptation_(PydanticBase):
    kind: Literal["null"]

    def make_instructions_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.instructions)

    def make_adapted_instructions(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.instructions)

    def make_wording_delta(self, exercise):
        return parsing.make_plain_wording_section_delta(exercise.wording)

    def make_adapted_wording(self, exercise):
        return parsing.adapt_plain_wording_section(exercise.wording)

    def make_example_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.example)

    def make_adapted_example(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.example)

    def make_clue_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.clue)

    def make_adapted_clue(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.clue)

class SelectThingsAdaptation_(PydanticBase):
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

Adaptation: TypeAlias = FillWithFreeTextAdaptation_ | ItemsAndEffectsAttempt1Adaptation_ | MultipleChoicesInInstructionsAdaptation_ | MultipleChoicesInWordingAdaptation_ | NullAdaptation_ | SelectThingsAdaptation_

class Exercise(PydanticBase, CreatedUpdatedByAtMixin):
    project: Annotated[Project, Constant()]

    textbook: Annotated[Textbook | None, Constant()] = None
    textbook_page: Annotated[int | None, Constant()] = None

    number: Annotated[str, Constant()]

    instructions: str = ""
    wording: str = ""
    example: str = ""
    clue: str = ""

    wording_paragraphs_per_pagelet: int = 3

    rectangles: list[PdfRectangle] = []

    adaptation: Adaptation = NullAdaptation_(kind="null")

class ParsedExercise(PydanticBase):
    number: Annotated[str, WriteOnly()]
    instructions: Annotated[str, WriteOnly()]
    wording: Annotated[str, WriteOnly()]
    example: Annotated[str, WriteOnly()]
    clue: Annotated[str, WriteOnly()]
    wording_paragraphs_per_pagelet: Annotated[int, WriteOnly()]
    adaptation: Annotated[Adaptation, WriteOnly()] = pydantic.Field(discriminator="kind")
    adapted: Annotated[renderable.Exercise, Computed()]
    delta: Annotated[exercise_delta.Exercise, Computed()]


class SyntheticError(PydanticBase):
    pass
