from __future__ import annotations
from contextlib import contextmanager
from typing import Annotated
import datetime

from pydantic import BaseModel
import django.conf

from .models import Ping
from fastjsonapi import Computed, Filterable
from fastjsonapi.django import wrap, unwrap


default_page_size = django.conf.settings.REST_FRAMEWORK["PAGE_SIZE"]


class PingModel(BaseModel):
    message: Annotated[str | None, Filterable()] = None
    created_at: Annotated[datetime.datetime, Computed()]
    prev: Annotated[PingModel | None, Filterable()] = None
    next: list[PingModel] = []

class PingsResource:
    singular_name = "ping"
    plural_name = "pings"

    Model = PingModel

    default_page_size = default_page_size

    class ItemCreator:
        def __call__(self, *, message, prev, next):
            ping = Ping.objects.create(message=message, prev=unwrap(prev))
            ping.next.set([unwrap(n) for n in next])
            ping.save()
            return wrap(ping)

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(Ping.objects.get(id=id))
            except Ping.DoesNotExist:
                return None

    class PageGetter:
        def __call__(self, sort, filters, first_index, page_size):
            sort = sort or ["id"]
            pings = Ping.objects.order_by(*sort)

            # @todo Use proper SQL filtering
            if filters.message:
                pings = [ping for ping in pings if ping.message == filters.message]
            if filters.prev:
                pings = [ping for ping in pings if ping.prev is not None and str(ping.prev.id) == filters.prev]

            return (
                # @todo Use proper SQL counting
                len(pings),
                # @todo Use proper SQL limits
                [wrap(ping) for ping in pings[first_index:first_index + page_size]],
            )

    class ItemSaver:
        @contextmanager
        def __call__(self, item):
            yield
            item.save()

    class ItemDeleter:
        def __call__(self, item):
            item.delete()
