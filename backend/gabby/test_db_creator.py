import atexit
import os

import sqlalchemy_utils.functions

from . import orm_models  # To populate the metadata
from .database_utils import OrmBase, create_engine, sql_create_exercise_number_collation
from .testing import TEST_DATABASE_URL


def create_test_database():
    sqlalchemy_utils.functions.create_database(TEST_DATABASE_URL)
    database_engine = create_engine(TEST_DATABASE_URL)
    with database_engine.connect() as conn:
        conn.execute(sql_create_exercise_number_collation)
        conn.commit()
    OrmBase.metadata.create_all(database_engine)
    database_engine.dispose()


def drop_test_database():
    sqlalchemy_utils.functions.drop_database(TEST_DATABASE_URL)


if os.environ.get("GABBY_UNITTESTING", "false") == "true":
    create_test_database()
    atexit.register(drop_test_database)
