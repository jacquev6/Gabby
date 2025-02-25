from fastapi import HTTPException
import sqlalchemy as sql

from .wrapping import OrmWrapper, wrap, unwrap


def create_item(session, model, **kwargs):
    kwargs = {key: unwrap(value) if isinstance(value, OrmWrapper) else value for key, value in kwargs.items()}
    kwargs = {key: [unwrap(v) if isinstance(v, OrmWrapper) else v for v in value] if isinstance(value, list) else value for key, value in kwargs.items()}
    item = model(**kwargs)
    session.add(item)
    try:
        session.flush()
    except sql.exc.IntegrityError as e:
        raise HTTPException(status_code=400, detail=e.orig.diag.constraint_name)
    return wrap(item)


def get_item(session, model, id):
    return wrap(session.get(model, id))


def get_page(session, query, first_index, page_size):
    # This probably won't work with joins, but it's a problem for future me
    count_query = sql.select(sql.func.count(query.selected_columns[0]))
    if query.whereclause is not None:
        count_query = count_query.where(query.whereclause)

    count = session.scalar(count_query)
    items = [wrap(item) for (item,) in session.execute(query.offset(first_index).limit(page_size))]
    return (count, items)


def save_item(session, item):
    try:
        session.flush()
    except sql.exc.IntegrityError as e:
        raise HTTPException(status_code=400, detail=e.orig.diag.constraint_name)


def delete_item(session, item):
    session.delete(unwrap(item))
    try:
        session.flush()
    except sql.exc.IntegrityError as e:
        raise HTTPException(status_code=400, detail=e.orig.diag.constraint_name)
