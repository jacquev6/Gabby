from __future__ import annotations
from typing import Annotated

from pydantic import BaseModel
import django.conf

from fastjsonapi import Computed, Filterable
from fastjsonapi.django import DjangoOrmWrapper, unwrap
from .models import PdfFile, PdfFileNaming, Project, Textbook, Section, Exercise, ExtractionEvent


default_page_size = django.conf.settings.REST_FRAMEWORK["PAGE_SIZE"]


class PdfFileModel(BaseModel):
    sha256: str
    bytes_count: int
    pages_count: int
    namings: Annotated[list[PdfFileNamingModel], Computed()] = []
    sections: Annotated[list[SectionModel], Computed()] = []

class PdfFilesResource:
    singular_name = "pdf_file"
    plural_name = "pdf_files"

    Model = PdfFileModel

    default_page_size = default_page_size

    def create_item(self, *, sha256, bytes_count, pages_count):
        (pdf_file, created) = PdfFile.objects.get_or_create(
            sha256=sha256,
            bytes_count=bytes_count,
            pages_count=pages_count,
        )
        return DjangoOrmWrapper(pdf_file)

    def get_item(self, id):
        try:
            return DjangoOrmWrapper(PdfFile.objects.get(sha256=id))
        except PdfFile.DoesNotExist:
            return None

    def get_page(self, filters, first_index, page_size):
        pdf_files = PdfFile.objects.all()
        return (
            # @todo Use proper SQL counting
            len(pdf_files),
            # @todo Use proper SQL limits
            [DjangoOrmWrapper(pdf_file) for pdf_file in pdf_files[first_index:first_index + page_size]],
        )


class PdfFileNamingModel(BaseModel):
    name: str
    pdf_file: PdfFileModel

class PdfFileNamingsResource:
    singular_name = "pdf_file_naming"
    plural_name = "pdf_file_namings"

    Model = PdfFileNamingModel

    default_page_size = default_page_size

    def create_item(self, *, name, pdf_file):
        (naming, created) = PdfFileNaming.objects.get_or_create(
            name=name,
            pdf_file=unwrap(pdf_file),
        )
        return DjangoOrmWrapper(naming)

    def get_item(self, id):
        try:
            return DjangoOrmWrapper(PdfFileNaming.objects.get(id=id))
        except PdfFileNaming.DoesNotExist:
            return None

    def get_page(self, filters, first_index, page_size):
        namings = PdfFileNaming.objects.all()
        return (
            # @todo Use proper SQL counting
            len(namings),
            # @todo Use proper SQL limits
            [DjangoOrmWrapper(naming) for naming in namings[first_index:first_index + page_size]],
        )


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
        project = Project.objects.create(
            title=title,
            description=description,
        )
        return DjangoOrmWrapper(project)

    def get_item(self, id):
        try:
            return DjangoOrmWrapper(Project.objects.get(id=id))
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
    exercises: Annotated[list[ExerciseModel], Computed()] = []
    sections: Annotated[list[SectionModel], Computed()] = []

class TextbooksResource:
    singular_name = "textbook"
    plural_name = "textbooks"

    Model = TextbookModel

    default_page_size = default_page_size

    def create_item(self, *, title, publisher, year, isbn, project):
        textbook = Textbook.objects.create(
            title=title,
            publisher=publisher,
            year=year,
            isbn=isbn,
            project=unwrap(project),
        )
        return DjangoOrmWrapper(textbook)

    def get_item(self, id):
        try:
            return DjangoOrmWrapper(Textbook.objects.get(id=id))
        except Textbook.DoesNotExist:
            return None

    def get_page(self, filters, first_index, page_size):
        textbooks = Textbook.objects.all()
        return (
            # @todo Use proper SQL counting
            len(textbooks),
            # @todo Use proper SQL limits
            [DjangoOrmWrapper(textbook) for textbook in textbooks[first_index:first_index + page_size]],
        )


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

    def create_item(self, *, textbook_start_page, pdf_file_start_page, pages_count, textbook, pdf_file):
        section = Section.objects.create(
            textbook_start_page=textbook_start_page,
            pdf_file_start_page=pdf_file_start_page,
            pages_count=pages_count,
            textbook=unwrap(textbook),
            pdf_file=unwrap(pdf_file),
        )
        return DjangoOrmWrapper(section)

    def get_item(self, id):
        try:
            return DjangoOrmWrapper(Section.objects.get(id=id))
        except Section.DoesNotExist:
            return None

    def get_page(self, filters, first_index, page_size):
        sections = Section.objects.all()
        return (
            # @todo Use proper SQL counting
            len(sections),
            # @todo Use proper SQL limits
            [DjangoOrmWrapper(section) for section in sections[first_index:first_index + page_size]],
        )


class ExerciseModel(BaseModel):
    textbook_page: Annotated[int | None, Filterable()] = None
    number: str
    instructions: str = ""
    example: str = ""
    clue: str = ""
    wording: str = ""
    project: ProjectModel
    textbook: Annotated[TextbookModel | None, Filterable()] = None
    extraction_events: Annotated[list[ExtractionEventModel], Computed()] = []

class ExercisesResource:
    singular_name = "exercise"
    plural_name = "exercises"

    Model = ExerciseModel

    default_page_size = default_page_size

    def create_item(self, *, textbook_page, number, instructions, example, clue, wording, project, textbook):
        exercise = Exercise.objects.create(
            textbook_page=textbook_page,
            number=number,
            instructions=instructions,
            example=example,
            clue=clue,
            wording=wording,
            project=unwrap(project),
            textbook=unwrap(textbook),
        )
        return DjangoOrmWrapper(exercise)

    def get_item(self, id):
        try:
            return DjangoOrmWrapper(Exercise.objects.get(id=id))
        except Exercise.DoesNotExist:
            return None

    def get_page(self, filters, first_index, page_size):
        exercises = Exercise.objects.all()
        # @todo Use proper SQL filtering
        if filters.textbook_page:
            exercises = [exercise for exercise in exercises if exercise.textbook_page == filters.textbook_page]
        if filters.textbook:
            exercises = [exercise for exercise in exercises if exercise.textbook is not None and str(exercise.textbook.id) == filters.textbook]

        return (
            # @todo Use proper SQL counting
            len(exercises),
            # @todo Use proper SQL limits
            [DjangoOrmWrapper(exercise) for exercise in exercises[first_index:first_index + page_size]],
        )


class ExtractionEventModel(BaseModel):
    event: str
    exercise: ExerciseModel

class ExtractionEventsResource:
    singular_name = "extraction_event"
    plural_name = "extraction_events"

    Model = ExtractionEventModel

    default_page_size = default_page_size

    def create_item(self, *, event, exercise):
        e = ExtractionEvent.objects.create(
            event=event,
            exercise=unwrap(exercise),
        )
        return DjangoOrmWrapper(e)

    def get_item(self, id):
        try:
            return DjangoOrmWrapper(ExtractionEvent.objects.get(id=id))
        except ExtractionEvent.DoesNotExist:
            return None

    def get_page(self, filters, first_index, page_size):
        events = ExtractionEvent.objects.all()
        return (
            # @todo Use proper SQL counting
            len(events),
            # @todo Use proper SQL limits
            [DjangoOrmWrapper(event) for event in events[first_index:first_index + page_size]],
        )
