from typing import Annotated
import datetime

from pydantic import Field as PydanticField
from pydantic import fields
from pydantic_core import PydanticUndefined
import pydantic


class PydanticBase(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid", strict=True)


def create_model(*args, **kwds):
    for k, v in kwds.items():
        if v[0] in [datetime.datetime, datetime.timedelta]:
            v = list(v)
            v[0] = Annotated[v[0], PydanticField(strict=False)]
            kwds[k] = tuple(v)
    return pydantic.create_model(*args, **kwds, __base__=PydanticBase)
