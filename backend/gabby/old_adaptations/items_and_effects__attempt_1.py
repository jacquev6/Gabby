from contextlib import contextmanager
from typing import Literal

from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import exercise_delta
from .. import parsing
from .. import renderable
from .. import settings
from ..api_utils import create_item, get_item, save_item, delete_item
from ..database_utils import SessionDependable
from ..exercises import OldAdaptation
from ..users import MandatoryAuthBearerDependable
from ..wrapping import set_wrapper, make_sqids, orm_wrapper_with_sqids


class ItemsAndEffectsAttempt1Adaptation(OldAdaptation):
    __tablename__ = "adaptations__iae1"
    __mapper_args__ = {
        "polymorphic_identity": "iae1",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(OldAdaptation.id), primary_key=True)

    _items: orm.Mapped[dict] = orm.mapped_column(sql.JSON, name="items")

    @property
    def items(self) -> api_models.ItemsAndEffectsAttempt1AdaptationOptionsItems:
        match self._items["kind"]:
            case "words":
                return api_models.ItemsAndEffectsAttempt1AdaptationOptionsWordsItems(**self._items)
            case "sentences":
                return api_models.ItemsAndEffectsAttempt1AdaptationOptionsSentencesItems(**self._items)
            case "manual":
                return api_models.ItemsAndEffectsAttempt1AdaptationOptionsManualItems(**self._items)
            case _:
                assert False, f"Unknown items kind: {self._items['kind']}"

    @items.setter
    def items(self, items: api_models.ItemsAndEffectsAttempt1AdaptationOptionsItems):
        self._items = items.model_dump()

    _effects: orm.Mapped[dict] = orm.mapped_column(sql.JSON, name="effects")

    @property
    def effects(self) -> api_models.ItemsAndEffectsAttempt1AdaptationOptionsEffects:
        return api_models.ItemsAndEffectsAttempt1AdaptationOptionsEffects(**self._effects)

    @effects.setter
    def effects(self, effects: api_models.ItemsAndEffectsAttempt1AdaptationOptionsEffects):
        self._effects = effects.model_dump()


class ItemsAndEffectsAttempt1AdaptationsResource:
    singular_name = "items_and_effects_attempt_1_adaptation"
    plural_name = "items_and_effects_attempt_1_adaptations"

    Model = api_models.ItemsAndEffectsAttempt1Adaptation

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    def create_item(
        self,
        exercise,
        items,
        effects,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        if exercise.old_adaptation is not None:
            session.delete(exercise.old_adaptation)
        return create_item(
            session, ItemsAndEffectsAttempt1Adaptation,
            exercise=exercise,
            items=items,
            effects=effects,
            created_by=authenticated_user,
            updated_by=authenticated_user,
        )

    def get_item(
        self,
        id,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        return get_item(session, ItemsAndEffectsAttempt1Adaptation, ItemsAndEffectsAttempt1AdaptationsResource.sqids.decode(id)[0])

    @contextmanager
    def save_item(
        self,
        item,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        yield
        item.updated_by = authenticated_user
        save_item(session, item)

    def delete_item(
        self,
        item,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        delete_item(session, item)


set_wrapper(ItemsAndEffectsAttempt1Adaptation, orm_wrapper_with_sqids(ItemsAndEffectsAttempt1AdaptationsResource.sqids))
