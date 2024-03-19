from __future__ import annotations
import dataclasses
import datetime
import json
from typing import Annotated

from django.test import TestCase
from fastapi import FastAPI, Query
from fastapi.testclient import TestClient
from pydantic import BaseModel
from starlette import status

from .annotations import Computed, Constant, Secret
from .router import make_jsonapi_router


class AllAttributesTestCase(TestCase):
    maxDiff = None

    class Resource:
        singular_name = "resource"
        plural_name = "resources"

        default_page_size = 2

        class Model(BaseModel):
            plain_int: int
            defaulted_datetime: datetime.datetime = datetime.datetime(2024, 3, 18, 15, 38, 15, tzinfo=datetime.timezone.utc)
            constant_str: Annotated[str, Constant()]
            defaulted_constant_float: Annotated[float, Constant()] = 3.14
            secret_str: Annotated[str, Secret()]
            computed_str: Annotated[str, Computed()]

        # @todo Provide utility to avoid writing 'filter[whatever]' here
        @staticmethod
        def filters(filter_computed_str: Annotated[str, Query(alias="filter[computedStr]")] = None):
            return {
                "computed_str": filter_computed_str,
            }

        _next_id = 1
        _items = {}

        @dataclasses.dataclass
        class _Item:
            id: str

            plain_int: int = 42
            defaulted_datetime: datetime.datetime = datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)
            constant_str: str = "Constant"
            defaulted_constant_float: float = 6.18
            secret_str: str = "Secret"

            saved: int = 0

            @property
            def computed_str(self):
                return self.secret_str.upper()
            
            def save(self):
                self.saved += 1

            def delete(self):
                AllAttributesTestCase.Resource._items.pop(self.id)

        @classmethod
        def create_item(cls, **kwds):
            item = cls._Item(id=str(cls._next_id), **kwds)
            cls._items[item.id] = item
            cls._next_id += 1
            return item

        @classmethod
        def get_item(cls, id):
            return cls._items.get(id)

        @classmethod
        def get_page(cls, filters, first_index, page_size):
            items = sorted(cls._items.values(), key=lambda item: int(item.id))
            if filters["computed_str"]:
                items = [item for item in items if item.computed_str == filters["computed_str"]]
            return (len(items), items[first_index:first_index + page_size])

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.__app = FastAPI()
        cls.__app.include_router(make_jsonapi_router([cls.Resource()]))
        cls.__client = TestClient(cls.__app)

    def setUp(self):
        super().setUp()
        self.Resource._next_id = 1
        self.Resource._items = {}

    def get(self, url):
        return self.__client.get(url, headers={"Content-Type": "application/vnd.api+json"})

    def post(self, url, payload):
        return self.__client.post(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def patch(self, url, payload):
        return self.__client.patch(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def delete(self, url):
        return self.__client.delete(url, headers={"Content-Type": "application/vnd.api+json"})

    def test_schema(self):
        file_path =  f"{__file__}.AllAttributesTestCase.openapi.json"
        with open(file_path) as file:
            expected = json.load(file)

        actual = self.__app.openapi()
        # @todo Remove all 'application/json' from schema; use only 'application/vnd.api+json'

        try:
            self.assertEqual(actual, expected)
        finally:
            with open(file_path, "w") as file:
                json.dump(actual, file, indent=2, sort_keys=True)
                file.write("\n")

    def test_create__minimal(self):
        response = self.post("http://server/resources", {
            "data": {
                "type": "Resource",
                "attributes": {
                    "plainInt": 57,
                    "constantStr": "Constant string",
                    "secretStr": "My password",
                },
                # No "relationships"
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "Resource",
                "id": "1",
                "links": {"self": "http://server/resources/1"},
                "attributes": {
                    "plainInt": 57,
                    "defaultedDatetime": "2024-03-18T15:38:15Z",
                    "constantStr": "Constant string",
                    "defaultedConstantFloat": 3.14,
                    "computedStr": "MY PASSWORD",
                },
                # No "relationships"
            },
        })

    def test_create__full(self):
        response = self.post("http://server/resources", {
            "data": {
                "type": "Resource",
                "attributes": {
                    "plainInt": 42,
                    "defaultedDatetime": "2024-01-02T03:04:05+01:00",
                    "constantStr": "Constant string",
                    "defaultedConstantFloat": 6.18,
                    "secretStr": "My password",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "Resource",
                "id": "1",
                "links": {"self": "http://server/resources/1"},
                "attributes": {
                    "constantStr": "Constant string",
                    "plainInt": 42,
                    "defaultedDatetime": "2024-01-02T03:04:05+01:00",
                    "constantStr": "Constant string",
                    "defaultedConstantFloat": 6.18,
                    "computedStr": "MY PASSWORD",
                },
            },
        })

        item = self.Resource.get_item("1")
        self.assertEqual(item.plain_int, 42)
        self.assertEqual(item.defaulted_datetime, datetime.datetime(2024, 1, 2, 3, 4, 5, tzinfo=datetime.timezone(datetime.timedelta(hours=1))))
        self.assertEqual(item.constant_str, "Constant string")
        self.assertEqual(item.defaulted_constant_float, 6.18)
        self.assertEqual(item.secret_str, "My password")
        self.assertEqual(item.computed_str, "MY PASSWORD")
        self.assertEqual(item.saved, 0)

    def test_create__computed(self):
        response = self.post("http://server/resources", {
            "data": {
                "type": "Resource",
                "attributes": {
                    "plainInt": 57,
                    "constantStr": "Constant string",
                    "secretStr": "My password",
                    "computedStr": "Refused on creation",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())

    def test_get_item(self):
        self.assertEqual(self.Resource.create_item().id, "1")

        response = self.get(f"http://server/resources/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "Resource",
                "id": "1",
                "links": {"self": f"http://server/resources/1"},
                "attributes": {
                    "plainInt": 42,
                    "defaultedDatetime": "2021-01-01T01:00:00Z",
                    "constantStr": "Constant",
                    "defaultedConstantFloat": 6.18,
                    "computedStr": "SECRET",
                },
            },
        })

    def test_get_item__non_existing(self):
        response = self.get(f"http://server/resources/1")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.json())

    def test_get_page(self):
        for i in range(5):
            self.Resource.create_item(plain_int=i + 1)

        response = self.get(f"http://server/resources")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "Resource",
                    "id": "1",
                    "links": {"self": f"http://server/resources/1"},
                    "attributes": {
                        "plainInt": 1,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "SECRET",
                    },
                },
                {
                    "type": "Resource",
                    "id": "2",
                    "links": {"self": f"http://server/resources/2"},
                    "attributes": {
                        "plainInt": 2,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "SECRET",
                    },
                },
            ],
            "links": {
                "first": "http://server/resources?page%5Bnumber%5D=1",
                "last": "http://server/resources?page%5Bnumber%5D=3",
                "next": "http://server/resources?page%5Bnumber%5D=2",
                "prev": None
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 1,
                    "pages": 3,
                },
            },
        })

    def test_update__nothing(self):
        self.assertEqual(self.Resource.create_item().id, "1")

        response = self.patch(f"http://server/resources/1", {
            "data": {
                "type": "Resource",
                "id": "1",
                # No "attributes", no "relationships"
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "Resource",
                "id": "1",
                "links": {"self": f"http://server/resources/1"},
                "attributes": {
                    "plainInt": 42,
                    "defaultedDatetime": "2021-01-01T01:00:00Z",
                    "constantStr": "Constant",
                    "defaultedConstantFloat": 6.18,
                    "computedStr": "SECRET",
                },
            },
        })

        item = self.Resource.get_item("1")
        self.assertEqual(item.plain_int, 42)
        self.assertEqual(item.defaulted_datetime, datetime.datetime(2021, 1, 1, 1, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(item.constant_str, "Constant")
        self.assertEqual(item.defaulted_constant_float, 6.18)
        self.assertEqual(item.secret_str, "Secret")
        self.assertEqual(item.computed_str, "SECRET")
        self.assertEqual(item.saved, 0)

    def test_update__one(self):
        self.assertEqual(self.Resource.create_item().id, "1")

        response = self.patch(f"http://server/resources/1", {
            "data": {
                "type": "Resource",
                "id": "1",
                "attributes": {
                    "plainInt": 57,
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "Resource",
                "id": "1",
                "links": {"self": f"http://server/resources/1"},
                "attributes": {
                    "plainInt": 57,
                    "defaultedDatetime": "2021-01-01T01:00:00Z",
                    "constantStr": "Constant",
                    "defaultedConstantFloat": 6.18,
                    "computedStr": "SECRET",
                },
            },
        })

        item = self.Resource.get_item("1")
        self.assertEqual(item.plain_int, 57)
        self.assertEqual(item.defaulted_datetime, datetime.datetime(2021, 1, 1, 1, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(item.constant_str, "Constant")
        self.assertEqual(item.defaulted_constant_float, 6.18)
        self.assertEqual(item.secret_str, "Secret")
        self.assertEqual(item.computed_str, "SECRET")
        self.assertEqual(item.saved, 1)

    def test_update__all(self):
        self.assertEqual(self.Resource.create_item().id, "1")

        response = self.patch(f"http://server/resources/1", {
            "data": {
                "type": "Resource",
                "id": "1",
                "attributes": {
                    "plainInt": 57,
                    "defaultedDatetime": "2024-01-02T03:04:05+01:00",
                    "secretStr": "My password",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "Resource",
                "id": "1",
                "links": {"self": f"http://server/resources/1"},
                "attributes": {
                    "plainInt": 57,
                    "defaultedDatetime": "2024-01-02T03:04:05+01:00",
                    "constantStr": "Constant",
                    "defaultedConstantFloat": 6.18,
                    "computedStr": "MY PASSWORD",
                },
            },
        })

        item = self.Resource.get_item("1")
        self.assertEqual(item.plain_int, 57)
        self.assertEqual(item.defaulted_datetime, datetime.datetime(2024, 1, 2, 3, 4, 5, tzinfo=datetime.timezone(datetime.timedelta(hours=1))))
        self.assertEqual(item.constant_str, "Constant")
        self.assertEqual(item.defaulted_constant_float, 6.18)
        self.assertEqual(item.secret_str, "My password")
        self.assertEqual(item.computed_str, "MY PASSWORD")
        self.assertEqual(item.saved, 1)

    def test_update__computed(self):
        self.assertEqual(self.Resource.create_item().id, "1")

        response = self.patch(f"http://server/resources/1", {
            "data": {
                "type": "Resource",
                "id": "1",
                "attributes": {
                    "computedStr": "Refused on update",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())

    def test_update__constant(self):
        self.assertEqual(self.Resource.create_item().id, "1")

        response = self.patch(f"http://server/resources/1", {
            "data": {
                "type": "Resource",
                "id": "1",
                "attributes": {
                    "constantStr": "Refused on update",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())

    def test_delete(self):
        self.assertEqual(self.Resource.create_item().id, "1")

        response = self.delete(f"http://server/resources/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertIsNone(self.Resource.get_item("1"))


class EmptyTestCase(TestCase):
    maxDiff = None

    class EmptyResource:
        singular_name = "empty_resource"
        plural_name = "empty_resources"

        default_page_size = 2

        class Model(BaseModel):
            pass

        @staticmethod
        def filters():
            return None

        _next_id = 1
        _items = {}

        @dataclasses.dataclass
        class _Item:
            id: str

            def save(self):
                self.saved += 1

            def delete(self):
                EmptyTestCase.EmptyResource._items.pop(self.id)

        @classmethod
        def create_item(cls):
            item = cls._Item(id=str(cls._next_id))
            cls._items[item.id] = item
            cls._next_id += 1
            return item

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.__app = FastAPI()
        cls.__app.include_router(make_jsonapi_router([cls.EmptyResource()]))
        cls.__client = TestClient(cls.__app)

    def setUp(self):
        super().setUp()
        self.EmptyResource._next_id = 1
        self.EmptyResource._items = {}

    def get(self, url):
        return self.__client.get(url, headers={"Content-Type": "application/vnd.api+json"})

    def post(self, url, payload):
        return self.__client.post(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def patch(self, url, payload):
        return self.__client.patch(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def delete(self, url):
        return self.__client.delete(url, headers={"Content-Type": "application/vnd.api+json"})

    def test_schema(self):
        file_path =  f"{__file__}.EmptyTestCase.openapi.json"
        with open(file_path) as file:
            expected = json.load(file)

        actual = self.__app.openapi()

        try:
            self.assertEqual(actual, expected)
        finally:
            with open(file_path, "w") as file:
                json.dump(actual, file, indent=2, sort_keys=True)
                file.write("\n")

    def test_create(self):
        response = self.post("http://server/emptyResources", {
            "data": {
                "type": "EmptyResource",
                # No "attributes", no "relationships"
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "EmptyResource",
                "id": "1",
                "links": {"self": "http://server/emptyResources/1"},
                # No "attributes", no "relationships"
            },
        })


class FullyOptionalTestCase(TestCase):
    pass
    # @todo Add test case for a resource with attributes and relationships, but all optional
    # It must allow creation without "attributes" and "relationships"
