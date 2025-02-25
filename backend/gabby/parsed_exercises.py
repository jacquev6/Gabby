import dataclasses
import uuid

from starlette import status

from . import api_models
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

    def create_item(self, number, instructions, wording, example, clue, text_reference, adaptation, authenticated_user: MandatoryAuthBearerDependable):
        exercise = Exercise(
            number=number, instructions=instructions, wording=wording, example=example, clue=clue, text_reference=text_reference, adaptation=adaptation
        )
        return ParsedExerciseItem(id=uuid.uuid4().hex, adapted=exercise.make_adapted())

    def get_item(self, id, authenticated_user: MandatoryAuthBearerDependable):
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
                    "adaptation": {
                        "kind": "generic",
                        "wording_paragraphs_per_pagelet": 3,
                        "single_item_per_paragraph": False,
                        "placeholder_for_fill_with_free_text": None,
                        "items": None,
                        "items_are_selectable": None,
                        "items_are_boxed": False,
                        "items_have_mcq_beside": False,
                        "items_have_mcq_below": False,
                        "items_have_predefined_mcq": {"grammatical_gender": False, "grammatical_number": False},
                        "items_are_repeated_with_mcq": False,
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                },
            }
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(
            response.json()["data"]["attributes"]["adapted"],
            {
                "number": "C",
                "textbook_page": None,  # @todo Rename to textbookPage
                "pagelets": [
                    {
                        "instructions": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {"kind": "text", "text": "This"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "is"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "the"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "{"},
                                        {"kind": "text", "text": "boxed"},
                                        {"kind": "text", "text": "-"},
                                        {"kind": "text", "text": "text"},
                                        {"kind": "text", "text": "|"},
                                        {"kind": "text", "text": "instructions"},
                                        {"kind": "text", "text": "}"},
                                        {"kind": "text", "text": "."},
                                    ]
                                }
                            ]
                        },
                        "wording": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {"kind": "text", "text": "This"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "is"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "the"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "wording"},
                                        {"kind": "text", "text": "."},
                                    ]
                                }
                            ]
                        },
                    }
                ],
            },
        )

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
                    "adaptation": {
                        "kind": "generic",
                        "wording_paragraphs_per_pagelet": 3,
                        "single_item_per_paragraph": False,
                        "placeholder_for_fill_with_free_text": None,
                        "items": {"kind": "tokens", "words": True, "punctuation": False},
                        "items_are_selectable": {"colors": ["red", "green", "blue"]},
                        "items_are_boxed": False,
                        "items_have_mcq_beside": False,
                        "items_have_mcq_below": False,
                        "items_have_predefined_mcq": {"grammatical_gender": False, "grammatical_number": False},
                        "items_are_repeated_with_mcq": False,
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                },
            }
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(
            response.json()["data"]["attributes"]["adapted"],
            {
                "number": "A.1",
                "textbook_page": None,  # @todo Rename to textbookPage
                "pagelets": [
                    {
                        "instructions": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {"kind": "text", "text": "This"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "is"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "the"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "instructions"},
                                        {"kind": "text", "text": "."},
                                    ]
                                }
                            ]
                        },
                        "wording": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {
                                            "kind": "selectableInput",
                                            "contents": [{"kind": "text", "text": "This"}],
                                            "colors": ["red", "green", "blue"],
                                            "boxed": False,
                                        },
                                        {"kind": "whitespace"},
                                        {
                                            "kind": "selectableInput",
                                            "contents": [{"kind": "text", "text": "is"}],
                                            "colors": ["red", "green", "blue"],
                                            "boxed": False,
                                        },
                                        {"kind": "whitespace"},
                                        {
                                            "kind": "selectableInput",
                                            "contents": [{"kind": "text", "text": "the"}],
                                            "colors": ["red", "green", "blue"],
                                            "boxed": False,
                                        },
                                        {"kind": "whitespace"},
                                        {
                                            "kind": "selectableInput",
                                            "contents": [{"kind": "text", "text": "wording"}],
                                            "colors": ["red", "green", "blue"],
                                            "boxed": False,
                                        },
                                        {"kind": "text", "text": "."},
                                    ]
                                }
                            ]
                        },
                    }
                ],
            },
        )

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
                    "adaptation": {
                        "kind": "generic",
                        "wording_paragraphs_per_pagelet": 3,
                        "single_item_per_paragraph": False,
                        "placeholder_for_fill_with_free_text": None,
                        "items": {"kind": "tokens", "words": True, "punctuation": False},
                        "items_are_selectable": {"colors": ["red", "green", "blue"]},
                        "items_are_boxed": False,
                        "items_have_mcq_beside": False,
                        "items_have_mcq_below": False,
                        "items_have_predefined_mcq": {"grammatical_gender": False, "grammatical_number": False},
                        "items_are_repeated_with_mcq": False,
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                },
            }
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(
            response.json()["data"]["attributes"]["adapted"],
            {
                "number": "A.1",
                "textbook_page": None,  # @todo Rename to textbookPage
                "pagelets": [
                    {
                        "instructions": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {"kind": "text", "text": "This"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "is"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "the"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "instructions"},
                                        {"kind": "text", "text": "."},
                                    ]
                                },
                                {
                                    "contents": [
                                        {"kind": "text", "text": "This"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "is"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "the"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "example"},
                                        {"kind": "text", "text": "."},
                                    ]
                                },
                                {
                                    "contents": [
                                        {"kind": "text", "text": "This"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "is"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "the"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "clue"},
                                        {"kind": "text", "text": "."},
                                    ]
                                },
                            ]
                        },
                        "wording": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {
                                            "kind": "selectableInput",
                                            "contents": [{"kind": "text", "text": "This"}],
                                            "colors": ["red", "green", "blue"],
                                            "boxed": False,
                                        },
                                        {"kind": "whitespace"},
                                        {
                                            "kind": "selectableInput",
                                            "contents": [{"kind": "text", "text": "is"}],
                                            "colors": ["red", "green", "blue"],
                                            "boxed": False,
                                        },
                                        {"kind": "whitespace"},
                                        {
                                            "kind": "selectableInput",
                                            "contents": [{"kind": "text", "text": "the"}],
                                            "colors": ["red", "green", "blue"],
                                            "boxed": False,
                                        },
                                        {"kind": "whitespace"},
                                        {
                                            "kind": "selectableInput",
                                            "contents": [{"kind": "text", "text": "wording"}],
                                            "colors": ["red", "green", "blue"],
                                            "boxed": False,
                                        },
                                        {"kind": "text", "text": "."},
                                    ]
                                }
                            ]
                        },
                    }
                ],
            },
        )

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
                    "adaptation": {
                        "kind": "fill-with-free-text",
                        "wording_paragraphs_per_pagelet": 3,
                        "single_item_per_paragraph": False,
                        "placeholder_for_fill_with_free_text": "@",
                        "items": None,
                        "items_are_selectable": None,
                        "items_are_boxed": False,
                        "items_have_mcq_beside": False,
                        "items_have_mcq_below": False,
                        "items_have_predefined_mcq": {"grammatical_gender": False, "grammatical_number": False},
                        "items_are_repeated_with_mcq": False,
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                },
            }
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(
            response.json()["data"]["attributes"]["adapted"],
            {
                "number": "A.1",
                "textbook_page": None,  # @todo Rename to textbookPage
                "pagelets": [
                    {
                        "instructions": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {"kind": "text", "text": "This"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "is"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "the"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "instructions"},
                                        {"kind": "text", "text": "."},
                                    ]
                                }
                            ]
                        },
                        "wording": {"paragraphs": [{"contents": [{"kind": "text", "text": "Fill"}, {"kind": "whitespace"}, {"kind": "freeTextInput"}]}]},
                    }
                ],
            },
        )

    def test_multiple_choices_in_instructions(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": [
                        {"insert": "a or b", "attributes": {"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "@"}}},
                        {"insert": "\n", "attributes": {}},
                    ],
                    "wording": [{"insert": "A @\n\nB @\n", "attributes": {}}],
                    "example": [{"insert": "\n", "attributes": {}}],
                    "clue": [{"insert": "\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "adaptation": {
                        "kind": "multiple-choices",
                        "wording_paragraphs_per_pagelet": 3,
                        "single_item_per_paragraph": False,
                        "placeholder_for_fill_with_free_text": None,
                        "items": None,
                        "items_are_selectable": None,
                        "items_are_boxed": False,
                        "items_have_mcq_beside": False,
                        "items_have_mcq_below": False,
                        "items_have_predefined_mcq": {"grammatical_gender": False, "grammatical_number": False},
                        "items_are_repeated_with_mcq": False,
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                },
            }
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(
            response.json()["data"]["attributes"]["adapted"],
            {
                "number": "A.1",
                "textbook_page": None,  # @todo Rename to textbookPage
                "pagelets": [
                    {
                        "instructions": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {"kind": "passiveSequence", "contents": [{"kind": "text", "text": "a"}], "boxed": True},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "ou"},
                                        {"kind": "whitespace"},
                                        {"kind": "passiveSequence", "contents": [{"kind": "text", "text": "b"}], "boxed": True},
                                    ]
                                }
                            ]
                        },
                        "wording": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {"kind": "text", "text": "A"},
                                        {"kind": "whitespace"},
                                        {
                                            "kind": "multipleChoicesInput",
                                            "show_arrow_before": False,
                                            "choices": [[{"kind": "text", "text": "a"}], [{"kind": "text", "text": "b"}]],
                                            "show_choices_by_default": False,
                                        },
                                    ]
                                },
                                {
                                    "contents": [
                                        {"kind": "text", "text": "B"},
                                        {"kind": "whitespace"},
                                        {
                                            "kind": "multipleChoicesInput",
                                            "show_arrow_before": False,
                                            "choices": [[{"kind": "text", "text": "a"}], [{"kind": "text", "text": "b"}]],
                                            "show_choices_by_default": False,
                                        },
                                    ]
                                },
                            ]
                        },
                    }
                ],
            },
        )

    def test_multiple_choices_in_wording(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "number": "A.1",
                    "instructions": [{"insert": "Instructions.\n", "attributes": {}}],
                    "wording": [
                        {"insert": "A ", "attributes": {}},
                        {"insert": "alpha/beta", "attributes": {"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}},
                        {"insert": ".\n", "attributes": {}},
                    ],
                    "example": [{"insert": "\n", "attributes": {}}],
                    "clue": [{"insert": "\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "adaptation": {
                        "kind": "multiple-choices",
                        "wording_paragraphs_per_pagelet": 3,
                        "single_item_per_paragraph": False,
                        "placeholder_for_fill_with_free_text": None,
                        "items": None,
                        "items_are_selectable": None,
                        "items_are_boxed": False,
                        "items_have_mcq_beside": False,
                        "items_have_mcq_below": False,
                        "items_have_predefined_mcq": {"grammatical_gender": False, "grammatical_number": False},
                        "items_are_repeated_with_mcq": False,
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                },
            }
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(
            response.json()["data"]["attributes"]["adapted"],
            {
                "number": "A.1",
                "textbook_page": None,  # @todo Rename to textbookPage
                "pagelets": [
                    {
                        "instructions": {"paragraphs": [{"contents": [{"kind": "text", "text": "Instructions"}, {"kind": "text", "text": "."}]}]},
                        "wording": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {"kind": "text", "text": "A"},
                                        {"kind": "whitespace"},
                                        {
                                            "kind": "multipleChoicesInput",
                                            "show_arrow_before": False,
                                            "choices": [[{"kind": "text", "text": "alpha"}], [{"kind": "text", "text": "beta"}]],
                                            "show_choices_by_default": False,
                                        },
                                        {"kind": "text", "text": "."},
                                    ]
                                }
                            ]
                        },
                    }
                ],
            },
        )

    def test_crash_79(self):
        payload = {
            "data": {
                "type": "parsedExercise",
                "attributes": {
                    "adaptation": {
                        "kind": "generic",
                        "wording_paragraphs_per_pagelet": None,
                        "single_item_per_paragraph": False,
                        "placeholder_for_fill_with_free_text": None,
                        "items": None,
                        "items_are_selectable": None,
                        "items_are_boxed": False,
                        "items_have_mcq_beside": False,
                        "items_have_mcq_below": False,
                        "items_have_predefined_mcq": {"grammatical_gender": False, "grammatical_number": False},
                        "items_are_repeated_with_mcq": False,
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                    "clue": [{"attributes": {}, "insert": "\n"}],
                    "example": [{"attributes": {}, "insert": "\n"}],
                    "instructions": [
                        {"attributes": {}, "insert": "Blah "},
                        {"attributes": {"choices2": {"placeholder": "", "separator1": "", "separator2": "o", "start": "", "stop": ""}}, "insert": "on ou ont"},
                        {"attributes": {}, "insert": ".\n"},
                    ],
                    "number": "",
                    "textReference": [{"attributes": {}, "insert": "\n"}],
                    "wording": [{"attributes": {}, "insert": "Blah ... blih.\n"}],
                },
                "relationships": {},
            }
        }
        response = self.post("http://server/parsedExercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(
            response.json()["data"]["attributes"]["adapted"],
            {
                "number": "",
                "textbook_page": None,
                "pagelets": [
                    {
                        "instructions": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {"kind": "text", "text": "Blah"},
                                        {"kind": "whitespace"},
                                        {"kind": "passiveSequence", "contents": [{"kind": "text", "text": "n"}], "boxed": True},
                                        {"kind": "whitespace"},
                                        {"kind": "passiveSequence", "contents": [{"kind": "text", "text": "u"}], "boxed": True},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "ou"},
                                        {"kind": "whitespace"},
                                        {"kind": "passiveSequence", "contents": [{"kind": "text", "text": "nt"}], "boxed": True},
                                        {"kind": "text", "text": "."},
                                    ]
                                }
                            ]
                        },
                        "wording": {
                            "paragraphs": [
                                {
                                    "contents": [
                                        {"kind": "text", "text": "Blah"},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "..."},
                                        {"kind": "whitespace"},
                                        {"kind": "text", "text": "blih"},
                                        {"kind": "text", "text": "."},
                                    ]
                                }
                            ]
                        },
                    }
                ],
            },
        )
