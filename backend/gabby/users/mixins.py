import datetime

from sqlalchemy import orm
import sqlalchemy as sql

from .user import User


class CreatedByAtMixin:
    @orm.declared_attr
    def created_at(self) -> orm.Mapped[datetime.datetime]:
        return orm.mapped_column(sql.DateTime(timezone=True), server_default=sql.func.now())

    @orm.declared_attr
    def created_by_id(self) -> orm.Mapped[int | None]:
        return orm.mapped_column(sql.ForeignKey("users.id"))

    @orm.declared_attr
    def created_by(self) -> orm.Mapped[User | None]:
        return orm.relationship(foreign_keys=[self.created_by_id])


class UpdatedByAtMixin:
    @orm.declared_attr
    def updated_at(self) -> orm.Mapped[datetime.datetime]:
        return orm.mapped_column(sql.DateTime(timezone=True), server_default=sql.func.now(), onupdate=sql.func.now())

    @orm.declared_attr
    def updated_by_id(self) -> orm.Mapped[int | None]:
        return orm.mapped_column(sql.ForeignKey("users.id"))

    @orm.declared_attr
    def updated_by(self) -> orm.Mapped[User | None]:
        return orm.relationship(foreign_keys=[self.updated_by_id])


class CreatedUpdatedByAtMixin(CreatedByAtMixin, UpdatedByAtMixin):
    pass
