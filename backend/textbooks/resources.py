from __future__ import annotations
from typing import Annotated

from pydantic import BaseModel
import django.conf

from fastjsonapi import Computed
from fastjsonapi.django import DjangoOrmWrapper, unwrap
from .models import PdfFile, PdfFileNaming, Project, Textbook, Section, Exercise, ExtractionEvent


default_page_size = django.conf.settings.REST_FRAMEWORK["PAGE_SIZE"]


class PdfFileModel(BaseModel):
    sha256: str
    bytes_count: int
    pages_count: int
    namings: list[PdfFileNamingModel] = []
    sections: list[SectionModel] = []

class PdfFilesResource:
    singular_name = "pdf_file"
    plural_name = "pdf_files"

    Model = PdfFileModel

    default_page_size = default_page_size


class PdfFileNamingModel(BaseModel):
    name: str
    pdf_file: PdfFileModel

class PdfFileNamingsResource:
    singular_name = "pdf_file_naming"
    plural_name = "pdf_file_namings"

    Model = PdfFileNamingModel

    default_page_size = default_page_size


class ProjectModel(BaseModel):
    title: str
    description: str = ""
    textbooks: Annotated[list[TextbookModel], Computed()] = []
    exercises: Annotated[list[ExerciseModel], Computed()] = []

class ProjectsResource:
    singular_name = "project"
    plural_name = "projects"

    Model = ProjectModel

    default_page_size = default_page_size

    def create_item(self, *, title, description):
        project = Project.objects.create(title=title, description=description)
        return DjangoOrmWrapper(project)

    def get_item(self, id):
        try:
            return DjangoOrmWrapper(Project.objects.get(id=str(id)))
        except Project.DoesNotExist:
            return None

    def get_page(self, filters, first_index, page_size):
        projects = Project.objects.all()
        return (
            # @todo Use proper SQL counting
            len(projects),
            # @todo Use proper SQL limits
            [DjangoOrmWrapper(project) for project in projects[first_index:first_index + page_size]],
        )


class TextbookModel(BaseModel):
    title: str
    publisher: str | None = None
    year: int | None = None
    isbn: str | None = None
    project: ProjectModel
    exercises: list[ExerciseModel] = []
    sections: list[SectionModel] = []

class TextbooksResource:
    singular_name = "textbook"
    plural_name = "textbooks"

    Model = TextbookModel

    default_page_size = default_page_size


class SectionModel(BaseModel):
    textbook_start_page: int
    pdf_file_start_page: int
    pages_count: int
    textbook: TextbookModel
    pdf_file: PdfFileModel

class SectionsResource:
    singular_name = "section"
    plural_name = "sections"

    Model = SectionModel

    default_page_size = default_page_size


class ExerciseModel(BaseModel):
    textbook_page: int | None = None
    number: str
    instructions: str = ""
    example: str = ""
    clue: str = ""
    wording: str = ""
    project: ProjectModel
    textbook: TextbookModel | None = None
    extraction_events: list[ExtractionEventModel] = []

class ExercisesResource:
    singular_name = "exercise"
    plural_name = "exercises"

    Model = ExerciseModel

    default_page_size = default_page_size


class ExtractionEventModel(BaseModel):
    event: str
    exercise: ExerciseModel

class ExtractionEventsResource:
    singular_name = "extraction_event"
    plural_name = "extraction_events"

    Model = ExtractionEventModel

    default_page_size = default_page_size
