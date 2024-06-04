from __future__ import annotations
from contextlib import contextmanager
from typing import Annotated
import datetime

from fastapi import Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import orm
from starlette import status
import sqlalchemy as sql

from fastjsonapi.annotations import Computed, Filterable
from fastjsonapi.sqlalchemy import set_wrapper, OrmWrapperWithStrIds, wrap, unwrap

from . import settings
from . import testing
from .database_utils import OrmBase, Session, session_dependable
from .users import User, UserModel, UsersResource, optional_authenticated_user_dependable


class Ping(OrmBase):
    __tablename__ = "pings"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    message: orm.Mapped[str | None] = orm.mapped_column()
    created_at: orm.Mapped[datetime.datetime] = orm.mapped_column(sql.DateTime(timezone=True), server_default=sql.func.now())
    created_by_id: orm.Mapped[int | None] = orm.mapped_column(sql.ForeignKey("users.id"))
    created_by: orm.Mapped[User | None] = orm.relationship(foreign_keys=[created_by_id])
    updated_at: orm.Mapped[datetime.datetime] = orm.mapped_column(sql.DateTime(timezone=True), server_default=sql.func.now(), onupdate=sql.func.now())
    updated_by_id: orm.Mapped[int | None] = orm.mapped_column(sql.ForeignKey("users.id"))
    updated_by: orm.Mapped[User | None] = orm.relationship(foreign_keys=[updated_by_id])

    prev_id: orm.Mapped[int | None] = orm.mapped_column(sql.ForeignKey("pings.id"))
    prev: orm.Mapped[Ping | None] = orm.relationship(back_populates="next", remote_side=[id], post_update=True)
    next: orm.Mapped[list[Ping]] = orm.relationship(back_populates="prev")


class PingModel(BaseModel):
    message: Annotated[str | None, Filterable()] = None
    created_at: Annotated[datetime.datetime, Computed()]
    created_by: Annotated[UserModel | None, Computed()] = None
    updated_at: Annotated[datetime.datetime, Computed()]
    updated_by: Annotated[UserModel | None, Computed()] = None
    prev: Annotated[PingModel | None, Filterable()] = None
    next: list[PingModel] = []


class PingsResource:
    singular_name = "ping"
    plural_name = "pings"

    Model = PingModel

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    class ItemCreator:
        def __init__(
            self,
            session: Session = Depends(session_dependable),
            authenticated_user: User | None = Depends(optional_authenticated_user_dependable),
        ):
            self.__session = session
            self.__authenticated_user = authenticated_user

        def __call__(self, *, message, prev, next):
            ping = Ping(
                message=message,
                created_by=self.__authenticated_user,
                updated_by=self.__authenticated_user,
                prev=unwrap(prev),
                next=[unwrap(next_item) for next_item in next],
            )
            self.__session.add(ping)
            self.__session.commit()
            return wrap(ping)

    class ItemGetter:
        def __init__(self, session: Session = Depends(session_dependable)):
            self.__session = session

        def __call__(self, id):
            return wrap(self.__session.get(Ping, id))

    class PageGetter:
        def __init__(self, session: Session = Depends(session_dependable)):
            self.__session = session

        def __call__(self, sort, filters, first_index, page_size):
            def add_filters(q):
                if filters.message:
                    q = q.where(Ping.message == filters.message)
                if filters.prev:
                    q = q.where(Ping.prev_id == filters.prev)
                return q

            count = self.__session.scalar(add_filters(sql.select(sql.func.count(Ping.id))))
            pings = [
                wrap(ping)
                for (ping,) in self.__session.execute(
                    add_filters(sql.select(Ping))
                        .offset(first_index)
                        .limit(page_size)
                )
            ]
            return (count, pings)

    class ItemSaver:
        def __init__(self, authenticated_user: User | None = Depends(optional_authenticated_user_dependable)):
            self.__authenticated_user = authenticated_user

        @contextmanager
        def __call__(self, item):
            created_by = unwrap(item.created_by)
            if created_by is not None:
                if self.__authenticated_user != created_by:
                    raise HTTPException(status.HTTP_403_FORBIDDEN, "You are not the creator of this ping")
            yield
            item.updated_by = self.__authenticated_user

    class ItemDeleter:
        def __init__(
            self,
            session: Session = Depends(session_dependable),
            authenticated_user: User | None = Depends(optional_authenticated_user_dependable),
        ):
            self.__session = session
            self.__authenticated_user = authenticated_user

        def __call__(self, item):
            created_by = unwrap(item.created_by)
            if created_by is not None:
                if self.__authenticated_user != created_by:
                    raise HTTPException(status.HTTP_403_FORBIDDEN, "You are not the creator of this ping")
            self.__session.delete(unwrap(item))


