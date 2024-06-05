from sqlalchemy import orm
import sqlalchemy as sql

from .database_utils import OrmBase


class PdfFile(OrmBase):
    __tablename__ = "pdf_files"

    sha256: orm.Mapped[str] = orm.mapped_column(primary_key=True)
    pages_count: orm.Mapped[int]

    sections: orm.Mapped[list["Section"]] = orm.relationship(back_populates="pdf_file")
    namings: orm.Mapped[list["PdfFileNaming"]] = orm.relationship(back_populates="pdf_file")


class PdfFileNaming(OrmBase):
    __tablename__ = "pdf_file_namings"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    pdf_file_sha256: orm.Mapped[str] = orm.mapped_column(sql.ForeignKey(PdfFile.sha256))
    pdf_file: orm.Mapped[PdfFile] = orm.relationship(back_populates="namings")
    name: orm.Mapped[str]
