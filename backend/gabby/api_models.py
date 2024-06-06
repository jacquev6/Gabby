from __future__ import annotations
from typing import Annotated

from pydantic import BaseModel

from fastjsonapi import Constant, Computed, Filterable, Secret as WriteOnly

from . import renderable


# @todo Remove 'Model' suffix from every model name

class PdfFileModel(BaseModel):
    sha256: Annotated[str, Constant()]
    bytes_count: Annotated[int, Constant()]
    pages_count: Annotated[int, Constant()]
    namings: Annotated[list[PdfFileNamingModel], Computed()] = []
    sections: Annotated[list[SectionModel], Computed()] = []


class PdfFileNamingModel(BaseModel):
    name: Annotated[str, Constant()]
    pdf_file: Annotated[PdfFileModel, Constant()]


class ProjectModel(BaseModel):
    title: str
    description: str = ""
    textbooks: Annotated[list[TextbookModel], Computed()] = []
    exercises: Annotated[list[ExerciseModel], Computed()] = []


class TextbookModel(BaseModel):
    title: str
    publisher: str | None = None
    year: int | None = None
    isbn: str | None = None
    project: Annotated[ProjectModel, Constant()]
    exercises: Annotated[list[ExerciseModel], Computed()] = []
    sections: Annotated[list[SectionModel], Computed()] = []


class SectionModel(BaseModel):
    textbook_start_page: int
    pdf_file_start_page: int
    pages_count: int
    textbook: Annotated[TextbookModel, Constant()]
    pdf_file: Annotated[PdfFileModel, Constant()]


class Point(BaseModel):
    x: float
    y: float

class Rectangle(BaseModel):
    start: Point
    stop: Point

class ExerciseModel(BaseModel):
    project: Annotated[ProjectModel, Constant()]

    textbook: Annotated[TextbookModel | None, Filterable(), Constant()] = None
    textbook_page: Annotated[int | None, Filterable(), Constant()] = None
    bounding_rectangle: Rectangle | None = None

    number: Annotated[str, Constant(), Filterable()]

    instructions: str = ""
    wording: str = ""
    example: str = ""
    clue: str = ""

    extraction_events: Annotated[list[ExtractionEventModel], Computed()] = []

    adaptation: (
        SelectThingsAdaptationModel
        | FillWithFreeTextAdaptationModel
        | MultipleChoicesInInstructionsAdaptationModel
        | MultipleChoicesInWordingAdaptationModel
        | None
    ) = None


class ExtractionEventModel(BaseModel):
    event: Annotated[str, Constant()]
    exercise: Annotated[ExerciseModel, Constant()]


class SelectThingsAdaptationOptionsModel(BaseModel):
    colors: int
    words: bool
    punctuation: bool

class SelectThingsAdaptationModel(SelectThingsAdaptationOptionsModel):
    exercise: Annotated[ExerciseModel, Constant()]


class FillWithFreeTextAdaptationOptionsModel(BaseModel):
    placeholder: str

class FillWithFreeTextAdaptationModel(FillWithFreeTextAdaptationOptionsModel):
    exercise: Annotated[ExerciseModel, Constant()]


class MultipleChoicesInInstructionsAdaptationOptionsModel(BaseModel):
    placeholder: str

class MultipleChoicesInInstructionsAdaptationModel(MultipleChoicesInInstructionsAdaptationOptionsModel):
    exercise: Annotated[ExerciseModel, Constant()]


class MultipleChoicesInWordingAdaptationOptionsModel(BaseModel):
    pass

class MultipleChoicesInWordingAdaptationModel(MultipleChoicesInWordingAdaptationOptionsModel):
    exercise: Annotated[ExerciseModel, Constant()]


class AdaptedExerciseModel(BaseModel):
    number: Annotated[str, WriteOnly()]
    textbookPage: Annotated[int | None, WriteOnly()]
    instructions: Annotated[str, WriteOnly()]
    wording: Annotated[str, WriteOnly()]
    example: Annotated[str, WriteOnly()]
    clue: Annotated[str, WriteOnly()]
    type: Annotated[str, WriteOnly()]
    adaptation_options: Annotated[
        (
            SelectThingsAdaptationOptionsModel
            | FillWithFreeTextAdaptationOptionsModel
            | MultipleChoicesInInstructionsAdaptationOptionsModel
            | MultipleChoicesInWordingAdaptationOptionsModel
        ),
        WriteOnly(),
    ]
    adapted: Annotated[renderable.AdaptedExercise, Computed()]
