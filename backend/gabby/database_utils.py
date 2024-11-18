from typing import Annotated
from fastapi import Depends, Request
from sqlalchemy import orm
import sqlalchemy
import sqlalchemy as sql


Engine = sqlalchemy.Engine
Session = orm.Session


# Custom collation: https://dba.stackexchange.com/a/285230
sql_create_exercise_number_collation = sql.text("CREATE COLLATION exercise_number (provider = icu, locale = 'en-u-kn-true')")
sql_drop_exercise_number_collation = sql.text("DROP COLLATION exercise_number")


class OrmBase(orm.DeclarativeBase):
    pass
    # @todo Enable a naming convention for constraints
    # https://github.com/sqlalchemy/alembic/issues/588#issuecomment-513232760
    # https://alembic.sqlalchemy.org/en/latest/naming.html
    # https://docs.sqlalchemy.org/en/20/core/constraints.html#configuring-a-naming-convention-for-a-metadata-collection
    # metadata = sql.MetaData(
    #     naming_convention=dict(
    #         ix="ix_%(column_0_label)s",
    #         uq="uq_%(table_name)s_%(column_0_name)s",
    #         ck="ck_%(table_name)s_%(constraint_name)s",
    #         fk="fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    #         pk="pk_%(table_name)s",
    #     ),
    # )


def create_engine(url):
    return sqlalchemy.create_engine(
        url,
        # echo=True,
    )


def truncate_all_tables(session):
    for table in reversed(OrmBase.metadata.sorted_tables):
        session.execute(table.delete())
        if table.name not in ["pdf_files"]:
            session.execute(sql.text(f"ALTER SEQUENCE {table.name}_id_seq RESTART WITH 1"))


class SessionMaker:
    def __init__(self, engine):
        self.__engine = engine

    def __call__(self):
        return orm.Session(self.__engine)


def _session_dependable(request: Request):
    with request.app.extra["make_session"]() as session:
        try:
            yield session
        except:
            session.rollback()
            raise
        else:
            session.commit()


SessionDependable = Annotated[Session, Depends(_session_dependable)]
