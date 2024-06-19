from contextlib import contextmanager

from sqlalchemy import orm
import sqlalchemy as sql

from . import api_models
from . import settings
from .database_utils import OrmBase
from .api_utils import make_item_creator, make_item_deleter, make_item_getter, make_item_saver, make_page_getter
from .pdfs import PdfFile
from .projects import Project
from .users.mixins import CreatedUpdatedByAtMixin
from .wrapping import wrap, unwrap, set_wrapper, make_sqids, orm_wrapper_with_sqids


class Textbook(OrmBase, CreatedUpdatedByAtMixin):
    __tablename__ = "textbooks"

    __table_args__ = (
        sql.CheckConstraint("regexp_like(isbn, '^[0-9]+$')", name="check_isbn_format"),
        sql.UniqueConstraint("id", "project_id"),  # Redondant ('id' is unique by itself), but required for the foreign key in 'Exercise'
    )

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    project_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Project.id))
    project: orm.Mapped[Project] = orm.relationship(back_populates="textbooks")

    title: orm.Mapped[str | None]
    publisher: orm.Mapped[str | None]  # De-normalized
    year: orm.Mapped[int | None]
    isbn: orm.Mapped[str | None]

    sections: orm.Mapped[list["Section"]] = orm.relationship(back_populates="textbook")
    exercises: orm.Mapped[list["Exercise"]] = orm.relationship(back_populates="textbook", cascade="all, delete-orphan", overlaps="exercises")


class TextbooksResource:
    singular_name = "textbook"
    plural_name = "textbooks"

    Model = api_models.Textbook

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    ItemCreator = make_item_creator(Textbook)

    ItemGetter = make_item_getter(Textbook, sqids=sqids)

    PageGetter = make_page_getter(Textbook)

    ItemSaver = make_item_saver()

    ItemDeleter = make_item_deleter()


set_wrapper(Textbook, orm_wrapper_with_sqids(TextbooksResource.sqids))


class Section(OrmBase, CreatedUpdatedByAtMixin):
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

    Model = api_models.Section

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    ItemCreator = make_item_creator(Section)

    ItemGetter = make_item_getter(Section, sqids=sqids)

    PageGetter = make_page_getter(Section)

    ItemSaver = make_item_saver()

    ItemDeleter = make_item_deleter()


set_wrapper(Section, orm_wrapper_with_sqids(SectionsResource.sqids))
