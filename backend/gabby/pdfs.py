from contextlib import contextmanager

from fastapi import HTTPException
from sqlalchemy import orm
import sqlalchemy as sql

from . import api_models
from . import settings
from .api_utils import create_item, get_item, get_page, save_item, delete_item
from .database_utils import OrmBase, SessionDependable
from .users import WanabeMandatoryAuthenticatedUserDependable
from .users.mixins import CreatedByAtMixin
from .wrapping import wrap, set_wrapper, OrmWrapper, make_sqids, orm_wrapper_with_sqids


class PdfFile(OrmBase, CreatedByAtMixin):
    __tablename__ = "pdf_files"

    __table_args__ = (
        sql.CheckConstraint("regexp_like(sha256, '^[0-9a-f]{64}$')", name="check_sha256_format"),
    )

    sha256: orm.Mapped[str] = orm.mapped_column(primary_key=True)
    bytes_count: orm.Mapped[int]
    pages_count: orm.Mapped[int]

    sections: orm.Mapped[list["Section"]] = orm.relationship(back_populates="pdf_file")
    namings: orm.Mapped[list["PdfFileNaming"]] = orm.relationship(back_populates="pdf_file")


class PdfFilesResource:
    singular_name = "pdf_file"
    plural_name = "pdf_files"

    Model = api_models.PdfFile

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    @staticmethod
    def ItemCreator(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def create(sha256, bytes_count, pages_count):
            pdf_file = PdfFile(
                sha256=sha256,
                bytes_count=bytes_count,
                pages_count=pages_count,
                created_by=authenticated_user,
            )
            session.add(pdf_file)
            try:
                session.flush()
            except sql.exc.IntegrityError as e:
                if e.orig.diag.constraint_name == "pdf_files_pkey":
                    session.rollback()
                    return get_item(session, PdfFile, sha256)
                else:
                    raise HTTPException(status_code=400, detail=e.orig.diag.constraint_name)
            return wrap(pdf_file)

        return create

    @staticmethod
    def ItemGetter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def get(id):
            return get_item(session, PdfFile, id)

        return get


    @staticmethod
    def PageGetter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def get(first_index, page_size):
            query = sql.select(PdfFile)
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


class PdfFileWrapper(OrmWrapper):
    @property
    def id(self):
        return self.sha256


set_wrapper(PdfFile, PdfFileWrapper)


class PdfFileNaming(OrmBase, CreatedByAtMixin):
    __tablename__ = "pdf_file_namings"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    pdf_file_sha256: orm.Mapped[str] = orm.mapped_column(sql.ForeignKey(PdfFile.sha256))
    pdf_file: orm.Mapped[PdfFile] = orm.relationship(back_populates="namings")
    name: orm.Mapped[str]


class PdfFileNamingsResource:
    singular_name = "pdf_file_naming"
    plural_name = "pdf_file_namings"

    Model = api_models.PdfFileNaming

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    @staticmethod
    def ItemCreator(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def create(pdf_file, name):
            return create_item(
                session, PdfFileNaming,
                pdf_file=pdf_file,
                name=name,
                created_by=authenticated_user,
            )

        return create

    @staticmethod
    def ItemGetter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def get(id):
            return get_item(session, PdfFileNaming, PdfFileNamingsResource.sqids.decode(id)[0])
        return get


    @staticmethod
    def PageGetter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def get(first_index, page_size):
            query = sql.select(PdfFileNaming)
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


set_wrapper(PdfFileNaming, orm_wrapper_with_sqids(PdfFileNamingsResource.sqids))
