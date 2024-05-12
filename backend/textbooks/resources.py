from __future__ import annotations
from contextlib import contextmanager
import dataclasses
from typing import Annotated
import uuid

from django.core.exceptions import ValidationError
from fastapi import HTTPException
from pydantic import BaseModel
import django.conf

from . import renderable
from .models import PdfFile, PdfFileNaming, Project, Textbook, Section, Exercise, ExtractionEvent
from .models import SelectThingsAdaptation, FillWithFreeTextAdaptation
from fastjsonapi import Computed, Filterable, Constant, Secret as WriteOnly
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

    class ItemCreator:
        def __call__(self, *, sha256, bytes_count, pages_count):
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

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(PdfFile.objects.get(sha256=id))
            except PdfFile.DoesNotExist:
                # @todo Raise the 404 here instead of 'fastjsonapi.router' (for all resources)
                return None

    class PageGetter:
        def __call__(self, sort, filters, first_index, page_size):
            sort = sort or ["sha256"]
            pdf_files = PdfFile.objects.order_by(*sort)

            return (
                # @todo Use proper SQL counting
                len(pdf_files),
                # @todo Use proper SQL limits
                [wrap(pdf_file) for pdf_file in pdf_files[first_index:first_index + page_size]],
            )

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            yield
            item.save()

    class ItemDeleter:
        def __call__(self, item):
            item.delete()


class PdfFileNamingModel(BaseModel):
    name: Annotated[str, Constant()]
    pdf_file: Annotated[PdfFileModel, Constant()]

class PdfFileNamingsResource:
    singular_name = "pdf_file_naming"
    plural_name = "pdf_file_namings"

    Model = PdfFileNamingModel

    default_page_size = default_page_size

    class ItemCreator:
        def __call__(self, *, name, pdf_file):
            (naming, created) = PdfFileNaming.objects.get_or_create(
                name=name,
                pdf_file=unwrap(pdf_file),
            )
            return wrap(naming)

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(PdfFileNaming.objects.get(id=id))
            except PdfFileNaming.DoesNotExist:
                return None

    class PageGetter:
        def __call__(self, sort, filters, first_index, page_size):
            sort = sort or ["id"]
            namings = PdfFileNaming.objects.order_by(*sort)

            return (
                # @todo Use proper SQL counting
                len(namings),
                # @todo Use proper SQL limits
                [wrap(naming) for naming in namings[first_index:first_index + page_size]],
            )

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            yield
            item.save()

    class ItemDeleter:
        def __call__(self, item):
            item.delete()


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

    class ItemCreator:
        def __call__(self, *, title, description):
            project = Project.objects.create(
                title=title,
                description=description,
            )
            return wrap(project)

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(Project.objects.get(id=id))
            except Project.DoesNotExist:
                return None

    class PageGetter:
        def __call__(self, sort, filters, first_index, page_size):
            sort = sort or ["id"]
            projects = Project.objects.order_by(*sort)

            return (
                # @todo Use proper SQL counting
                len(projects),
                # @todo Use proper SQL limits
                [wrap(project) for project in projects[first_index:first_index + page_size]],
            )

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            yield
            item.save()

    class ItemDeleter:
        def __call__(self, item):
            item.delete()


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

    class ItemCreator:
        def __call__(self, *, title, publisher, year, isbn, project):
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

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(Textbook.objects.get(id=id))
            except Textbook.DoesNotExist:
                return None

    class PageGetter:
        def __call__(self, sort, filters, first_index, page_size):
            sort = sort or ["id"]
            textbooks = Textbook.objects.order_by(*sort)

            return (
                # @todo Use proper SQL counting
                len(textbooks),
                # @todo Use proper SQL limits
                [wrap(textbook) for textbook in textbooks[first_index:first_index + page_size]],
            )

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            yield
            item.save()

    class ItemDeleter:
        def __call__(self, item):
            item.delete()


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

    class ItemCreator:
        def __call__(self, *, textbook_start_page, pdf_file_start_page, pages_count, textbook, pdf_file):
            section = Section.objects.create(
                textbook_start_page=textbook_start_page,
                pdf_file_start_page=pdf_file_start_page,
                pages_count=pages_count,
                textbook=unwrap(textbook),
                pdf_file=unwrap(pdf_file),
            )
            return wrap(section)

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(Section.objects.get(id=id))
            except Section.DoesNotExist:
                return None

    class PageGetter:
        def __call__(self, sort, filters, first_index, page_size):
            sort = sort or ["id"]
            sections = Section.objects.order_by(*sort)

            return (
                # @todo Use proper SQL counting
                len(sections),
                # @todo Use proper SQL limits
                [wrap(section) for section in sections[first_index:first_index + page_size]],
            )

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            yield
            item.save()

    class ItemDeleter:
        def __call__(self, item):
            item.delete()


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

    adaptation: SelectThingsAdaptationModel | FillWithFreeTextAdaptationModel | None = None

