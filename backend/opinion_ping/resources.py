from __future__ import annotations
from typing import Annotated
import datetime

from pydantic import BaseModel
import django.conf


from fastjsonapi import Computed, Filterable
from fastjsonapi.django import DjangoOrmWrapper, unwrap
from .models import Ping


default_page_size = django.conf.settings.REST_FRAMEWORK["PAGE_SIZE"]


class PingModel(BaseModel):
    message: Annotated[str | None, Filterable()] = None
    created_at: Annotated[datetime.datetime, Computed()]
    prev: PingModel | None = None
    next: list[PingModel] = []

class PingsResource:
    singular_name = "ping"
    plural_name = "pings"

    Model = PingModel

    default_page_size = default_page_size

    def create_item(self, *, message, prev, next):
        ping = Ping.objects.create(message=message, prev=unwrap(prev))
        ping.next.set([unwrap(n) for n in next])
        ping.save()
        return DjangoOrmWrapper(ping)

    def get_item(self, id):
        try:
            return DjangoOrmWrapper(Ping.objects.get(id=id))
        except Ping.DoesNotExist:
            return None

    def get_page(self, filters, first_index, page_size):
        pings = Ping.objects.all()
        # @todo Use proper SQL filtering
        if filters.message:
            pings = [ping for ping in pings if ping.message == filters.message]

        return (
            # @todo Use proper SQL counting
            len(pings),
            # @todo Use proper SQL limits
            [DjangoOrmWrapper(ping) for ping in pings[first_index:first_index + page_size]],
        )
