from django.test import TestCase
from starlette import status

from ..models import Exercise, SelectWordsAdaptedExercise, FillWithFreeTextAdaptedExercise
from ..resources import AdaptedExerciseResource
from .. import renderable as r
from fastjsonapi.testing import TestMixin


class SelectWordsAdaptedExerciseBusinessTestCase(TestCase):
    def test_single_sentence(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="The wording of this exercise is a single sentence.",
        )
        adapted = SelectWordsAdaptedExercise(exercise=exercise, colors=2)

        self.assertEqual(
            adapted.make_adapted(),
            r.AdaptedExercise(
                number="number",
                textbook_page=None,
                instructions="instructions",
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableWord(type="selectableWord", text="The"),
                            r.Whitespace(type="whitespace"),
                            r.SelectableWord(type="selectableWord", text="wording"),
                            r.Whitespace(type="whitespace"),
                            r.SelectableWord(type="selectableWord", text="of"),
                            r.Whitespace(type="whitespace"),
                            r.SelectableWord(type="selectableWord", text="this"),
                            r.Whitespace(type="whitespace"),
                            r.SelectableWord(type="selectableWord", text="exercise"),
                            r.Whitespace(type="whitespace"),
                            r.SelectableWord(type="selectableWord", text="is"),
                            r.Whitespace(type="whitespace"),
                            r.SelectableWord(type="selectableWord", text="a"),
                            r.Whitespace(type="whitespace"),
                            r.SelectableWord(type="selectableWord", text="single"),
                            r.Whitespace(type="whitespace"),
                            r.SelectableWord(type="selectableWord", text="sentence"),
                            r.Punctuation(type="punctuation", text="."),
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
                            r.PlainWord(type="plainWord", text="The"),
                            r.Whitespace(type="whitespace"),
                            r.PlainWord(type="plainWord", text="wording"),
                            r.Whitespace(type="whitespace"),
                            r.PlainWord(type="plainWord", text="of"),
                            r.Whitespace(type="whitespace"),
                            r.PlainWord(type="plainWord", text="this"),
                            r.Whitespace(type="whitespace"),
                            r.FreeTextInput(type="freeTextInput"),
                            r.Whitespace(type="whitespace"),
                            r.PlainWord(type="plainWord", text="is"),
                            r.Whitespace(type="whitespace"),
                            r.PlainWord(type="plainWord", text="a"),
                            r.Whitespace(type="whitespace"),
                            r.FreeTextInput(type="freeTextInput"),
                            r.Whitespace(type="whitespace"),
                            r.PlainWord(type="plainWord", text="sentence"),
                            r.Punctuation(type="punctuation", text="."),
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
                            r.PlainWord(type="plainWord", text="a"),
                            r.Whitespace(type="whitespace"),
                            r.FreeTextInput(type="freeTextInput"),
                        ]),
                    ]),
                ]),
            ),
        )


class AdaptedExerciseApiTestCase(TestMixin, TestCase):
    resources = [AdaptedExerciseResource]

    def test_select_words(self):
        payload = {
            "data": {
                "type": "adaptedExercise",
                "attributes": {
                    "number": "A.1",
                    "textbookPage": 1,
                    "instructions": "This is the instructions.",
                    "wording": "This is the wording.",
                    "type": "selectWords",
                    "options": {
                        "colors": 3,
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
                {"type": "selectableWord", "text": "This"},
                {"type": "whitespace"},
                {"type": "selectableWord", "text": "is"},
                {"type": "whitespace"},
                {"type": "selectableWord", "text": "the"},
                {"type": "whitespace"},
                {"type": "selectableWord", "text": "wording"},
                {"type": "punctuation", "text": "."},
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
                {"type": "plainWord", "text": "Fill"},
                {"type": "whitespace"},
                {"type": "freeTextInput"},
            ]}]}]},
        })
