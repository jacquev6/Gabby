from sqlalchemy import orm

from . import api_models
from . import settings
from .database_utils import OrmBase, make_item_creator, make_item_deleter, make_item_getter, make_item_saver, make_page_getter
from .wrapping import wrap, set_wrapper, make_sqids, orm_wrapper_with_sqids


class Project(OrmBase):
    __tablename__ = "projects"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    title: orm.Mapped[str]
    description: orm.Mapped[str]

    textbooks: orm.Mapped[list["Textbook"]] = orm.relationship(back_populates="project")
    exercises: orm.Mapped[list["Exercise"]] = orm.relationship(back_populates="project")


class ProjectsResource:
    singular_name = "project"
    plural_name = "projects"

    Model = api_models.Project

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    ItemCreator = make_item_creator(Project)

    ItemGetter = make_item_getter(Project, sqids=sqids)

    PageGetter = make_page_getter(Project)

    ItemSaver = make_item_saver()

    ItemDeleter = make_item_deleter()


set_wrapper(Project, orm_wrapper_with_sqids(ProjectsResource.sqids))
