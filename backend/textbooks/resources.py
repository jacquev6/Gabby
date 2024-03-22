from __future__ import annotations
from typing import Annotated

from django.core.exceptions import ValidationError
from fastapi import HTTPException
from pydantic import BaseModel
import django.conf

from .models import PdfFile, PdfFileNaming, Project, Textbook, Section, Exercise, ExtractionEvent
from fastjsonapi import Computed, Filterable, Constant
from fastjsonapi.django import wrap, unwrap


default_page_size = django.conf.settings.REST_FRAMEWORK["PAGE_SIZE"]


class PdfFileModel(BaseModel):
    sha256: Annotated[str, Constant()]
    bytes_count: Annotated[int, Constant()]
    pages_count: Annotated[int, Constant()]
    namings: Annotated[list[PdfFileNamingModel], Computed()] = []
    sections: Annotated[list[SectionModel], Computed()] = []

class PdfFilesResource:
    singular_name = "pdf_file"
    plural_name = "pdf_files"

    Model = PdfFileModel

    default_page_size = default_page_size

    def create_item(self, *, sha256, bytes_count, pages_count):
        pdf_file = PdfFile(
            sha256=sha256,
            bytes_count=bytes_count,
            pages_count=pages_count,
        )
        try:
            pdf_file.full_clean(validate_unique=False)
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=e.message_dict)
        pdf_file.save()
        return wrap(pdf_file)

    def get_item(self, id):
        try:
            return wrap(PdfFile.objects.get(sha256=id))
        except PdfFile.DoesNotExist:
            # @todo Raise the 404 here instead of 'fastjsonapi.router' (for all resources)
            return None

    def get_page(self, sort, filters, first_index, page_size):
        sort = sort or ["sha256"]
        pdf_files = PdfFile.objects.order_by(*sort)

        return (
            # @todo Use proper SQL counting
            len(pdf_files),
            # @todo Use proper SQL limits
            [wrap(pdf_file) for pdf_file in pdf_files[first_index:first_index + page_size]],
        )


class PdfFileNamingModel(BaseModel):
    name: Annotated[str, Constant()]
    pdf_file: Annotated[PdfFileModel, Constant()]

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
        return wrap(naming)

    def get_item(self, id):
        try:
            return wrap(PdfFileNaming.objects.get(id=id))
        except PdfFileNaming.DoesNotExist:
            return None

    def get_page(self, sort, filters, first_index, page_size):
        sort = sort or ["id"]
        namings = PdfFileNaming.objects.order_by(*sort)

        return (
            # @todo Use proper SQL counting
            len(namings),
            # @todo Use proper SQL limits
            [wrap(naming) for naming in namings[first_index:first_index + page_size]],
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
        return wrap(project)

    def get_item(self, id):
        try:
            return wrap(Project.objects.get(id=id))
        except Project.DoesNotExist:
            return None

    def get_page(self, sort, filters, first_index, page_size):
        sort = sort or ["id"]
        projects = Project.objects.order_by(*sort)

        return (
            # @todo Use proper SQL counting
            len(projects),
            # @todo Use proper SQL limits
            [wrap(project) for project in projects[first_index:first_index + page_size]],
        )


class TextbookModel(BaseModel):
    title: str
    publisher: str | None = None
    year: int | None = None
    isbn: str | None = None
    project: Annotated[ProjectModel, Constant()]
    exercises: Annotated[list[ExerciseModel], Computed()] = []
    sections: Annotated[list[SectionModel], Computed()] = []

class TextbooksResource:
    singular_name = "textbook"
    plural_name = "textbooks"

    Model = TextbookModel

    default_page_size = default_page_size

    def create_item(self, *, title, publisher, year, isbn, project):
        textbook = Textbook(
            title=title,
            publisher=publisher,
            year=year,
            isbn=isbn,
            project=unwrap(project),
        )
        try:
            textbook.full_clean()
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=e.message_dict)
        textbook.save()
        return wrap(textbook)

    def get_item(self, id):
        try:
            return wrap(Textbook.objects.get(id=id))
        except Textbook.DoesNotExist:
            return None

    def get_page(self, sort, filters, first_index, page_size):
        sort = sort or ["id"]
        textbooks = Textbook.objects.order_by(*sort)

        return (
            # @todo Use proper SQL counting
            len(textbooks),
            # @todo Use proper SQL limits
            [wrap(textbook) for textbook in textbooks[first_index:first_index + page_size]],
        )


class SectionModel(BaseModel):
    textbook_start_page: int
    pdf_file_start_page: int
    pages_count: int
    textbook: Annotated[TextbookModel, Constant()]
    pdf_file: Annotated[PdfFileModel, Constant()]

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
        return wrap(section)

    def get_item(self, id):
        try:
            return wrap(Section.objects.get(id=id))
        except Section.DoesNotExist:
            return None

    def get_page(self, sort, filters, first_index, page_size):
        sort = sort or ["id"]
        sections = Section.objects.order_by(*sort)

        return (
            # @todo Use proper SQL counting
            len(sections),
            # @todo Use proper SQL limits
            [wrap(section) for section in sections[first_index:first_index + page_size]],
        )


class ExerciseModel(BaseModel):
    textbook_page: Annotated[int | None, Filterable(), Constant()] = None
    number: Annotated[str, Constant()]
    instructions: str = ""
    example: str = ""
    clue: str = ""
    wording: str = ""
    project: Annotated[ProjectModel, Constant()]
    textbook: Annotated[TextbookModel | None, Filterable(), Constant()] = None
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
        return wrap(exercise)

    def get_item(self, id):
        try:
            return wrap(Exercise.objects.get(id=id))
        except Exercise.DoesNotExist:
            return None

    def get_page(self, sort, filters, first_index, page_size):
        sort = sort or ["textbook", "textbook_page", "number"]
        exercises = Exercise.objects.order_by(*sort)

        # @todo Use proper SQL filtering
        if filters.textbook_page:
            exercises = [exercise for exercise in exercises if exercise.textbook_page == filters.textbook_page]
        if filters.textbook:
            exercises = [exercise for exercise in exercises if exercise.textbook is not None and str(exercise.textbook.id) == filters.textbook]

        return (
            # @todo Use proper SQL counting
            len(exercises),
            # @todo Use proper SQL limits
            [wrap(exercise) for exercise in exercises[first_index:first_index + page_size]],
        )


class ExtractionEventModel(BaseModel):
    event: Annotated[str, Constant()]
    exercise: Annotated[ExerciseModel, Constant()]

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
        return wrap(e)

    def get_item(self, id):
        try:
            return wrap(ExtractionEvent.objects.get(id=id))
        except ExtractionEvent.DoesNotExist:
            return None

    def get_page(self, sort, filters, first_index, page_size):
        sort = sort or ["id"]
        events = ExtractionEvent.objects.order_by(*sort)

        return (
            # @todo Use proper SQL counting
            len(events),
            # @todo Use proper SQL limits
            [wrap(event) for event in events[first_index:first_index + page_size]],
        )
