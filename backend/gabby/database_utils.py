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


def create_engine(url):
    return sqlalchemy.create_engine(
        url,
        # echo=True,
    )


def truncate_all_tables(session):
    for table in reversed(OrmBase.metadata.sorted_tables):
        session.execute(table.delete())
        if table.name not in ["pdf_files", "adaptations__st", "adaptations__g", "adaptations__fwft", "adaptations__mcii", "adaptations__mciw"]:
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
