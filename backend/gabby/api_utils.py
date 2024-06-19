from contextlib import contextmanager

from fastapi import Depends, HTTPException
import sqlalchemy as sql

from .database_utils import Session, session_dependable
from .wrapping import OrmWrapper, wrap, unwrap
from .users import User, optional_authenticated_user_dependable


class SessionAndUserDependent:
    def __init__(self, session: Session = Depends(session_dependable), logged_in_user: User = Depends(optional_authenticated_user_dependable)):
        self.session = session
        self.logged_in_user = logged_in_user


def make_item_creator(model, *, preprocess=lambda **kwargs: kwargs):
    class ItemCreator(SessionAndUserDependent):
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
            item.created_by = self.logged_in_user
            item.updated_by = self.logged_in_user
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

    class ItemGetter(SessionAndUserDependent):
        def __call__(self, id):
            return wrap(self.session.get(model, decode_id(id)))

    return ItemGetter


def make_page_getter(
    model,
    *,
    default_sort=("id",),
    filter_functions={},
    base=SessionAndUserDependent,
):
    def add_filters(query, filters):
        for filter_name, filter_function in filter_functions.items():
            if value := getattr(filters, filter_name, None):
                query = filter_function(query, value)
        return query

    class PageGetter(base):
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
    class ItemSaver(SessionAndUserDependent):
        @contextmanager
        def __call__(self, item):
            yield
            item.updated_by = self.logged_in_user
            self.session.flush()

    return ItemSaver


def make_item_deleter():
    class ItemDeleter(SessionAndUserDependent):
        def __call__(self, item):
            self.session.delete(item)

    return ItemDeleter
