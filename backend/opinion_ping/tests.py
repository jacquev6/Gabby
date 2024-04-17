import datetime

from starlette import status
from django.test import TransactionTestCase
import django.contrib.auth

from .models import Ping
from .resources import PingsResource
from fastjsonapi.django import UserResource
from fastjsonapi.testing import TestMixin


User = django.contrib.auth.get_user_model()


class PingTestCase(TestMixin, TransactionTestCase):
    reset_sequences = True  # Primary keys appear in API responses

    resources = [UserResource(), PingsResource()]

    def test_create__minimal(self):
        before = datetime.datetime.now(tz=datetime.timezone.utc)
        response = self.post(
            "http://server/pings",
            {
                "data": {
                    "type": "ping",
                },
            },
        )
        after = datetime.datetime.now(tz=datetime.timezone.utc)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        created_at = response.json()["data"]["attributes"]["createdAt"]
        updated_at = response.json()["data"]["attributes"]["updatedAt"]
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "1",
                "links": {"self": "http://server/pings/1"},
                "attributes": {
                    "createdAt": created_at,
                    "updatedAt": updated_at,
                    "message": None,
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": None},
                    "next": {"data": [], "meta": {"count": 0}},
                },
            },
        })

        created_at = datetime.datetime.fromisoformat(created_at)
        updated_at = datetime.datetime.fromisoformat(updated_at)
        self.assertGreaterEqual(created_at, before)
        self.assertLessEqual(created_at, after)
        self.assertGreaterEqual(updated_at, before)
        self.assertLessEqual(updated_at, after)

        self.assertEqual(Ping.objects.count(), 1)
        ping = Ping.objects.get()
        self.assertEqual(ping.id, 1)
        self.assertEqual(ping.created_at, created_at)
        self.assertEqual(ping.created_by, None)
        self.assertEqual(ping.updated_at, updated_at)
        self.assertEqual(ping.updated_by, None)
        self.assertIsNone(ping.message)
        self.assertIsNone(ping.prev)
        self.assertEqual(ping.next.count(), 0)

    def test_create__full(self):
        self.assertEqual(Ping.objects.create().id, 1)
        self.assertEqual(Ping.objects.create().id, 2)

        response = self.post(
            "http://server/pings?include=prev,next",
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
        updated_at = response.json()["data"]["attributes"]["updatedAt"]
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "3",
                "links": {"self": "http://server/pings/3"},
                "attributes": {
                    "createdAt": created_at,
                    "updatedAt": updated_at,
                    "message": "hello",
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [{"type": "ping", "id": "2"}], "meta": {"count": 1}},
                },
            },
            "included": [
                {
                    "type": "ping",
                    "id": "1",
                    "links": {"self": "http://server/pings/1"},
                    "attributes": {
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                        "message": None,
                    },
                    "relationships": {
                        "createdBy": {"data": None},
                        "updatedBy": {"data": None},
                        "prev": {"data": None},
                        "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                    },
                },
                {
                    "type": "ping",
                    "id": "2",
                    "links": {"self": "http://server/pings/2"},
                    "attributes": {
                        "createdAt": response.json()["included"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][1]["attributes"]["updatedAt"],
                        "message": None,
                    },
                    "relationships": {
                        "createdBy": {"data": None},
                        "updatedBy": {"data": None},
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
        self.assertEqual(ping.created_by, None)
        self.assertEqual(ping.updated_at, datetime.datetime.fromisoformat(updated_at))
        self.assertEqual(ping.updated_by, None)
        self.assertEqual(ping.message, "hello")
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=2)])

    def test_get_one(self):
        ping = Ping.objects.create()
        response = self.get("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "1",
                "links": {"self": "http://server/pings/1"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "updatedAt": ping.updated_at.isoformat().replace("+00:00", "Z"),
                    "message": None,
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": None},
                    "next": {"data": [], "meta": {"count": 0}},
                },
            },
        })

    def test_get_one__nonexisting(self):
        ping = Ping.objects.create()
        response = self.get("http://server/pings/0")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.json())

    def test_get_all(self):
        ping1 = Ping.objects.create()
        ping2 = Ping.objects.create(prev=ping1)
        ping3 = Ping.objects.create()

        response = self.get("http://server/pings")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "ping",
                    "id": "1",
                    "links": {"self": "http://server/pings/1"},
                    "attributes": {
                        "createdAt": ping1.created_at.isoformat().replace("+00:00", "Z"),
                        "updatedAt": ping1.updated_at.isoformat().replace("+00:00", "Z"),
                        "message": None,
                    },
                    "relationships": {
                        "createdBy": {"data": None},
                        "updatedBy": {"data": None},
                        "prev": {"data": None},
                        "next": {"data": [{"type": "ping", "id": "2"}], "meta": {"count": 1}},
                    },
                },
                {
                    "type": "ping",
                    "id": "2",
                    "links": {"self": "http://server/pings/2"},
                    "attributes": {
                        "createdAt": ping2.created_at.isoformat().replace("+00:00", "Z"),
                        "updatedAt": ping2.updated_at.isoformat().replace("+00:00", "Z"),
                        "message": None,
                    },
                    "relationships": {
                        "createdBy": {"data": None},
                        "updatedBy": {"data": None},
                        "prev": {"data": {"type": "ping", "id": "1"}},
                        "next": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "links": {
                "first": "http://server/pings?page%5Bnumber%5D=1",
                "last": "http://server/pings?page%5Bnumber%5D=2",
                "next": "http://server/pings?page%5Bnumber%5D=2",
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
                    "links": {"self": "http://server/pings/3"},
                    "attributes": {
                        "createdAt": ping3.created_at.isoformat().replace("+00:00", "Z"),
                        "updatedAt": ping3.updated_at.isoformat().replace("+00:00", "Z"),
                        "message": None,
                    },
                    "relationships": {
                        "createdBy": {"data": None},
                        "updatedBy": {"data": None},
                        "prev": {"data": None},
                        "next": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "links": {
                "first": "http://server/pings?page%5Bnumber%5D=1",
                "last": "http://server/pings?page%5Bnumber%5D=2",
                "next": None,
                "prev": "http://server/pings?page%5Bnumber%5D=1",
            },
            "meta": {
                "pagination": {"count": 3, "page": 2, "pages": 2},
            },
        })

    # @todo Add tests for 'filter[message]' set to null. How do we even set a query parameter to null?

    def test_filter__message_some(self):
        Ping.objects.create(message="Hello")
        Ping.objects.create(message="Good bye")
        Ping.objects.create(message="Hello")
        Ping.objects.create(message="Good bye")
        Ping.objects.create(message="Hello")

        response = self.get("http://server/pings?filter[message]=Hello")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "ping",
                    "id": "1",
                    "links": {"self": "http://server/pings/1"},
                    "attributes": {
                        "createdAt": Ping.objects.get(id=1).created_at.isoformat().replace("+00:00", "Z"),
                        "updatedAt": Ping.objects.get(id=1).updated_at.isoformat().replace("+00:00", "Z"),
                        "message": "Hello",
                    },
                    "relationships": {
                        "createdBy": {"data": None},
                        "updatedBy": {"data": None},
                        "prev": {"data": None},
                        "next": {"data": [], "meta": {"count": 0}},
                    },
                },
                {
                    "type": "ping",
                    "id": "3",
                    "links": {"self": "http://server/pings/3"},
                    "attributes": {
                        "createdAt": Ping.objects.get(id=3).created_at.isoformat().replace("+00:00", "Z"),
                        "updatedAt": Ping.objects.get(id=3).updated_at.isoformat().replace("+00:00", "Z"),
                        "message": "Hello",
                    },
                    "relationships": {
                        "createdBy": {"data": None},
                        "updatedBy": {"data": None},
                        "prev": {"data": None},
                        "next": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "links": {
                "first": "http://server/pings?filter%5Bmessage%5D=Hello&page%5Bnumber%5D=1",
                "last": "http://server/pings?filter%5Bmessage%5D=Hello&page%5Bnumber%5D=2",
                "next": "http://server/pings?filter%5Bmessage%5D=Hello&page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {
                "pagination": {"count": 3, "page": 1, "pages": 2},
            },
        })

    # @todo Add tests for 'filter[prev]' set to null

    def test_filter__prev_some(self):
        prev = Ping.objects.create()
        Ping.objects.create(prev=prev)
        Ping.objects.create(prev=None)
        Ping.objects.create(prev=prev)
        Ping.objects.create(prev=None)
        Ping.objects.create(prev=prev)

        response = self.get("http://server/pings?filter[prev]=1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "ping",
                    "id": "2",
                    "links": {"self": "http://server/pings/2"},
                    "attributes": {
                        "createdAt": Ping.objects.get(id=2).created_at.isoformat().replace("+00:00", "Z"),
                        "updatedAt": Ping.objects.get(id=2).updated_at.isoformat().replace("+00:00", "Z"),
                        "message": None,
                    },
                    "relationships": {
                        "createdBy": {"data": None},
                        "updatedBy": {"data": None},
                        "prev": {"data": {"type": "ping", "id": "1"}},
                        "next": {"data": [], "meta": {"count": 0}},
                    },
                },
                {
                    "type": "ping",
                    "id": "4",
                    "links": {"self": "http://server/pings/4"},
                    "attributes": {
                        "createdAt": Ping.objects.get(id=4).created_at.isoformat().replace("+00:00", "Z"),
                        "updatedAt": Ping.objects.get(id=4).updated_at.isoformat().replace("+00:00", "Z"),
                        "message": None,
                    },
                    "relationships": {
                        "createdBy": {"data": None},
                        "updatedBy": {"data": None},
                        "prev": {"data": {"type": "ping", "id": "1"}},
                        "next": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "links": {
                "first": "http://server/pings?filter%5Bprev%5D=1&page%5Bnumber%5D=1",
                "last": "http://server/pings?filter%5Bprev%5D=1&page%5Bnumber%5D=2",
                "next": "http://server/pings?filter%5Bprev%5D=1&page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {
                "pagination": {"count": 3, "page": 1, "pages": 2},
            },
        })

    def test_update_nothing(self):
        ping = Ping.objects.create(message="Hello", prev=Ping.objects.create())
        Ping.objects.create(prev=ping)

        before_update = ping.updated_at

        response = self.patch("http://server/pings/2", {
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
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "updatedAt": before_update.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                },
            },
        })

        ping = Ping.objects.get(id=2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.updated_at, before_update)
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=3)])

    def test_update_message(self):
        ping = Ping.objects.create(message="Hello", prev=Ping.objects.create())
        Ping.objects.create(prev=ping)

        before_update = ping.updated_at

        response = self.patch("http://server/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "attributes": {
                    "message": "Bonjour",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        ping = Ping.objects.get(id=2)
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "updatedAt": ping.updated_at.isoformat().replace("+00:00", "Z"),
                    "message": "Bonjour",
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                },
            },
        })
        self.assertEqual(ping.message, "Bonjour")
        self.assertGreater(ping.updated_at, before_update)
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=3)])

    def test_update_message_to_none(self):
        Ping.objects.create(prev=Ping.objects.create(message="Hello", prev=Ping.objects.create()))

        response = self.patch("http://server/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "attributes": {
                    "message": None,
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        ping = Ping.objects.get(id=2)
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "updatedAt": ping.updated_at.isoformat().replace("+00:00", "Z"),
                    "message": None,
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                },
            },
        })

        self.assertEqual(ping.message, None)
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=3)])

    def test_update_prev__some_to_some(self):
        Ping.objects.create(prev=Ping.objects.create(message="Hello", prev=Ping.objects.create()))
        Ping.objects.create()

        response = self.patch("http://server/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "relationships": {
                    "prev": {"data": {"type": "ping", "id": "4"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        ping = Ping.objects.get(id=2)
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "updatedAt": ping.updated_at.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": {"type": "ping", "id": "4"}},
                    "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                },
            },
        })
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, Ping.objects.get(id=4))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=3)])

    def test_update_prev__some_to_none(self):
        Ping.objects.create(prev=Ping.objects.create(message="Hello", prev=Ping.objects.create()))

        response = self.patch("http://server/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "relationships": {
                    "prev": {"data": None},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        ping = Ping.objects.get(id=2)
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "updatedAt": ping.updated_at.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": None},
                    "next": {"data": [{"type": "ping", "id": "3"}], "meta": {"count": 1}},
                },
            },
        })
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, None)
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=3)])

    def test_update_prev__none_to_some(self):
        Ping.objects.create(prev=Ping.objects.create(message="Hello", prev=None))
        Ping.objects.create()

        response = self.patch("http://server/pings/1", {
            "data": {
                "type": "ping",
                "id": "1",
                "relationships": {
                    "prev": {"data": {"type": "ping", "id": "3"}},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        ping = Ping.objects.get(id=1)
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "1",
                "links": {"self": "http://server/pings/1"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "updatedAt": ping.updated_at.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": {"type": "ping", "id": "3"}},
                    "next": {"data": [{"type": "ping", "id": "2"}], "meta": {"count": 1}},
                },
            },
        })
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, Ping.objects.get(id=3))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=2)])

    def test_update_next(self):
        Ping.objects.create(prev=Ping.objects.create(message="Hello", prev=Ping.objects.create()))
        Ping.objects.create()

        response = self.patch("http://server/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "relationships": {
                    "next": {"data": [{"type": "ping", "id": "4"}]},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        ping = Ping.objects.get(id=2)
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "updatedAt": ping.updated_at.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [{"type": "ping", "id": "4"}], "meta": {"count": 1}},
                },
            },
        })
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [Ping.objects.get(id=4)])

    def test_update_next_to_empty(self):
        Ping.objects.create(prev=Ping.objects.create(message="Hello", prev=Ping.objects.create()))

        response = self.patch("http://server/pings/2", {
            "data": {
                "type": "ping",
                "id": "2",
                "relationships": {
                    "next": {"data": []},
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        ping = Ping.objects.get(id=2)
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": ping.created_at.isoformat().replace("+00:00", "Z"),
                    "updatedAt": ping.updated_at.isoformat().replace("+00:00", "Z"),
                    "message": "Hello",
                },
                "relationships": {
                    "createdBy": {"data": None},
                    "updatedBy": {"data": None},
                    "prev": {"data": {"type": "ping", "id": "1"}},
                    "next": {"data": [], "meta": {"count": 0}},
                },
            },
        })
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, Ping.objects.get(id=1))
        self.assertEqual(list(ping.next.all()), [])


