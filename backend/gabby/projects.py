from sqlalchemy import orm

from .database_utils import OrmBase


class Project(OrmBase):
    __tablename__ = "projects"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    title: orm.Mapped[str]
    description: orm.Mapped[str]
