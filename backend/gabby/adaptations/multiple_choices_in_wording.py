from typing import Literal

from mydantic import PydanticBase


# @todo(After production data is migrated) Remove this class
# Note that it's not unit-tested anymore
class MultipleChoicesInWordingAdaptation(PydanticBase):
    kind: Literal["multiple-choices-in-wording"]

    def make_effects(self):
        return []
