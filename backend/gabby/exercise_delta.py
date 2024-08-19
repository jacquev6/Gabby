from typing import Literal

from mydantic import PydanticBase


class InsertOp(PydanticBase):
    insert: str
    attributes: dict[str, Literal[True]] = {}


class Exercise(PydanticBase):
    instructions: list[InsertOp]
    example: list[InsertOp]
    clue: list[InsertOp]
