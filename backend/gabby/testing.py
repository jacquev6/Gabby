import datetime
import inspect
import json
import unittest

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient
import sqlalchemy as sql

from fastjsonapi import make_jsonapi_router

from . import settings
from .database_utils import create_engine, Session, truncate_all_tables
from .users import authentication_token_dependable


class TestCase(unittest.TestCase):
    maxDiff = None


TEST_DATABASE_URL = f"{settings.DATABASE_URL}-test-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"


class TransactionTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.__database_engine = create_engine(TEST_DATABASE_URL)

    @classmethod
    def tearDownClass(cls):
        cls.__database_engine.dispose()
        super().tearDownClass()

    class SessionWrapper:
        def __init__(self, test_class, session):
            self.__test_class = test_class
            self.__session = session

        def flush(self):
            self.__session.flush()

        def commit(self):
            self.__test_class.actual_commits_count += 1
            self.__session.commit()

        def rollback(self):
            self.__test_class.actual_rollbacks_count += 1
            self.__session.rollback()

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def scalar(self, *args, **kwds):
            return self.__session.scalar(*args, **kwds)

        def execute(self, *args, **kwds):
            return self.__session.execute(*args, **kwds)

        def get(self, *args, **kwds):
            return self.__session.get(*args, **kwds)

        def add(self, *args, **kwds):
            return self.__session.add(*args, **kwds)

        def delete(self, *args, **kwds):
            return self.__session.delete(*args, **kwds)

    def setUp(self):
        super().setUp()
        self.__class__.__session = Session(self.__database_engine)
        truncate_all_tables(self.__class__.__session)
        self.__class__.__session.commit()
        self.expect_commits_rollbacks(0, 0)
        self.__class__.actual_commits_count = 0
        self.__class__.actual_rollbacks_count = 0

    @classmethod
    def make_session(cls):
        return cls.SessionWrapper(cls, cls.__session)

    def expect_commit(self):
        self.__expected_commits_rollbacks_count = (1, 0)

    def expect_rollback(self):
        self.__expected_commits_rollbacks_count = (0, 1)

    def expect_commits_rollbacks(self, commits, rollbacks):
        self.__expected_commits_rollbacks_count = (commits, rollbacks)

    def tearDown(self):
        self.assertEqual((self.actual_commits_count, self.actual_rollbacks_count), self.__expected_commits_rollbacks_count)
        self.__session.close()
        super().tearDown()

    def create_model(self, model, *args, **kwds):
        instance = model(*args, **kwds)
        self.__session.add(instance)
        self.__session.commit()
        return instance

    def delete_model(self, model, id):
        self.__session.execute(sql.delete(model).where(model.id == id))

    def count_models(self, model):
        return self.__session.query(model).count()

    def get_model(self, model, id):
        instance = self.__session.get(model, id)
        self.__session.refresh(instance)
        return instance


class ApiTestCase(TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        if cls is not ApiTestCase:
            cls.api_app = FastAPI(make_session=cls.make_session)
            cls.api_app.include_router(make_jsonapi_router(cls.resources, cls.polymorphism))

            @cls.api_app.post("/token")
            def login(access_token: str = Depends(authentication_token_dependable)):
                return {
                    "access_token": access_token,
                    "token_type": "bearer",
                }

            cls.__schema_file_path = f"{inspect.getfile(cls)}.{cls.__name__}.openapi.json"
            cls.api_client = TestClient(cls.api_app)

    def setUp(self):
        super().setUp()
        self.expect_commit()

    def tearDown(self):
        if self.__class__ is not ApiTestCase:
            self.logout()
        super().tearDown()

    def login(self, username, password):
        response = self.api_client.post("http://server/token", data={"username": username, "password": password})
        self.assertEqual(response.status_code, 200, response.json())
        self.api_client.headers["Authorization"] = f"Bearer {response.json()["access_token"]}"

    def logout(self):
        self.api_client.headers.pop("Authorization", None)

    def get(self, url):
        return self.api_client.get(url, headers={"Content-Type": "application/vnd.api+json"})

    def post(self, url, payload):
        return self.api_client.post(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def patch(self, url, payload):
        return self.api_client.patch(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def delete(self, url):
        return self.api_client.delete(url, headers={"Content-Type": "application/vnd.api+json"})

    def test_schema(self):
        self.expect_commits_rollbacks(0, 0)

        if self.__class__ is not ApiTestCase:
            try:
                with open(self.__schema_file_path) as file:
                    expected = json.load(file)
            except FileNotFoundError:
                expected = {}

            actual = self.api_app.openapi()

            try:
                self.assertEqual(actual, expected)
            finally:
                with open(self.__schema_file_path, "w") as file:
                    json.dump(actual, file, indent=2, sort_keys=True)
                    file.write("\n")


class AdaptationTestCase(TestCase):
    def do_test(self, adaptation, expected):
        self.assertEqual(adaptation.make_adapted(), expected)
        self.assertEqual(adaptation.to_generic_adaptation().make_adapted(), expected)
