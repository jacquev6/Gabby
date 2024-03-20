from __future__ import annotations
import dataclasses
import datetime
import json
from typing import Annotated

from django.test import TestCase
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
from starlette import status

from .annotations import Computed, Constant, Secret, Filterable
from .router import make_jsonapi_router


class TextCaseMixin:
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.__app = FastAPI()
        cls.__app.include_router(make_jsonapi_router(cls.resources))
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
        file_path =  f"{__file__}.{self.__class__.__name__}.openapi.json"
        try:
            with open(file_path) as file:
                expected = json.load(file)
        except FileNotFoundError:
            expected = {}

        actual = self.__app.openapi()
        # @todo Remove all 'application/json' from schema; use only 'application/vnd.api+json'

        try:
            self.assertEqual(actual, expected)
        finally:
            with open(file_path, "w") as file:
                json.dump(actual, file, indent=2, sort_keys=True)
                file.write("\n")


# @todo Use this factory in all test cases
class ItemsFactory:
    def __init__(self):
        self.__next_id = 1
        self.__items = {}

    def create_item(self, cls, **kwds):
        item = cls(id=str(self.__next_id), **kwds)
        self.__items[item.id] = item
        self.__next_id += 1
        return item

    def get_item(self, cls, id):
        item = self.__items.get(id)
        if item is None:
            return None
        else:
            assert isinstance(item, cls)
            return item

    def get_page(self, cls):
        items = filter(lambda item: isinstance(item, cls), self.__items.values())
        items = sorted(items, key=lambda item: int(item.id))
        return items


