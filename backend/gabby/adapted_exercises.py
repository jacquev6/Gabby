import dataclasses
import uuid

from fastapi import HTTPException
from starlette import status

from . import api_models
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

    def make_adapted_instructions(self):
        return parsing.parse_plain_instructions_section(self.exercise.instructions)

    def make_adapted_wording(self):
        return parsing.parse_plain_wording_section(self.exercise.wording)

    def make_adapted_example(self):
        return parsing.parse_plain_instructions_section(self.exercise.example)

    def make_adapted_clue(self):
        return parsing.parse_plain_instructions_section(self.exercise.clue)


@dataclasses.dataclass
class AdaptedExerciseItem:
    id: str
    adapted: renderable.AdaptedExercise


class AdaptedExercisesResource:
    singular_name = "adapted_exercise"
    plural_name = "adapted_exercises"

    Model = api_models.AdaptedExercise

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    def create_item(
        self,
        number,
        textbook_page,
        instructions,
        wording,
        example,
        clue,
        type,
        adaptation_options,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        exercise = Exercise(
            number=number,
            textbook_page=textbook_page,
            instructions=instructions,
            wording=wording,
            example=example,
            clue=clue,
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
        return AdaptedExerciseItem(
            id=uuid.uuid4().hex,
            adapted=adaptation.make_adapted(),
        )

    def get_item(
        self,
        id,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        return None


class AdaptedExerciseApiTestCase(LoggedInApiTestCase):
    resources = [AdaptedExercisesResource()]
    polymorphism = {}

    def test_null(self):
        payload = {
            "data": {
                "type": "adaptedExercise",
                "attributes": {
                    "number": "C",
                    "textbookPage": 1,
                    "instructions": "This is the {boxed-text|instructions}.",
                    "wording": "This is the wording.",
                    "example": "",
                    "clue": "",
                    "type": "-",
                    "adaptationOptions": {},
                },
            },
        }
        response = self.post("http://server/adaptedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()["data"]["attributes"]["adapted"], {
            "number": "C",
            "textbook_page": 1,
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
        })

    def test_select_things(self):
        payload = {
            "data": {
                "type": "adaptedExercise",
                "attributes": {
                    "number": "A.1",
                    "textbookPage": 1,
                    "instructions": "This is the instructions.",
                    "wording": "This is the wording.",
                    "example": "",
                    "clue": "",
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
            "example": {"paragraphs": []},
            "clue": {"paragraphs": []},
        })

    def test_select_things_with_example_and_clue(self):
        payload = {
            "data": {
                "type": "adaptedExercise",
                "attributes": {
                    "number": "A.1",
                    "textbookPage": 1,
                    "instructions": "This is the instructions.",
                    "wording": "This is the wording.",
                    "example": "This is the example.",
                    "clue": "This is the clue.",
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
                    "example": "",
                    "clue": "",
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
            "example": {"paragraphs": []},
            "clue": {"paragraphs": []},
        })

    def test_multiple_choices_in_instructions(self):
        payload = {
            "data": {
                "type": "adaptedExercise",
                "attributes": {
                    "number": "A.1",
                    "textbookPage": 1,
                    "instructions": "{choice|a} or {choice|b}",
                    "wording": "A @\n\nB @",
                    "example": "",
                    "clue": "",
                    "type": "multipleChoicesInInstructionsAdaptation",
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
        })
