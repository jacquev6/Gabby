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
from ..exercises import Adaptation
from ..users import MandatoryAuthBearerDependable
from ..wrapping import set_wrapper, make_sqids, orm_wrapper_with_sqids


class ItemsAndEffectsAttempt1Adaptation(Adaptation):
    __tablename__ = "adaptations__iae1"
    __mapper_args__ = {
        "polymorphic_identity": "iae1",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)

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

    @property
    def _color_indexes(self):
        if self.effects.selectable is None:
            return []
        else:
            return range(1, len(self.effects.selectable.colors) + 1)

    def _make_tags(self):
        tags = {}
        if self.effects.selectable is not None:
            tags.update({f"sel{color_index}": r""" "|" STR """ for color_index in self._color_indexes})
        return tags

    def _make_adapter_type(self):
        tag_functions = {}
        if self.effects.selectable is not None:
            colors = self.effects.selectable.colors
            tag_functions.update({
                f"sel{color_index}_tag": (lambda color: staticmethod(lambda args: renderable.SelectedText(text=args[0], color=color)))(colors[color_index - 1])
                for color_index in self._color_indexes
            })
        return type("InstructionsAdapter", (parsing.InstructionsSectionAdapter,), tag_functions)

    def adapt_instructions(self, section):
        return parsing.InstructionsSectionParser(
            self._make_tags(),
            self._make_adapter_type()(),
        )(
            section,
        )

    def make_adapted_instructions(self):
        return self.adapt_instructions(self.exercise.instructions)

    class WordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, punctuation, colors, boxed):
            self.select_punctuation = punctuation
            self.colors = colors
            self.boxed = boxed

        def WORD(self, arg):
            return renderable.SelectableText(text=arg.value, colors=self.colors, boxed=self.boxed)

        def PUNCTUATION_IN_SENTENCE(self, arg):
            if self.select_punctuation:
                return renderable.SelectableText(text=arg.value, colors=self.colors, boxed=self.boxed)
            else:
                return renderable.PlainText(text=arg.value)

        PUNCTUATION_AT_END_OF_SENTENCE = PUNCTUATION_IN_SENTENCE
        PUNCTUATION_IN_LENIENT_PARAGRAPH = PUNCTUATION_IN_SENTENCE

    def make_adapted_wording(self):
        if self.effects.selectable is None:
            return parsing.adapt_plain_wording_section(self.exercise.wording)
        else:
            assert self.items.kind == "words"
            return parsing.parse_wording_section(
                {},
                self.WordingAdapter(self.items.punctuation, self.effects.selectable.colors, self.effects.boxed),
                self.exercise.wording,
            )

    def make_adapted_example(self):
        return self.adapt_instructions(self.exercise.example)

    def make_adapted_clue(self):
        return self.adapt_instructions(self.exercise.clue)

    def _make_delta_maker_type(self):
        tag_functions = {}
        if self.effects.selectable is not None:
            tag_functions.update({
                f"sel{color_index}_tag": (lambda color_index: staticmethod(lambda args: exercise_delta.InsertOp(insert=args[0], attributes={"sel": color_index})))(color_index)
                for color_index in self._color_indexes
            })
        return type("InstructionsDeltaMaker", (parsing.InstructionsSectionDeltaMaker,), tag_functions)

    def _make_instructions_delta(self, section):
        return parsing.InstructionsSectionParser(
            self._make_tags(),
            self._make_delta_maker_type()(),
        )(
            section,
        )

    def make_instructions_delta(self):
        return self._make_instructions_delta(self.exercise.instructions)

    def make_wording_delta(self):
        return parsing.make_plain_wording_section_delta(self.exercise.wording)

    def make_example_delta(self):
        return self._make_instructions_delta(self.exercise.example)

    def make_clue_delta(self):
        return self._make_instructions_delta(self.exercise.clue)


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
        if exercise.adaptation is not None:
            session.delete(exercise.adaptation)
        return create_item(
            session, ItemsAndEffectsAttempt1Adaptation,
            exercise=exercise,
            items=items.model_dump(),
            effects=effects.model_dump(),
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
