from typing import Annotated
import dataclasses

from fastapi import Depends, Header, Query
from pydantic import BaseModel
from starlette import status

from ..testing import ApiTestCase



def make_foo():
    return "FOO"


class Model(BaseModel):
    foo: str
    bar: str
    host: str
    optional: str | None


@dataclasses.dataclass
class Item:
    id: str

    foo: str
    bar: str
    host: str
    optional: str | None


class Resource:
    singular_name = "resource"
    plural_name = "resources"

    default_page_size = 2

    Model = Model

    def __init__(self, bar: str):
        self.bar = bar

    def get_item(
        self,
        id: str,
        foo: Annotated[str, Depends(make_foo)],
        host: Annotated[str, Header()],
        optional: Annotated[str | None, Query()] = None,
    ):
        return Item(id=id, foo=foo, bar=self.bar, host=host, optional=optional)


class DependenciesTestCase(ApiTestCase):
    resources = [Resource("BAR")]
    polymorphism = {}

    def test_get_item__without_query(self):
        response = self.get("http://server/resources/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "1",
                "attributes": {
                    "foo": "FOO",
                    "bar": "BAR",
                    "host": "server",
                    "optional": None,
                },
                "links": {"self": "http://server/resources/1"},
            },
        })

    def test_get_item__with_query(self):
        response = self.get("http://server/resources/1?optional=OPTIONAL")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "1",
                "attributes": {
                    "foo": "FOO",
                    "bar": "BAR",
                    "host": "server",
                    "optional": "OPTIONAL",
                },
                # @todo Add '?optional=OPTIONAL' to the 'self' link
                "links": {"self": "http://server/resources/1"},
            },
        })
