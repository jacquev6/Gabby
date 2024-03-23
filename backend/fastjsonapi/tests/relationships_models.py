from __future__ import annotations
import dataclasses

from pydantic import BaseModel


class TopModel(BaseModel):
    lefts: list[LeftModel] = []
    rights: list[RightModel] = []


@dataclasses.dataclass
class TopItem:
    id: str

    lefts: list[LeftItem]
    rights: list[RightItem]

    saved: int = 0


class LeftModel(BaseModel):
    top: TopModel
    right_or_none: RightModel | None = None


@dataclasses.dataclass
class LeftItem:
    id: str

    top: TopItem
    right_or_none: RightItem | None

    saved: int = 0


class RightModel(BaseModel):
    top: TopModel
    left_or_none: LeftModel | None = None


@dataclasses.dataclass
class RightItem:
    id: str

    top: TopItem
    left_or_none: LeftItem | None

    saved: int = 0