class ExercisesResource:
    singular_name = "exercise"
    plural_name = "exercises"

    Model = ExerciseModel

    default_page_size = default_page_size

    class ItemCreator:
        def __call__(
            self,
            *,
            project,
            textbook,
            textbook_page,
            bounding_rectangle,
            number,
            instructions,
            wording,
            example,
            clue,
            adaptation,
        ):
            if bounding_rectangle:
                bounding_rectangle = bounding_rectangle.model_dump()
            exercise = Exercise.objects.create(
                project=unwrap(project),
                textbook=unwrap(textbook),
                textbook_page=textbook_page,
                bounding_rectangle=bounding_rectangle,
                number=number,
                instructions=instructions,
                wording=wording,
                example=example,
                clue=clue,
                adaptation=unwrap(adaptation),
            )
            return wrap(exercise)

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(Exercise.objects.get(id=id))
            except Exercise.DoesNotExist:
                return None

    class PageGetter:
        def __call__(self, sort, filters, first_index, page_size):
            sort = sort or ["textbook", "textbook_page", "number"]
            exercises = Exercise.objects.order_by(*sort)

            # @todo Use proper SQL filtering
            if filters.textbook_page:
                exercises = [exercise for exercise in exercises if exercise.textbook_page == filters.textbook_page]
            if filters.textbook:
                exercises = [exercise for exercise in exercises if exercise.textbook is not None and str(exercise.textbook.id) == filters.textbook]
            if filters.number:
                exercises = [exercise for exercise in exercises if exercise.number == filters.number]

            return (
                # @todo Use proper SQL counting
                len(exercises),
                # @todo Use proper SQL limits
                [wrap(exercise) for exercise in exercises[first_index:first_index + page_size]],
            )

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            previous_adaptation = item.adaptation
            previous_bounding_rectangle = item.bounding_rectangle
            yield
            if item.bounding_rectangle is not previous_bounding_rectangle and item.bounding_rectangle is not None:
                item.bounding_rectangle = item.bounding_rectangle.model_dump()
            item.save()
            if previous_adaptation is not None and unwrap(item.adaptation) != unwrap(previous_adaptation):
                previous_adaptation.delete()

    class ItemDeleter:
        def __call__(self, item):
            item.delete()


class ExtractionEventModel(BaseModel):
    event: Annotated[str, Constant()]
    exercise: Annotated[ExerciseModel, Constant()]

class ExtractionEventsResource:
    singular_name = "extraction_event"
    plural_name = "extraction_events"

    Model = ExtractionEventModel

    default_page_size = default_page_size

    class ItemCreator:
        def __call__(self, *, event, exercise):
            e = ExtractionEvent.objects.create(
                event=event,
                exercise=unwrap(exercise),
            )
            return wrap(e)

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(ExtractionEvent.objects.get(id=id))
            except ExtractionEvent.DoesNotExist:
                return None

    class PageGetter:
        def __call__(self, sort, filters, first_index, page_size):
            sort = sort or ["id"]
            events = ExtractionEvent.objects.order_by(*sort)

            return (
                # @todo Use proper SQL counting
                len(events),
                # @todo Use proper SQL limits
                [wrap(event) for event in events[first_index:first_index + page_size]],
            )

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            yield
            item.save()

    class ItemDeleter:
        def __call__(self, item):
            item.delete()


