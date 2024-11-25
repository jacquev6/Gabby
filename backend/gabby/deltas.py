from typing import Any

from mydantic import PydanticBase


class InsertOp(PydanticBase):
    insert: str
    attributes: dict[str, Any]


Deltas = list[InsertOp]


empty = [InsertOp(insert="\n", attributes={})]

empty_as_list = [{"insert": "\n", "attributes": {}}]

empty_as_string = '[{"insert": "\\n", "attributes": {}}]'


# @todo Remove
class Exercise(PydanticBase):
    instructions: list[InsertOp]
    wording: list[InsertOp]
    example: list[InsertOp]
    clue: list[InsertOp]
