from contextlib import contextmanager

from fastapi import HTTPException
from sqlalchemy import orm
import sqlalchemy as sql

from . import api_models
from . import settings
from .api_utils import create_item, get_item, get_page, save_item, delete_item
from .database_utils import OrmBase, SessionDependable
from .users import MandatoryAuthBearerDependable
from .users.mixins import CreatedByAtMixin
from .wrapping import wrap, set_wrapper, OrmWrapper, make_sqids, orm_wrapper_with_sqids


class PdfFile(OrmBase, CreatedByAtMixin):
    __tablename__ = "pdf_files"

    __table_args__ = (sql.CheckConstraint("regexp_like(sha256, '^[0-9a-f]{64}$')", name="check_sha256_format"),)

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

    def create_item(self, sha256, bytes_count, pages_count, session: SessionDependable, authenticated_user: MandatoryAuthBearerDependable):
        pdf_file = PdfFile(sha256=sha256, bytes_count=bytes_count, pages_count=pages_count, created_by=authenticated_user)
        with session.begin_nested() as nested:
            session.add(pdf_file)
            try:
                session.flush()
            except sql.exc.IntegrityError as e:
                if e.orig.diag.constraint_name == "pdf_files_pkey":
                    nested.rollback()
                else:
                    raise HTTPException(status_code=400, detail=e.orig.diag.constraint_name)
            else:
                return wrap(pdf_file)
        return get_item(session, PdfFile, sha256)

    def get_item(self, id, session: SessionDependable, authenticated_user: MandatoryAuthBearerDependable):
        return get_item(session, PdfFile, id)

    def get_page(self, first_index, page_size, session: SessionDependable, authenticated_user: MandatoryAuthBearerDependable):
        query = sql.select(PdfFile)
        return get_page(session, query, first_index, page_size)

    @contextmanager
    def save_item(self, item, session: SessionDependable, authenticated_user: MandatoryAuthBearerDependable):
        yield
        item.updated_by = authenticated_user
        save_item(session, item)

    def delete_item(self, item, session: SessionDependable, authenticated_user: MandatoryAuthBearerDependable):
        delete_item(session, item)


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

    def create_item(self, pdf_file, name, session: SessionDependable, authenticated_user: MandatoryAuthBearerDependable):
        return create_item(session, PdfFileNaming, pdf_file=pdf_file, name=name, created_by=authenticated_user)

    def get_item(self, id, session: SessionDependable, authenticated_user: MandatoryAuthBearerDependable):
        return get_item(session, PdfFileNaming, PdfFileNamingsResource.sqids.decode(id)[0])

    def get_page(self, first_index, page_size, session: SessionDependable, authenticated_user: MandatoryAuthBearerDependable):
        query = sql.select(PdfFileNaming)
        return get_page(session, query, first_index, page_size)

    @contextmanager
    def save_item(self, item, session: SessionDependable, authenticated_user: MandatoryAuthBearerDependable):
        yield
        item.updated_by = authenticated_user
        save_item(session, item)

    def delete_item(self, item, session: SessionDependable, authenticated_user: MandatoryAuthBearerDependable):
        delete_item(session, item)


set_wrapper(PdfFileNaming, orm_wrapper_with_sqids(PdfFileNamingsResource.sqids))
