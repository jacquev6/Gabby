from contextlib import contextmanager

import django.conf
import django.contrib.auth
from fastapi import HTTPException
from starlette import status

from .models import Ping, PingModel
from fastjsonapi.django import OptionalAuthenticatedUser, wrap, unwrap


default_page_size = django.conf.settings.REST_FRAMEWORK["PAGE_SIZE"]


class PingsResource:
    singular_name = "ping"
    plural_name = "pings"

    Model = PingModel

    default_page_size = default_page_size

    class ItemCreator:
        def __init__(self, authenticated_user: OptionalAuthenticatedUser):
            self.__authenticated_user = authenticated_user

        def __call__(self, *, message, prev, next):
            ping = Ping.objects.create(
                message=message,
                prev=unwrap(prev),
                created_by=self.__authenticated_user,
                updated_by=self.__authenticated_user,
            )
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
        def __init__(self, authenticated_user: OptionalAuthenticatedUser):
            self.__authenticated_user = authenticated_user

        @contextmanager
        def __call__(self, item):
            created_by = unwrap(item.created_by)
            if created_by is not None:
                if self.__authenticated_user != created_by:
                    raise HTTPException(status.HTTP_403_FORBIDDEN, "You are not the creator of this ping")
            yield
            item.updated_by = self.__authenticated_user
            item.save()

    class ItemDeleter:
        def __init__(self, authenticated_user: OptionalAuthenticatedUser):
            self.__authenticated_user = authenticated_user

        def __call__(self, item):
            created_by = unwrap(item.created_by)
            if created_by is not None:
                if self.__authenticated_user != created_by:
                    raise HTTPException(status.HTTP_403_FORBIDDEN, "You are not the creator of this ping")
            item.delete()
