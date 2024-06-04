import inspect
import json
import unittest

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient
import sqlalchemy as sql
import sqlalchemy_utils.functions

from fastjsonapi import make_jsonapi_router

from . import settings
from .database_utils import create_engine, create_tables, drop_tables, Session
from .users import authentication_token_dependable


class TestCase(unittest.TestCase):
    maxDiff = None


DATABASE_URL = settings.DATABASE_URL + "-test"

if sqlalchemy_utils.functions.database_exists(DATABASE_URL):
    sqlalchemy_utils.functions.drop_database(DATABASE_URL)

sqlalchemy_utils.functions.create_database(DATABASE_URL)


class TransactionTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.database_engine = create_engine(DATABASE_URL)

    @classmethod
    def tearDownClass(cls):
        cls.database_engine.dispose()
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        create_tables(self.database_engine)
        self.__session = Session(self.database_engine)
        self.__created = []

    def tearDown(self):
        self.__session.close()
        drop_tables(self.database_engine)
        super().tearDown()

    def create_model(self, model, *args, **kwds):
        instance = model(*args, **kwds)
        self.__session.add(instance)
        self.__session.commit()
        self.__created.append(instance)
        for i in self.__created:
            self.__session.refresh(i)
        return instance

    def delete_model(self, model, id):
        self.__session.execute(sql.delete(model).where(model.id == id))
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

        if hasattr(cls, "resources"):
            cls.api_app = FastAPI(database_engine=cls.database_engine)
            cls.api_app.include_router(make_jsonapi_router(cls.resources, cls.polymorphism))

            @cls.api_app.post("/token")
            def login(access_token: str = Depends(authentication_token_dependable)):
                return {
                    "access_token": access_token,
                    "token_type": "bearer",
                }

            cls.__schema_file_path = f"{inspect.getfile(cls)}.{cls.__name__}.openapi.json"
            cls.api_client = TestClient(cls.api_app)

            cls.test_schema = cls._test_schema

    def tearDown(self):
        if hasattr(self, "resources"):
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

    def _test_schema(self):
        try:
            with open(self.__schema_file_path) as file:
                expected = json.load(file)
        except FileNotFoundError:
            expected = {}

        actual = self.api_app.openapi()
        # @todo Remove all 'application/json' from schema; use only 'application/vnd.api+json'

        try:
            self.assertEqual(actual, expected)
        finally:
            with open(self.__schema_file_path, "w") as file:
                json.dump(actual, file, indent=2, sort_keys=True)
                file.write("\n")
