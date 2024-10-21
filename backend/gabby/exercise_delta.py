from typing import Any

from mydantic import PydanticBase


class TextInsertOp(PydanticBase):
    insert: str
    attributes: dict[str, Any]

class EmbedInsertOp(PydanticBase):
    insert: dict[str, Any]

InsertOp = TextInsertOp | EmbedInsertOp


class Exercise(PydanticBase):
    instructions: list[InsertOp]
    wording: list[InsertOp]
    example: list[InsertOp]
    clue: list[InsertOp]
