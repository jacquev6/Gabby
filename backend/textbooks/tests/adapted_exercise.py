from django.test import TestCase
from starlette import status

from ..models import Exercise, SelectThingsAdaptation, FillWithFreeTextAdaptation, MultipleChoicesAdaptation
from ..resources import AdaptedExerciseResource
from .. import renderable as r
from fastjsonapi.testing import TestMixin


class AdaptationTestCase(TestCase):
    def do_test(self, adaptation, expected):
        self.assertEqual(adaptation.make_adapted(), expected)


class SelectThingsAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        exercise = Exercise(
            number="number",
            textbook_page=None,
            instructions="instructions",
            wording="The wording of this exercise is a single sentence.",
        )
        adaptation = SelectThingsAdaptation(exercise=exercise, colors=2, words=True, punctuation=False)

        self.do_test(
            adaptation,
            r.AdaptedExercise(
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

        self.do_test(
            adaptation,
            r.AdaptedExercise(
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
                            r.PlainText(text="{sel4|jkl}"),
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

        self.do_test(
            adaptation,
            r.AdaptedExercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{sel1|abc}"),
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

        self.do_test(
            adaptation,
            r.AdaptedExercise(
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

        self.do_test(
            adaptation,
            r.AdaptedExercise(
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

        self.do_test(
            adaptation,
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{tag|abc}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{tag|def}"),
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

        self.do_test(
            adaptation,
            r.AdaptedExercise(
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
            ),
        )


class FillWithFreeTextAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="instructions",
            wording="The wording of this ... is a ... sentence.",
        )
        adaptation = FillWithFreeTextAdaptation(exercise=exercise, placeholder="...")

        self.do_test(
            adaptation,
            r.AdaptedExercise(
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
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="wording"),
                            r.Whitespace(),
                            r.PlainText(text="of"),
                            r.Whitespace(),
                            r.PlainText(text="this"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="sentence"),
                            r.PlainText(text="."),
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
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.FreeTextInput(),
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

        self.do_test(
            adaptation,
            r.AdaptedExercise(
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
                            r.PlainText(text="wording"),
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

        self.do_test(
            adaptation,
            r.AdaptedExercise(
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
                            r.PlainText(text="foo"),
                            r.Whitespace(),
                            r.PlainText(text="toto"),
                            r.Whitespace(),
                            r.PlainText(text=":"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="bar"),
                            r.Whitespace(),
                            r.PlainText(text=":"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="baz"),
                            r.Whitespace(),
                            r.PlainText(text=":"),
                            r.Whitespace(),
                            r.FreeTextInput(),
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

        self.do_test(
            adaptation,
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{tag|abc}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{tag|def}"),
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

        self.do_test(
            adaptation,
            r.AdaptedExercise(
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
                            r.PlainText(text="def"),
                        ]),
                    ]),
                ]),
            ),
        )


class MultipleChoicesAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        exercise = Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose {choice|a} or {choice|b}.",
            wording="A ... B ...",
        )
        adaptation = MultipleChoicesAdaptation(exercise=exercise, placeholder="...")

        self.do_test(
            adaptation,
            r.AdaptedExercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.PlainText(text="b"),
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

    def test_multiple_choices(self):
        payload = {
            "data": {
                "type": "adaptedExercise",
                "attributes": {
                    "number": "A.1",
                    "textbookPage": 1,
                    "instructions": "{choice|a} or {choice|b}",
                    "wording": "A @\n\nB @",
                    "type": "multipleChoicesAdaptation",
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
                {"type": "plainText", "text": "a"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "or"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "b"},
            ]}]}]},
            "wording": {"paragraphs": [
                {"sentences": [{"tokens": [
                    {"type": "plainText", "text": "A"},
                    {"type": "whitespace"},
                    {"type": "multipleChoicesInput", "choices": ["a", "b"]},
                ]}]},
                {"sentences": [{"tokens": [
                    {"type": "plainText", "text": "B"},
                    {"type": "whitespace"},
                    {"type": "multipleChoicesInput", "choices": ["a", "b"]},
                ]}]},
            ]},
        })
