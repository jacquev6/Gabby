from typing import Any

from mydantic import PydanticBase


class InsertOp(PydanticBase):
    insert: str
    attributes: dict[str, Any] = {}


class Exercise(PydanticBase):
    instructions: list[InsertOp]
    wording: list[InsertOp]
    example: list[InsertOp]
    clue: list[InsertOp]