set_wrapper(Ping, OrmWrapperWithStrIds)


def create_test_pings(session):
    session.add(Ping(message="Hello 1"))
    session.add(ping2 := Ping(message="Hello 2"))
    session.add(ping3 := Ping(message="Hello 3", prev=ping2))
    session.add(Ping(message="Hello 4", prev=ping3))
    session.add(ping5 := Ping(message="Hello 5", prev=ping3))
    session.add(Ping(message="Hello 6", prev=ping5))


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
        self.create_model(Ping)
        self.create_model(Ping)

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
        ping = self.create_model(Ping)

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
        response = self.get("http://server/pings/0")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.json())

    def test_get_all(self):
        ping1 = self.create_model(Ping)
        ping2 = self.create_model(Ping, prev=ping1)
        ping3 = self.create_model(Ping)

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
        ping1 = self.create_model(Ping, message="Hello")
        self.create_model(Ping, message="Good bye")
        ping3 = self.create_model(Ping, message="Hello")
        self.create_model(Ping, message="Good bye")
        self.create_model(Ping, message="Hello")

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
        prev = self.create_model(Ping)
        ping2 = self.create_model(Ping, prev=prev)
        self.create_model(Ping, prev=None)
        ping4 = self.create_model(Ping, prev=prev)
        self.create_model(Ping, prev=None)
        self.create_model(Ping, prev=prev)

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
        ping = self.create_model(Ping, message="Hello", prev=self.create_model(Ping))
        self.create_model(Ping, prev=ping)

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
        ping = self.create_model(Ping, message="Hello", prev=self.create_model(Ping))
        self.create_model(Ping, prev=ping)

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
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=self.create_model(Ping)))

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
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=self.create_model(Ping)))
        self.create_model(Ping)

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

    def test_update_prev__some_to_none(self):
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=self.create_model(Ping)))

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
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=None))
        self.create_model(Ping)

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
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=self.create_model(Ping)))
        self.create_model(Ping)

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

    def test_update_next_to_empty(self):
        self.create_model(Ping, prev=self.create_model(Ping, message="Hello", prev=self.create_model(Ping)))

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
            {"data": {"type": "user", "id": "1"}},
        )
        self.assertEqual(
            response.json()["data"]["relationships"]["updatedBy"],
            {"data": {"type": "user", "id": "1"}},
        )

        self.assertEqual(self.get_model(Ping, 1).created_by, self.get_model(User, 1))
        self.assertEqual(self.get_model(Ping, 1).updated_by, self.get_model(User, 1))

    def test_update__unauthenticated_ok(self):
        ping = self.create_model(Ping, message="Hello")
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
        self.create_model(User, username="alice", clear_text_password="alice's password")
        ping = self.create_model(Ping, message="Hello")
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
        self.assertEqual(ping.updated_by, self.get_model(User, 1))
        self.assertGreater(ping.updated_at, before_update)

    def test_update__authenticated_on_own(self):
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
        ping = self.create_model(Ping, message="Hello")
        before_update = ping.updated_at

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertEqual(self.count_models(Ping), 0)

    def test_delete__unauthenticated_error(self):
        user = self.create_model(User, username="alice", clear_text_password="alice's password")
        self.create_model(Ping, message="Hello", created_by=user, updated_by=user)

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.text)

        self.assertEqual(self.count_models(Ping), 1)

    def test_delete__authenticated_on_not_owned(self):
        self.create_model(User, username="alice", clear_text_password="alice's password")
        ping = self.create_model(Ping, message="Hello")
        before_update = ping.updated_at

        self.login("alice", "alice's password")

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertEqual(self.count_models(Ping), 0)

    def test_delete__authenticated_on_own(self):
        user = self.create_model(User, username="alice", clear_text_password="alice's password")
        self.create_model(Ping, message="Hello", created_by=user, updated_by=user)

        self.login("alice", "alice's password")

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.text)

        self.assertEqual(self.count_models(Ping), 0)

    def test_delete__authenticated_on_someone_elses(self):
        alice = self.create_model(User, username="alice", clear_text_password="alice's password")
        self.create_model(User, username="bob", clear_text_password="bob's password")
        self.create_model(Ping, message="Hello", created_by=alice, updated_by=alice)

        self.login("bob", "bob's password")

        response = self.delete("http://server/pings/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.text)

        self.assertEqual(self.count_models(Ping), 1)