class SelectThingsAdaptationOptionsModel(BaseModel):
    colors: int
    words: bool
    punctuation: bool

class SelectThingsAdaptationModel(SelectThingsAdaptationOptionsModel):
    exercise: Annotated[ExerciseModel, Constant()]

class SelectThingsAdaptationsResource:
    singular_name = "select_things_adaptation"
    plural_name = "select_things_adaptations"

    Model = SelectThingsAdaptationModel

    default_page_size = default_page_size

    class ItemCreator:
        def __call__(self, *, exercise, colors, words, punctuation):
            if exercise.adaptation is not None:
                exercise.adaptation.delete()
            adaptation = SelectThingsAdaptation(
                exercise=unwrap(exercise),
                colors=colors,
                words=words,
                punctuation=punctuation,
            )
            adaptation.save()
            exercise.save()
            return wrap(adaptation)

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(SelectThingsAdaptation.objects.get(id=id))
            except SelectThingsAdaptation.DoesNotExist:
                return None

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            yield
            item.save()

    class ItemDeleter:
        def __call__(self, item):
            item.delete()


class FillWithFreeTextAdaptationOptionsModel(BaseModel):
    placeholder: str

class FillWithFreeTextAdaptationModel(FillWithFreeTextAdaptationOptionsModel):
    exercise: Annotated[ExerciseModel, Constant()]

class FillWithFreeTextAdaptationsResource:
    singular_name = "fill_with_free_text_adaptation"
    plural_name = "fill_with_free_text_adaptations"

    Model = FillWithFreeTextAdaptationModel

    default_page_size = default_page_size

    class ItemCreator:
        def __call__(self, *, exercise, placeholder):
            if exercise.adaptation is not None:
                exercise.adaptation.delete()
            adaptation = FillWithFreeTextAdaptation(
                exercise=unwrap(exercise),
                placeholder=placeholder,
            )
            adaptation.save()
            exercise.save()
            return wrap(adaptation)

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(FillWithFreeTextAdaptation.objects.get(id=id))
            except FillWithFreeTextAdaptation.DoesNotExist:
                return None

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            yield
            item.save()

    class ItemDeleter:
        def __call__(self, item):
            item.delete()


class AdaptedExerciseModel(BaseModel):
    number: Annotated[str, WriteOnly()]
    textbookPage: Annotated[int | None, WriteOnly()]
    instructions: Annotated[str, WriteOnly()]
    wording: Annotated[str, WriteOnly()]
    type: Annotated[str, WriteOnly()]
    adaptation_options: Annotated[SelectThingsAdaptationOptionsModel | FillWithFreeTextAdaptationOptionsModel, WriteOnly()]
    adapted: Annotated[renderable.AdaptedExercise, Computed()]

@dataclasses.dataclass
class AdaptedExerciseItem:
    id: str
    adapted: renderable.AdaptedExercise

class AdaptedExerciseResource:
    singular_name = "adapted_exercise"
    plural_name = "adapted_exercises"

    Model = AdaptedExerciseModel

    default_page_size = default_page_size

    class ItemCreator:
        def __call__(self, *, number, textbook_page, instructions, wording, type, adaptation_options):
            exercise = Exercise(
                number=number,
                textbook_page=textbook_page,
                instructions=instructions,
                wording=wording,
            )
            if type == "selectThingsAdaptation":
                adapted = SelectThingsAdaptation(
                    exercise=exercise,
                    **adaptation_options.model_dump(),
                )
            elif type == "fillWithFreeTextAdaptation":
                adapted = FillWithFreeTextAdaptation(
                    exercise=exercise,
                    **adaptation_options.model_dump(),
                )
            else:
                raise HTTPException(status_code=400, detail="Unknown type")
            return AdaptedExerciseItem(
                id=uuid.uuid4().hex,
                adapted=adapted.make_adapted(),
            )

    class ItemGetter:
        def __call__(self, id):
            return None
