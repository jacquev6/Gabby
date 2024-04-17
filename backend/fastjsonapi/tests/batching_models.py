from __future__ import annotations

from pydantic import BaseModel


class Model(BaseModel):
    name: str
    single: Model | None = None
    several: list[Model] = []


class Item:
    def __init__(self, id: str, name: str, single: Item | None, several: list[Item]):
        if name == "raise":
            raise ValueError("name == 'raise'")
        self.id = id
        self.name = name
        self.single = single
        self.several = several
