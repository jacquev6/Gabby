from typing import Literal

from mydantic import PydanticBase


class NullAdaptation(PydanticBase):
    kind: Literal["null"]

    def make_effects(self):
        return []
