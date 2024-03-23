import json
import inspect

from fastapi import FastAPI
from fastapi.testclient import TestClient

from .router import make_jsonapi_router


class TestMixin:
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.__app = FastAPI()
        cls.__app.include_router(make_jsonapi_router(cls.resources))

        cls.__schema_file_path = f"{inspect.getfile(cls)}.{cls.__name__}.openapi.json"
        cls.__client = TestClient(cls.__app)

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
            assert isinstance(item, cls)
            return item

    def get_all(self, cls):
        items = filter(lambda item: isinstance(item, cls), self.__items.values())
        items = sorted(items, key=lambda item: int(item.id))
        return items

    def delete(self, cls, id):
        item = self.__items.pop(id)
        assert isinstance(item, cls)
