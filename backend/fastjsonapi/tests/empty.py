from typing import Annotated
import dataclasses

from fastapi import Depends
from pydantic import BaseModel
from starlette import status

from ..testing import ApiTestCase, ItemsFactory



@dataclasses.dataclass
class Item:
    id: str

    saved: int = 0


class FactoryMixin:
    def __init__(self, factory: Annotated[ItemsFactory, Depends(lambda: EmptyTestCase.factory)]):
        self.factory = factory


class Resource:
    singular_name = "empty_resource"
    plural_name = "empty_resources"

    default_page_size = 2

    class Model(BaseModel):
        pass

    class ItemGetter(FactoryMixin):
        def __call__(self, id):
            return self.factory.get(Item, id)

    class ItemCreator(FactoryMixin):
        def __call__(self, **kwds):
            return self.factory.create(Item, **kwds)


class EmptyTestCase(ApiTestCase):
    resources = [Resource()]
    polymorphism = {}

    def setUp(self):
        super().setUp()
        self.__class__.factory = ItemsFactory()

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
