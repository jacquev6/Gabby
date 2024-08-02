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


class SelectThingsAdaptation(Adaptation):
    __tablename__ = "adaptations__st"
    __mapper_args__ = {
        "polymorphic_identity": "st",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(Adaptation.id), primary_key=True)

    punctuation: orm.Mapped[bool]
    words: orm.Mapped[bool]
    colors: orm.Mapped[int]

    @property
    def color_indexes(self):
        return range(1, self.colors + 1)

    def _make_tags(self):
        return {f"sel{color_index}": r""" "|" STR """ for color_index in self.color_indexes}

    def _make_adapter_type(self):
        return type("InstructionsAdapter", (parsing.InstructionsSectionAdapter,), {
            f"sel{color_index}_tag": (lambda color: staticmethod(lambda args: renderable.SelectedText(text=args[0], color=color, colors=self.colors)))(color_index)
            for color_index in self.color_indexes
        })

    def adapt_instructions(self, section):
        return parsing.InstructionsSectionParser(
            self._make_tags(),
            self._make_adapter_type()(),
        )(
            section,
        )

    def make_adapted_instructions(self):
        section = self.adapt_instructions(self.exercise.instructions)

        if self.colors > 1:
            tokens = []
            for color in self.color_indexes:
                if color != 1:
                    tokens.append(renderable.Whitespace())
                tokens.append(renderable.SelectedClicks(color=color, colors=self.colors))
            section.paragraphs.append(renderable.Paragraph(sentences=[renderable.Sentence(tokens=tokens)]))

        return section

    class WordingAdapter(parsing.WordingSectionAdapter):
        def __init__(self, words, punctuation, colors):
            self.select_words = words
            self.select_punctuation = punctuation
            self.colors = colors

        def word(self, args):
            if self.select_words:
                return renderable.SelectableText(text=args[0].value, colors=self.colors)
            else:
                return renderable.PlainText(text=args[0].value)

        def punctuation(self, args):
            if self.select_punctuation:
                return renderable.SelectableText(text=args[0].value, colors=self.colors)
            else:
                return renderable.PlainText(text=args[0].value)

    def make_adapted_wording(self):
        return parsing.parse_wording_section(
            {},
            self.WordingAdapter(self.words, self.punctuation, self.colors),
            self.exercise.wording,
        )

    def make_adapted_example(self):
        return self.adapt_instructions(self.exercise.example)

    def make_adapted_clue(self):
        return self.adapt_instructions(self.exercise.clue)

    def make_instructions_delta(self):
        # @todo Implement
        return parsing.make_plain_instructions_section_delta(self.exercise.instructions)


class SelectThingsAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="The wording of this exercise is a single sentence.",
            example="",
            clue="",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=2, words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedClicks(color=1, colors=2),
                            r.Whitespace(),
                            r.SelectedClicks(color=2, colors=2),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="The", colors=2),
                            r.Whitespace(),
                            r.SelectableText(text="wording", colors=2),
                            r.Whitespace(),
                            r.SelectableText(text="of", colors=2),
                            r.Whitespace(),
                            r.SelectableText(text="this", colors=2),
                            r.Whitespace(),
                            r.SelectableText(text="exercise", colors=2),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=2),
                            r.Whitespace(),
                            r.SelectableText(text="a", colors=2),
                            r.Whitespace(),
                            r.SelectableText(text="single", colors=2),
                            r.Whitespace(),
                            r.SelectableText(text="sentence", colors=2),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
            ),
        )

    def test_sel_tags(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="{sel1|abc} {sel2|def} {sel3|ghi} {sel4|jkl}",
            wording="wording",
            example="",
            clue="",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=3, words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color=1, colors=3),
                            r.Whitespace(),
                            r.SelectedText(text="def", color=2, colors=3),
                            r.Whitespace(),
                            r.SelectedText(text="ghi", color=3, colors=3),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="sel4"),
                            r.PlainText(text="|"),
                            r.PlainText(text="jkl"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedClicks(color=1, colors=3),
                            r.Whitespace(),
                            r.SelectedClicks(color=2, colors=3),
                            r.Whitespace(),
                            r.SelectedClicks(color=3, colors=3),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=3),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
            ),
        )

    def test_single_color(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="{sel1|abc}",
            wording="wording",
            example="",
            clue="",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color=1, colors=1),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=1),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
            ),
        )

    def test_multiple_lines_in_instructions(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions\nare\n\non\n\nmultiple\nlines",
            wording="wording",
            example="",
            clue="",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                            r.Whitespace(),
                            r.PlainText(text="are"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="on"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="multiple"),
                            r.Whitespace(),
                            r.PlainText(text="lines"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=1),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
            ),
        )

    def test_multiple_lines_in_wording(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="wording is\n\non\n\nmultiple lines",
            example="",
            clue="",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=1),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=1),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="on", colors=1),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="multiple", colors=1),
                            r.Whitespace(),
                            r.SelectableText(text="lines", colors=1),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
            ),
        )

    def test_unknown_tags(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="{tag|abc}",
            wording="{tag|def}",
            example="",
            clue="",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{"),
                            r.PlainText(text="tag"),
                            r.PlainText(text="|"),
                            r.PlainText(text="abc"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{"),
                            r.SelectableText(text="tag", colors=1),
                            r.PlainText(text="|"),
                            r.SelectableText(text="def", colors=1),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
            ),
        )

    def test_strip_whitespace(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="   abc   ",
            wording="   def   ",
            example="",
            clue="",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="abc"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="def", colors=1),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
            ),
        )

    def test_example_and_clue(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="wording",
            example="This is the example.",
            clue="This is the clue.",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=1),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="example"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                clue=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="clue"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_example_and_clue_with_sel_tags(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="wording",
            example="{sel1|abc} {sel2|def}",
            clue="{sel3|ghi} {sel4|jkl}",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=3, words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedClicks(color=1, colors=3),
                            r.Whitespace(),
                            r.SelectedClicks(color=2, colors=3),
                            r.Whitespace(),
                            r.SelectedClicks(color=3, colors=3),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=3),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color=1, colors=3),
                            r.Whitespace(),
                            r.SelectedText(text="def", color=2, colors=3),
                        ]),
                    ]),
                ]),
                clue=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="ghi", color=3, colors=3),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="sel4"),
                            r.PlainText(text="|"),
                            r.PlainText(text="jkl"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
            ),
        )


class SelectThingsAdaptationsResource:
    singular_name = "select_things_adaptation"
    plural_name = "select_things_adaptations"

    Model = api_models.SelectThingsAdaptation

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    def create_item(
        self,
        exercise,
        punctuation,
        words,
        colors,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        if exercise.adaptation is not None:
            session.delete(exercise.adaptation)
        return create_item(
            session, SelectThingsAdaptation,
            exercise=exercise,
            punctuation=punctuation,
            words=words,
            colors=colors,
            created_by=authenticated_user,
            updated_by=authenticated_user,
        )

    def get_item(
        self,
        id,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        return get_item(session, SelectThingsAdaptation, SelectThingsAdaptationsResource.sqids.decode(id)[0])

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


set_wrapper(SelectThingsAdaptation, orm_wrapper_with_sqids(SelectThingsAdaptationsResource.sqids))
