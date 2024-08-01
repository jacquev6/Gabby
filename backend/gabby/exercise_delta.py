from typing import Literal

import pydantic


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class InsertOp(BaseModel):
    insert: str
    attributes: dict[str, Literal[True]] = {}


class Exercise(BaseModel):
    instructions: list[InsertOp]
