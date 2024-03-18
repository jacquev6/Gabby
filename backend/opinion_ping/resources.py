from __future__ import annotations
from typing import Annotated
import datetime

from pydantic import BaseModel
from fastapi import Query

from fastjsonapi import Computed
from .models import Ping


class PingModel(BaseModel):
    message: str | None = None
    # @todo Name fields in snake_case, transform them into camelCase in API
    createdAt: Annotated[datetime.datetime, Computed()]
    prev: PingModel | None = None
    next: list[PingModel] = []


class PingsResource:
    singular_name = "ping"
    plural_name = "pings"

    Model = PingModel

    # @todo Pre-populate 'relationships' to avoid calling 'Ping.objects.get' here
    def create_item(self, attributes, relationships):
        ping = Ping.objects.create(message=attributes.message)

        prev = relationships.prev.data
        ping.prev = None if prev is None else Ping.objects.get(id=int(prev.id))

        ping.next.set([Ping.objects.get(id=int(next.id)) for next in relationships.next.data])

        ping.save()

        return ping

    def get_item(self, id):
        try:
            return Ping.objects.get(id=id)
        except Ping.DoesNotExist:
            return None

    # @todo Provide utility to avoid writing 'filter[whatever]' here
    @staticmethod
    def filters(filter_message: Annotated[str, Query(alias="filter[message]")] = None):
        return {
            "message": filter_message,
        }

    def get_page(self, filters, first_index, page_size):
        pings = Ping.objects.all()
        if filters["message"]:
            pings = [ping for ping in pings if ping.message == filters["message"]]

        return (len(pings), pings[first_index:first_index + page_size])

    # @todo Pre-populate 'relationships' to avoid calling 'Ping.objects.get' here
    # @todo Handle generic JSON:API stuff in the common part, not here
    def update_item(self, ping, attributes, relationships):
        attributes_actually_set = set(attributes.model_dump(exclude_unset=True).keys())
        if "message" in attributes_actually_set:
            ping.message = attributes.message

        relationships_actually_set = set(relationships.model_dump(exclude_unset=True).keys())
        if "prev" in relationships_actually_set:
            prev = relationships.prev.data
            ping.prev = None if prev is None else Ping.objects.get(id=int(prev.id))
        if "next" in relationships_actually_set:
            ping.next.set(Ping.objects.get(id=int(next.id)) for next in relationships.next.data)

        ping.save()

    def delete_item(self, ping):
        ping.delete()

    def make_attributes(self, ping):
        return dict(
            createdAt=ping.created_at,
            message=ping.message,
        )

    # @todo Do the "data" thing in the common part, not here
    def make_relationships(self, ping):
        return {
            "prev": {"data": None if ping.prev is None else self.make_item_id(ping.prev)},
            "next": {"data": [self.make_item_id(next) for next in ping.next.all()], "meta": {"count": ping.next.count()}},
        }

    def make_item_id(self, item):
        return {
            "type": self.singular_name,
            "id": str(item.id),
        }
