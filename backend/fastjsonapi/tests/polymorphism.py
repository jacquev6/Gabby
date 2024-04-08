from contextlib import contextmanager
from typing import Annotated
import dataclasses

from django.test import TestCase
from fastapi import Depends
from pydantic import BaseModel
from starlette import status

from ..testing import ItemsFactory, TestMixin


class AlphaPolyModel(BaseModel):
    pass

class BravoPolyModel(BaseModel):
    pass

class OptionalRelationshipModel(BaseModel):
    rel: AlphaPolyModel | BravoPolyModel | None = None

# @todo Support polymorphic mandatory relationships
# @todo Support polymorphic list relationships

@dataclasses.dataclass
class AlphaPolyItem:
    id: str

@dataclasses.dataclass
class BravoPolyItem:
    id: str

@dataclasses.dataclass
class OptionalRelationshipItem:
    id: str

    rel: AlphaPolyItem | BravoPolyItem | None

    saved: int = 0

class OptionalRelationshipFactoryMixin:
    def __init__(self, factory: Annotated[ItemsFactory, Depends(lambda: OptionalRelationshipTestCase.factory)]):
        self.factory = factory

class AlphaPolyResource:
    singular_name = "alpha_poly"
    plural_name = "alpha_polys"

    default_page_size = 2

    Model = AlphaPolyModel

    class ItemGetter(OptionalRelationshipFactoryMixin):
        def __call__(self, id):
            return self.factory.get(AlphaPolyItem, id)

class BravoPolyResource:
    singular_name = "bravo_poly"
    plural_name = "bravo_polys"

    default_page_size = 2

    Model = BravoPolyModel

    class ItemGetter(OptionalRelationshipFactoryMixin):
        def __call__(self, id):
            return self.factory.get(BravoPolyItem, id)

class OptionalRelationshipResource:
    singular_name = "resource"
    plural_name = "resources"

    default_page_size = 2

    Model = OptionalRelationshipModel

    class ItemCreator(OptionalRelationshipFactoryMixin):
        def __call__(self, rel):
            return self.factory.create(OptionalRelationshipItem, rel=rel)

    class ItemGetter(OptionalRelationshipFactoryMixin):
        def __call__(self, id):
            return self.factory.get(OptionalRelationshipItem, id)

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            yield
            item.saved += 1

class OptionalRelationshipTestCase(TestMixin, TestCase):
    resources = [AlphaPolyResource(), BravoPolyResource(), OptionalRelationshipResource()]
    polymorphism = {
        AlphaPolyItem: "alpha_poly",
        BravoPolyItem: "bravo_poly",
    }

    def setUp(self):
        super().setUp()
        self.__class__.factory = ItemsFactory()

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
        self.factory.create(AlphaPolyItem)
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

    def test_create_item__alpha__include(self):
        self.factory.create(AlphaPolyItem)
        response = self.post("http://server/resources?include=rel", {
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
            "included": [
                {
                    "type": "alphaPoly",
                    "id": "1",
                    "links": {"self": "http://server/alphaPolys/1"},
                },
            ],
        })

    def test_create_item__bravo(self):
        self.factory.create(BravoPolyItem)
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

    def test_create_item__bravo__include(self):
        self.factory.create(BravoPolyItem)
        response = self.post("http://server/resources?include=rel", {
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
            "included": [
                {
                    "type": "bravoPoly",
                    "id": "1",
                    "links": {"self": "http://server/bravoPolys/1"},
                },
            ],
        })

    def test_get_item__none(self):
        self.factory.create(OptionalRelationshipItem, rel=None)
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

    def test_get_item__none__include(self):
        self.factory.create(OptionalRelationshipItem, rel=None)
        response = self.get("http://server/resources/1?include=rel")
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
            "included": [],
        })

    def test_get_item__alpha(self):
        self.factory.create(OptionalRelationshipItem, rel=self.factory.create(AlphaPolyItem))
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

    def test_get_item__alpha__include(self):
        self.factory.create(OptionalRelationshipItem, rel=self.factory.create(AlphaPolyItem))
        response = self.get("http://server/resources/2?include=rel")
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
            "included": [
                {
                    "type": "alphaPoly",
                    "id": "1",
                    "links": {"self": "http://server/alphaPolys/1"},
                },
            ],
        })

    def test_get_item__bravo(self):
        self.factory.create(OptionalRelationshipItem, rel=self.factory.create(BravoPolyItem))
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

    def test_get_item__bravo__include(self):
        self.factory.create(OptionalRelationshipItem, rel=self.factory.create(BravoPolyItem))
        response = self.get("http://server/resources/2?include=rel")
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
            "included": [
                {
                    "type": "bravoPoly",
                    "id": "1",
                    "links": {"self": "http://server/bravoPolys/1"},
                },
            ],
        })

    def test_update_item__none_to_alpha(self):
        item = self.factory.create(OptionalRelationshipItem, rel=None)
        alpha = self.factory.create(AlphaPolyItem)
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

    def test_update_item__none_to_alpha__include(self):
        self.factory.create(OptionalRelationshipItem, rel=None)
        self.factory.create(AlphaPolyItem)
        response = self.patch("http://server/resources/1?include=rel", {
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
            "included": [
                {
                    "type": "alphaPoly",
                    "id": "2",
                    "links": {"self": "http://server/alphaPolys/2"},
                },
            ],
        })

    def test_update_item__alpha_to_none(self):
        item = self.factory.create(OptionalRelationshipItem, rel=self.factory.create(AlphaPolyItem))
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
        item = self.factory.create(OptionalRelationshipItem, rel=self.factory.create(AlphaPolyItem))
        bravo = self.factory.create(BravoPolyItem)
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
