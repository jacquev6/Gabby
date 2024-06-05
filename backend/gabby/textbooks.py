from sqlalchemy import orm
import sqlalchemy as sql

from .database_utils import OrmBase

from .pdfs import PdfFile
from .projects import Project


class Textbook(OrmBase):
    __tablename__ = "textbooks"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    project_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Project.id))
    project: orm.Mapped[Project] = orm.relationship()

    title: orm.Mapped[str | None]
    publisher: orm.Mapped[str | None]
    year: orm.Mapped[int | None]
    isbn: orm.Mapped[str | None]


class Section(OrmBase):
    __tablename__ = "sections"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    textbook_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Textbook.id))
    textbook: orm.Mapped[Textbook] = orm.relationship()
    pdf_file_sha256: orm.Mapped[str] = orm.mapped_column(sql.ForeignKey(PdfFile.sha256))
    pdf_file: orm.Mapped[PdfFile] = orm.relationship()

    textbook_start_page: orm.Mapped[int]
    pdf_file_start_page: orm.Mapped[int]
    pages_count: orm.Mapped[int]
