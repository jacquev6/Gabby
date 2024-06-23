from contextlib import contextmanager
from typing import Annotated

from fastapi import Depends

from ..testing import ItemsFactory, ApiTestCase
from .batching_models import Item, Model as BatchingModel


def make_transaction():
    with BatchingTestCase.factory.atomic():
        yield

TransactionDependable = Annotated[None, Depends(make_transaction)]


class BatchingTestCase(ApiTestCase):
    class Resource:
        singular_name = "resource"
        plural_name = "resources"

        default_page_size = 2

        Model = BatchingModel

        def __init__(self, factory):
            self.factory = factory

        def create_item(self, transaction: TransactionDependable, **kwds):
            return self.factory.create(Item, **kwds)

        def get_item(self, id):
            return self.factory.get(Item, id)

        def get_page(self, sort, first_index, page_size):
            items = self.factory.get_all(Item)
            return (len(items), items[first_index:first_index + page_size])

        @contextmanager
        def save_item(self, transaction: TransactionDependable, item):
            yield
            item.saved += 1

        def delete_item(self, transaction: TransactionDependable, item):
            self.factory.delete(Item, item.id)

    factory = ItemsFactory()
    resources = [Resource(factory)]
    polymorphism = {}

    def setUp(self):
        super().setUp()
        self.factory.clear()

    def test_empty(self):
        response = self.post("http://server/batch", {"atomic:operations": []})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"atomic:results": []})

    def test_single_add(self):
        response = self.post("http://server/batch", {"atomic:operations": [
            {
                "op": "add",
                "data": {
                    "type": "resource",
                    "attributes": {
                        "name": "item1",
                    },
                },
            },
        ]})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"atomic:results": [
            {
                "data": {
                    "type": "resource",
                    "id": "1",
                    "attributes": {
                        "name": "item1",
                    },
                    "relationships": {
                        "single": {"data": None},
                        "several": {"data": [], "meta": {"count": 0}},
                    },
                    "links": {
                        "self": "http://server/resources/1",
                    },
                },
            },
        ]})

    def test_independent_adds(self):
        response = self.post("http://server/batch", {"atomic:operations": [
            {
                "op": "add",
                "data": {
                    "type": "resource",
                    "attributes": {
                        "name": "item1",
                    },
                },
            },
            {
                "op": "add",
                "data": {
                    "type": "resource",
                    "attributes": {
                        "name": "item2",
                    },
                },
            },
            {
                "op": "add",
                "data": {
                    "type": "resource",
                    "attributes": {
                        "name": "item3",
                    },
                },
            },
        ]})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"atomic:results": [
            {
                "data": {
                    "type": "resource",
                    "id": "1",
                    "attributes": {
                        "name": "item1",
                    },
                    "relationships": {
                        "single": {"data": None},
                        "several": {"data": [], "meta": {"count": 0}},
                    },
                    "links": {
                        "self": "http://server/resources/1",
                    },
                },
            },
            {
                "data": {
                    "type": "resource",
                    "id": "2",
                    "attributes": {
                        "name": "item2",
                    },
                    "relationships": {
                        "single": {"data": None},
                        "several": {"data": [], "meta": {"count": 0}},
                    },
                    "links": {
                        "self": "http://server/resources/2",
                    },
                },
            },
            {
                "data": {
                    "type": "resource",
                    "id": "3",
                    "attributes": {
                        "name": "item3",
                    },
                    "relationships": {
                        "single": {"data": None},
                        "several": {"data": [], "meta": {"count": 0}},
                    },
                    "links": {
                        "self": "http://server/resources/3",
                    },
                },
            },
        ]})

    def test_dependent_adds(self):
        response = self.post("http://server/batch", {"atomic:operations": [
            {
                "op": "add",
                "data": {
                    "type": "resource",
                    "lid": "single",
                    "attributes": {
                        "name": "item1",
                    },
                },
            },
            {
                "op": "add",
                "data": {
                    "type": "resource",
                    "lid": "several",
                    "attributes": {
                        "name": "item2",
                    },
                },
            },
            {
                "op": "add",
                "data": {
                    "type": "resource",
                    "attributes": {
                        "name": "item3",
                    },
                    "relationships": {
                        "single": {"data": {"type": "resource", "lid": "single"}},
                        "several": {"data": [{"type": "resource", "lid": "several"}]},
                    },
                },
            },
        ]})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"atomic:results": [
            {
                "data": {
                    "type": "resource",
                    "id": "1",
                    "attributes": {
                        "name": "item1",
                    },
                    "relationships": {
                        "single": {"data": None},
                        "several": {"data": [], "meta": {"count": 0}},
                    },
                    "links": {
                        "self": "http://server/resources/1",
                    },
                },
            },
            {
                "data": {
                    "type": "resource",
                    "id": "2",
                    "attributes": {
                        "name": "item2",
                    },
                    "relationships": {
                        "single": {"data": None},
                        "several": {"data": [], "meta": {"count": 0}},
                    },
                    "links": {
                        "self": "http://server/resources/2",
                    },
                },
            },
            {
                "data": {
                    "type": "resource",
                    "id": "3",
                    "attributes": {
                        "name": "item3",
                    },
                    "relationships": {
                        "single": {"data": {"type": "resource", "id": "1"}},
                        "several": {"data": [{"type": "resource", "id": "2"}], "meta": {"count": 1}},
                    },
                    "links": {
                        "self": "http://server/resources/3",
                    },
                },
            },
        ]})

    def test_atomicity(self):
        with self.assertRaises(ValueError):
            self.post("http://server/batch", {"atomic:operations": [
                {
                    "op": "add",
                    "data": {
                        "type": "resource",
                        "lid": "single",
                        "attributes": {
                            "name": "item1",
                        },
                    },
                },
                {
                    "op": "add",
                    "data": {
                        "type": "resource",
                        "lid": "several",
                        "attributes": {
                            "name": "raise",
                        },
                    },
                },
            ]})

        self.assertEqual(self.factory.commits_count, 0)
        self.assertEqual(self.factory.rollbacks_count, 1)
        self.assertEqual(len(self.factory.get_all(Item)), 0)

    # @todo Add test showing an error if a same lid is associated to several created resources

    # def _test_dependent_adds__referring_to_object_to_be_created(self):
    #     response = self.post("http://server/batch", {"atomic:operations": [
    #         {
    #             "op": "add",
    #             "data": {
    #                 "type": "resource",
    #                 "attributes": {
    #                     "name": "item1",
    #                 },
    #             },
    #         },
    #         {
    #             "op": "add",
    #             "data": {
    #                 "type": "resource",
    #                 "attributes": {
    #                     "name": "item2",
    #                 },
    #                 "relationships": {
    #                     # This object does not exist at the time of the request, so it can't be referred
    #                     "single": {"data": {"type": "resource", "id": "1"}}
    #                 },
    #             },
    #         },
    #     ]})
    #     self.assertEqual(response.status_code, 400, response.json())

    # @todo Add a test where ids are generated by client, and so it's OK to refer to an object that will be created
