import dataclasses
import uuid

from starlette import status

from . import api_models
from . import deltas
from . import renderable
from . import settings
from .exercises import Exercise
from .testing import LoggedInApiTestCase
from .users import MandatoryAuthBearerDependable


@dataclasses.dataclass
class ParsedExerciseItem:
    id: str
    adapted: renderable.Exercise


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
        text_reference,
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
            text_reference=text_reference,
            wording_paragraphs_per_pagelet=wording_paragraphs_per_pagelet,
            adaptation=adaptation,
        )
        return ParsedExerciseItem(
            id=uuid.uuid4().hex,
            adapted=exercise.make_adapted(),
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
                    "instructions": [{"insert": "This is the {boxed-text|instructions}.\n", "attributes": {}}],
                    "wording": [{"insert": "This is the wording.\n", "attributes": {}}],
                    "example": [{"insert": "\n", "attributes": {}}],
                    "clue": [{"insert": "\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {"kind": "generic", "effects": []},
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "C",
            "textbook_page": None,  # @todo Rename to textbookPage
            "pagelets": [{
                "instructions": {"paragraphs": [
                    {"tokens": [
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
                    ]},
                ]},
                "wording": {"paragraphs": [{"tokens": [
                    {"type": "plainText", "text": "This"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "is"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "the"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "wording"},
                    {"type": "plainText", "text": "."},
                ]}]},
            }],
        })

    def test_select_things(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": [{"insert": "This is the instructions.\n", "attributes": {}}],
                    "wording": [{"insert": "This is the wording.\n", "attributes": {}}],
                    "example": [{"insert": "\n", "attributes": {}}],
                    "clue": [{"insert": "\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {
                        "kind": "generic",
                        "effects": [
                            {
                                "kind": "itemized",
                                "items": {
                                    "kind": "tokens",
                                    "words": True,
                                    "punctuation": False,
                                },
                                "effects": {
                                    "selectable": {
                                        "colors": ["red", "green", "blue"],
                                    },
                                    "boxed": False,
                                },
                            },
                        ],
                    },
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": None,  # @todo Rename to textbookPage
            "pagelets": [{
                "instructions": {"paragraphs": [
                    {"tokens": [
                        {"type": "plainText", "text": "This"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "is"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "the"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "instructions"},
                        {"type": "plainText", "text": "."},
                    ]},
                ]},
                "wording": {"paragraphs": [{"tokens": [
                    {"type": "selectableText", "text": "This", "colors": ["red", "green", "blue"], "boxed": False},
                    {"type": "whitespace"},
                    {"type": "selectableText", "text": "is", "colors": ["red", "green", "blue"], "boxed": False},
                    {"type": "whitespace"},
                    {"type": "selectableText", "text": "the", "colors": ["red", "green", "blue"], "boxed": False},
                    {"type": "whitespace"},
                    {"type": "selectableText", "text": "wording", "colors": ["red", "green", "blue"], "boxed": False},
                    {"type": "plainText", "text": "."},
                ]}]},
            }],
        })

    def test_select_things_with_example_and_clue(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": [{"insert": "This is the instructions.\n", "attributes": {}}],
                    "wording": [{"insert": "This is the wording.\n", "attributes": {}}],
                    "example": [{"insert": "This is the example.\n", "attributes": {}}],
                    "clue": [{"insert": "This is the clue.\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {
                        "kind": "generic",
                        "effects": [
                            {
                                "kind": "itemized",
                                "items": {
                                    "kind": "tokens",
                                    "words": True,
                                    "punctuation": False,
                                },
                                "effects": {
                                    "selectable": {
                                        "colors": ["red", "green", "blue"],
                                    },
                                    "boxed": False,
                                },
                            },
                        ],
                    },
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": None,  # @todo Rename to textbookPage
            "pagelets": [{
                "instructions": {"paragraphs": [
                    {"tokens": [
                        {"type": "plainText", "text": "This"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "is"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "the"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "instructions"},
                        {"type": "plainText", "text": "."},
                    ]},
                    {"tokens": [
                        {"type": "plainText", "text": "This"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "is"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "the"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "example"},
                        {"type": "plainText", "text": "."},
                    ]},
                    {"tokens": [
                        {"type": "plainText", "text": "This"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "is"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "the"},
                        {"type": "whitespace"},
                        {"type": "plainText", "text": "clue"},
                        {"type": "plainText", "text": "."},
                    ]},
                ]},
                "wording": {"paragraphs": [{"tokens": [
                    {"type": "selectableText", "text": "This", "colors": ["red", "green", "blue"], "boxed": False},
                    {"type": "whitespace"},
                    {"type": "selectableText", "text": "is", "colors": ["red", "green", "blue"], "boxed": False},
                    {"type": "whitespace"},
                    {"type": "selectableText", "text": "the", "colors": ["red", "green", "blue"], "boxed": False},
                    {"type": "whitespace"},
                    {"type": "selectableText", "text": "wording", "colors": ["red", "green", "blue"], "boxed": False},
                    {"type": "plainText", "text": "."},
                ]}]},
            }],
        })

    def test_fill_with_free_text(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": [{"insert": "This is the instructions.\n", "attributes": {}}],
                    "wording": [{"insert": "Fill @\n", "attributes": {}}],
                    "example": [{"insert": "\n", "attributes": {}}],
                    "clue": [{"insert": "\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {
                        "kind": "fill-with-free-text",
                        "effects": [
                            {
                                "kind": "fill-with-free-text",
                                "placeholder": "@",
                            },
                        ],
                    },
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": None,  # @todo Rename to textbookPage
            "pagelets": [{
                "instructions": {"paragraphs": [{"tokens": [
                    {"type": "plainText", "text": "This"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "is"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "the"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "instructions"},
                    {"type": "plainText", "text": "."},
                ]}]},
                "wording": {"paragraphs": [{"tokens": [
                    {"type": "plainText", "text": "Fill"},
                    {"type": "whitespace"},
                    {"type": "freeTextInput"},
                ]}]},
            }],
        })

    def test_multiple_choices_in_instructions(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": [
                        {
                            "insert": "a or b",
                            "attributes": {
                                "choices2": {
                                    "start": "",
                                    "separator1": "or",
                                    "separator2": "",
                                    "stop": "",
                                    "placeholder": "@",
                                },
                            },
                        },
                        {"insert": "\n", "attributes": {}},
                    ],
                    "wording": [{"insert": "A @\n\nB @\n", "attributes": {}}],
                    "example": [{"insert": "\n", "attributes": {}}],
                    "clue": [{"insert": "\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {"kind": "multiple-choices", "effects": []},
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": None,  # @todo Rename to textbookPage
            "pagelets": [{
                "instructions": {"paragraphs": [{"tokens": [
                    {"type": "boxedText", "text": "a"},
                    {"type": "whitespace"},
                    {"type": "plainText", "text": "or"},
                    {"type": "whitespace"},
                    {"type": "boxedText", "text": "b"},
                ]}]},
                "wording": {"paragraphs": [
                    {"tokens": [
                        {"type": "plainText", "text": "A"},
                        {"type": "whitespace"},
                        {"type": "multipleChoicesInput", "choices": ["a", "b"]},
                    ]},
                    {"tokens": [
                        {"type": "plainText", "text": "B"},
                        {"type": "whitespace"},
                        {"type": "multipleChoicesInput", "choices": ["a", "b"]},
                    ]},
                ]},
            }],
        })

    def test_multiple_choices_in_wording(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": [{"insert": "Instructions.\n", "attributes": {}}],
                    "wording": [
                        {"insert": "A ", "attributes": {}},
                        {
                            "insert": "alpha/beta",
                            "attributes": {
                                "choices2": {
                                    "start": "",
                                    "separator1": "/",
                                    "separator2": "",
                                    "stop": "",
                                    "placeholder": "",
                                },
                            },
                        },
                        {"insert": ".\n", "attributes": {}},
                    ],
                    "example": [{"insert": "\n", "attributes": {}}],
                    "clue": [{"insert": "\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "wordingParagraphsPerPagelet": 3,
                    "adaptation": {"kind": "multiple-choices", "effects": []},
                },
            },
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "A.1",
            "textbook_page": None,  # @todo Rename to textbookPage
            "pagelets": [{
                "instructions": {"paragraphs": [{"tokens": [
                    {"type": "plainText", "text": "Instructions"},
                    {"type": "plainText", "text": "."},
                ]}]},
                "wording": {"paragraphs": [{"tokens": [
                    {"type": "plainText", "text": "A"},
                    {"type": "whitespace"},
                    {"type": "multipleChoicesInput", "choices": ["alpha", "beta"]},
                    {"type": "plainText", "text": "."},
                ]}]},
            }],
        })
