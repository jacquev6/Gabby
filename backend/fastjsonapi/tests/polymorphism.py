from __future__ import annotations
from contextlib import contextmanager
import dataclasses

from pydantic import BaseModel
from starlette import status

from ..testing import ItemsFactory, ApiTestCase


# @todo Support polymorphic mandatory relationships
# @todo Support polymorphic list relationships


class AlphaPolyModel(BaseModel):
    pass

class BravoPolyModel(BaseModel):
    pass

class OptionalRelationshipModel(BaseModel):
    rel: AlphaPolyModel | BravoPolyModel | None = None

class OptionalRelationshipTestCase(ApiTestCase):
    class AlphaPolyResource:
        singular_name = "alpha_poly"
        plural_name = "alpha_polys"

        default_page_size = 2

        Model = AlphaPolyModel

        @dataclasses.dataclass
        class Item:
            id: str

        def __init__(self, factory):
            self.factory = factory

        def get_item(self, id):
            return self.factory.get(self.Item, id)

    class BravoPolyResource:
        singular_name = "bravo_poly"
        plural_name = "bravo_polys"

        default_page_size = 2

        Model = BravoPolyModel

        @dataclasses.dataclass
        class Item:
            id: str

        def __init__(self, factory):
            self.factory = factory

        def get_item(self, id):
            return self.factory.get(self.Item, id)

    class OptionalRelationshipResource:
        singular_name = "resource"
        plural_name = "resources"

        default_page_size = 2

        Model = OptionalRelationshipModel

        @dataclasses.dataclass
        class Item:
            id: str

            rel: OptionalRelationshipTestCase.AlphaPolyResource.Item | OptionalRelationshipTestCase.BravoPolyResource.Item | None

            saved: int = 0

        def __init__(self, factory):
            self.factory = factory

        def create_item(self, rel):
            return self.factory.create(self.Item, rel=rel)

        def get_item(self, id):
            return self.factory.get(self.Item, id)

        class ItemSaver:
            @contextmanager
            def __call__(self, item):
                yield
                item.saved += 1

    factory = ItemsFactory()
    resources = [AlphaPolyResource(factory), BravoPolyResource(factory), OptionalRelationshipResource(factory)]
    polymorphism = {
        AlphaPolyResource.Item: "alpha_poly",
        BravoPolyResource.Item: "bravo_poly",
    }

    def setUp(self):
        super().setUp()
        self.factory.clear()

    def test_create_item__none(self):
        response = self.post("http://server/resources", {
            "data": {
                "type": "resource",
                "relationships": {
                    "rel": {"data": None},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "1",
                "links": {"self": "http://server/resources/1"},
                "relationships": {
                    "rel": {"data": None},
                },
            },
        })

    def test_create_item__alpha(self):
        self.factory.create(self.AlphaPolyResource.Item)
        response = self.post("http://server/resources", {
            "data": {
                "type": "resource",
                "relationships": {
                    "rel": {"data": {"type": "alphaPoly", "id": "1"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "2",
                "links": {"self": "http://server/resources/2"},
                "relationships": {
                    "rel": {"data": {"type": "alphaPoly", "id": "1"}},
                },
            },
        })

    def test_create_item__bravo(self):
        self.factory.create(self.BravoPolyResource.Item)
        response = self.post("http://server/resources", {
            "data": {
                "type": "resource",
                "relationships": {
                    "rel": {"data": {"type": "bravoPoly", "id": "1"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "2",
                "links": {"self": "http://server/resources/2"},
                "relationships": {
                    "rel": {"data": {"type": "bravoPoly", "id": "1"}},
                },
            },
        })

    def test_get_item__none(self):
        self.factory.create(self.OptionalRelationshipResource.Item, rel=None)
        response = self.get("http://server/resources/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "1",
                "links": {"self": "http://server/resources/1"},
                "relationships": {
                    "rel": {"data": None},
                },
            },
        })

    def test_get_item__alpha(self):
        self.factory.create(self.OptionalRelationshipResource.Item, rel=self.factory.create(self.AlphaPolyResource.Item))
        response = self.get("http://server/resources/2")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "2",
                "links": {"self": "http://server/resources/2"},
                "relationships": {
                    "rel": {"data": {"type": "alphaPoly", "id": "1"}},
                },
            },
        })

    def test_get_item__bravo(self):
        self.factory.create(self.OptionalRelationshipResource.Item, rel=self.factory.create(self.BravoPolyResource.Item))
        response = self.get("http://server/resources/2")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "2",
                "links": {"self": "http://server/resources/2"},
                "relationships": {
                    "rel": {"data": {"type": "bravoPoly", "id": "1"}},
                },
            },
        })

    def test_update_item__none_to_alpha(self):
        item = self.factory.create(self.OptionalRelationshipResource.Item, rel=None)
        alpha = self.factory.create(self.AlphaPolyResource.Item)
        response = self.patch("http://server/resources/1", {
            "data": {
                "type": "resource",
                "id": "1",
                "relationships": {
                    "rel": {"data": {"type": "alphaPoly", "id": "2"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "1",
                "links": {"self": "http://server/resources/1"},
                "relationships": {
                    "rel": {"data": {"type": "alphaPoly", "id": "2"}},
                },
            },
        })
        self.assertEqual(item.rel, alpha)
        self.assertEqual(item.saved, 1)

    def test_update_item__alpha_to_none(self):
        item = self.factory.create(self.OptionalRelationshipResource.Item, rel=self.factory.create(self.AlphaPolyResource.Item))
        response = self.patch("http://server/resources/2", {
            "data": {
                "type": "resource",
                "id": "2",
                "relationships": {
                    "rel": {"data": None},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "2",
                "links": {"self": "http://server/resources/2"},
                "relationships": {
                    "rel": {"data": None},
                },
            },
        })
        self.assertEqual(item.rel, None)
        self.assertEqual(item.saved, 1)

    def test_update_item__alpha_to_bravo(self):
        item = self.factory.create(self.OptionalRelationshipResource.Item, rel=self.factory.create(self.AlphaPolyResource.Item))
        bravo = self.factory.create(self.BravoPolyResource.Item)
        response = self.patch("http://server/resources/2", {
            "data": {
                "type": "resource",
                "id": "2",
                "relationships": {
                    "rel": {"data": {"type": "bravoPoly", "id": "3"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "2",
                "links": {"self": "http://server/resources/2"},
                "relationships": {
                    "rel": {"data": {"type": "bravoPoly", "id": "3"}},
                },
            },
        })
        self.assertEqual(item.rel, bravo)
        self.assertEqual(item.saved, 1)
