from contextlib import contextmanager

from sqlalchemy import orm
import sqlalchemy as sql

from . import api_models
from . import settings
from .api_utils import create_item, get_item, get_page, save_item, delete_item
from .database_utils import OrmBase, SessionDependable
from .pdfs import PdfFile
from .projects import Project
from .users import WanabeMandatoryAuthenticatedUserDependable
from .users.mixins import CreatedUpdatedByAtMixin
from .wrapping import set_wrapper, make_sqids, orm_wrapper_with_sqids


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

    @staticmethod
    def ItemCreator(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def create(
            project,
            title,
            publisher,
            year,
            isbn,
        ):
            return create_item(
                session, Textbook,
                project=project,
                title=title,
                publisher=publisher,
                year=year,
                isbn=isbn,
                created_by=authenticated_user,
                updated_by=authenticated_user,
            )
        return create

    @staticmethod
    def ItemGetter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def get(id):
            return get_item(session, Textbook, TextbooksResource.sqids.decode(id)[0])
        return get

    @staticmethod
    def PageGetter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def get(sort, filters, first_index, page_size):
            sort = sort or ("id",)
            query = sql.select(Textbook).order_by(*sort)
            return get_page(session, query, first_index, page_size)
        return get

    @staticmethod
    def ItemSaver(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        @contextmanager
        def save(item):
            yield
            item.updated_by = authenticated_user
            save_item(session, item)
        return save

    @staticmethod
    def ItemDeleter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def delete(item):
            delete_item(session, item)
        return delete


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

    @staticmethod
    def ItemCreator(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def create(
            textbook,
            pdf_file,
            textbook_start_page,
            pdf_file_start_page,
            pages_count,
        ):
            return create_item(
                session, Section,
                textbook=textbook,
                pdf_file=pdf_file,
                textbook_start_page=textbook_start_page,
                pdf_file_start_page=pdf_file_start_page,
                pages_count=pages_count,
                created_by=authenticated_user,
                updated_by=authenticated_user,
            )
        return create

    @staticmethod
    def ItemGetter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def get(id):
            return get_item(session, Section, SectionsResource.sqids.decode(id)[0])
        return get

    @staticmethod
    def PageGetter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def get(sort, filters, first_index, page_size):
            sort = sort or ("id",)
            query = sql.select(Section).order_by(*sort)
            return get_page(session, query, first_index, page_size)
        return get

    @staticmethod
    def ItemSaver(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        @contextmanager
        def save(item):
            yield
            item.updated_by = authenticated_user
            save_item(session, item)
        return save

    @staticmethod
    def ItemDeleter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def delete(item):
            delete_item(session, item)
        return delete


set_wrapper(Section, orm_wrapper_with_sqids(SectionsResource.sqids))