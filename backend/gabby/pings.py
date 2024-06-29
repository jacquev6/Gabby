from contextlib import contextmanager
import datetime
from typing import Annotated

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import orm
from starlette import status
import sqlalchemy as sql

from fastjsonapi import make_filters

from . import api_models
from . import settings
from . import testing
from .database_utils import OrmBase, SessionDependable
from .api_utils import create_item, get_item, get_page, save_item, delete_item
from .users import User, UsersResource, OptionalAuthBearerDependable
from .users.mixins import OptionalCreatedUpdatedByAtMixin
from .wrapping import set_wrapper, OrmWrapperWithStrIds, unwrap


class Ping(OrmBase, OptionalCreatedUpdatedByAtMixin):
    __tablename__ = "pings"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    message: orm.Mapped[str | None] = orm.mapped_column()

    prev_id: orm.Mapped[int | None] = orm.mapped_column(sql.ForeignKey("pings.id"))
    prev: orm.Mapped["Ping | None"] = orm.relationship(back_populates="next", remote_side=[id], post_update=True)
    next: orm.Mapped[list["Ping"]] = orm.relationship(back_populates="prev")


class PingsResource:
    singular_name = "ping"
    plural_name = "pings"

    Model = api_models.Ping

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    def create_item(
        self,
        message,
        prev,
        next,
        session: SessionDependable,
        authenticated_user: OptionalAuthBearerDependable,
    ):
        return create_item(
            session,
            Ping,
            message=message,
            created_by=authenticated_user,
            updated_by=authenticated_user,
            prev=prev,
            next=next,
        )

    def get_item(
        self,
        id: str,
        session: SessionDependable,
    ):
        return get_item(session, Ping, int(id))

    class Filters(BaseModel):
        message: str | None
        prev: str | None

    def get_page(
        self,
        first_index,
        page_size,
        session: SessionDependable,
        filters: Annotated[Filters, make_filters(Filters)],
    ):
        query = sql.select(Ping)
        if filters.message is not None:
            query = query.where(Ping.message == filters.message)
        if filters.prev is not None:
            query = query.where(Ping.prev_id == filters.prev)
        return get_page(session, query, first_index, page_size)

    @contextmanager
    def save_item(
        self,
        item,
        session: SessionDependable,
        authenticated_user: OptionalAuthBearerDependable,
    ):
        created_by = unwrap(item.created_by)
        if created_by is not None:
            if authenticated_user != created_by:
                raise HTTPException(status.HTTP_403_FORBIDDEN, "You are not the creator of this ping")
        yield
        item.updated_by = authenticated_user
        save_item(session, item)

    def delete_item(
        self,
        item,
        session: SessionDependable,
        authenticated_user: OptionalAuthBearerDependable,
    ):
        created_by = unwrap(item.created_by)
        if created_by is not None:
            if authenticated_user != created_by:
                raise HTTPException(status.HTTP_403_FORBIDDEN, "You are not the creator of this ping")
        delete_item(session, item)


set_wrapper(Ping, OrmWrapperWithStrIds)


