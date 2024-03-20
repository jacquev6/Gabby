import datetime
import json
import os

from django.test import TransactionTestCase, TestCase
from fastapi.testclient import TestClient
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from .models import Ping
from main import app


class PingTestsMixin:
    maxDiff = None
    reset_sequences = True  # Primary keys appear in API responses

    def test_create__minimal(self):
        before = datetime.datetime.now(tz=datetime.timezone.utc)
        response = self.post(
            "http://testserver/api/pings",
            {
                "data": {
                    "type": "ping",
                    "attributes": {},  # @todo Remove
                    "relationships": {  # @todo Remove
                        "prev": {"data": None},
                        "next": {"data": []},
                    },
                },
            },
        )
        after = datetime.datetime.now(tz=datetime.timezone.utc)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        created_at = response.json()["data"]["attributes"]["createdAt"]
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "1",
                "links": {"self": "http://testserver/api/pings/1"},
                "attributes": {
                    "createdAt": created_at,
                    "message": None,
                },
                "relationships": {
                    "prev": {"data": None},
                    "next": {"data": [], "meta": {"count": 0}},
                },
            },
        })

        created_at = datetime.datetime.fromisoformat(created_at)
        self.assertGreaterEqual(created_at, before)
        self.assertLessEqual(created_at, after)

        self.assertEqual(Ping.objects.count(), 1)
        ping = Ping.objects.get()
        self.assertEqual(ping.id, 1)
        self.assertEqual(ping.created_at, created_at)
        self.assertIsNone(ping.message)
        self.assertIsNone(ping.prev)
        self.assertEqual(ping.next.count(), 0)

    def test_create__full(self):
        self.assertEqual(Ping.objects.create().id, 1)
        self.assertEqual(Ping.objects.create().id, 2)

        response = self.post(
            "http://testserver/api/pings?include=prev,next",
            {
                "data": {
                    "type": "ping",
                    "attributes": {
                        "message": "hello",
                    },
                    "relationships": {
                        "prev": {"data": {"type": "ping", "id": "1"}},
                        "next": {"data": [{"type": "ping", "id": "2"}]},
                    },
                },
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        created_at = response.json()["data"]["attributes"]["createdAt"]
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "3",
                "links": {"self": "http://testserver/api/pings/3"},
                "attributes": {
                    "createdAt": created_at,
                    "message": "hello",
                },
                "relationships": {
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [{"type": "ping", "id": "2"}], "meta": {"count": 1}},
                },
            },
            "included": [
                {
                    "type": "ping",
                    "id": "1",
                    "links": {"self": "http://testserver/api/pings/1"},
                    "attributes": {
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "message": None,
                    },
                    "relationships": {
                        "prev": {"data": None},
                        "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                    },
                },
                {
                    "type": "ping",
                    "id": "2",
                    "links": {"self": "http://testserver/api/pings/2"},
                    "attributes": {
                        "createdAt": response.json()["included"][1]["attributes"]["createdAt"],
                        "message": None,
                    },
                    "relationships": {
                        "prev": {"data": {"type": "ping", "id": "3"}},
                        "next": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
        })

        self.assertEqual(Ping.objects.count(), 3)
        ping = Ping.objects.get(id=3)
        self.assertEqual(ping.id, 3)
        self.assertEqual(ping.created_at, datetime.datetime.fromisoformat(created_at))
        self.assertEqual(ping.message, "hello")
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=2)])

    def test_get_one(self):
        ping = Ping.objects.create()
        response = self.get("http://testserver/api/pings/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "1",
                "links": {"self": "http://testserver/api/pings/1"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "message": None,
                },
                "relationships": {
                    "prev": {"data": None},
                    "next": {"data": [], "meta": {"count": 0}},
                },
            },
        })

    def test_get_one__nonexisting(self):
        ping = Ping.objects.create()
        response = self.get("http://testserver/api/pings/0")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.json())

    def test_get_all(self):
        ping1 = Ping.objects.create()
        ping2 = Ping.objects.create(prev=ping1)
        ping3 = Ping.objects.create()

        response = self.get("http://testserver/api/pings")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "ping",
                    "id": "1",
                    "links": {"self": "http://testserver/api/pings/1"},
                    "attributes": {
                        "createdAt": ping1.created_at.isoformat().replace("+00:00", "Z"),
                        "message": None,
                    },
                    "relationships": {
                        "prev": {"data": None},
                        "next": {"data": [{"type": "ping", "id": "2"}], "meta": {"count": 1}},
                    },
                },
                {
                    "type": "ping",
                    "id": "2",
                    "links": {"self": "http://testserver/api/pings/2"},
                    "attributes": {
                        "createdAt": ping2.created_at.isoformat().replace("+00:00", "Z"),
                        "message": None,
                    },
                    "relationships": {
                        "prev": {"data": {"type": "ping", "id": "1"}},
                        "next": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/pings?page%5Bnumber%5D=1",
                "last": "http://testserver/api/pings?page%5Bnumber%5D=2",
                "next": "http://testserver/api/pings?page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {
                "pagination": {"count": 3, "page": 1, "pages": 2},
            },
        })

        response = self.get(response.json()["links"]["next"])
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "ping",
                    "id": "3",
                    "links": {"self": "http://testserver/api/pings/3"},
                    "attributes": {
                        "createdAt": ping3.created_at.isoformat().replace("+00:00", "Z"),
                        "message": None,
                    },
                    "relationships": {
                        "prev": {"data": None},
                        "next": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/pings?page%5Bnumber%5D=1",
                "last": "http://testserver/api/pings?page%5Bnumber%5D=2",
                "next": None,
                "prev": "http://testserver/api/pings?page%5Bnumber%5D=1",
            },
            "meta": {
                "pagination": {"count": 3, "page": 2, "pages": 2},
            },
        })

    # @todo Add tests for the 'filter[message]': one where it's set to a string, and one where it's set to null. How do we even set a query parameter to null?

    def test_update_nothing(self):
        ping = Ping.objects.create(message="Hello", prev=Ping.objects.create())
        Ping.objects.create(prev=ping)

        response = self.patch("http://testserver/api/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://testserver/api/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                },
            },
        })

        ping = Ping.objects.get(id=2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=3)])

    def test_update_message(self):
        ping = Ping.objects.create(message="Hello", prev=Ping.objects.create())
        Ping.objects.create(prev=ping)

        response = self.patch("http://testserver/api/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "attributes": {
                    "message": "Bonjour",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://testserver/api/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "message": "Bonjour",
                },
                "relationships": {
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                },
            },
        })

        ping = Ping.objects.get(id=2)
        self.assertEqual(ping.message, "Bonjour")
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=3)])

    def test_update_message_to_none(self):
        ping = Ping.objects.create(message="Hello", prev=Ping.objects.create())
        Ping.objects.create(prev=ping)

        response = self.patch("http://testserver/api/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "attributes": {
                    "message": None,
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://testserver/api/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "message": None,
                },
                "relationships": {
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                },
            },
        })

        ping = Ping.objects.get(id=2)
        self.assertEqual(ping.message, None)
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=3)])

    def test_update_prev(self):
        ping = Ping.objects.create(message="Hello", prev=Ping.objects.create())
        Ping.objects.create(prev=ping)
        Ping.objects.create()

        response = self.patch("http://testserver/api/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "relationships": {
                    "prev": {"data": {"type": "ping", "id": "4"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://testserver/api/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "prev": {"data": {"type": "ping", "id": "4"}},
                    "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                },
            },
        })

        ping = Ping.objects.get(id=2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, Ping.objects.get(id=4))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=3)])

    def test_update_prev_to_none(self):
        ping = Ping.objects.create(message="Hello", prev=Ping.objects.create())
        Ping.objects.create(prev=ping)

        response = self.patch("http://testserver/api/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "relationships": {
                    "prev": {"data": None},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://testserver/api/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "prev": {"data": None},
                    "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                },
            },
        })

        ping = Ping.objects.get(id=2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, None)
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=3)])

    def test_update_next(self):
        ping = Ping.objects.create(message="Hello", prev=Ping.objects.create())
        Ping.objects.create(prev=ping)
        Ping.objects.create()

        response = self.patch("http://testserver/api/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "relationships": {
                    "next": {"data": [{"type": "ping", "id": "4"}]},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://testserver/api/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [{"type": "ping", "id": "4"}], "meta": {"count": 1}},
                },
            },
        })

        ping = Ping.objects.get(id=2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=4)])

    def test_update_next_to_empty(self):
        ping = Ping.objects.create(message="Hello", prev=Ping.objects.create())
        Ping.objects.create(prev=ping)

        response = self.patch("http://testserver/api/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "relationships": {
                    "next": {"data": []},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://testserver/api/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [], "meta": {"count": 0}},
                },
            },
        })

        ping = Ping.objects.get(id=2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [])


class PingTestsAgainstDjango(PingTestsMixin, APITransactionTestCase):
    def post(self, url, payload):
        return self.client.post(url, payload, format="vnd.api+json")

    def get(self, url):
        return self.client.get(url, format="vnd.api+json")

    def patch(self, url, payload):
        return self.client.patch(url, payload, format="vnd.api+json")


class PingTestsAgainstFastApi(PingTestsMixin, TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.__client = TestClient(app)

    def get(self, url):
        return self.__client.get(url, headers={"Content-Type": "application/vnd.api+json"})

    def post(self, url, payload):
        return self.__client.post(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})

    def patch(self, url, payload):
        return self.__client.patch(url, content=json.dumps(payload), headers={"Content-Type": "application/vnd.api+json"})


class SchemaTest(TestCase):
    def test(self):
        file_path = os.path.join(os.path.dirname(__file__), "..", "openapi.json")
        with open(file_path) as file:
            expected = json.load(file)

        response = TestClient(app).get("http://server/api/openapi.json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        actual = response.json()

        try:
            self.assertEqual(actual, expected)
        finally:
            with open(file_path, "w") as file:
                json.dump(actual, file, indent=2, sort_keys=True)
                file.write("\n")
