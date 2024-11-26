from typing import Any

from mydantic import PydanticBase


class InsertOp(PydanticBase):
    insert: str
    attributes: dict[str, Any]


Deltas = list[InsertOp]


def _as_list(deltas):
    return [d.model_dump() for d in deltas]

empty = [InsertOp(insert="\n", attributes={})]

empty_as_list = _as_list(empty)

empty_as_string = '[{"insert": "\\n", "attributes": {}}]'
