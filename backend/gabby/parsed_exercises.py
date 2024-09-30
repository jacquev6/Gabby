import dataclasses
import uuid

from starlette import status

from . import api_models
from . import exercise_delta
from . import renderable
from . import settings
from .exercises import Exercise
from .testing import LoggedInApiTestCase
from .users import MandatoryAuthBearerDependable


@dataclasses.dataclass
class ParsedExerciseItem:
    id: str
    adapted: renderable.Exercise
    delta: exercise_delta.Exercise


class ParsedExercisesResource:
    singular_name = "parsed_exercise"
    plural_name = "parsed_exercises"

    Model = api_models.ParsedExercise

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    def create_item(
        self,
        number,
        instructions,
        wording,
        example,
        clue,
        wording_paragraphs_per_pagelet,
        adaptation,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        exercise = Exercise(
            number=number,
            instructions=instructions,
            wording=wording,
            example=example,
            clue=clue,
            wording_paragraphs_per_pagelet=wording_paragraphs_per_pagelet,
            adaptation=adaptation,
        )
        return ParsedExerciseItem(
            id=uuid.uuid4().hex,
            adapted=exercise.make_adapted(),
            delta=exercise.make_delta(),
        )

    def get_item(
        self,
        id,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        return None


class ParsedExerciseApiTestCase(LoggedInApiTestCase):
    resources = [ParsedExercisesResource()]
    polymorphism = {}

    def test_null(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "C",
                    "instructions": "This is the {boxed-text|instructions}.",
                    "wording": "This is the wording.",
                    "example": "",
                    "clue": "",
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {"kind": "null"},
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "C",
            "textbook_page": None,  # @todo Rename to textbookPage
            "instructions": {"paragraphs": [
                {"sentences": [{"tokens": [
                    {"type": "plainText", "text": "This"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "is"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "the"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "{"},
                    {"type": "plainText", "text": "boxed"},
                    {"type": "plainText", "text": "-"},
                    {"type": "plainText", "text": "text"},
                    {"type": "plainText", "text": "|"},
                    {"type": "plainText", "text": "instructions"},
                    {"type": "plainText", "text": "}"},
                    {"type": "plainText", "text": "."},
                ]}]},
            ]},
            "wording": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "plainText", "text": "This"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "is"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "the"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "wording"},
                {"type": "plainText", "text": "."},
            ]}]}]},
            "example": {"paragraphs": []},
            "clue": {"paragraphs": []},
            "wording_paragraphs_per_pagelet": 3,
        })

    def test_select_things(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": "This is the instructions.",
                    "wording": "This is the wording.",
                    "example": "",
                    "clue": "",
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {
                        "kind": "select-things",
                        "colors": ["red", "green", "blue"],
                        "words": True,
                        "punctuation": False,
                    },
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": None,  # @todo Rename to textbookPage
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
            ]},
            "wording": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "selectableText", "text": "This", "colors": ["red", "green", "blue"], "boxed": False},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "is", "colors": ["red", "green", "blue"], "boxed": False},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "the", "colors": ["red", "green", "blue"], "boxed": False},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "wording", "colors": ["red", "green", "blue"], "boxed": False},
                {"type": "plainText", "text": "."},
            ]}]}]},
            "example": {"paragraphs": []},
            "clue": {"paragraphs": []},
            "wording_paragraphs_per_pagelet": 3,
        })

    def test_select_things_with_example_and_clue(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": "This is the instructions.",
                    "wording": "This is the wording.",
                    "example": "This is the example.",
                    "clue": "This is the clue.",
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {
                        "kind": "select-things",
                        "colors": ["red", "green", "blue"],
                        "words": True,
                        "punctuation": False,
                    },
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": None,  # @todo Rename to textbookPage
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
            ]},
            "wording": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "selectableText", "text": "This", "colors": ["red", "green", "blue"], "boxed": False},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "is", "colors": ["red", "green", "blue"], "boxed": False},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "the", "colors": ["red", "green", "blue"], "boxed": False},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "wording", "colors": ["red", "green", "blue"], "boxed": False},
                {"type": "plainText", "text": "."},
            ]}]}]},
            "example": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "plainText", "text": "This"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "is"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "the"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "example"},
                {"type": "plainText", "text": "."},
            ]}]}]},
            "clue": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "plainText", "text": "This"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "is"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "the"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "clue"},
                {"type": "plainText", "text": "."},
            ]}]}]},
            "wording_paragraphs_per_pagelet": 3,
        })

    def test_fill_with_free_text(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": "This is the instructions.",
                    "wording": "Fill @",
                    "example": "",
                    "clue": "",
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {
                        "kind": "fill-with-free-text",
                        "placeholder": "@",
                    },
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": None,  # @todo Rename to textbookPage
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
            "example": {"paragraphs": []},
            "clue": {"paragraphs": []},
            "wording_paragraphs_per_pagelet": 3,
        })

    def test_multiple_choices_in_instructions(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": "{choice|a} or {choice|b}",
                    "wording": "A @\n\nB @",
                    "example": "",
                    "clue": "",
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {
                        "kind": "multiple-choices-in-instructions",
                        "placeholder": "@",
                    },
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": None,  # @todo Rename to textbookPage
            "instructions": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "boxedText", "text": "a"},
                {"type": "whitespace"},
                {"type": "plainText", "text": "or"},
                {"type": "whitespace"},
                {"type": "boxedText", "text": "b"},
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
            "example": {"paragraphs": []},
            "clue": {"paragraphs": []},
            "wording_paragraphs_per_pagelet": 3,
        })

    def test_multiple_choices_in_wording(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": "Instructions.",
                    "wording": "A {choices|alpha|beta}.",
                    "example": "",
                    "clue": "",
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {
                        "kind": "multiple-choices-in-wording",
                    },
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": None,  # @todo Rename to textbookPage
            "instructions": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "plainText", "text": "Instructions"},
                {"type": "plainText", "text": "."},
            ]}]}]},
            "wording": {"paragraphs": [{"sentences": [{"tokens": [
                {"type": "plainText", "text": "A"},
                {"type": "whitespace"},
                {"type": "multipleChoicesInput", "choices": ["alpha", "beta"]},
                {"type": "plainText", "text": "."},
            ]}]}]},
            "example": {"paragraphs": []},
            "clue": {"paragraphs": []},
            "wording_paragraphs_per_pagelet": 3,
        })