class PingsApiTestCase(testing.ApiTestCase):
    resources = [UsersResource(), PingsResource()]
    polymorphism = {}

    def format_date(self, d):
        return d.isoformat().replace("+00:00", "Z")

    def parse_date(self, s):
        return datetime.datetime.fromisoformat(s)

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
        created_at = self.parse_date(response.json()["data"]["attributes"]["createdAt"])
        updated_at = self.parse_date(response.json()["data"]["attributes"]["updatedAt"])
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "1",
                "links": {"self": "http://server/pings/1"},
                "attributes": {
                    "createdAt": self.format_date(created_at),
                    "updatedAt": self.format_date(updated_at),
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

        self.assertGreaterEqual(created_at, before)
        self.assertLessEqual(created_at, after)
        self.assertGreaterEqual(updated_at, before)
        self.assertLessEqual(updated_at, after)

        self.assertEqual(self.count_models(Ping), 1)
        ping = self.get_model(Ping, 1)
        self.assertEqual(ping.id, 1)
        self.assertEqual(ping.created_at, created_at)
        self.assertEqual(ping.created_by, None)
        self.assertEqual(ping.updated_at, updated_at)
        self.assertEqual(ping.updated_by, None)
        self.assertIsNone(ping.message)
        self.assertIsNone(ping.prev)
        self.assertEqual(len(ping.next), 0)

    def test_create__full(self):
        self.create_model(Ping, created_by=None, updated_by=None)
        self.create_model(Ping, created_by=None, updated_by=None)

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
        created_at = self.parse_date(response.json()["data"]["attributes"]["createdAt"])
        updated_at = self.parse_date(response.json()["data"]["attributes"]["updatedAt"])
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "3",
                "links": {"self": "http://server/pings/3"},
                "attributes": {
                    "createdAt": self.format_date(created_at),
                    "updatedAt": self.format_date(updated_at),
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

        self.assertEqual(self.count_models(Ping), 3)
        ping = self.get_model(Ping, 3)
        self.assertEqual(ping.id, 3)
        self.assertEqual(ping.created_at, created_at)
        self.assertEqual(ping.created_by, None)
        self.assertEqual(ping.updated_at, updated_at)
        self.assertEqual(ping.updated_by, None)
        self.assertEqual(ping.message, "hello")
        self.assertEqual(ping.prev, self.get_model(Ping, 1))
        self.assertEqual(ping.next, [self.get_model(Ping, 2)])

    def test_get_one(self):
        ping = self.create_model(Ping, created_by=None, updated_by=None)

        response = self.get("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "1",
                "links": {"self": "http://server/pings/1"},
                "attributes": {
                    "createdAt": self.format_date(ping.created_at),
                    "updatedAt": self.format_date(ping.updated_at),
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
        self.expect_rollback()

        response = self.get("http://server/pings/0")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.json())

    def test_get_all(self):
        self.expect_commits_rollbacks(2, 0)

        ping1 = self.create_model(Ping, created_by=None, updated_by=None)
        ping2 = self.create_model(Ping, prev=ping1, created_by=None, updated_by=None)
        ping3 = self.create_model(Ping, created_by=None, updated_by=None)

        response = self.get("http://server/pings")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "ping",
                    "id": "1",
                    "links": {"self": "http://server/pings/1"},
                    "attributes": {
                        "createdAt": self.format_date(ping1.created_at),
                        "updatedAt": self.format_date(ping1.updated_at),
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
                        "createdAt": self.format_date(ping2.created_at),
                        "updatedAt": self.format_date(ping2.updated_at),
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
                        "createdAt": self.format_date(ping3.created_at),
                        "updatedAt": self.format_date(ping3.updated_at),
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
        ping1 = self.create_model(Ping, message="Hello", created_by=None, updated_by=None)
        self.create_model(Ping, message="Good bye", created_by=None, updated_by=None)
        ping3 = self.create_model(Ping, message="Hello", created_by=None, updated_by=None)
        self.create_model(Ping, message="Good bye", created_by=None, updated_by=None)
        self.create_model(Ping, message="Hello", created_by=None, updated_by=None)

        response = self.get("http://server/pings?filter[message]=Hello")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "ping",
                    "id": "1",
                    "links": {"self": "http://server/pings/1"},
                    "attributes": {
                        "createdAt": self.format_date(ping1.created_at),
                        "updatedAt": self.format_date(ping1.updated_at),
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
                        "createdAt": self.format_date(ping3.created_at),
                        "updatedAt": self.format_date(ping3.updated_at),
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
        prev = self.create_model(Ping, created_by=None, updated_by=None)
        ping2 = self.create_model(Ping, prev=prev, created_by=None, updated_by=None)
        self.create_model(Ping, prev=None, created_by=None, updated_by=None)
        ping4 = self.create_model(Ping, prev=prev, created_by=None, updated_by=None)
        self.create_model(Ping, prev=None, created_by=None, updated_by=None)
        self.create_model(Ping, prev=prev, created_by=None, updated_by=None)

        response = self.get("http://server/pings?filter[prev]=1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "ping",
                    "id": "2",
                    "links": {"self": "http://server/pings/2"},
                    "attributes": {
                        "createdAt": self.format_date(ping2.created_at),
                        "updatedAt": self.format_date(ping2.updated_at),
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
                        "createdAt": self.format_date(ping4.created_at),
                        "updatedAt": self.format_date(ping4.updated_at),
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
        ping = self.create_model(Ping, message="Hello", prev=self.create_model(Ping, created_by=None, updated_by=None), created_by=None, updated_by=None)
        self.create_model(Ping, prev=ping, created_by=None, updated_by=None)

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
                    "createdAt": self.format_date(ping.created_at),
                    "updatedAt": self.format_date(before_update),
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

        ping = self.get_model(Ping, 2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.updated_at, before_update)
        self.assertEqual(ping.prev, self.get_model(Ping, 1))
        self.assertEqual(ping.next, [self.get_model(Ping, 3)])

    def test_update_message(self):
        ping = self.create_model(Ping, message="Hello", prev=self.create_model(Ping, created_by=None, updated_by=None), created_by=None, updated_by=None)
        self.create_model(Ping, prev=ping, created_by=None, updated_by=None)

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
        created_at = self.parse_date(response.json()["data"]["attributes"]["createdAt"])
        updated_at = self.parse_date(response.json()["data"]["attributes"]["updatedAt"])
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": self.format_date(created_at),
                    "updatedAt": self.format_date(updated_at),
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

        ping = self.get_model(Ping, 2)
        self.assertEqual(ping.message, "Bonjour")
        self.assertGreater(ping.updated_at, before_update)
        self.assertEqual(ping.prev, self.get_model(Ping, 1))
        self.assertEqual(ping.next, [self.get_model(Ping, 3)])

    def test_update_message_to_none(self):
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=self.create_model(Ping, created_by=None, updated_by=None), created_by=None, updated_by=None), created_by=None, updated_by=None)

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
        created_at = self.parse_date(response.json()["data"]["attributes"]["createdAt"])
        updated_at = self.parse_date(response.json()["data"]["attributes"]["updatedAt"])
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": self.format_date(created_at),
                    "updatedAt": self.format_date(updated_at),
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

        ping = self.get_model(Ping, 2)
        self.assertEqual(ping.message, None)
        self.assertEqual(ping.prev, self.get_model(Ping, 1))
        self.assertEqual(ping.next, [self.get_model(Ping, 3)])

    def test_update_prev__some_to_some(self):
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=self.create_model(Ping, created_by=None, updated_by=None), created_by=None, updated_by=None), created_by=None, updated_by=None)
        self.create_model(Ping, created_by=None, updated_by=None)

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
        created_at = self.parse_date(response.json()["data"]["attributes"]["createdAt"])
        updated_at = self.parse_date(response.json()["data"]["attributes"]["updatedAt"])
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": self.format_date(created_at),
                    "updatedAt": self.format_date(updated_at),
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

        ping = self.get_model(Ping, 2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, self.get_model(Ping, 4))
        self.assertEqual(ping.next, [self.get_model(Ping, 3)])

    # @todo Add test_update_prev__to_unexisting, where the new prev does not exist

    def test_update_prev__some_to_none(self):
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=self.create_model(Ping, created_by=None, updated_by=None), created_by=None, updated_by=None), created_by=None, updated_by=None)

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
        created_at = self.parse_date(response.json()["data"]["attributes"]["createdAt"])
        updated_at = self.parse_date(response.json()["data"]["attributes"]["updatedAt"])
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": self.format_date(created_at),
                    "updatedAt": self.format_date(updated_at),
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

        ping = self.get_model(Ping, 2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, None)
        self.assertEqual(ping.next, [self.get_model(Ping, 3)])

    def test_update_prev__none_to_some(self):
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=None, created_by=None, updated_by=None), created_by=None, updated_by=None)
        self.create_model(Ping, created_by=None, updated_by=None)

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
        created_at = self.parse_date(response.json()["data"]["attributes"]["createdAt"])
        updated_at = self.parse_date(response.json()["data"]["attributes"]["updatedAt"])
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "1",
                "links": {"self": "http://server/pings/1"},
                "attributes": {
                    "createdAt": self.format_date(created_at),
                    "updatedAt": self.format_date(updated_at),
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

        ping = self.get_model(Ping, 1)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, self.get_model(Ping, 3))
        self.assertEqual(ping.next, [self.get_model(Ping, 2)])

    def test_update_next(self):
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=self.create_model(Ping, created_by=None, updated_by=None), created_by=None, updated_by=None), created_by=None, updated_by=None)
        self.create_model(Ping, created_by=None, updated_by=None)

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
        created_at = self.parse_date(response.json()["data"]["attributes"]["createdAt"])
        updated_at = self.parse_date(response.json()["data"]["attributes"]["updatedAt"])
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": self.format_date(created_at),
                    "updatedAt": self.format_date(updated_at),
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

        ping = self.get_model(Ping, 2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, self.get_model(Ping, 1))
        self.assertEqual(ping.next, [self.get_model(Ping, 4)])

    # @todo Add test_update_next__to_self test_update_prev__to_self (Currently trigger a 'sqlalchemy.exc.CircularDependencyError')

    def test_update_next_to_empty(self):
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=self.create_model(Ping, created_by=None, updated_by=None), created_by=None, updated_by=None), created_by=None, updated_by=None)

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
        created_at = self.parse_date(response.json()["data"]["attributes"]["createdAt"])
        updated_at = self.parse_date(response.json()["data"]["attributes"]["updatedAt"])
        self.assertEqual(response.json(), {
            "data": {
                "type": "ping",
                "id": "2",
                "links": {"self": "http://server/pings/2"},
                "attributes": {
                    "createdAt": self.format_date(created_at),
                    "updatedAt": self.format_date(updated_at),
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

        ping = self.get_model(Ping, 2)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.prev, self.get_model(Ping, 1))
        self.assertEqual(ping.next, [])


class PingOwnershipApiTestCase(testing.ApiTestCase):
    resources = [UsersResource(), PingsResource()]
    polymorphism = {}

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

        ping = self.get_model(Ping, 1)
        self.assertEqual(ping.created_by, None)
        self.assertEqual(ping.updated_by, None)

    def test_create__authenticated(self):
        self.expect_commits_rollbacks(2, 0)

        self.create_model(User, username="alice", clear_text_password="alice's password")
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
            {"data": {"type": "user", "id": "ckylfa"}},
        )
        self.assertEqual(
            response.json()["data"]["relationships"]["updatedBy"],
            {"data": {"type": "user", "id": "ckylfa"}},
        )

        self.assertEqual(self.get_model(Ping, 1).created_by, self.get_model(User, 2))
        self.assertEqual(self.get_model(Ping, 1).updated_by, self.get_model(User, 2))

    def test_update__unauthenticated_ok(self):
        ping = self.create_model(Ping, message="Hello", created_by=None, updated_by=None)
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

        ping = self.get_model(Ping, 1)
        self.assertEqual(ping.message, "Bonjour")
        self.assertEqual(ping.created_by, None)
        self.assertEqual(ping.updated_by, None)
        self.assertGreater(ping.updated_at, before_update)

    def test_update__unauthenticated_error(self):
        self.expect_rollback()

        user = self.create_model(User, username="alice", clear_text_password="alice's password")
        ping = self.create_model(Ping, message="Hello", created_by=user, updated_by=user)
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

        ping = self.get_model(Ping, 1)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.created_by, user)
        self.assertEqual(ping.updated_by, user)
        self.assertEqual(ping.updated_at, before_update)

    def test_update__authenticated_on_not_owned(self):
        self.expect_commits_rollbacks(2, 0)

        self.create_model(User, username="alice", clear_text_password="alice's password")
        ping = self.create_model(Ping, message="Hello", created_by=None, updated_by=None)
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

        ping = self.get_model(Ping, 1)
        self.assertEqual(ping.message, "Bonjour")
        self.assertEqual(ping.created_by, None)
        self.assertEqual(ping.updated_by, self.get_model(User, 2))
        self.assertGreater(ping.updated_at, before_update)

    def test_update__authenticated_on_own(self):
        self.expect_commits_rollbacks(2, 0)

        user = self.create_model(User, username="alice", clear_text_password="alice's password")
        ping = self.create_model(Ping, message="Hello", created_by=user, updated_by=user)
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

        ping = self.get_model(Ping, 1)
        self.assertEqual(ping.message, "Bonjour")
        self.assertEqual(ping.created_by, user)
        self.assertEqual(ping.updated_by, user)
        self.assertGreater(ping.updated_at, before_update)

    def test_update__authenticated_on_someone_elses(self):
        self.expect_commits_rollbacks(1, 1)

        alice = self.create_model(User, username="alice", clear_text_password="alice's password")
        bob = self.create_model(User, username="bob", clear_text_password="bob's password")
        ping = self.create_model(Ping, message="Hello", created_by=alice, updated_by=alice)
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

        ping = self.get_model(Ping, 1)
        self.assertEqual(ping.message, "Hello")
        self.assertEqual(ping.created_by, alice)
        self.assertEqual(ping.updated_by, alice)
        self.assertEqual(ping.updated_at, before_update)

    def test_delete__unauthenticated_ok(self):
        ping = self.create_model(Ping, message="Hello", created_by=None, updated_by=None)
        before_update = ping.updated_at

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertEqual(self.count_models(Ping), 0)

    def test_delete__unauthenticated_error(self):
        self.expect_rollback()

        user = self.create_model(User, username="alice", clear_text_password="alice's password")
        self.create_model(Ping, message="Hello", created_by=user, updated_by=user)

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.text)

        self.assertEqual(self.count_models(Ping), 1)

    def test_delete__authenticated_on_not_owned(self):
        self.expect_commits_rollbacks(2, 0)

        self.create_model(User, username="alice", clear_text_password="alice's password")
        ping = self.create_model(Ping, message="Hello", created_by=None, updated_by=None)
        before_update = ping.updated_at

        self.login("alice", "alice's password")

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertEqual(self.count_models(Ping), 0)

    def test_delete__authenticated_on_own(self):
        self.expect_commits_rollbacks(2, 0)

        user = self.create_model(User, username="alice", clear_text_password="alice's password")
        self.create_model(Ping, message="Hello", created_by=user, updated_by=user)

        self.login("alice", "alice's password")

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertEqual(self.count_models(Ping), 0)

    def test_delete__authenticated_on_someone_elses(self):
        self.expect_commits_rollbacks(1, 1)

        alice = self.create_model(User, username="alice", clear_text_password="alice's password")
        self.create_model(User, username="bob", clear_text_password="bob's password")
        self.create_model(Ping, message="Hello", created_by=alice, updated_by=alice)

        self.login("bob", "bob's password")

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.text)

        self.assertEqual(self.count_models(Ping), 1)
