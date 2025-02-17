from typing import Literal, Annotated

from pydantic import AliasChoices

from mydantic import PydanticBase, PydanticField


class Choices2(PydanticBase):
    start: str
    separator1: str
    separator2: str
    stop: str
    placeholder: str
    mcqFieldUid: str | None = None

class TextInsertOpAttributes(PydanticBase):
    italic: bool = False
    bold: bool = False
    choices2: Choices2 | None = None
    mcq_placeholder: Annotated[bool, PydanticField(serialization_alias="mcq-placeholder", validation_alias=AliasChoices("mcq-placeholder", "mcq_placeholder"))] = False
    manual_item: Annotated[bool, PydanticField(serialization_alias="manual-item", validation_alias=AliasChoices("manual-item", "manual_item"))] = False
    sel: int | None = None

class TextInsertOp(PydanticBase):
    kind: Annotated[Literal["text"], PydanticField(exclude=True)] = "text"
    insert: str
    attributes: TextInsertOpAttributes


class McqFieldEmbedInsertOpInsert(PydanticBase):
    kind: Annotated[Literal["mcq-field"], PydanticField(exclude=True)] = "mcq-field"
    mcq_field: Annotated[str, PydanticField(serialization_alias="mcq-field", validation_alias=AliasChoices("mcq-field", "mcq_field"))]

EmbedInsertOpInsert = McqFieldEmbedInsertOpInsert

class EmbedInsertOp(PydanticBase):
    kind: Annotated[Literal["embed"], PydanticField(exclude=True)] = "embed"
    insert: EmbedInsertOpInsert


Deltas = list[TextInsertOp | EmbedInsertOp]


def to_list(deltas: Deltas):
    return [d.model_dump(by_alias=True, exclude_defaults=True) for d in deltas]

empty = [TextInsertOp(insert="\n", attributes={})]

empty_as_list = to_list(empty)

empty_as_string = '[{"insert": "\\n", "attributes": {}}]'


def make(deltas):
    return [
        TextInsertOp(**d) if isinstance(d["insert"], str) else EmbedInsertOp(**d)
        for d in deltas
    ]
