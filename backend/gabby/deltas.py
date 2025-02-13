from typing import Any

from mydantic import PydanticBase


class TextInsertOp(PydanticBase):
    insert: str
    attributes: dict[str, Any]


class EmbedInsertOp(PydanticBase):
    insert: dict[str, Any]


Deltas = list[TextInsertOp | EmbedInsertOp]


def _as_list(deltas):
    return [d.model_dump() for d in deltas]

empty = [TextInsertOp(insert="\n", attributes={})]

empty_as_list = _as_list(empty)

empty_as_string = '[{"insert": "\\n", "attributes": {}}]'


def make(deltas):
    return [
        TextInsertOp(**d) if isinstance(d["insert"], str) else EmbedInsertOp(**d)
        for d in deltas
    ]
