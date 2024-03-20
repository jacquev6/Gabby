from __future__ import annotations
from typing import Annotated
import datetime

from pydantic import BaseModel

from fastjsonapi import Computed, Filterable
from .models import Ping


class PingModel(BaseModel):
    message: Annotated[str | None, Filterable()] = None
    created_at: Annotated[datetime.datetime, Computed()]
    prev: PingModel | None = None
    next: list[PingModel] = []


class PingItem:
    def __init__(self, ping):
        self._ping = ping

    @property
    def id(self):
        return str(self._ping.id)

    @property
    def message(self):
        return self._ping.message

    @message.setter
    def message(self, message):
        self._ping.message = message

    @property
    def created_at(self):
        return self._ping.created_at

    @property
    def prev(self):
        return None if self._ping.prev is None else PingItem(self._ping.prev)

    @prev.setter
    def prev(self, prev):
        self._ping.prev = None if prev is None else prev._ping

    @property
    def next(self):
        return [PingItem(next) for next in self._ping.next.all()]

    @next.setter
    def next(self, next):
        self._ping.next.set([n._ping for n in next])

    def save(self):
        self._ping.save()

    def delete(self):
        self._ping.delete()


class PingsResource:
    singular_name = "ping"
    plural_name = "pings"

    Model = PingModel

    default_page_size = 2

    def create_item(self, *, message, prev, next):
        ping = Ping.objects.create(message=message, prev=None if prev is None else prev._ping)
        ping.next.set([n._ping for n in next])
        ping.save()
        return PingItem(ping)

    def get_item(self, id):
        try:
            return PingItem(Ping.objects.get(id=id))
        except Ping.DoesNotExist:
            return None

    def get_page(self, filters, first_index, page_size):
        pings = Ping.objects.all()
        if filters.message:
            pings = [ping for ping in pings if ping.message == filters.message]

        return (len(pings), [PingItem(ping) for ping in pings[first_index:first_index + page_size]])
