from contextlib import contextmanager
from fastapi import Depends, HTTPException, Request
from sqlalchemy import orm
import sqlalchemy
import sqlalchemy as sql

from .wrapping import OrmWrapper, unwrap, wrap


Engine = sqlalchemy.Engine
Session = orm.Session


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


def session_dependable(request: Request):
    with orm.Session(request.app.extra["database_engine"]) as session:
        try:
            yield session
        except:
            session.rollback()
            raise
        else:
            session.commit()


class SessionDependent:
    def __init__(self, session: Session = Depends(session_dependable)):
        self.session = session


def make_item_creator(model, *, preprocess=lambda **kwargs: kwargs):
    class ItemCreator(SessionDependent):
        def __call__(self, **kwargs):
            kwargs = {
                key: unwrap(value) if isinstance(value, OrmWrapper) else value
                for key, value in kwargs.items()
            }
            kwargs = {
                key: [unwrap(v) if isinstance(v, OrmWrapper) else v for v in value] if isinstance(value, list) else value
                for key, value in kwargs.items()
            }
            kwargs = preprocess(**kwargs)
            item = model(**kwargs)
            self.session.add(item)
            try:
                self.session.flush()
            except sql.exc.IntegrityError as e:
                raise HTTPException(status_code=400, detail=e.orig.diag.constraint_name)
            return wrap(item)

    return ItemCreator


def make_item_getter(model, *, sqids=None):
    if sqids is None:
        def decode_id(id):
            return id
    else:
        def decode_id(id):
            return sqids.decode(id)[0]

    class ItemGetter(SessionDependent):
        def __call__(self, id):
            return wrap(self.session.get(model, decode_id(id)))

    return ItemGetter


def make_page_getter(
    model,
    *,
    default_sort=("id",),
    filter_functions={},
):
    def add_filters(query, filters):
        for filter_name, filter_function in filter_functions.items():
            if value := getattr(filters, filter_name, None):
                query = filter_function(query, value)
        return query

    class PageGetter(SessionDependent):
        def __call__(self, sort, filters, first_index, page_size):
            sort = sort or default_sort

            count = self.session.scalar(add_filters(sql.select(sql.func.count(model.id)), filters))
            textbooks = [
                wrap(textbook)
                for (textbook,) in self.session.execute(
                    add_filters(sql.select(model), filters)
                        .order_by(*sort)
                        .offset(first_index)
                        .limit(page_size)
                )
            ]
            return (count, textbooks)

    return PageGetter


def make_item_saver():
    class ItemSaver(SessionDependent):
        @contextmanager
        def __call__(self, item):
            yield

    return ItemSaver


def make_item_deleter():
    class ItemDeleter(SessionDependent):
        def __call__(self, item):
            self.session.delete(item)

    return ItemDeleter