class PingOwnershipTestCase(TestMixin, TransactionTestCase):
    reset_sequences = True

    resources = [UserResource(), PingsResource()]

    def test_create__unauthenticated(self):
        response = self.post(
            "http://server/pings",
            {
                "data": {
                    "type": "ping",
                },
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(
            response.json()["data"]["relationships"]["createdBy"],
            {"data": None},
        )
        self.assertEqual(
            response.json()["data"]["relationships"]["updatedBy"],
            {"data": None},
        )

        ping = Ping.objects.get(id=1)
        self.assertEqual(ping.created_by, None)
        self.assertEqual(ping.updated_by, None)

    def test_create__authenticated(self):
        User.objects.create_user("alice", password="alice's password")
        self.login("alice", "alice's password")

        response = self.post(
            "http://server/pings",
            {
                "data": {
                    "type": "ping",
                },
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(
            response.json()["data"]["relationships"]["createdBy"],
            {"data": {"type": "user", "id": "1"}},
        )
        self.assertEqual(
            response.json()["data"]["relationships"]["updatedBy"],
            {"data": {"type": "user", "id": "1"}},
        )

        self.assertEqual(Ping.objects.get(id=1).created_by, User.objects.get(username="alice"))
        self.assertEqual(Ping.objects.get(id=1).updated_by, User.objects.get(username="alice"))

    def test_update__unauthenticated_ok(self):
        ping = Ping.objects.create(message="Hello")
        before_update = ping.updated_at

        response = self.patch("http://server/pings/1", {
            "data": {
                "type": "ping",
                "id": "2",
                "attributes": {
                    "message": "Bonjour",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        ping = Ping.objects.get(id=1)
        self.assertEqual(ping.message, "Bonjour")
        self.assertEqual(ping.created_by, None)
        self.assertEqual(ping.updated_by, None)
        self.assertGreater(ping.updated_at, before_update)

    def test_update__unauthenticated_error(self):
        user = User.objects.create_user("alice", password="alice's password")
        ping = Ping.objects.create(message="Hello", created_by=user, updated_by=user)
        before_update = ping.updated_at

        response = self.patch("http://server/pings/1", {
            "data": {
                "type": "ping",
                "id": "2",
                "attributes": {
                    "message": "Bonjour",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.json())

        ping = Ping.objects.get(id=1)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.created_by, user)
        self.assertEqual(ping.updated_by, user)
        self.assertEqual(ping.updated_at, before_update)

    def test_update__authenticated_on_not_owned(self):
        User.objects.create_user("alice", password="alice's password")
        ping = Ping.objects.create(message="Hello")
        before_update = ping.updated_at

        self.login("alice", "alice's password")

        response = self.patch("http://server/pings/1", {
            "data": {
                "type": "ping",
                "id": "2",
                "attributes": {
                    "message": "Bonjour",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        ping = Ping.objects.get(id=1)
        self.assertEqual(ping.message, "Bonjour")
        self.assertEqual(ping.created_by, None)
        self.assertEqual(ping.updated_by, User.objects.get(username="alice"))
        self.assertGreater(ping.updated_at, before_update)

    def test_update__authenticated_on_own(self):
        user = User.objects.create_user("alice", password="alice's password")
        ping = Ping.objects.create(message="Hello", created_by=user, updated_by=user)
        before_update = ping.updated_at

        self.login("alice", "alice's password")

        response = self.patch("http://server/pings/1", {
            "data": {
                "type": "ping",
                "id": "2",
                "attributes": {
                    "message": "Bonjour",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        ping = Ping.objects.get(id=1)
        self.assertEqual(ping.message, "Bonjour")
        self.assertEqual(ping.created_by, user)
        self.assertEqual(ping.updated_by, user)
        self.assertGreater(ping.updated_at, before_update)

    def test_update__authenticated_on_someone_elses(self):
        alice = User.objects.create_user("alice", password="alice's password")
        bob = User.objects.create_user("bob", password="bob's password")
        ping = Ping.objects.create(message="Hello", created_by=alice, updated_by=alice)
        before_update = ping.updated_at

        self.login("bob", "bob's password")

        response = self.patch("http://server/pings/1", {
            "data": {
                "type": "ping",
                "id": "2",
                "attributes": {
                    "message": "Bonjour",
                },
            },
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.json())

        ping = Ping.objects.get(id=1)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.created_by, alice)
        self.assertEqual(ping.updated_by, alice)
        self.assertEqual(ping.updated_at, before_update)

    def test_delete__unauthenticated_ok(self):
        ping = Ping.objects.create(message="Hello")
        before_update = ping.updated_at

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertEqual(Ping.objects.count(), 0)

    def test_delete__unauthenticated_error(self):
        user = User.objects.create_user("alice", password="alice's password")
        Ping.objects.create(message="Hello", created_by=user, updated_by=user)

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.text)

        self.assertEqual(Ping.objects.count(), 1)

    def test_delete__authenticated_on_not_owned(self):
        User.objects.create_user("alice", password="alice's password")
        ping = Ping.objects.create(message="Hello")
        before_update = ping.updated_at

        self.login("alice", "alice's password")

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertEqual(Ping.objects.count(), 0)

    def test_delete__authenticated_on_own(self):
        user = User.objects.create_user("alice", password="alice's password")
        Ping.objects.create(message="Hello", created_by=user, updated_by=user)

        self.login("alice", "alice's password")

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertEqual(Ping.objects.count(), 0)

    def test_delete__authenticated_on_someone_elses(self):
        alice = User.objects.create_user("alice", password="alice's password")
        User.objects.create_user("bob", password="bob's password")
        Ping.objects.create(message="Hello", created_by=alice, updated_by=alice)

        self.login("bob", "bob's password")

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.text)

        self.assertEqual(Ping.objects.count(), 1)
