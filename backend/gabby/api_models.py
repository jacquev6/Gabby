from __future__ import annotations
from typing import Annotated, Literal, TypeAlias
import datetime

from fastjsonapi import Constant, Computed, Secret, WriteOnly

from . import exercise_delta
from . import parsing
from . import renderable
from .adaptations.fill_with_free_text import FillWithFreeTextAdaptation
from .adaptations.items_and_effects_attempt_1 import ItemsAndEffectsAttempt1Adaptation
from .adaptations.multiple_choices_in_instructions import MultipleChoicesInInstructionsAdaptation
from .adaptations.multiple_choices_in_wording import MultipleChoicesInWordingAdaptation
from .adaptations.null import NullAdaptation
from .adaptations.select_things import SelectThingsAdaptation
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


# @todo(After production data is migrated) Remove this type alias
AdaptationV1: TypeAlias = FillWithFreeTextAdaptation | ItemsAndEffectsAttempt1Adaptation | MultipleChoicesInInstructionsAdaptation | MultipleChoicesInWordingAdaptation | NullAdaptation | SelectThingsAdaptation

class AdaptationV2(PydanticBase):
    kind: Literal["fill-with-free-text", "items-and-effects-attempt-1", "select-things", "multiple-choices-in-instructions", "multiple-choices-in-wording", "multiple-choices"] | None
    effects: list[parsing.AdaptationEffect]

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

    adaptation: AdaptationV2 = AdaptationV2(kind=None, effects=[])

class ParsedExercise(PydanticBase):
    number: Annotated[str, WriteOnly()]
    instructions: Annotated[str, WriteOnly()]
    wording: Annotated[str, WriteOnly()]
    example: Annotated[str, WriteOnly()]
    clue: Annotated[str, WriteOnly()]
    wording_paragraphs_per_pagelet: Annotated[int, WriteOnly()]
    adaptation: Annotated[AdaptationV2, WriteOnly()]
    adapted: Annotated[renderable.Exercise, Computed()]
    delta: Annotated[exercise_delta.Exercise, Computed()]


class SyntheticError(PydanticBase):
    pass
