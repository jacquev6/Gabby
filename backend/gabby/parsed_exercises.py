import dataclasses
import uuid

from fastapi import HTTPException
from starlette import status

from . import api_models
from . import exercise_delta
from . import parsing
from . import renderable
from . import settings
from .adaptations.fill_with_free_text import FillWithFreeTextAdaptation
from .adaptations.multiple_choices_in_instructions import MultipleChoicesInInstructionsAdaptation
from .adaptations.multiple_choices_in_wording import MultipleChoicesInWordingAdaptation
from .adaptations.select_things import SelectThingsAdaptation
from .exercises import Exercise, Adaptation
from .testing import LoggedInApiTestCase
from .users import MandatoryAuthBearerDependable


class NullAdaptation(Adaptation):
    __abstract__ = True  # Abstract with regards to SQL tables, but instantiable in Python

    def make_instructions_delta(self):
        return parsing.make_plain_instructions_section_delta(self.exercise.instructions)

    def make_adapted_instructions(self):
        return parsing.adapt_plain_instructions_section(self.exercise.instructions)

    def make_wording_delta(self):
        return parsing.make_plain_wording_section_delta(self.exercise.wording)

    def make_adapted_wording(self):
        return parsing.adapt_plain_wording_section(self.exercise.wording)

    def make_example_delta(self):
        return parsing.make_plain_instructions_section_delta(self.exercise.example)

    def make_adapted_example(self):
        return parsing.adapt_plain_instructions_section(self.exercise.example)

    def make_clue_delta(self):
        return parsing.make_plain_instructions_section_delta(self.exercise.clue)

    def make_adapted_clue(self):
        return parsing.adapt_plain_instructions_section(self.exercise.clue)


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
        type,
        adaptation_options,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        exercise = Exercise(
            number=number,
            instructions=instructions,
            wording=wording,
            example=example,
            clue=clue,
            wording_paragraphs_per_pagelet=wording_paragraphs_per_pagelet,
        )
        if type == "-":
            adaptation = NullAdaptation(
                exercise=exercise,
            )
        elif type == "selectThingsAdaptation":
            adaptation = SelectThingsAdaptation(
                exercise=exercise,
                **adaptation_options.model_dump(),
            )
        elif type == "fillWithFreeTextAdaptation":
            adaptation = FillWithFreeTextAdaptation(
                exercise=exercise,
                **adaptation_options.model_dump(),
            )
        elif type == "multipleChoicesInInstructionsAdaptation":
            adaptation = MultipleChoicesInInstructionsAdaptation(
                exercise=exercise,
                **adaptation_options.model_dump(),
            )
        elif type == "multipleChoicesInWordingAdaptation":
            adaptation = MultipleChoicesInWordingAdaptation(
                exercise=exercise,
                **adaptation_options.model_dump(),
            )
        else:
            raise HTTPException(status_code=400, detail="Unknown type")
        return ParsedExerciseItem(
            id=uuid.uuid4().hex,
            adapted=adaptation.make_adapted(),
            delta=adaptation.make_delta(),
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
                    "type": "-",
                    "adaptationOptions": {},
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
                    "type": "selectThingsAdaptation",
                    "adaptationOptions": {
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
                {"type": "selectableText", "text": "This", "colors": ["red", "green", "blue"]},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "is", "colors": ["red", "green", "blue"]},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "the", "colors": ["red", "green", "blue"]},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "wording", "colors": ["red", "green", "blue"]},
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
                    "type": "selectThingsAdaptation",
                    "adaptationOptions": {
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
                {"type": "selectableText", "text": "This", "colors": ["red", "green", "blue"]},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "is", "colors": ["red", "green", "blue"]},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "the", "colors": ["red", "green", "blue"]},
                {"type": "whitespace"},
                {"type": "selectableText", "text": "wording", "colors": ["red", "green", "blue"]},
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
                    "type": "fillWithFreeTextAdaptation",
                    "adaptationOptions": {
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
                    "type": "multipleChoicesInInstructionsAdaptation",
                    "adaptationOptions": {
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
                    "type": "multipleChoicesInWordingAdaptation",
                    "adaptationOptions": {},
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
