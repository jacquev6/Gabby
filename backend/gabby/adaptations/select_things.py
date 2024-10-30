from typing import Literal

from .. import parsing
from mydantic import PydanticBase


# @todo(After production data is migrated) Remove this class
# Note that it's not unit-tested anymore
class SelectThingsAdaptation(PydanticBase):
    kind: Literal["select-things"]

    colors: list[str]
    words: bool
    punctuation: bool

    def make_effects(self):
        return [parsing.SelectThingsAdaptationEffect(
            kind="select-things",
            colors=self.colors,
            words=self.words,
            punctuation=self.punctuation,
        )]