class AllAttributesTestCase(TextCaseMixin, TestCase):
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
            computed_str: Annotated[str, Computed(), Filterable()]

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
            if filters.computed_str:
                items = [item for item in items if item.computed_str == filters.computed_str]
            return (len(items), items[first_index:first_index + page_size])

    resources = [Resource()]

    def setUp(self):
        super().setUp()
        self.Resource._next_id = 1
        self.Resource._items = {}

    def test_create__insufficient(self):
        response = self.post("http://server/resources", {
            "data": {
                "type": "resource",
                "attributes": {
                    "plainInt": 57,
                    "secretStr": "My password",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())

    def test_create__minimal(self):
        response = self.post("http://server/resources", {
            "data": {
                "type": "resource",
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
                "type": "resource",
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
                "type": "resource",
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
                "type": "resource",
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
                "type": "resource",
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
                "type": "resource",
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

    def test_get_page__first(self):
        for i in range(5):
            self.Resource.create_item(plain_int=i + 1)

        response = self.get(f"http://server/resources")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "resource",
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
                    "type": "resource",
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
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 1,
                    "pages": 3,
                },
            },
        })

    def test_get_page__second(self):
        for i in range(5):
            self.Resource.create_item(plain_int=i + 1)

        response = self.get(f"http://server/resources?page[number]=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "resource",
                    "id": "3",
                    "links": {"self": f"http://server/resources/3"},
                    "attributes": {
                        "plainInt": 3,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "SECRET",
                    },
                },
                {
                    "type": "resource",
                    "id": "4",
                    "links": {"self": f"http://server/resources/4"},
                    "attributes": {
                        "plainInt": 4,
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
                "next": "http://server/resources?page%5Bnumber%5D=3",
                "prev": "http://server/resources?page%5Bnumber%5D=1",
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 2,
                    "pages": 3,
                },
            },
        })

    def test_get_page__third(self):
        for i in range(5):
            self.Resource.create_item(plain_int=i + 1)

        response = self.get(f"http://server/resources?page[number]=3")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "resource",
                    "id": "5",
                    "links": {"self": f"http://server/resources/5"},
                    "attributes": {
                        "plainInt": 5,
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
                "next": None,
                "prev": "http://server/resources?page%5Bnumber%5D=2",
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 3,
                    "pages": 3,
                },
            },
        })

    def test_get_page__medium_page_size__first(self):
        for i in range(5):
            self.Resource.create_item(plain_int=i + 1)

        response = self.get(f"http://server/resources?page[size]=3")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "resource",
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
                    "type": "resource",
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
                {
                    "type": "resource",
                    "id": "3",
                    "links": {"self": f"http://server/resources/3"},
                    "attributes": {
                        "plainInt": 3,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "SECRET",
                    },
                },
            ],
            "links": {
                "first": "http://server/resources?page%5Bnumber%5D=1&page%5Bsize%5D=3",
                "last": "http://server/resources?page%5Bnumber%5D=2&page%5Bsize%5D=3",
                "next": "http://server/resources?page%5Bnumber%5D=2&page%5Bsize%5D=3",
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 1,
                    "pages": 2,
                },
            },
        })

    def test_get_page__medium_page_size__second(self):
        for i in range(5):
            self.Resource.create_item(plain_int=i + 1)

        response = self.get(f"http://server/resources?page[number]=2&page[size]=3")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "resource",
                    "id": "4",
                    "links": {"self": f"http://server/resources/4"},
                    "attributes": {
                        "plainInt": 4,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "SECRET",
                    },
                },
                {
                    "type": "resource",
                    "id": "5",
                    "links": {"self": f"http://server/resources/5"},
                    "attributes": {
                        "plainInt": 5,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "SECRET",
                    },
                },
            ],
            "links": {
                "first": "http://server/resources?page%5Bnumber%5D=1&page%5Bsize%5D=3",
                "last": "http://server/resources?page%5Bnumber%5D=2&page%5Bsize%5D=3",
                "next": None,
                "prev": "http://server/resources?page%5Bnumber%5D=1&page%5Bsize%5D=3",
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 2,
                    "pages": 2,
                },
            },
        })

    def test_get_page__large_page_size(self):
        for i in range(5):
            self.Resource.create_item(plain_int=i + 1)

        response = self.get(f"http://server/resources?page[size]=5")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "resource",
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
                    "type": "resource",
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
                {
                    "type": "resource",
                    "id": "3",
                    "links": {"self": f"http://server/resources/3"},
                    "attributes": {
                        "plainInt": 3,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "SECRET",
                    },
                },
                {
                    "type": "resource",
                    "id": "4",
                    "links": {"self": f"http://server/resources/4"},
                    "attributes": {
                        "plainInt": 4,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "SECRET",
                    },
                },
                {
                    "type": "resource",
                    "id": "5",
                    "links": {"self": f"http://server/resources/5"},
                    "attributes": {
                        "plainInt": 5,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "SECRET",
                    },
                },
            ],
            "links": {
                "first": "http://server/resources?page%5Bnumber%5D=1&page%5Bsize%5D=5",
                "last": "http://server/resources?page%5Bnumber%5D=1&page%5Bsize%5D=5",
                "next": None,
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 1,
                    "pages": 1,
                },
            },
        })

    def test_get_page__filtered__first(self):
        for i in range(5):
            secret_str = "Even" if i % 2 else "Odd"
            self.Resource.create_item(plain_int=i + 1, secret_str=secret_str)

        response = self.get(f"http://server/resources?filter[computedStr]=ODD")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "resource",
                    "id": "1",
                    "links": {"self": f"http://server/resources/1"},
                    "attributes": {
                        "plainInt": 1,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "ODD",
                    },
                },
                {
                    "type": "resource",
                    "id": "3",
                    "links": {"self": f"http://server/resources/3"},
                    "attributes": {
                        "plainInt": 3,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "ODD",
                    },
                },
            ],
            "links": {
                "first": "http://server/resources?filter%5BcomputedStr%5D=ODD&page%5Bnumber%5D=1",
                "last": "http://server/resources?filter%5BcomputedStr%5D=ODD&page%5Bnumber%5D=2",
                "next": "http://server/resources?filter%5BcomputedStr%5D=ODD&page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 3,
                    "page": 1,
                    "pages": 2,
                },
            },
        })

    def test_get_page__filtered__second(self):
        for i in range(5):
            secret_str = "Even" if i % 2 else "Odd"
            self.Resource.create_item(plain_int=i + 1, secret_str=secret_str)

        response = self.get(f"http://server/resources?filter[computedStr]=ODD&page[number]=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "resource",
                    "id": "5",
                    "links": {"self": f"http://server/resources/5"},
                    "attributes": {
                        "plainInt": 5,
                        "defaultedDatetime": "2021-01-01T01:00:00Z",
                        "constantStr": "Constant",
                        "defaultedConstantFloat": 6.18,
                        "computedStr": "ODD",
                    },
                },
            ],
            "links": {
                "first": "http://server/resources?filter%5BcomputedStr%5D=ODD&page%5Bnumber%5D=1",
                "last": "http://server/resources?filter%5BcomputedStr%5D=ODD&page%5Bnumber%5D=2",
                "next": None,
                "prev": "http://server/resources?filter%5BcomputedStr%5D=ODD&page%5Bnumber%5D=1",
            },
            "meta": {
                "pagination": {
                    "count": 3,
                    "page": 2,
                    "pages": 2,
                },
            },
        })

    def test_update__nothing(self):
        self.assertEqual(self.Resource.create_item().id, "1")

        response = self.patch(f"http://server/resources/1", {
            "data": {
                "type": "resource",
                "id": "1",
                # No "attributes", no "relationships"
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
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
                "type": "resource",
                "id": "1",
                "attributes": {
                    "plainInt": 57,
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
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
                "type": "resource",
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
                "type": "resource",
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
                "type": "resource",
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
                "type": "resource",
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


class EmptyTestCase(TextCaseMixin, TestCase):
    class EmptyResource:
        singular_name = "empty_resource"
        plural_name = "empty_resources"

        default_page_size = 2

        class Model(BaseModel):
            pass

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

    resources = [EmptyResource()]

    def setUp(self):
        super().setUp()
        self.EmptyResource._next_id = 1
        self.EmptyResource._items = {}

    def test_create(self):
        response = self.post("http://server/emptyResources", {
            "data": {
                "type": "emptyResource",
                # No "attributes", no "relationships"
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "emptyResource",
                "id": "1",
                "links": {"self": "http://server/emptyResources/1"},
                # No "attributes", no "relationships"
            },
        })

    def test_create__weirdly_empty(self):
        response = self.post("http://server/emptyResources", {
            "data": {
                "type": "emptyResource",
                "attributes": {},
                "relationships": {},
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "emptyResource",
                "id": "1",
                "links": {"self": "http://server/emptyResources/1"},
                # No "attributes", no "relationships"
            },
        })


class TopModel(BaseModel):
    lefts: list[LeftModel] = []
    rights: list[RightModel] = []

class LeftModel(BaseModel):
    top: TopModel
    right_or_none: RightModel | None = None

class RightModel(BaseModel):
    top: TopModel
    left_or_none: LeftModel | None = None

class AllRelationsTestCase(TextCaseMixin, TestCase):
    class TopResource:
        singular_name = "top"
        plural_name = "tops"

        default_page_size = 2

        Model = TopModel

        class Item:
            def __init__(self, id, lefts, rights):
                self.id = id
                self.lefts = lefts
                self.rights = rights
                self.saved = 0

            def save(self):
                self.saved += 1

        @classmethod
        def create_item(cls, **kwds):
            return AllRelationsTestCase.factory.create_item(cls.Item, **kwds)

        @classmethod
        def get_item(cls, id):
            return AllRelationsTestCase.factory.get_item(cls.Item, id)

        @classmethod
        def get_page(cls, filters, first_index, page_size):
            assert dict(filters) == {}
            items = AllRelationsTestCase.factory.get_page(cls.Item)
            return (len(items), items[first_index:first_index + page_size])

    class LeftResource:
        singular_name = "left"
        plural_name = "lefts"

        default_page_size = 2

        Model = LeftModel

        class Item:
            def __init__(self, id, top, right_or_none):
                self.id = id
                assert top is not None
                self.top = top
                self.right_or_none = right_or_none
                self.saved = 0

            def save(self):
                self.saved += 1

        @classmethod
        def create_item(cls, **kwds):
            return AllRelationsTestCase.factory.create_item(cls.Item, **kwds)

        @classmethod
        def get_item(cls, id):
            return AllRelationsTestCase.factory.get_item(cls.Item, id)

    class RightResource:
        singular_name = "right"
        plural_name = "rights"

        default_page_size = 2

        Model = RightModel

        class Item:
            def __init__(self, id, top, left_or_none):
                self.id = id
                assert top is not None
                self.top = top
                self.left_or_none = left_or_none
                self.saved = 0

            def save(self):
                self.saved += 1

        @classmethod
        def create_item(cls, **kwds):
            return AllRelationsTestCase.factory.create_item(cls.Item, **kwds)

        @classmethod
        def get_item(cls, id):
            return AllRelationsTestCase.factory.get_item(cls.Item, id)

    # @todo Shuffle the resources to test their order doesn't matter. Use Django's shuffle seed
    resources = [TopResource(), LeftResource(), RightResource()]

    def setUp(self):
        super().setUp()
        AllRelationsTestCase.factory = ItemsFactory()

    def test_create_top__minimal(self):
        response = self.post("http://server/tops", {
            "data": {
                "type": "topResource",
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "1",
                "links": {"self": "http://server/tops/1"},
                "relationships": {
                    "lefts": {
                        "data": [],
                        "meta": {"count": 0},
                        # @todo Add links
                        # "links": {
                        #     "self": "http://server/tops/1/relationships/lefts",
                        #     "related": "http://server/tops/1/lefts"
                        # },
                    },
                    "rights": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                },
            },
        })

        top = self.TopResource.get_item("1")
        self.assertEqual(top.lefts, [])
        self.assertEqual(top.rights, [])

    def test_create_top__weirdly_empty(self):
        response = self.post("http://server/tops", {
            "data": {
                "type": "topResource",
                "relationships": {},
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "1",
                "links": {"self": "http://server/tops/1"},
                "relationships": {
                    "lefts": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                    "rights": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                },
            },
        })

        top = self.TopResource.get_item("1")
        self.assertEqual(top.lefts, [])
        self.assertEqual(top.rights, [])

    def test_create_top__explicitly_empty(self):
        response = self.post("http://server/tops", {
            "data": {
                "type": "topResource",
                "relationships": {
                    "lefts": {"data": []},
                    "rights": {"data": []},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "1",
                "links": {"self": "http://server/tops/1"},
                "relationships": {
                    "lefts": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                    "rights": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                },
            },
        })

        top = self.TopResource.get_item("1")
        self.assertEqual(top.lefts, [])
        self.assertEqual(top.rights, [])

    def test_create_top__full(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        self.LeftResource.create_item(top=top, right_or_none=None)
        self.LeftResource.create_item(top=top, right_or_none=None)
        self.RightResource.create_item(top=top, left_or_none=None)
        self.RightResource.create_item(top=top, left_or_none=None)

        response = self.post("http://server/tops", {
            "data": {
                "type": "topResource",
                "relationships": {
                    "lefts": {"data": [{"type": "left", "id": "2"}, {"type": "left", "id": "3"}]},
                    "rights": {"data": [{"type": "right", "id": "4"}, {"type": "right", "id": "5"}]},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "6",
                "links": {"self": "http://server/tops/6"},
                "relationships": {
                    "lefts": {
                        "data": [{"type": "left", "id": "2"}, {"type": "left", "id": "3"}],
                        "meta": {"count": 2},
                    },
                    "rights": {
                        "data": [{"type": "right", "id": "4"}, {"type": "right", "id": "5"}],
                        "meta": {"count": 2},
                    },
                },
            },
        })

        top = self.TopResource.get_item("6")
        self.assertEqual(top.lefts, [self.LeftResource.get_item("2"), self.LeftResource.get_item("3")])
        self.assertEqual(top.rights, [self.RightResource.get_item("4"), self.RightResource.get_item("5")])

    def test_create_left__minimal(self):
        self.TopResource.create_item(lefts=[], rights=[])

        response = self.post("http://server/lefts", {
            "data": {
                "type": "left",
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": None},
                },
            },
        })

        left = self.LeftResource.get_item("2")
        self.assertEqual(left.top, self.TopResource.get_item("1"))
        self.assertEqual(left.right_or_none, None)

    def test_create_left__explicitly_none(self):
        self.TopResource.create_item(lefts=[], rights=[])

        response = self.post("http://server/lefts", {
            "data": {
                "type": "left",
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": None},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": None},
                },
            },
        })

        left = self.LeftResource.get_item("2")
        self.assertEqual(left.top, self.TopResource.get_item("1"))
        self.assertEqual(left.right_or_none, None)

    def test_create_left__full(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        self.RightResource.create_item(top=top, left_or_none=None)

        response = self.post("http://server/lefts", {
            "data": {
                "type": "left",
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": {"type": "right", "id": "2"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "3",
                "links": {"self": "http://server/lefts/3"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": {"type": "right", "id": "2"}},
                },
            },
        })

        left = self.LeftResource.get_item("3")
        self.assertEqual(left.top, self.TopResource.get_item("1"))
        self.assertEqual(left.right_or_none, self.RightResource.get_item("2"))

    def test_get_page__tops(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        for i in range(4):
            lefts = [self.LeftResource.create_item(top=top, right_or_none=None) for _ in range(i + 1)]
            rights = [self.RightResource.create_item(top=top, left_or_none=None) for _ in range(i + 1)]
            self.TopResource.create_item(lefts=lefts, rights=rights)

        response = self.get("http://server/tops?page[size]=3")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "top",
                    "id": "1",
                    "links": {"self": "http://server/tops/1"},
                    "relationships": {
                        "lefts": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                        "rights": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                    },
                },
                {
                    "type": "top",
                    "id": "4",
                    "links": {"self": "http://server/tops/4"},
                    "relationships": {
                        "lefts": {
                            "data": [{"id": "2", "type": "left"}],
                            "meta": {"count": 1},
                        },
                        "rights": {
                            "data": [{"id": "3", "type": "right"}],
                            "meta": {"count": 1},
                        },
                    },
                },
                {
                    "type": "top",
                    "id": "9",
                    "links": {"self": "http://server/tops/9"},
                    "relationships": {
                        "lefts": {
                            "data": [{"id": "5", "type": "left"}, {"id": "6", "type": "left"}],
                            "meta": {"count": 2},
                        },
                        "rights": {
                            "data": [{"id": "7", "type": "right"}, {"id": "8", "type": "right"}],
                            "meta": {"count": 2},
                        },
                    },
                },
            ],
            "links": {
                "first": "http://server/tops?page%5Bnumber%5D=1&page%5Bsize%5D=3",
                "last": "http://server/tops?page%5Bnumber%5D=2&page%5Bsize%5D=3",
                "next": "http://server/tops?page%5Bnumber%5D=2&page%5Bsize%5D=3",
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 1,
                    "pages": 2,
                },
            },
        })

    def test_get_page__tops__include_empty(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        for i in range(4):
            lefts = [self.LeftResource.create_item(top=top, right_or_none=None) for _ in range(i + 1)]
            rights = [self.RightResource.create_item(top=top, left_or_none=None) for _ in range(i + 1)]
            self.TopResource.create_item(lefts=lefts, rights=rights)

        response = self.get("http://server/tops?page[size]=3&include=")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "top",
                    "id": "1",
                    "links": {"self": "http://server/tops/1"},
                    "relationships": {
                        "lefts": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                        "rights": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                    },
                },
                {
                    "type": "top",
                    "id": "4",
                    "links": {"self": "http://server/tops/4"},
                    "relationships": {
                        "lefts": {
                            "data": [{"id": "2", "type": "left"}],
                            "meta": {"count": 1},
                        },
                        "rights": {
                            "data": [{"id": "3", "type": "right"}],
                            "meta": {"count": 1},
                        },
                    },
                },
                {
                    "type": "top",
                    "id": "9",
                    "links": {"self": "http://server/tops/9"},
                    "relationships": {
                        "lefts": {
                            "data": [{"id": "5", "type": "left"}, {"id": "6", "type": "left"}],
                            "meta": {"count": 2},
                        },
                        "rights": {
                            "data": [{"id": "7", "type": "right"}, {"id": "8", "type": "right"}],
                            "meta": {"count": 2},
                        },
                    },
                },
            ],
            "included": [],
            "links": {
                "first": "http://server/tops?page%5Bnumber%5D=1&page%5Bsize%5D=3&include=",
                "last": "http://server/tops?page%5Bnumber%5D=2&page%5Bsize%5D=3&include=",
                "next": "http://server/tops?page%5Bnumber%5D=2&page%5Bsize%5D=3&include=",
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 1,
                    "pages": 2,
                },
            },
        })

    def test_get_page__tops__include_lefts(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        for i in range(4):
            lefts = [self.LeftResource.create_item(top=top, right_or_none=None) for _ in range(i + 1)]
            rights = [self.RightResource.create_item(top=top, left_or_none=None) for _ in range(i + 1)]
            self.TopResource.create_item(lefts=lefts, rights=rights)

        response = self.get("http://server/tops?page[size]=3&include=lefts")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "top",
                    "id": "1",
                    "links": {"self": "http://server/tops/1"},
                    "relationships": {
                        "lefts": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                        "rights": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                    },
                },
                {
                    "type": "top",
                    "id": "4",
                    "links": {"self": "http://server/tops/4"},
                    "relationships": {
                        "lefts": {
                            "data": [{"id": "2", "type": "left"}],
                            "meta": {"count": 1},
                        },
                        "rights": {
                            "data": [{"id": "3", "type": "right"}],
                            "meta": {"count": 1},
                        },
                    },
                },
                {
                    "type": "top",
                    "id": "9",
                    "links": {"self": "http://server/tops/9"},
                    "relationships": {
                        "lefts": {
                            "data": [{"id": "5", "type": "left"}, {"id": "6", "type": "left"}],
                            "meta": {"count": 2},
                        },
                        "rights": {
                            "data": [{"id": "7", "type": "right"}, {"id": "8", "type": "right"}],
                            "meta": {"count": 2},
                        },
                    },
                },
            ],
            "included": [
                {
                    "type": "left",
                    "id": "2",
                    "links": {"self": "http://server/lefts/2"},
                    "relationships": {
                        "top": {"data": {"type": "top", "id": "1"}},
                        "rightOrNone": {"data": None},
                    },
                },
                {
                    "type": "left",
                    "id": "5",
                    "links": {"self": "http://server/lefts/5"},
                    "relationships": {
                        "top": {"data": {"type": "top", "id": "1"}},
                        "rightOrNone": {"data": None},
                    },
                },
                {
                    "type": "left",
                    "id": "6",
                    "links": {"self": "http://server/lefts/6"},
                    "relationships": {
                        "top": {"data": {"type": "top", "id": "1"}},
                        "rightOrNone": {"data": None},
                    },
                },
            ],
            "links": {
                "first": "http://server/tops?page%5Bnumber%5D=1&page%5Bsize%5D=3&include=lefts",
                "last": "http://server/tops?page%5Bnumber%5D=2&page%5Bsize%5D=3&include=lefts",
                "next": "http://server/tops?page%5Bnumber%5D=2&page%5Bsize%5D=3&include=lefts",
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 1,
                    "pages": 2,
                },
            },
        })

    def test_get_page__tops__include_lefts_top(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        for i in range(4):
            lefts = [self.LeftResource.create_item(top=top, right_or_none=None) for _ in range(i + 1)]
            rights = [self.RightResource.create_item(top=top, left_or_none=None) for _ in range(i + 1)]
            self.TopResource.create_item(lefts=lefts, rights=rights)

        response = self.get("http://server/tops?page[size]=3&include=lefts.top")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "top",
                    "id": "1",
                    "links": {"self": "http://server/tops/1"},
                    "relationships": {
                        "lefts": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                        "rights": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                    },
                },
                {
                    "type": "top",
                    "id": "4",
                    "links": {"self": "http://server/tops/4"},
                    "relationships": {
                        "lefts": {
                            "data": [{"id": "2", "type": "left"}],
                            "meta": {"count": 1},
                        },
                        "rights": {
                            "data": [{"id": "3", "type": "right"}],
                            "meta": {"count": 1},
                        },
                    },
                },
                {
                    "type": "top",
                    "id": "9",
                    "links": {"self": "http://server/tops/9"},
                    "relationships": {
                        "lefts": {
                            "data": [{"id": "5", "type": "left"}, {"id": "6", "type": "left"}],
                            "meta": {"count": 2},
                        },
                        "rights": {
                            "data": [{"id": "7", "type": "right"}, {"id": "8", "type": "right"}],
                            "meta": {"count": 2},
                        },
                    },
                },
            ],
            "included": [
                {
                    "type": "left",
                    "id": "2",
                    "links": {"self": "http://server/lefts/2"},
                    "relationships": {
                        "top": {"data": {"type": "top", "id": "1"}},
                        "rightOrNone": {"data": None},
                    },
                },
                {
                    "type": "top",
                    "id": "1",
                    "links": {"self": "http://server/tops/1"},
                    "relationships": {
                        "lefts": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                        "rights": {
                            "data": [],
                            "meta": {"count": 0},
                        },
                    },
                },
                {
                    "type": "left",
                    "id": "5",
                    "links": {"self": "http://server/lefts/5"},
                    "relationships": {
                        "top": {"data": {"type": "top", "id": "1"}},
                        "rightOrNone": {"data": None},
                    },
                },
                {
                    "type": "left",
                    "id": "6",
                    "links": {"self": "http://server/lefts/6"},
                    "relationships": {
                        "top": {"data": {"type": "top", "id": "1"}},
                        "rightOrNone": {"data": None},
                    },
                },
            ],
            "links": {
                "first": "http://server/tops?page%5Bnumber%5D=1&page%5Bsize%5D=3&include=lefts.top",
                "last": "http://server/tops?page%5Bnumber%5D=2&page%5Bsize%5D=3&include=lefts.top",
                "next": "http://server/tops?page%5Bnumber%5D=2&page%5Bsize%5D=3&include=lefts.top",
                "prev": None,
            },
            "meta": {
                "pagination": {
                    "count": 5,
                    "page": 1,
                    "pages": 2,
                },
            },
        })

    def test_update_top__nothing(self):
        self.TopResource.create_item(lefts=[], rights=[])

        response = self.patch("http://server/tops/1", {
            "data": {
                "type": "topResource",
                "id": "1",
                # No "attributes", no "relationships"
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "1",
                "links": {"self": "http://server/tops/1"},
                "relationships": {
                    "lefts": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                    "rights": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                },
            },
        })

        top = self.TopResource.get_item("1")
        self.assertEqual(top.lefts, [])
        self.assertEqual(top.rights, [])
        self.assertEqual(top.saved, 0)

    def test_update_top__one(self):
        top1 = self.TopResource.create_item(lefts=[], rights=[])
        right = self.RightResource.create_item(top=top1, left_or_none=None)
        top = self.TopResource.create_item(lefts=[], rights=[right])
        self.LeftResource.create_item(top=top, right_or_none=None)

        response = self.patch("http://server/tops/3", {
            "data": {
                "type": "topResource",
                "id": "3",
                "relationships": {
                    "lefts": {"data": [{"type": "left", "id": "4"}]},
                }
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "3",
                "links": {"self": "http://server/tops/3"},
                "relationships": {
                    "lefts": {
                        "data": [{"type": "left", "id": "4"}],
                        "meta": {"count": 1},
                    },
                    "rights": {
                        "data": [{"type": "right", "id": "2"}],
                        "meta": {"count": 1},
                    },
                },
            },
        })

        top = self.TopResource.get_item("3")
        self.assertEqual(top.lefts, [self.LeftResource.get_item("4")])
        self.assertEqual(top.rights, [self.RightResource.get_item("2")])
        self.assertEqual(top.saved, 1)

    def test_update_top__full(self):
        top1 = self.TopResource.create_item(lefts=[], rights=[])
        left1 = self.LeftResource.create_item(top=top1, right_or_none=None)
        left2 = self.LeftResource.create_item(top=top1, right_or_none=None)
        top = self.TopResource.create_item(lefts=[left1, left2], rights=[])
        self.RightResource.create_item(top=top, left_or_none=None)
        self.RightResource.create_item(top=top, left_or_none=None)

        response = self.patch("http://server/tops/4", {
            "data": {
                "type": "topResource",
                "id": "4",
                "relationships": {
                    "lefts": {"data": []},
                    "rights": {"data": [{"type": "right", "id": "5"}, {"type": "right", "id": "6"}]},
                }
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "top",
                "id": "4",
                "links": {"self": "http://server/tops/4"},
                "relationships": {
                    "lefts": {
                        "data": [],
                        "meta": {"count": 0},
                    },
                    "rights": {
                        "data": [{"type": "right", "id": "5"}, {"type": "right", "id": "6"}],
                        "meta": {"count": 2},
                    },
                },
            },
        })

        top = self.TopResource.get_item("4")
        self.assertEqual(top.lefts, [])
        self.assertEqual(top.rights, [self.RightResource.get_item("5"), self.RightResource.get_item("6")])
        self.assertEqual(top.saved, 1)

    def test_update_left__nothing(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        self.LeftResource.create_item(top=top, right_or_none=None)

        response = self.patch("http://server/lefts/2", {
            "data": {
                "type": "left",
                "id": "2",
                # No "attributes", no "relationships"
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": None},
                },
            },
        })

        left = self.LeftResource.get_item("2")
        self.assertEqual(left.top, top)
        self.assertEqual(left.right_or_none, None)
        self.assertEqual(left.saved, 0)

    def test_update_left__right_some(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        self.LeftResource.create_item(top=top, right_or_none=None)
        self.RightResource.create_item(top=top, left_or_none=None)

        response = self.patch("http://server/lefts/2", {
            "data": {
                "type": "left",
                "id": "2",
                "relationships": {
                    "rightOrNone": {"data": {"type": "right", "id": "3"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": {"type": "right", "id": "3"}},
                },
            },
        })

        left = self.LeftResource.get_item("2")
        self.assertEqual(left.top, self.TopResource.get_item("1"))
        self.assertEqual(left.right_or_none, self.RightResource.get_item("3"))
        self.assertEqual(left.saved, 1)

    def test_update_left__right_none(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        self.LeftResource.create_item(top=top, right_or_none=None)

        response = self.patch("http://server/lefts/2", {
            "data": {
                "type": "left",
                "id": "2",
                "relationships": {
                    "rightOrNone": {"data": None},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "1"}},
                    "rightOrNone": {"data": None},
                },
            },
        })

        left = self.LeftResource.get_item("2")
        self.assertEqual(left.top, self.TopResource.get_item("1"))
        self.assertEqual(left.right_or_none, None)
        self.assertEqual(left.saved, 1)

    def test_update_left__top(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        self.LeftResource.create_item(top=top, right_or_none=None)
        self.TopResource.create_item(lefts=[], rights=[])

        response = self.patch("http://server/lefts/2", {
            "data": {
                "type": "left",
                "id": "2",
                "relationships": {
                    "top": {"data": {"type": "top", "id": "3"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "left",
                "id": "2",
                "links": {"self": "http://server/lefts/2"},
                "relationships": {
                    "top": {"data": {"type": "top", "id": "3"}},
                    "rightOrNone": {"data": None},
                },
            },
        })

        left = self.LeftResource.get_item("2")
        self.assertEqual(left.top, self.TopResource.get_item("3"))
        self.assertEqual(left.right_or_none, None)
        self.assertEqual(left.saved, 1)

    def test_update_left__top_none(self):
        top = self.TopResource.create_item(lefts=[], rights=[])
        self.LeftResource.create_item(top=top, right_or_none=None)

        response = self.patch("http://server/lefts/2", {
            "data": {
                "type": "left",
                "id": "2",
                "relationships": {
                    "top": {"data": None},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())


# class TreeNode(BaseModel):
#     label: str | None = None
#     parent : TreeNode | None = None
#     children : list[TreeNode] = []

# class TreeNodeTestCase(TextCaseMixin, TestCase):
#     class NodeResource:
#         singular_name = "node"
#         plural_name = "nodes"

#         default_page_size = 2

#         Model = TreeNode

#     resources = [NodeResource()]

#     # @todo Test it allows creation without "attributes" and "relationships"
