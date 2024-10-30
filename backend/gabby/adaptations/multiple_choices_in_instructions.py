from typing import Literal

from .. import parsing
from mydantic import PydanticBase


# @todo(After production data is migrated) Remove this class
# Note that it's not unit-tested anymore
class MultipleChoicesInInstructionsAdaptation(PydanticBase):
    kind: Literal["multiple-choices-in-instructions"]

    placeholder: str

    def make_effects(self):
        return [parsing.MultipleChoicesInInstructionsAdaptationEffect(
            kind="multiple-choices-in-instructions",
            placeholder=self.placeholder,
        )]
