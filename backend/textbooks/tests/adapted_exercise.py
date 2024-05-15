from django.test import TestCase
from starlette import status

from ..models import Exercise, SelectThingsAdaptation, FillWithFreeTextAdaptation
from ..resources import AdaptedExerciseResource
from .. import renderable as r
from fastjsonapi.testing import TestMixin


class SelectThingsAdaptedExerciseBusinessTestCase(TestCase):
    def test_single_sentence(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="The wording of this exercise is a single sentence.",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=2, words=True, punctuation=False)

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="instructions"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedClicks(type="selectedClicks", color=1, colors=2),
                            r.Whitespace(type="whitespace"),
                            r.SelectedClicks(type="selectedClicks", color=2, colors=2),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(type="selectableText", text="The", colors=2),
                            r.Whitespace(type="whitespace"),
                            r.SelectableText(type="selectableText", text="wording", colors=2),
                            r.Whitespace(type="whitespace"),
                            r.SelectableText(type="selectableText", text="of", colors=2),
                            r.Whitespace(type="whitespace"),
                            r.SelectableText(type="selectableText", text="this", colors=2),
                            r.Whitespace(type="whitespace"),
                            r.SelectableText(type="selectableText", text="exercise", colors=2),
                            r.Whitespace(type="whitespace"),
                            r.SelectableText(type="selectableText", text="is", colors=2),
                            r.Whitespace(type="whitespace"),
                            r.SelectableText(type="selectableText", text="a", colors=2),
                            r.Whitespace(type="whitespace"),
                            r.SelectableText(type="selectableText", text="single", colors=2),
                            r.Whitespace(type="whitespace"),
                            r.SelectableText(type="selectableText", text="sentence", colors=2),
                            r.PlainText(type="plainText", text="."),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_sel_tags(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="{sel1|abc} {sel2|def} {sel3|ghi} {sel4|jkl}",
            wording="wording",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=3, words=True, punctuation=False)

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(type="selectedText", text="abc", color=1, colors=3),
                            r.Whitespace(type="whitespace"),
                            r.SelectedText(type="selectedText", text="def", color=2, colors=3),
                            r.Whitespace(type="whitespace"),
                            r.SelectedText(type="selectedText", text="ghi", color=3, colors=3),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="{sel4|jkl}"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedClicks(type="selectedClicks", color=1, colors=3),
                            r.Whitespace(type="whitespace"),
                            r.SelectedClicks(type="selectedClicks", color=2, colors=3),
                            r.Whitespace(type="whitespace"),
                            r.SelectedClicks(type="selectedClicks", color=3, colors=3),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(type="selectableText", text="wording", colors=3),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_single_color(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="{sel1|abc}",
            wording="wording",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="{sel1|abc}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(type="selectableText", text="wording", colors=1),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_multiple_lines_in_instructions(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions\nare\n\non\n\nmultiple\nlines",
            wording="wording",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="instructions"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="are"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="on"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="multiple"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="lines"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(type="selectableText", text="wording", colors=1),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_multiple_lines_in_wording(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="wording\nis\n\non\n\nmultiple\nlines",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(type="selectableText", text="wording", colors=1),
                            r.Whitespace(type="whitespace"),
                            r.SelectableText(type="selectableText", text="is", colors=1),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(type="selectableText", text="on", colors=1),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(type="selectableText", text="multiple", colors=1),
                            r.Whitespace(type="whitespace"),
                            r.SelectableText(type="selectableText", text="lines", colors=1),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_unknown_tags(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="{tag|abc}",
            wording="{tag|def}",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="{tag|abc}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="{tag|def}"),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_strip_whitespace(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="   abc   ",
            wording="   def   ",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=1, words=True, punctuation=False)

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="abc"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(type="selectableText", text="def", colors=1),
                        ]),
                    ]),
                ]),
            ),
        )


