import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from .models import Ping


class PingTests(APITransactionTestCase):
    maxDiff = None
    reset_sequences = True  # Primary keys appear in API responses

    def test_create__minimal(self):
        before = datetime.datetime.now(tz=datetime.timezone.utc)
        response = self.client.post(
            reverse("ping-list"),
            {
                "data": {
                    "type": "ping",
                    "attributes": {},
                    "relationships": {
                        "prev": {"data": None},
                        "next": {"data": []},
                    },
                },
            },
            format="vnd.api+json",
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

        response = self.client.post(
            reverse("ping-list"),
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
            format="vnd.api+json",
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
        })

        self.assertEqual(Ping.objects.count(), 3)
        ping = Ping.objects.get(id=3)
        self.assertEqual(ping.id, 3)
        self.assertEqual(ping.created_at, datetime.datetime.fromisoformat(created_at))
        self.assertEqual(ping.message, "hello")
        self.assertEqual(ping.prev.id, 1)
        self.assertEqual(ping.next.count(), 1)
        self.assertEqual(ping.next.get().id, 2)

    def test_get_one(self):
        ping = Ping.objects.create()
        response = self.client.get(reverse("ping-detail", args=[1]), format="vnd.api+json")
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

    def test_get_all(self):
        ping1 = Ping.objects.create()
        ping2 = Ping.objects.create(prev=ping1)
        ping3 = Ping.objects.create()

        response = self.client.get(reverse("ping-list"), format="vnd.api+json")
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

        response = self.client.get(response.json()["links"]["next"], format="vnd.api+json")
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
