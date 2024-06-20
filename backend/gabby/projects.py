from contextlib import contextmanager

from sqlalchemy import orm
import sqlalchemy as sql

from . import api_models
from . import settings
from .api_utils import create_item, get_item, get_page, save_item, delete_item
from .database_utils import OrmBase, SessionDependable
from .users import WanabeMandatoryAuthenticatedUserDependable
from .users.mixins import CreatedUpdatedByAtMixin
from .wrapping import set_wrapper, make_sqids, orm_wrapper_with_sqids


class Project(OrmBase, CreatedUpdatedByAtMixin):
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

    @staticmethod
    def ItemCreator(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def create(title, description):
            return create_item(
                session, Project,
                title=title,
                description=description,
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
            return get_item(session, Project, ProjectsResource.sqids.decode(id)[0])
        return get

    @staticmethod
    def PageGetter(
        session: SessionDependable,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        def get(sort, filters, first_index, page_size):
            sort = sort or ("id",)
            query = sql.select(Project).order_by(*sort)
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


set_wrapper(Project, orm_wrapper_with_sqids(ProjectsResource.sqids))
