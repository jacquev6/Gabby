from contextlib import contextmanager

from fastapi import HTTPException
from sqlalchemy import orm
import sqlalchemy as sql

from . import settings
from .api_models import TextbookModel, SectionModel
from .database_utils import OrmBase, SessionDependent, make_item_creator, make_item_deleter, make_item_getter, make_item_saver, make_page_getter
from .pdfs import PdfFile
from .projects import Project
from .wrapping import wrap, unwrap, set_wrapper, make_sqids, orm_wrapper_with_sqids


class Textbook(OrmBase):
    __tablename__ = "textbooks"

    __table_args__ = (
        sql.CheckConstraint("regexp_like(isbn, '^[0-9]+$')", name="check_isbn_format"),
    )

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    project_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Project.id))
    project: orm.Mapped[Project] = orm.relationship(back_populates="textbooks")

    title: orm.Mapped[str | None]
    publisher: orm.Mapped[str | None]  # De-normalized
    year: orm.Mapped[int | None]
    isbn: orm.Mapped[str | None]

    sections: orm.Mapped[list["Section"]] = orm.relationship(back_populates="textbook")
    exercises: orm.Mapped[list["Exercise"]] = orm.relationship(back_populates="textbook", cascade="all, delete-orphan")


class TextbooksResource:
    singular_name = "textbook"
    plural_name = "textbooks"

    Model = TextbookModel

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    ItemCreator = make_item_creator(Textbook)

    ItemGetter = make_item_getter(Textbook, sqids=sqids)

    PageGetter = make_page_getter(Textbook)

    ItemSaver = make_item_saver()

    ItemDeleter = make_item_deleter()


set_wrapper(Textbook, orm_wrapper_with_sqids(TextbooksResource.sqids))


class Section(OrmBase):
    __tablename__ = "sections"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    textbook_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Textbook.id))
    textbook: orm.Mapped[Textbook] = orm.relationship(back_populates="sections")
    pdf_file_sha256: orm.Mapped[str] = orm.mapped_column(sql.ForeignKey(PdfFile.sha256))
    pdf_file: orm.Mapped[PdfFile] = orm.relationship(back_populates="sections")

    textbook_start_page: orm.Mapped[int]
    pdf_file_start_page: orm.Mapped[int]
    pages_count: orm.Mapped[int]


class SectionsResource:
    singular_name = "section"
    plural_name = "sections"

    Model = SectionModel

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    ItemCreator = make_item_creator(Section)

    ItemGetter = make_item_getter(Section, sqids=sqids)

    PageGetter = make_page_getter(Section)

    ItemSaver = make_item_saver()

    ItemDeleter = make_item_deleter()


set_wrapper(Section, orm_wrapper_with_sqids(SectionsResource.sqids))
