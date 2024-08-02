import datetime
import json
import unittest

from fastapi import FastAPI
from fastapi.testclient import TestClient
import sqlalchemy as sql

from fastjsonapi import make_jsonapi_router

from . import settings
from .database_utils import create_engine, Session, truncate_all_tables
from .users import User, AuthenticationDependable


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

        def refresh(self, *args, **kwds):
            return self.__session.refresh(*args, **kwds)

        def add(self, *args, **kwds):
            return self.__session.add(*args, **kwds)

        def delete(self, *args, **kwds):
            return self.__session.delete(*args, **kwds)

        def begin_nested(self, *args, **kwds):
            return self.__session.begin_nested(*args, **kwds)

    def setUp(self):
        super().setUp()
        self.__class__.__session = Session(self.__database_engine)
        truncate_all_tables(self.__session)
        self.__session.commit()
        self.user_for_create = self.__create_user_for_create()
        self.expect_commits_rollbacks(0, 0)
        self.__class__.actual_commits_count = 0
        self.__class__.actual_rollbacks_count = 0

    @classmethod
    def make_session(cls):
        return cls.SessionWrapper(cls, Session(cls.__database_engine))

    def expect_commit(self):
        self.__expected_commits_count = 1
        self.__expected_rollbacks_count = 0

    def expect_one_more_commit(self):
        self.__expected_commits_count += 1

    def expect_rollback(self):
        self.__expected_commits_count = 0
        self.__expected_rollbacks_count = 1

    def expect_commits_rollbacks(self, commits, rollbacks):
        self.__expected_commits_count = commits
        self.__expected_rollbacks_count = rollbacks

    def tearDown(self):
        # https://stackoverflow.com/a/39606065/905845
        if all(test != self for test, text in self._outcome.result.errors + self._outcome.result.failures):
            self.assert_commits_rollbacks(self.__expected_commits_count, self.__expected_rollbacks_count)
        self.__session.close()
        super().tearDown()

    def assert_commits_rollbacks(self, commits, rollbacks):
        self.assertEqual((self.actual_commits_count, self.actual_rollbacks_count), (commits, rollbacks))

    def create_model(self, model, *args, **kwds):
        # @todo Understand why using the relationships instead of the ids results in a not-null violation
        if hasattr(model, "created_by") and "created_by_id" not in kwds and "created_by" not in kwds:
            kwds["created_by_id"] = self.user_for_create.id
        if hasattr(model, "updated_by") and "updated_by_id" not in kwds and "updated_by" not in kwds:
            kwds["updated_by_id"] = self.user_for_create.id
        instance = model(*args, **kwds)
        self.__session.add(instance)
        self.__session.commit()
        return instance

    def __create_user_for_create(self):
        user = User(username="creator", created_by_id=1, updated_by_id=1)
        self.__session.add(user)
        self.__session.flush()
        user.created_by_id = user.id
        user.updated_by_id = user.id
        self.__session.commit()
        return user

    def delete_model(self, model, id):
        self.__session.execute(sql.delete(model).where(model.id == id))
        self.__session.commit()

    def delete_item(self, item):
        self.__session.delete(item)
        self.__session.commit()

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

        cls.api_app = FastAPI(make_session=cls.make_session)
        cls.api_app.include_router(make_jsonapi_router(resources=cls.resources, polymorphism=cls.polymorphism, batching=True))

        @cls.api_app.post("/token")
        def login(authentication: AuthenticationDependable):
            return authentication

        cls.api_client = TestClient(cls.api_app)

    def setUp(self):
        super().setUp()
        self.expect_commit()

    def tearDown(self):
        self.logout()
        super().tearDown()

    def login(self, username, password):
        response = self.api_client.post("http://server/token", data={"username": username, "password": password})
        self.assertEqual(response.status_code, 200, response.json())
        self.api_client.headers["Authorization"] = f"Bearer {response.json()["access_token"]}"

    def logout(self):
        self.api_client.headers.pop("Authorization", None)

    # @todo Automate counting the API requests to set the expected commits and rollbacks
    # We could even check them for success (resp. failure) to expect a commit (resp. rollback)
    def get(self, url):
        return self.api_client.get(url, headers={"Content-Type": "application/vnd.api+json"})

    def post(self, url, payload):
        return self.api_client.post(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def patch(self, url, payload):
        return self.api_client.patch(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def delete(self, url):
        return self.api_client.delete(url, headers={"Content-Type": "application/vnd.api+json"})


class LoggedInApiTestCase(ApiTestCase):
    def setUp(self):
        super().setUp()
        super().create_model(User, username="updater", clear_text_password="password")
        self.login("updater", "password")

    def tearDown(self):
        self.expect_one_more_commit()
        super().tearDown()


class AdaptationTestCase(TestCase):
    # @todo Remove default vale, enforce testing the delta
    def do_test(self, adaptation, expected_adapted, expected_delta=None):
        self.assertEqual(adaptation.make_adapted(), expected_adapted)
        self.assertEqual(adaptation.to_generic_adaptation().make_adapted(), expected_adapted)
        if expected_delta is not None:
            self.assertEqual(adaptation.make_delta(), expected_delta)
