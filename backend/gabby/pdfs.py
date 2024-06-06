from contextlib import contextmanager

from fastapi import HTTPException
from sqlalchemy import orm
import sqlalchemy as sql

from . import settings
from .api_models import PdfFileModel, PdfFileNamingModel
from .database_utils import OrmBase, SessionDependent, make_item_creator, make_item_deleter, make_item_getter, make_item_saver, make_page_getter
from .wrapping import wrap, set_wrapper, OrmWrapper, make_sqids, orm_wrapper_with_sqids


class PdfFile(OrmBase):
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

    Model = PdfFileModel

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    class ItemCreator(SessionDependent):
        def __call__(self, *, sha256, bytes_count, pages_count):
            pdf_file = PdfFile(sha256=sha256, bytes_count=bytes_count, pages_count=pages_count)
            self.session.add(pdf_file)

            try:
                self.session.commit()
            except sql.exc.IntegrityError as e:
                if e.orig.diag.constraint_name == "pdf_files_pkey":
                    self.session.rollback()
                    pdf_file = self.session.get(PdfFile, sha256)
                else:
                    raise HTTPException(status_code=400, detail=e.orig.diag.constraint_name)

            return wrap(pdf_file)

    ItemGetter = make_item_getter(PdfFile)

    PageGetter = make_page_getter(PdfFile)

    ItemSaver = make_item_saver()

    ItemDeleter = make_item_deleter()


class PdfFileWrapper(OrmWrapper):
    @property
    def id(self):
        return self.sha256


set_wrapper(PdfFile, PdfFileWrapper)


class PdfFileNaming(OrmBase):
    __tablename__ = "pdf_file_namings"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    pdf_file_sha256: orm.Mapped[str] = orm.mapped_column(sql.ForeignKey(PdfFile.sha256))
    pdf_file: orm.Mapped[PdfFile] = orm.relationship(back_populates="namings")
    name: orm.Mapped[str]


class PdfFileNamingsResource:
    singular_name = "pdf_file_naming"
    plural_name = "pdf_file_namings"

    Model = PdfFileNamingModel

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    ItemCreator = make_item_creator(PdfFileNaming)

    ItemGetter = make_item_getter(PdfFileNaming, sqids=sqids)

    PageGetter = make_page_getter(PdfFileNaming)

    ItemSaver = make_item_saver()

    ItemDeleter = make_item_deleter()


set_wrapper(PdfFileNaming, orm_wrapper_with_sqids(PdfFileNamingsResource.sqids))
