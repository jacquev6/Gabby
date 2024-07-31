from __future__ import annotations
from typing import Annotated
import datetime

from pydantic import BaseModel as Base

from fastjsonapi import Constant, Computed, Secret, WriteOnly

from . import renderable


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


class User(Base, CreatedUpdatedByAtMixin):
    username: str | None
    clear_text_password: Annotated[str, Secret()]


class RecoveryEmailRequest(Base):
    address: Annotated[str, WriteOnly()]
    language: Annotated[str, WriteOnly()]


class Ping(Base, OptionalCreatedUpdatedByAtMixin):
    message: str | None = None
    prev: Ping | None = None
    next: list[Ping] = []


class PdfFile(Base, CreatedByAtMixin):
    sha256: Annotated[str, Constant()]
    bytes_count: Annotated[int, Constant()]
    pages_count: Annotated[int, Constant()]
    namings: Annotated[list[PdfFileNaming], Computed()] = []
    sections: Annotated[list[Section], Computed()] = []


class PdfFileNaming(Base, CreatedByAtMixin):
    name: Annotated[str, Constant()]
    pdf_file: Annotated[PdfFile, Constant()]


class Project(Base, CreatedUpdatedByAtMixin):
    title: str
    description: str = ""
    textbooks: Annotated[list[Textbook], Computed()] = []
    exercises: Annotated[list[Exercise], Computed()] = []


class Textbook(Base, CreatedUpdatedByAtMixin):
    title: str
    publisher: str | None = None
    year: int | None = None
    isbn: str | None = None
    project: Annotated[Project, Constant()]
    exercises: Annotated[list[Exercise], Computed()] = []
    sections: Annotated[list[Section], Computed()] = []


class Section(Base, CreatedUpdatedByAtMixin):
    textbook_start_page: int
    pdf_file_start_page: int
    pages_count: int
    textbook: Annotated[Textbook, Constant()]
    pdf_file: Annotated[PdfFile, Constant()]


class Point(Base):
    x: float
    y: float

class Rectangle(Base):
    start: Point
    stop: Point

class Exercise(Base, CreatedUpdatedByAtMixin):
    project: Annotated[Project, Constant()]

    textbook: Annotated[Textbook | None, Constant()] = None
    textbook_page: Annotated[int | None, Constant()] = None
    bounding_rectangle: Rectangle | None = None

    number: Annotated[str, Constant()]

    instructions: str = ""
    wording: str = ""
    example: str = ""
    clue: str = ""

    extraction_events: Annotated[list[ExtractionEvent], Computed(), WriteOnly()] = []

    adaptation: (
        SelectThingsAdaptation
        | FillWithFreeTextAdaptation
        | MultipleChoicesInInstructionsAdaptation
        | MultipleChoicesInWordingAdaptation
        | None
    ) = None


class ExtractionEvent(Base, CreatedUpdatedByAtMixin):
    event: Annotated[str, Constant()]
    exercise: Annotated[Exercise, Constant()]


class SelectThingsAdaptationOptions(Base):
    colors: int
    words: bool
    punctuation: bool

class SelectThingsAdaptation(SelectThingsAdaptationOptions, CreatedUpdatedByAtMixin):
    exercise: Annotated[Exercise, Constant()]


class FillWithFreeTextAdaptationOptions(Base):
    placeholder: str

class FillWithFreeTextAdaptation(FillWithFreeTextAdaptationOptions, CreatedUpdatedByAtMixin):
    exercise: Annotated[Exercise, Constant()]


class MultipleChoicesInInstructionsAdaptationOptions(Base):
    placeholder: str

class MultipleChoicesInInstructionsAdaptation(MultipleChoicesInInstructionsAdaptationOptions, CreatedUpdatedByAtMixin):
    exercise: Annotated[Exercise, Constant()]


class MultipleChoicesInWordingAdaptationOptions(Base):
    pass

class MultipleChoicesInWordingAdaptation(MultipleChoicesInWordingAdaptationOptions, CreatedUpdatedByAtMixin):
    exercise: Annotated[Exercise, Constant()]


class ParsedExercise(Base):
    number: Annotated[str, WriteOnly()]
    instructions: Annotated[str, WriteOnly()]
    wording: Annotated[str, WriteOnly()]
    example: Annotated[str, WriteOnly()]
    clue: Annotated[str, WriteOnly()]
    type: Annotated[str, WriteOnly()]
    adaptation_options: Annotated[
        (
            SelectThingsAdaptationOptions
            | FillWithFreeTextAdaptationOptions
            | MultipleChoicesInInstructionsAdaptationOptions
            | MultipleChoicesInWordingAdaptationOptions
        ),
        WriteOnly(),
    ]
    adapted: Annotated[renderable.Exercise, Computed()]


class SyntheticError(Base):
    pass
