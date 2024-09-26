from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from ..exercises import OldAdaptation


class ItemsAndEffectsAttempt1Adaptation(OldAdaptation):
    __tablename__ = "adaptations__iae1"
    __mapper_args__ = {
        "polymorphic_identity": "iae1",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(OldAdaptation.id), primary_key=True)

    _items: orm.Mapped[dict] = orm.mapped_column(sql.JSON, name="items")

    @property
    def items(self) -> api_models.ItemsAndEffectsAttempt1Adaptation.Items:
        match self._items["kind"]:
            case "words":
                return api_models.ItemsAndEffectsAttempt1Adaptation.WordsItems(**self._items)
            case "sentences":
                return api_models.ItemsAndEffectsAttempt1Adaptation.SentencesItems(**self._items)
            case "manual":
                return api_models.ItemsAndEffectsAttempt1Adaptation.ManualItems(**self._items)
            case _:
                assert False, f"Unknown items kind: {self._items['kind']}"

    @items.setter
    def items(self, items: api_models.ItemsAndEffectsAttempt1Adaptation.Items):
        self._items = items.model_dump()

    _effects: orm.Mapped[dict] = orm.mapped_column(sql.JSON, name="effects")

    @property
    def effects(self) -> api_models.ItemsAndEffectsAttempt1Adaptation.Effects:
        return api_models.ItemsAndEffectsAttempt1Adaptation.Effects(**self._effects)

    @effects.setter
    def effects(self, effects: api_models.ItemsAndEffectsAttempt1Adaptation.Effects):
        self._effects = effects.model_dump()
