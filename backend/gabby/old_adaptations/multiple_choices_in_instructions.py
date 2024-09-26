from contextlib import contextmanager

from sqlalchemy import orm
import sqlalchemy as sql

from .. import api_models
from .. import exercise_delta as d
from .. import renderable as r
from .. import settings
from ..api_utils import create_item, get_item, save_item, delete_item
from ..database_utils import SessionDependable
from ..exercises import OldAdaptation
from ..exercises import OldAdaptation, Exercise
from ..testing import AdaptationTestCase
from ..users import MandatoryAuthBearerDependable
from ..wrapping import set_wrapper, make_sqids, orm_wrapper_with_sqids


class MultipleChoicesInInstructionsAdaptation(OldAdaptation):
    __tablename__ = "adaptations__mcii"
    __mapper_args__ = {
        "polymorphic_identity": "mcii",
    }

    id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey(OldAdaptation.id), primary_key=True)

    placeholder: orm.Mapped[str]

    def to_new_adaptation(self):
        return api_models.MultipleChoicesInInstructionsAdaptation_(
            kind="multiple-choices-in-instructions",
            placeholder=self.placeholder,
        )


class MultipleChoicesInInstructionsAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose {choice|a} or {choice|b}.",
            wording="A ... B ...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = MultipleChoicesInInstructionsAdaptation(exercise=exercise, placeholder="...")

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
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="Choose "),
                    d.InsertOp(insert="a", attributes={"choice": True}),
                    d.InsertOp(insert=" or "),
                    d.InsertOp(insert="b", attributes={"choice": True}),
                    d.InsertOp(insert="."),
                ],
                wording=[
                    d.InsertOp(insert="A ... B ..."),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_example_and_clue(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose {choice|a} or {choice|b}.",
            wording="A @ B @",
            example="This {choice|is} the @ example.",
            clue="This is {choice|the} @ clue.",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = MultipleChoicesInInstructionsAdaptation(exercise=exercise, placeholder="@")

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
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="choice"),
                            r.PlainText(text="|"),
                            r.PlainText(text="is"),
                            r.PlainText(text="}"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="@"),
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
                            r.PlainText(text="{"),
                            r.PlainText(text="choice"),
                            r.PlainText(text="|"),
                            r.PlainText(text="the"),
                            r.PlainText(text="}"),
                            r.Whitespace(),
                            r.PlainText(text="@"),
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
                    d.InsertOp(insert="Choose "),
                    d.InsertOp(insert="a", attributes={"choice": True}),
                    d.InsertOp(insert=" or "),
                    d.InsertOp(insert="b", attributes={"choice": True}),
                    d.InsertOp(insert="."),
                ],
                wording=[
                    d.InsertOp(insert="A @ B @"),
                ],
                example=[
                    d.InsertOp(insert="This {choice|is} the @ example."),
                ],
                clue=[
                    d.InsertOp(insert="This is {choice|the} @ clue."),
                ],
            ),
        )

    def test_lenient_paragraphs(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="{choice|a} # {choice|b}\n\n c #\nd.",
            wording="...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = MultipleChoicesInInstructionsAdaptation(exercise=exercise, placeholder="...")

        self.do_test(
            adaptation,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="#"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="c"),
                            r.Whitespace(),
                            r.PlainText(text="#"),
                            r.Whitespace(),
                            r.PlainText(text="d"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert="a", attributes={"choice": True}),
                    d.InsertOp(insert=" # "),
                    d.InsertOp(insert="b", attributes={"choice": True}),
                    d.InsertOp(insert="\n\n c #\nd."),
                ],
                wording=[
                    d.InsertOp(insert="..."),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_whitespace(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions=" \t  Choose  \t\n  {choice|a}.   Or {choice|b} .   \t\n   ",
            wording="...",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
        )
        adaptation = MultipleChoicesInInstructionsAdaptation(exercise=exercise, placeholder="...")

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
                            r.BoxedText(text="a"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.Whitespace(),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.InsertOp(insert=" \t  Choose  \t\n  "),
                    d.InsertOp(insert="a", attributes={"choice": True}),
                    d.InsertOp(insert=".   Or "),
                    d.InsertOp(insert="b", attributes={"choice": True}),
                    d.InsertOp(insert=" .   \t\n   "),
                ],
                wording=[
                    d.InsertOp(insert="..."),
                ],
                example=[],
                clue=[],
            ),
        )


class MultipleChoicesInInstructionsAdaptationsResource:
    singular_name = "multiple_choices_in_instructions_adaptation"
    plural_name = "multiple_choices_in_instructions_adaptations"

    Model = api_models.MultipleChoicesInInstructionsAdaptation

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    def create_item(
        self,
        exercise,
        placeholder,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        if exercise.old_adaptation is not None:
            session.delete(exercise.old_adaptation)
        return create_item(
            session, MultipleChoicesInInstructionsAdaptation,
            exercise=exercise,
            placeholder=placeholder,
            created_by=authenticated_user,
            updated_by=authenticated_user,
        )

    def get_item(
        self,
        id,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        return get_item(session, MultipleChoicesInInstructionsAdaptation, MultipleChoicesInInstructionsAdaptationsResource.sqids.decode(id)[0])

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


set_wrapper(MultipleChoicesInInstructionsAdaptation, orm_wrapper_with_sqids(MultipleChoicesInInstructionsAdaptationsResource.sqids))
