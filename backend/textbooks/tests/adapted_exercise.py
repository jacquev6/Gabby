from django.test import TestCase
from starlette import status

from ..models import Exercise, SelectThingsAdaptedExercise, FillWithFreeTextAdaptedExercise
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
        adapted = SelectThingsAdaptedExercise(exercise=exercise, colors=2, words=True, punctuation=False)

        self.assertEqual(
            adapted.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=None,
                instructions="instructions",
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


class FillWithFreeTextAdaptedExerciseBusinessTestCase(TestCase):
    def test_single_sentence(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="The wording of this ... is a ... sentence.",
        )
        adapted = FillWithFreeTextAdaptedExercise(exercise=exercise, placeholder="...")

        self.assertEqual(
            adapted.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions="instructions",
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
        adapted = FillWithFreeTextAdaptedExercise(exercise=exercise, placeholder="@")

        self.assertEqual(
            adapted.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=None,
                instructions="instructions",
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
                    "type": "selectThings",
                    "options": {
                        "colors": 3,
                        "words": True,
                        "punctuation": False,
                    }
                },
            },
        }
        response = self.post("http://server/adaptedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": 1,  # @todo Rename to textbookPage
            "instructions": "This is the instructions.",
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
                    "type": "fillWithFreeText",
                    "options": {
                        "placeholder": "@",
                    }
                },
            },
        }
        response = self.post("http://server/adaptedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": 1,  # @todo Rename to textbookPage
            "instructions": "This is the instructions.",
            "wording": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "plainText", "text": "Fill"},
                {"type": "whitespace"},
                {"type": "freeTextInput"},
            ]}]}]},
        })
