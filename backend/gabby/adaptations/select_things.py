from contextlib import contextmanager

from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import exercise_delta
from .. import exercise_delta as d
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
    old_colors_count: orm.Mapped[int]
    colors: orm.Mapped[list[str]] = orm.mapped_column(sql.JSON, name="colors")

    @property
    def _color_indexes(self):
        return range(1, len(self.colors) + 1)

    def _make_tags(self):
        return {f"sel{color_index}": r""" "|" STR """ for color_index in self._color_indexes}

    def _make_adapter_type(self):
        return type("InstructionsAdapter", (parsing.InstructionsSectionAdapter,), {
            f"sel{color_index}_tag": (lambda color_index: staticmethod(lambda args: renderable.SelectedText(text=args[0], color=self.colors[color_index - 1])))(color_index)
            for color_index in self._color_indexes
        })

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
        def __init__(self, words, punctuation, colors):
            self.select_words = words
            self.select_punctuation = punctuation
            self.colors = colors

        def WORD(self, arg):
            if self.select_words:
                return renderable.SelectableText(text=arg.value, colors=self.colors)
            else:
                return renderable.PlainText(text=arg.value)

        def PUNCTUATION_IN_SENTENCE(self, arg):
            if self.select_punctuation:
                return renderable.SelectableText(text=arg.value, colors=self.colors)
            else:
                return renderable.PlainText(text=arg.value)

        PUNCTUATION_AT_END_OF_SENTENCE = PUNCTUATION_IN_SENTENCE
        PUNCTUATION_IN_LENIENT_PARAGRAPH = PUNCTUATION_IN_SENTENCE

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

    def _make_delta_maker_type(self):
        return type("InstructionsDeltaMaker", (parsing.InstructionsSectionDeltaMaker,), {
            f"sel{color_index}_tag": (lambda color: staticmethod(lambda args: exercise_delta.InsertOp(insert=args[0], attributes={"sel": color})))(color_index)
            for color_index in self._color_indexes
        })

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


class SelectThingsAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="The wording of this exercise is a single sentence.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, old_colors_count=2, colors=["red", "blue"], words=True, punctuation=False)

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
                            r.SelectableText(text="The", colors=["red", "blue"]),
                            r.Whitespace(),
                            r.SelectableText(text="wording", colors=["red", "blue"]),
                            r.Whitespace(),
                            r.SelectableText(text="of", colors=["red", "blue"]),
                            r.Whitespace(),
                            r.SelectableText(text="this", colors=["red", "blue"]),
                            r.Whitespace(),
                            r.SelectableText(text="exercise", colors=["red", "blue"]),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=["red", "blue"]),
                            r.Whitespace(),
                            r.SelectableText(text="a", colors=["red", "blue"]),
                            r.Whitespace(),
                            r.SelectableText(text="single", colors=["red", "blue"]),
                            r.Whitespace(),
                            r.SelectableText(text="sentence", colors=["red", "blue"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="instructions"),
                ],
                wording=[
                    d.InsertOp(insert="The wording of this exercise is a single sentence."),
                ],
                example=[],
                clue=[],
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
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red", "green", "blue"], words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color="red"),
                            r.Whitespace(),
                            r.SelectedText(text="def", color="green"),
                            r.Whitespace(),
                            r.SelectedText(text="ghi", color="blue"),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="sel4"),
                            r.PlainText(text="|"),
                            r.PlainText(text="jkl"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red", "green", "blue"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="abc", attributes={"sel": 1}),
                    d.InsertOp(insert=" "),
                    d.InsertOp(insert="def", attributes={"sel": 2}),
                    d.InsertOp(insert=" "),
                    d.InsertOp(insert="ghi", attributes={"sel": 3}),
                    d.InsertOp(insert=" {sel4|jkl}"),
                ],
                wording=[
                    d.InsertOp(insert="wording"),
                ],
                example=[],
                clue=[],
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
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, old_colors_count=1, colors=["red"], words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color="red"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="abc", attributes={"sel": 1}),
                ],
                wording=[
                    d.InsertOp(insert="wording"),
                ],
                example=[],
                clue=[],
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
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, old_colors_count=1, colors=["red"], words=True, punctuation=False)

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
                            r.SelectableText(text="wording", colors=["red"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines"),
                ],
                wording=[
                    d.InsertOp(insert="wording"),
                ],
                example=[],
                clue=[],
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
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, old_colors_count=1, colors=["red"], words=True, punctuation=False)

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
                            r.SelectableText(text="wording", colors=["red"]),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=["red"]),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="on", colors=["red"]),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="multiple", colors=["red"]),
                            r.Whitespace(),
                            r.SelectableText(text="lines", colors=["red"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="instructions"),
                ],
                wording=[
                    d.InsertOp(insert="wording is\n\non\n\nmultiple lines"),
                ],
                example=[],
                clue=[],
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
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, old_colors_count=1, colors=["red"], words=True, punctuation=False)

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
                            r.SelectableText(text="tag", colors=["red"]),
                            r.PlainText(text="|"),
                            r.SelectableText(text="def", colors=["red"]),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="{tag|abc}"),
                ],
                wording=[
                    d.InsertOp(insert="{tag|def}"),
                ],
                example=[],
                clue=[],
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
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, old_colors_count=1, colors=["red"], words=True, punctuation=False)

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
                            r.SelectableText(text="def", colors=["red"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="   abc   "),
                ],
                wording=[
                    d.InsertOp(insert="   def   "),
                ],
                example=[],
                clue=[],
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
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, old_colors_count=1, colors=["red"], words=True, punctuation=False)

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
                            r.SelectableText(text="wording", colors=["red"]),
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
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="instructions"),
                ],
                wording=[
                    d.InsertOp(insert="wording"),
                ],
                example=[
                    d.InsertOp(insert="This is the example."),
                ],
                clue=[
                    d.InsertOp(insert="This is the clue."),
                ],
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
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=["red", "green", "blue"], words=True, punctuation=False)

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
                            r.SelectableText(text="wording", colors=["red", "green", "blue"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color="red"),
                            r.Whitespace(),
                            r.SelectedText(text="def", color="green"),
                        ]),
                    ]),
                ]),
                clue=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="ghi", color="blue"),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="sel4"),
                            r.PlainText(text="|"),
                            r.PlainText(text="jkl"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="instructions"),
                ],
                wording=[
                    d.InsertOp(insert="wording"),
                ],
                example=[
                    d.InsertOp(insert="abc", attributes={"sel": 1}),
                    d.InsertOp(insert=" "),
                    d.InsertOp(insert="def", attributes={"sel": 2}),
                ],
                clue=[
                    d.InsertOp(insert="ghi", attributes={"sel": 3}),
                    d.InsertOp(insert=" {sel4|jkl}"),
                ],
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
            old_colors_count=len(colors),
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
        item: SelectThingsAdaptation,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        yield
        item.updated_by = authenticated_user
        item.old_colors_count = len(item.colors)
        save_item(session, item)

    def delete_item(
        self,
        item,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        delete_item(session, item)


set_wrapper(SelectThingsAdaptation, orm_wrapper_with_sqids(SelectThingsAdaptationsResource.sqids))
