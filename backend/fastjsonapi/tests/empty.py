import dataclasses

from pydantic import BaseModel
from starlette import status

from ..testing import ApiTestCase, ItemsFactory


class EmptyTestCase(ApiTestCase):
    class Resource:
        singular_name = "empty_resource"
        plural_name = "empty_resources"

        default_page_size = 2

        class Model(BaseModel):
            pass

        @dataclasses.dataclass
        class Item:
            id: str

        def __init__(self):
            self.factory = ItemsFactory()

        def get_item(self, id):
            return None

        def create_item(self, **kwds):
            return self.Item(id="1")

    resources = [Resource()]
    polymorphism = {}

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
