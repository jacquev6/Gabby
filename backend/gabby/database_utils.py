from fastapi import Request
import sqlalchemy
from sqlalchemy import orm


Engine = sqlalchemy.Engine
Session = orm.Session


class OrmBase(orm.DeclarativeBase):
    pass


def create_engine(url):
    return sqlalchemy.create_engine(
        url,
        # echo=True,
    )


def drop_tables(engine):
    OrmBase.metadata.drop_all(engine)


def create_tables(engine):
    OrmBase.metadata.create_all(engine)


def session_dependable(request: Request):
    with orm.Session(request.app.extra["database_engine"]) as session:
        try:
            yield session
        except:
            session.rollback()
            raise
        else:
            session.commit()
