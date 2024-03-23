from typing import Annotated
import dataclasses

from django.test import TestCase
from fastapi import Header
from pydantic import BaseModel
from starlette import status

from ..testing import TestMixin


class Model(BaseModel):
    foo: str | None
    host: str | None


@dataclasses.dataclass
class Item:
    id: str

    foo: str | None
    host: str | None


class Resource:
    singular_name = "resource"
    plural_name = "resources"

    default_page_size = 2

    Model = Model

    class ItemGetter:
        def __init__(
            self,
            foo: str | None = None,
            host: Annotated[str | None, Header()] = None
        ):
            self.foo = foo
            self.host = host

        def __call__(self, id: str):
            return Item(
                id=id,
                foo=self.foo,
                host=self.host,
            )


class DependenciesTestCase(TestMixin, TestCase):
    resources = [Resource()]

    def test_get_item__no_foo(self):
        response = self.get("http://server/resources/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "1",
                "attributes": {
                    "foo": None,
                    "host": "server",
                },
                "links": {"self": "http://server/resources/1"},
            },
        })

    def test_get_item__some_foo(self):
        response = self.get("http://blahblah/resources/1?foo=bar")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "resource",
                "id": "1",
                "attributes": {
                    "foo": "bar",
                    "host": "blahblah",
                },
                "links": {"self": "http://blahblah/resources/1"},
            },
        })
