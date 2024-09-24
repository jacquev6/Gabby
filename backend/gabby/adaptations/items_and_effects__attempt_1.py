from contextlib import contextmanager

from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import parsing
from .. import renderable
from .. import settings
from ..api_utils import create_item, get_item, save_item, delete_item
from ..database_utils import SessionDependable
from ..exercises import Adaptation
from ..users import MandatoryAuthBearerDependable
from ..wrapping import set_wrapper, make_sqids, orm_wrapper_with_sqids


class ItemsAndEffectsAttempt1Adaptation(Adaptation):
    __tablename__ = "adaptations__iae1"
    __mapper_args__ = {
        "polymorphic_identity": "iae1",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)

    def make_adapted_instructions(self):
        return parsing.adapt_plain_instructions_section(self.exercise.instructions)

    def make_adapted_wording(self):
        return parsing.adapt_plain_wording_section(self.exercise.wording)

    def make_adapted_example(self):
        return parsing.adapt_plain_instructions_section(self.exercise.example)

    def make_adapted_clue(self):
        return parsing.adapt_plain_instructions_section(self.exercise.clue)

    def make_instructions_delta(self):
        return parsing.make_plain_instructions_section_delta(self.exercise.instructions)

    def make_wording_delta(self):
        return parsing.make_plain_wording_section_delta(self.exercise.wording)

    def make_example_delta(self):
        return parsing.make_plain_instructions_section_delta(self.exercise.example)

    def make_clue_delta(self):
        return parsing.make_plain_instructions_section_delta(self.exercise.clue)


class ItemsAndEffectsAttempt1AdaptationsResource:
    singular_name = "items_and_effects_attempt_1_adaptation"
    plural_name = "items_and_effects_attempt_1_adaptations"

    Model = api_models.ItemsAndEffectsAttempt1Adaptation

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    def create_item(
        self,
        exercise,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        if exercise.adaptation is not None:
            session.delete(exercise.adaptation)
        return create_item(
            session, ItemsAndEffectsAttempt1Adaptation,
            exercise=exercise,
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
