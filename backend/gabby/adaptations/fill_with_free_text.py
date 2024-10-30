from typing import Literal

from .. import parsing
from mydantic import PydanticBase


# @todo(After production data is migrated) Remove this class
# Note that it's not unit-tested anymore
class FillWithFreeTextAdaptation(PydanticBase):
    kind: Literal["fill-with-free-text"]

    placeholder: str

    def make_effects(self):
        return [parsing.FillWithFreeTextAdaptationEffect(
            kind="fill-with-free-text",
            placeholder=self.placeholder,
        )]
