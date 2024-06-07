import os

import sqlalchemy_utils.functions

from . import orm_models  # To populate the metadata
from .database_utils import OrmBase, create_engine
from .testing import TEST_DATABASE_URL


def create_test_database():
    if sqlalchemy_utils.functions.database_exists(TEST_DATABASE_URL):
        sqlalchemy_utils.functions.drop_database(TEST_DATABASE_URL)
    sqlalchemy_utils.functions.create_database(TEST_DATABASE_URL)
    database_engine = create_engine(TEST_DATABASE_URL)
    OrmBase.metadata.create_all(database_engine)
    database_engine.dispose()


if os.environ.get("GABBY_UNITTESTING", "false") == "true":
    create_test_database()
