from contextlib import contextmanager

from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import parsing
from .. import renderable
from .. import renderable as r
from .. import settings
from ..api_utils import create_item, get_item, save_item, delete_item
from ..database_utils import SessionDependable
from ..exercises import Adaptation, Exercise
from ..testing import AdaptationTestCase
from ..users import MandatoryAuthBearerDependable
from ..wrapping import set_wrapper, make_sqids, orm_wrapper_with_sqids


class MultipleChoicesInWordingAdaptation(Adaptation):
    __tablename__ = "adaptations__mciw"
    __mapper_args__ = {
        "polymorphic_identity": "mciw",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)

    def make_adapted_instructions(self):
        return parsing.adapt_plain_instructions_section(self.exercise.instructions)

    class WordingAdapter(parsing.WordingSectionAdapter):
        def choices_tag(self, args):
            return renderable.MultipleChoicesInput(choices=[arg for arg in args])

    adapt_wording = parsing.WordingSectionParser({"choices": r""" ("|" STR)+ """}, WordingAdapter())

    def make_adapted_wording(self):
        return self.adapt_wording(self.exercise.wording)

    def make_adapted_example(self):
        return parsing.adapt_plain_instructions_section(self.exercise.example)

    def make_adapted_clue(self):
        return parsing.adapt_plain_instructions_section(self.exercise.clue)

    def make_instructions_delta(self):
        return parsing.make_plain_instructions_section_delta(self.exercise.instructions)


class MultipleChoicesInWordingAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices|a|b|c} B {choices|d|e}.",
            example="",
            clue="",
        )
        adaptation = MultipleChoicesInWordingAdaptation(exercise=exercise)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["d", "e"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
            ),
        )

    def test_example_and_clue(self):
        pass  # @todo Implement this test


class MultipleChoicesInWordingAdaptationsResource:
    singular_name = "multiple_choices_in_wording_adaptation"
    plural_name = "multiple_choices_in_wording_adaptations"

    Model = api_models.MultipleChoicesInWordingAdaptation

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
            session, MultipleChoicesInWordingAdaptation,
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
        return get_item(session, MultipleChoicesInWordingAdaptation, MultipleChoicesInWordingAdaptationsResource.sqids.decode(id)[0])

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


set_wrapper(MultipleChoicesInWordingAdaptation, orm_wrapper_with_sqids(MultipleChoicesInWordingAdaptationsResource.sqids))
