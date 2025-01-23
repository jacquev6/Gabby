from __future__ import annotations
from typing import Annotated, ClassVar, Literal
import datetime

from fastjsonapi import Constant, Computed, Secret, WriteOnly
import pydantic

from . import deltas
from . import renderable
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
    role: Literal["bounding", "instructions", "wording", "example", "clue", "textReference"]


class FillWithFreeTextAdaptationEffect(PydanticBase):
    kind: Literal["fill-with-free-text"]

    placeholder: str

class ItemizedAdaptationEffect(PydanticBase):
    kind: Literal["itemized"]

    # To implement #47, this could have been simply 'LettersItems', but 'CharactersItems' is homogeneous with 'TokensItems' below,
    # and future-proof for when we need to support spacing and punctuation items (as characters).
    class CharactersItems(PydanticBase):
        kind: Literal["characters"]
        letters: bool

    class TokensItems(PydanticBase):
        kind: Literal["tokens"]
        words: bool
        punctuation: bool

    class SentencesItems(PydanticBase):
        kind: Literal["sentences"]

    class ManualItems(PydanticBase):
        kind: Literal["manual"]

    Items: ClassVar = CharactersItems | TokensItems | SentencesItems | ManualItems

    class Effects(PydanticBase):
        class Selectable(PydanticBase):
            colors: list[str]

        selectable: Selectable | None
        boxed: bool

    items: Items
    effects: Effects

AdaptationEffect = Annotated[
    FillWithFreeTextAdaptationEffect | ItemizedAdaptationEffect,
    pydantic.Field(discriminator="kind"),
]

class AdaptationV2(PydanticBase):
    kind: Literal["generic", "fill-with-free-text", "multiple-choices"]
    effects: list[AdaptationEffect]

class Exercise(PydanticBase, CreatedUpdatedByAtMixin):
    project: Annotated[Project, Constant()]

    textbook: Annotated[Textbook | None, Constant()] = None
    textbook_page: Annotated[int | None, Constant()] = None

    number: Annotated[str, Constant()]

    instructions: deltas.Deltas = deltas.empty
    wording: deltas.Deltas = deltas.empty
    example: deltas.Deltas = deltas.empty
    clue: deltas.Deltas = deltas.empty
    text_reference: deltas.Deltas = deltas.empty

    wording_paragraphs_per_pagelet: int | None = None

    rectangles: list[PdfRectangle] = []

    adaptation: AdaptationV2 = AdaptationV2(kind="generic", effects=[])

class ParsedExercise(PydanticBase):
    number: Annotated[str, WriteOnly()]
    instructions: Annotated[deltas.Deltas, WriteOnly()]
    wording: Annotated[deltas.Deltas, WriteOnly()]
    example: Annotated[deltas.Deltas, WriteOnly()]
    clue: Annotated[deltas.Deltas, WriteOnly()]
    text_reference: Annotated[deltas.Deltas, WriteOnly()]
    wording_paragraphs_per_pagelet: Annotated[int | None, WriteOnly()]
    adaptation: Annotated[AdaptationV2, WriteOnly()]
    adapted: Annotated[renderable.Exercise, Computed()]


class SyntheticError(PydanticBase):
    pass
