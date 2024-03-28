from __future__ import annotations
import dataclasses

from pydantic import BaseModel


class Model(BaseModel):
    name: str
    single: Model | None = None
    several: list[Model] = []


@dataclasses.dataclass
class Item:
    id: str

    name: str
    single: Item | None
    several: list[Item]
