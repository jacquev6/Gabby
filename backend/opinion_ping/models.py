from __future__ import annotations
from typing import Annotated
import datetime

from django.conf import settings
from django.db import models
from pydantic import BaseModel

from fastjsonapi.annotations import Computed, Filterable
from fastjsonapi.django import UserModel


# @todo Automate calling './manage.py graph_models' on change

class Ping(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="+")

    prev = models.ForeignKey("self", null=True, on_delete=models.SET_NULL, related_name="next")
    message = models.TextField(null=True, max_length=16)


class PingModel(BaseModel):
    message: Annotated[str | None, Filterable()] = None
    created_at: Annotated[datetime.datetime, Computed()]
    created_by: Annotated[UserModel | None, Computed()] = None
    updated_at: Annotated[datetime.datetime, Computed()]
    updated_by: Annotated[UserModel | None, Computed()] = None
    prev: Annotated[PingModel | None, Filterable()] = None
    next: list[PingModel] = []
