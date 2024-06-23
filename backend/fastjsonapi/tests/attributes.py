from contextlib import contextmanager
from typing import Annotated
import dataclasses
import datetime

from pydantic import BaseModel
from starlette import status

from ..annotations import Computed, Constant, Secret
from ..testing import ApiTestCase, ItemsFactory
from ..filtering import make_filters


# @todo Split these test cases: make one for each kind of attribute:
# - each of the existing in 'AtomicAttributesTestCase.Resource.Model'
# - int | None, without default
# @todo Add tests for each (relevant) combination of presence/absence of 'create_item', 'get_item', 'get_page', 'save_item', 'delete_item'


class AtomicAttributesTestCase(ApiTestCase):
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

        @dataclasses.dataclass
        class Item:
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

        def __init__(self, factory):
            self.factory = factory

        def create_item(self, **kwds):
            return self.factory.create(self.Item, **kwds)

        def get_item(self, id: str):
            return self.factory.get(self.Item, id)

        class Filters(BaseModel):
            computed_str: str | None

        def get_page(self, sort, filters: Annotated[Filters, make_filters(Filters)], first_index, page_size):
            items = self.factory.get_all(self.Item)
            if filters.computed_str:
                items = [item for item in items if item.computed_str == filters.computed_str]
            return (len(items), items[first_index:first_index + page_size])

        @contextmanager
        def save_item(self, item):
            yield
            item.saved += 1

        def delete_item(self, item):
            self.factory.delete(self.Item, item.id)

    factory = ItemsFactory()
    resources = [Resource(factory)]
    polymorphism = {}

    def setUp(self):
        super().setUp()
        self.factory.clear()

    # @todo Add tests where the id is given by the client (sha256, etc.)

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

        item = self.factory.get(self.Resource.Item, "1")
        self.assertEqual(item.plain_int, 57)
        self.assertEqual(item.defaulted_datetime, datetime.datetime(2024, 3, 18, 15, 38, 15, tzinfo=datetime.timezone.utc))
        self.assertEqual(item.constant_str, "Constant string")
        self.assertEqual(item.defaulted_constant_float, 3.14)
        self.assertEqual(item.secret_str, "My password")
        self.assertEqual(item.computed_str, "MY PASSWORD")
        self.assertEqual(item.saved, 0)

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

        item = self.factory.get(self.Resource.Item, "1")
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
        self.assertEqual(self.factory.create(self.Resource.Item).id, "1")

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
            self.factory.create(self.Resource.Item, plain_int=i + 1)

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
            self.factory.create(self.Resource.Item, plain_int=i + 1)

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
            self.factory.create(self.Resource.Item, plain_int=i + 1)

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
            self.factory.create(self.Resource.Item, plain_int=i + 1)

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
                "first": "http://server/resources?page%5Bsize%5D=3&page%5Bnumber%5D=1",
                "last": "http://server/resources?page%5Bsize%5D=3&page%5Bnumber%5D=2",
                "next": "http://server/resources?page%5Bsize%5D=3&page%5Bnumber%5D=2",
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
            self.factory.create(self.Resource.Item, plain_int=i + 1)

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
            self.factory.create(self.Resource.Item, plain_int=i + 1)

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
                "first": "http://server/resources?page%5Bsize%5D=5&page%5Bnumber%5D=1",
                "last": "http://server/resources?page%5Bsize%5D=5&page%5Bnumber%5D=1",
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
            self.factory.create(self.Resource.Item, plain_int=i + 1, secret_str=secret_str)

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
            self.factory.create(self.Resource.Item, plain_int=i + 1, secret_str=secret_str)

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

    # @todo Add tests for sorting

    def test_update__nothing(self):
        self.assertEqual(self.factory.create(self.Resource.Item).id, "1")

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

        item = self.factory.get(self.Resource.Item, "1")
        self.assertEqual(item.plain_int, 42)
        self.assertEqual(item.defaulted_datetime, datetime.datetime(2021, 1, 1, 1, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(item.constant_str, "Constant")
        self.assertEqual(item.defaulted_constant_float, 6.18)
        self.assertEqual(item.secret_str, "Secret")
        self.assertEqual(item.computed_str, "SECRET")
        self.assertEqual(item.saved, 0)

    def test_update__one(self):
        self.assertEqual(self.factory.create(self.Resource.Item).id, "1")

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

        item = self.factory.get(self.Resource.Item, "1")
        self.assertEqual(item.plain_int, 57)
        self.assertEqual(item.defaulted_datetime, datetime.datetime(2021, 1, 1, 1, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(item.constant_str, "Constant")
        self.assertEqual(item.defaulted_constant_float, 6.18)
        self.assertEqual(item.secret_str, "Secret")
        self.assertEqual(item.computed_str, "SECRET")
        self.assertEqual(item.saved, 1)

    def test_update__all(self):
        self.assertEqual(self.factory.create(self.Resource.Item).id, "1")

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

        item = self.factory.get(self.Resource.Item, "1")
        self.assertEqual(item.plain_int, 57)
        self.assertEqual(item.defaulted_datetime, datetime.datetime(2024, 1, 2, 3, 4, 5, tzinfo=datetime.timezone(datetime.timedelta(hours=1))))
        self.assertEqual(item.constant_str, "Constant")
        self.assertEqual(item.defaulted_constant_float, 6.18)
        self.assertEqual(item.secret_str, "My password")
        self.assertEqual(item.computed_str, "MY PASSWORD")
        self.assertEqual(item.saved, 1)

    def test_update__computed(self):
        self.assertEqual(self.factory.create(self.Resource.Item).id, "1")

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
        self.assertEqual(self.factory.create(self.Resource.Item).id, "1")

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
        self.assertEqual(self.factory.create(self.Resource.Item).id, "1")

        response = self.delete(f"http://server/resources/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertIsNone(self.factory.get(self.Resource.Item, "1"))


class CompoundAttributesTestCase(ApiTestCase):
    class Resource:
        singular_name = "resource"
        plural_name = "resources"

        default_page_size = 2

        class Model(BaseModel):
            class Rectangle(BaseModel):
                class Point(BaseModel):
                    x: float
                    y: float

                tl: Point
                br: Point

            d: dict
            l: list
            r: Rectangle

        @dataclasses.dataclass
        class Item:
            @dataclasses.dataclass
            class Rectangle:
                @dataclasses.dataclass
                class Point:
                    x: float
                    y: float

                tl: Point
                br: Point

            id: str

            d: dict
            l: list
            r: Rectangle

            saved: int = 0

        def __init__(self, factory):
            self.factory = factory

        def create_item(self, **kwds):
            return self.factory.create(self.Item, **kwds)

        def get_item(self, id):
            return self.factory.get(self.Item, id)

        @contextmanager
        def save_item(self, item):
            yield
            item.saved += 1

        def delete_item(self, item):
            self.factory.delete(self.Item, item.id)

    factory = ItemsFactory()
    resources = [Resource(factory)]
    polymorphism = {}

    def setUp(self):
        super().setUp()
        self.factory.clear()

    def test_create(self):
        response = self.post("http://server/resources", {
            "data": {
                "type": "resource",
                "attributes": {
                    "d": {"a": 1},
                    "l": [2, 3],
                    "r": {"tl": {"x": 4, "y": 5}, "br": {"x": 6, "y": 7}},
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
                    "d": {"a": 1},
                    "l": [2, 3],
                    "r": {"tl": {"x": 4, "y": 5}, "br": {"x": 6, "y": 7}},
                },
            },
        })

        item = self.factory.get(self.Resource.Item, "1")
        self.assertEqual(item.d, {"a": 1})
        self.assertEqual(item.l, [2, 3])
        self.assertEqual(item.r.tl.x, 4)
        self.assertEqual(item.r.tl.y, 5)
        self.assertEqual(item.r.br.x, 6)
        self.assertEqual(item.r.br.y, 7)

    def test_get_item(self):
        self.factory.create(
            self.Resource.Item,
            d={"a": 1},
            l=[2, 3],
            r=self.Resource.Item.Rectangle(
                tl=self.Resource.Item.Rectangle.Point(x=4, y=5),
                br=self.Resource.Item.Rectangle.Point(x=6, y=7),
            ),
        )

        response = self.get(f"http://server/resources/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "1",
                "links": {"self": f"http://server/resources/1"},
                "attributes": {
                    "d": {"a": 1},
                    "l": [2, 3],
                    "r": {"tl": {"x": 4, "y": 5}, "br": {"x": 6, "y": 7}},
                },
            },
        })

    def test_update__nothing(self):
        self.factory.create(
            self.Resource.Item,
            d={"a": 1},
            l=[2, 3],
            r=self.Resource.Item.Rectangle(
                tl=self.Resource.Item.Rectangle.Point(x=4, y=5),
                br=self.Resource.Item.Rectangle.Point(x=6, y=7),
            ),
        )

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
                    "d": {"a": 1},
                    "l": [2, 3],
                    "r": {"tl": {"x": 4, "y": 5}, "br": {"x": 6, "y": 7}},
                },
            },
        })

        item = self.factory.get(self.Resource.Item, "1")
        self.assertEqual(item.d, {"a": 1})
        self.assertEqual(item.l, [2, 3])
        self.assertEqual(item.r.tl.x, 4)
        self.assertEqual(item.r.tl.y, 5)
        self.assertEqual(item.r.br.x, 6)
        self.assertEqual(item.r.br.y, 7)
        self.assertEqual(item.saved, 0)

    def test_update__all(self):
        self.factory.create(
            self.Resource.Item,
            d={"a": 1},
            l=[2, 3],
            r=self.Resource.Item.Rectangle(
                tl=self.Resource.Item.Rectangle.Point(x=4, y=5),
                br=self.Resource.Item.Rectangle.Point(x=6, y=7),
            ),
        )

        response = self.patch(f"http://server/resources/1", {
            "data": {
                "type": "resource",
                "id": "1",
                "attributes": {
                    "d": {"a": 10},
                    "l": [20, 30],
                    "r": {"tl": {"x": 40, "y": 50}, "br": {"x": 60, "y": 70}},
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
                    "d": {"a": 10},
                    "l": [20, 30],
                    "r": {"tl": {"x": 40, "y": 50}, "br": {"x": 60, "y": 70}},
                },
            },
        })

        item = self.factory.get(self.Resource.Item, "1")
        self.assertEqual(item.d, {"a": 10})
        self.assertEqual(item.l, [20, 30])
        self.assertEqual(item.r.tl.x, 40)
        self.assertEqual(item.r.tl.y, 50)
        self.assertEqual(item.r.br.x, 60)
        self.assertEqual(item.r.br.y, 70)
        self.assertEqual(item.saved, 1)
