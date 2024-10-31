from typing import Literal

from .. import parsing
from mydantic import PydanticBase


# @todo(After production data is migrated) Remove this class
# Note that it's not unit-tested anymore
class ItemsAndEffectsAttempt1Adaptation(PydanticBase):
    kind: Literal["items-and-effects-attempt-1"]

    items: parsing.ItemsAndEffectsAttempt1AdaptationEffect.Items
    effects: parsing.ItemsAndEffectsAttempt1AdaptationEffect.Effects

    def make_effects(self):
        return [parsing.ItemsAndEffectsAttempt1AdaptationEffect(
            kind="items-and-effects-attempt-1",
            items=self.items,
            effects=self.effects,
        )]