class FillWithFreeTextAdaptationBusinessTestCase(TestCase):
    def test_single_sentence(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="The wording of this ... is a ... sentence.",
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="The"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="wording"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="of"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="this"),
                            r.Whitespace(type="whitespace"),
                            r.FreeTextInput(type="freeTextInput"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="is"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="a"),
                            r.Whitespace(type="whitespace"),
                            r.FreeTextInput(type="freeTextInput"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="sentence"),
                            r.PlainText(type="plainText", text="."),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_start_and_end_with_placeholder(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="@ a @",
        )
        adapted = FillWithFreeTextAdaptation(exercise=exercise, placeholder="@")

        self.assertEqual(
            adapted.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.FreeTextInput(type="freeTextInput"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="a"),
                            r.Whitespace(type="whitespace"),
                            r.FreeTextInput(type="freeTextInput"),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_multiple_lines_in_instructions(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions\nare\n\non\n\nmultiple\nlines",
            wording="wording",
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="instructions"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="are"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="on"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="multiple"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="lines"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="wording"),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_multiple_lines_in_wording(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="foo\ntoto : ...\n\nbar : ...\n\nbaz : ...",
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="foo"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text="toto"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text=":"),
                            r.Whitespace(type="whitespace"),
                            r.FreeTextInput(type="freeTextInput"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="bar"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text=":"),
                            r.Whitespace(type="whitespace"),
                            r.FreeTextInput(type="freeTextInput"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="baz"),
                            r.Whitespace(type="whitespace"),
                            r.PlainText(type="plainText", text=":"),
                            r.Whitespace(type="whitespace"),
                            r.FreeTextInput(type="freeTextInput"),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_unknown_tags(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="{tag|abc}",
            wording="{tag|def}",
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="{tag|abc}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="{tag|def}"),
                        ]),
                    ]),
                ]),
            ),
        )

    def test_strip_whitespace(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="   abc   ",
            wording="   def   ",
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.assertEqual(
            adaptation.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="abc"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(type="plainText", text="def"),
                        ]),
                    ]),
                ]),
            ),
        )


class AdaptedExerciseApiTestCase(TestMixin, TestCase):
    resources = [AdaptedExerciseResource]

    def test_select_things(self):
        payload = {
            "data": {
                "type": "adaptedExercise",
                "attributes": {
                    "number": "A.1",
                    "textbookPage": 1,
                    "instructions": "This is the instructions.",
                    "wording": "This is the wording.",
                    "type": "selectThingsAdaptation",
                    "adaptationOptions": {
                        "colors": 3,
                        "words": True,
                        "punctuation": False,
                    },
                },
            },
        }
        response = self.post("http://server/adaptedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": 1,  # @todo Rename to textbookPage
            "instructions": {"paragraphs": [
                {"sentences": [{"tokens": [
                    {"type": "plainText", "text": "This"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "is"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "the"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "instructions"},
                    {"type": "plainText", "text": "."},
                ]}]},
                {"sentences": [{"tokens": [
                    {"type": "selectedClicks", "color": 1, "colors": 3},
                    {"type": "whitespace"},
                    {"type": "selectedClicks", "color": 2, "colors": 3},
                    {"type": "whitespace"},
                    {"type": "selectedClicks", "color": 3, "colors": 3},
                ]}]},
            ]},
            "wording": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "selectableText", "text": "This", "colors": 3},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "is", "colors": 3},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "the", "colors": 3},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "wording", "colors": 3},
                {"type": "plainText", "text": "."},
            ]}]}]},
        })

    def test_fill_with_free_text(self):
        payload = {
            "data": {
                "type": "adaptedExercise",
                "attributes": {
                    "number": "A.1",
                    "textbookPage": 1,
                    "instructions": "This is the instructions.",
                    "wording": "Fill @",
                    "type": "fillWithFreeTextAdaptation",
                    "adaptationOptions": {
                        "placeholder": "@",
                    },
                },
            },
        }
        response = self.post("http://server/adaptedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": 1,  # @todo Rename to textbookPage
            "instructions": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "plainText", "text": "This"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "is"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "the"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "instructions"},
                {"type": "plainText", "text": "."},
            ]}]}]},
            "wording": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "plainText", "text": "Fill"},
                {"type": "whitespace"},
                {"type": "freeTextInput"},
            ]}]}]},
        })
