from contextlib import contextmanager
import json
import inspect

from fastapi import FastAPI
from fastapi.testclient import TestClient

from .django import AuthenticationToken
from .router import make_jsonapi_router


class TestMixin:
    maxDiff = None
    polymorphism = {}

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.__app = FastAPI()
        cls.__app.include_router(make_jsonapi_router(cls.resources, cls.polymorphism))

        @cls.__app.post("/token")
        def login(access_token: AuthenticationToken):
            return {
                "access_token": access_token,
                "token_type": "bearer",
            }

        cls.__schema_file_path = f"{inspect.getfile(cls)}.{cls.__name__}.openapi.json"
        cls.__client = TestClient(cls.__app)

    def setUp(self):
        super().setUp()
        self.__client.headers.pop("Authorization", None)

    def login(self, username, password):
        response = self.__client.post("http://server/token", data={"username": username, "password": password})
        self.assertEqual(response.status_code, 200, response.json())
        self.__client.headers["Authorization"] = f"Bearer {response.json()["access_token"]}"

    def get(self, url):
        return self.__client.get(url, headers={"Content-Type": "application/vnd.api+json"})

    def post(self, url, payload):
        return self.__client.post(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def patch(self, url, payload):
        return self.__client.patch(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def delete(self, url):
        return self.__client.delete(url, headers={"Content-Type": "application/vnd.api+json"})

    def test_schema(self):
        try:
            with open(self.__class__.__schema_file_path) as file:
                expected = json.load(file)
        except FileNotFoundError:
            expected = {}

        actual = self.__app.openapi()
        # @todo Remove all 'application/json' from schema; use only 'application/vnd.api+json'

        try:
            self.assertEqual(actual, expected)
        finally:
            with open(self.__class__.__schema_file_path, "w") as file:
                json.dump(actual, file, indent=2, sort_keys=True)
                file.write("\n")


class ItemsFactory:
    def __init__(self):
        self.__next_id = 1
        self.__items = {}
        self.commits_count = 0
        self.rollbacks_count = 0

    @contextmanager
    def atomic(self):
        prev_next_id = self.__next_id
        prev_items = self.__items.copy()
        try:
            yield
        except:
            self.__next_id = prev_next_id
            self.__items = prev_items
            self.rollbacks_count += 1
            raise
        else:
            self.commits_count += 1

    def create(self, cls, **kwds):
        item = cls(id=str(self.__next_id), **kwds)
        self.__items[item.id] = item
        self.__next_id += 1
        return item

    def get(self, cls, id):
        item = self.__items.get(id)
        if item is None:
            return None
        else:
            assert isinstance(item, cls), (item, cls)
            return item

    def get_all(self, cls):
        items = filter(lambda item: isinstance(item, cls), self.__items.values())
        items = sorted(items, key=lambda item: int(item.id))
        return items

    def delete(self, cls, id):
        item = self.__items.pop(id)
        assert isinstance(item, cls)