from starlette import status

from .adaptations.fill_with_free_text import FillWithFreeTextAdaptation, FillWithFreeTextAdaptationsResource
from .adaptations.multiple_choices_in_instructions import MultipleChoicesInInstructionsAdaptation, MultipleChoicesInInstructionsAdaptationsResource
from .adaptations.multiple_choices_in_wording import MultipleChoicesInWordingAdaptation, MultipleChoicesInWordingAdaptationsResource
from .adaptations.select_things import SelectThingsAdaptation, SelectThingsAdaptationsResource
from .adapted_exercises import AdaptedExercisesResource
from .exercises import Exercise, ExercisesResource, ExtractionEventsResource
from .pdfs import PdfFile, PdfFileNaming, PdfFilesResource, PdfFileNamingsResource
from .pings import PingsResource
from .projects import Project, ProjectsResource
from .testing import ApiTestCase, LoggedInApiTestCase
from .textbooks import Textbook, TextbooksResource, SectionsResource
from .users import UsersResource
from .users.recovery import RecoveryEmailRequestsResource
from .wrapping import get_wrapper


resources = [
    UsersResource(),
    RecoveryEmailRequestsResource(),
    PingsResource(),
    PdfFilesResource(),
    PdfFileNamingsResource(),
    ProjectsResource(),
    TextbooksResource(),
    SectionsResource(),
    ExercisesResource(),
    ExtractionEventsResource(),
    SelectThingsAdaptationsResource(),
    FillWithFreeTextAdaptationsResource(),
    MultipleChoicesInInstructionsAdaptationsResource(),
    MultipleChoicesInWordingAdaptationsResource(),
    AdaptedExercisesResource(),
]


polymorphism = {
    get_wrapper(SelectThingsAdaptation): "select_things_adaptation",
    get_wrapper(FillWithFreeTextAdaptation): "fill_with_free_text_adaptation",
    get_wrapper(MultipleChoicesInInstructionsAdaptation): "multiple_choices_in_instructions_adaptation",
    get_wrapper(MultipleChoicesInWordingAdaptation): "multiple_choices_in_wording_adaptation",
}


class PdfFilesApiTestCase(LoggedInApiTestCase):
    resources = resources
    polymorphism = polymorphism

    def test_create__ok(self):
        payload = {
            "data": {
                "type": "pdfFile",
                "attributes": {
                    "sha256": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                    "bytesCount": 123456789, "pagesCount": 42,
                },
            },
        }
        response = self.post("http://server/pdfFiles", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "pdfFile",
                "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                "links": {"self": "http://server/pdfFiles/87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                "attributes": {
                    "sha256": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                    "bytesCount": 123456789, "pagesCount": 42,
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                },
                "relationships": {
                    "sections": {"data": [], "meta": {"count": 0}},
                    "namings": {"data": [], "meta": {"count": 0}},
                    "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(PdfFile), 1)
        pdf_file = self.get_model(PdfFile, "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7")
        self.assertEqual(pdf_file.sha256, "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7")
        self.assertEqual(pdf_file.bytes_count, 123456789)
        self.assertEqual(pdf_file.pages_count, 42)

    def test_create_twice(self):
        self.expect_commits_rollbacks(2, 1)

        payload = {
            "data": {
                "type": "pdfFile",
                "attributes": {
                    "sha256": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                    "bytesCount": 123456789, "pagesCount": 42,
                },
            },
        }
        response = self.post("http://server/pdfFiles", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        created_at = response.json()["data"]["attributes"]["createdAt"]
        response = self.post("http://server/pdfFiles", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "pdfFile",
                "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                "links": {"self": "http://server/pdfFiles/87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                "attributes": {
                    "sha256": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                    "bytesCount": 123456789, "pagesCount": 42,
                    "createdAt": created_at,
                },
                "relationships": {
                    "sections": {"data": [], "meta": {"count": 0}},
                    "namings": {"data": [], "meta": {"count": 0}},
                    "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(PdfFile), 1)
        pdf_file = self.get_model(PdfFile, "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7")
        self.assertEqual(pdf_file.sha256, "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7")
        self.assertEqual(pdf_file.bytes_count, 123456789)
        self.assertEqual(pdf_file.pages_count, 42)

    def test_create__short_sha256(self):
        self.expect_rollback()

        payload = {
            "data": {
                "type": "pdfFile",
                "attributes": {
                    "sha256": "0263829989b6fd954f7",
                    "bytesCount": 123456789, "pagesCount": 42,
                },
            },
        }
        response = self.post("http://server/pdfFiles", payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
        self.assertEqual(response.json(), {"detail": "check_sha256_format"})

        self.assertEqual(self.count_models(PdfFile), 0)

    def test_create__bad_sha256(self):
        self.expect_rollback()

        payload = {
            "data": {
                "type": "pdfFile",
                "attributes": {
                    "sha256": "0263829989b6fd954f72baaf2fc64bc2e2f01d692d4de72986ea808f6e99813x",
                    "bytesCount": 123456789, "pagesCount": 42,
                },
            },
        }
        response = self.post("http://server/pdfFiles", payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
        self.assertEqual(response.json(), {"detail": "check_sha256_format"})

        self.assertEqual(self.count_models(Exercise), 0)

    def test_get(self):
        pdf_file = self.create_model(PdfFile, sha256="87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7", bytes_count=123456789, pages_count=42)
        self.create_model(PdfFileNaming, pdf_file=pdf_file, name="amazing.pdf")

        response = self.get("http://server/pdfFiles/87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "pdfFile",
                "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                "links": {"self": "http://server/pdfFiles/87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                "attributes": {
                    "sha256": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                    "bytesCount": 123456789, "pagesCount": 42,
                    "createdAt": pdf_file.created_at.isoformat().replace("+00:00", "Z"),
                },
                "relationships": {
                    "namings": {"data": [{"type": "pdfFileNaming", "id": "tnahml"}], "meta": {"count": 1}},
                    "sections": {"data": [], "meta": {"count": 0}},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
        })

    def test_get__include_namings(self):
        pdf_file = self.create_model(PdfFile, sha256="87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7", bytes_count=123456789, pages_count=42)
        naming_1 = self.create_model(PdfFileNaming, pdf_file=pdf_file, name="amazing.pdf")
        naming_2 = self.create_model(PdfFileNaming, pdf_file=pdf_file, name="alias.pdf")

        response = self.get("http://server/pdfFiles/87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7?include=namings")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "pdfFile",
                "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                "links": {"self": "http://server/pdfFiles/87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                "attributes": {
                    "sha256": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                    "bytesCount": 123456789, "pagesCount": 42,
                    "createdAt": pdf_file.created_at.isoformat().replace("+00:00", "Z"),
                },
                "relationships": {
                    "namings": {
                        "data": [
                            {"type": "pdfFileNaming", "id": "tnahml"},
                            {"type": "pdfFileNaming", "id": "wmyxrm"},
                        ],
                        "meta": {"count": 2},
                    },
                    "sections": {"data": [], "meta": {"count": 0}},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
            "included": [
                {
                    "type": "pdfFileNaming",
                    "id": "tnahml",
                    "links": {"self": "http://server/pdfFileNamings/tnahml"},
                    "attributes": {
                        "name": "amazing.pdf",
                        "createdAt": naming_1.created_at.isoformat().replace("+00:00", "Z"),
                    },
                    "relationships": {
                        "pdfFile": {
                            "data": {"type": "pdfFile", "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                        },
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "pdfFileNaming",
                    "id": "wmyxrm",
                    "links": {"self": "http://server/pdfFileNamings/wmyxrm"},
                    "attributes": {
                        "name": "alias.pdf",
                        "createdAt": naming_2.created_at.isoformat().replace("+00:00", "Z"),
                    },
                    "relationships": {
                        "pdfFile": {
                            "data": {"type": "pdfFile", "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                        },
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
        })


class TextbooksApiTestCase(LoggedInApiTestCase):
    resources = resources
    polymorphism = polymorphism

    def setUp(self):
        super().setUp()
        self.project = self.create_model(Project, title="The project", description="Description")

    def test_create__minimal(self):
        payload = {
            "data": {
                "type": "textbook",
                "attributes": {
                    "title": "The title",
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                },
            },
        }
        response = self.post("http://server/textbooks", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "klxufv",
                "links": {"self": "http://server/textbooks/klxufv"},
                "attributes": {
                    "title": "The title",
                    "publisher": None, "year": None, "isbn": None,
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "exercises": {"data": [], "meta": {"count": 0}},
                    "sections": {"data": [], "meta": {"count": 0}},
                    "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(Textbook), 1)
        textbook = self.get_model(Textbook, 1)
        self.assertEqual(textbook.id, 1)
        self.assertEqual(textbook.project, self.project)
        self.assertEqual(textbook.title, "The title")
        self.assertIsNone(textbook.publisher)
        self.assertIsNone(textbook.year)
        self.assertIsNone(textbook.isbn)

    def test_create__full(self):
        payload = {
            "data": {
                "type": "textbook",
                "attributes": {
                    "title": "The title",
                    "publisher": "The publisher",
                    "year": 2023,
                    "isbn": "9783161484100",
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                },
            },
        }
        response = self.post("http://server/textbooks", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "klxufv",
                "links": {"self": "http://server/textbooks/klxufv"},
                "attributes": {
                    "title": "The title",
                    "publisher": "The publisher",
                    "year": 2023,
                    "isbn": "9783161484100",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "exercises": {"data": [], "meta": {"count": 0}},
                    "sections": {"data": [], "meta": {"count": 0}},
                    "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(Textbook), 1)
        textbook = self.get_model(Textbook, 1)
        self.assertEqual(textbook.id, 1)
        self.assertEqual(textbook.project, self.project)
        self.assertEqual(textbook.title, "The title")
        self.assertEqual(textbook.publisher, "The publisher")
        self.assertEqual(textbook.year, 2023)
        self.assertEqual(textbook.isbn, "9783161484100")

    def test_create__bad_isbn(self):
        self.expect_rollback()

        payload = {
            "data": {
                "type": "textbook",
                "attributes": {
                    "title": "The title",
                    "isbn": "abcdefgh",
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                },
            },
        }
        response = self.post("http://server/textbooks", payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
        self.assertEqual(response.json(), {"detail": "check_isbn_format"})

        self.assertEqual(self.count_models(Textbook), 0)

    def test_get__no_include(self):
        textbook = self.create_model(Textbook, project=self.project, title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=16, number="11", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=17, number="13", instructions="", wording="", example="", clue="")

        response = self.get("http://server/textbooks/klxufv")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "klxufv",
                "links": {"self": "http://server/textbooks/klxufv"},
                "attributes": {
                    "title": "The title",
                    "publisher": "The publisher",
                    "year": 2023,
                    "isbn": "9783161484100",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "exercises": {
                        "data": [
                            {"type": "exercise", "id": "wbqloc"},
                            {"type": "exercise", "id": "bylced"},
                        ],
                        "meta": {"count": 2},
                    },
                    "sections": {"data": [], "meta": {"count": 0}},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
        })

    def test_get__include_exercises(self):
        textbook = self.create_model(Textbook, project=self.project, title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=16, number="11", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=17, number="13", instructions="", wording="", example="", clue="")

        response = self.get("http://server/textbooks/klxufv?include=exercises")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "klxufv",
                "links": {"self": "http://server/textbooks/klxufv"},
                "attributes": {
                    "title": "The title",
                    "publisher": "The publisher",
                    "year": 2023,
                    "isbn": "9783161484100",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "exercises": {
                        "data": [
                            {"type": "exercise", "id": "wbqloc"},
                            {"type": "exercise", "id": "bylced"},
                        ],
                        "meta": {"count": 2},
                    },
                    "sections": {"data": [], "meta": {"count": 0}},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
            "included": [
                {
                    "type": "exercise",
                    "id": "bylced",
                    "links": {"self": "http://server/exercises/bylced"},
                    "attributes": {
                        "textbookPage": 17, "number": "13",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "wbqloc",
                    "links": {"self": "http://server/exercises/wbqloc"},
                    "attributes": {
                        "textbookPage": 16, "number": "11",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["included"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
        })

    def test_list(self):
        self.expect_commits_rollbacks(2, 0)

        textbook = self.create_model(Textbook, project=self.project, title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=12, number="4", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=13, number="5", instructions="", wording="", example="", clue="")
        textbook = self.create_model(Textbook, project=self.project, title="Another title", publisher="Another publisher", year=2024, isbn="9783161484101")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=14, number="6", instructions="", wording="", example="", clue="")
        textbook = self.create_model(Textbook, project=self.project, title="Yet another title", publisher="Yet another publisher", year=2025, isbn="9783161484102")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=15, number="7", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=16, number="8", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=17, number="9", instructions="", wording="", example="", clue="")

        response = self.get("http://server/textbooks")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "textbook",
                    "id": "klxufv",
                    "links": {"self": "http://server/textbooks/klxufv"},
                    "attributes": {
                        "title": "The title",
                        "publisher": "The publisher",
                        "year": 2023,
                        "isbn": "9783161484100",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "exercises": {"data": [{"type": "exercise", "id": "wbqloc"}, {"type": "exercise", "id": "bylced"}], "meta": {"count": 2}},
                        "sections": {"data": [], "meta": {"count": 0}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "textbook",
                    "id": "ojsbmy",
                    "links": {"self": "http://server/textbooks/ojsbmy"},
                    "attributes": {
                        "title": "Another title",
                        "publisher": "Another publisher",
                        "year": 2024,
                        "isbn": "9783161484101",
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "exercises": {"data": [{"type": "exercise", "id": "jkrudc"}], "meta": {"count": 1}},
                        "sections": {"data": [], "meta": {"count": 0}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/textbooks?page%5Bnumber%5D=1",
                "last": "http://server/textbooks?page%5Bnumber%5D=2",
                "next": "http://server/textbooks?page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.get("http://server/textbooks?page[number]=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "textbook",
                    "id": "pkdksv",
                    "links": {"self": "http://server/textbooks/pkdksv"},
                    "attributes": {
                        "title": "Yet another title",
                        "publisher": "Yet another publisher",
                        "year": 2025,
                        "isbn": "9783161484102",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "exercises": {
                            "data": [
                                {"type": "exercise", "id": "ufefwu"},
                                {"type": "exercise", "id": "orxbzq"},
                                {"type": "exercise", "id": "ahbwey"},
                            ],
                            "meta": {"count": 3},
                        },
                        "sections": {"data": [], "meta": {"count": 0}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/textbooks?page%5Bnumber%5D=1",
                "last": "http://server/textbooks?page%5Bnumber%5D=2",
                "next": None,
                "prev": "http://server/textbooks?page%5Bnumber%5D=1",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_list__include_exercises(self):
        self.expect_commits_rollbacks(2, 0)

        textbook = self.create_model(Textbook, project=self.project, title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=12, number="4", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=13, number="5", instructions="", wording="", example="", clue="")
        textbook = self.create_model(Textbook, project=self.project, title="Another title", publisher="Another publisher", year=2024, isbn="9783161484101")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=14, number="6", instructions="", wording="", example="", clue="")
        textbook = self.create_model(Textbook, project=self.project, title="Yet another title", publisher="Yet another publisher", year=2025, isbn="9783161484102")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=15, number="7", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=16, number="8", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=17, number="9", instructions="", wording="", example="", clue="")

        response = self.get("http://server/textbooks?include=exercises")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "textbook",
                    "id": "klxufv",
                    "links": {"self": "http://server/textbooks/klxufv"},
                    "attributes": {
                        "title": "The title",
                        "publisher": "The publisher",
                        "year": 2023,
                        "isbn": "9783161484100",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "exercises": {"data": [{"type": "exercise", "id": "wbqloc"}, {"type": "exercise", "id": "bylced"}], "meta": {"count": 2}},
                        "sections": {"data": [], "meta": {"count": 0}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "textbook",
                    "id": "ojsbmy",
                    "links": {"self": "http://server/textbooks/ojsbmy"},
                    "attributes": {
                        "title": "Another title",
                        "publisher": "Another publisher",
                        "year": 2024,
                        "isbn": "9783161484101",
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "exercises": {"data": [{"type": "exercise", "id": "jkrudc"}], "meta": {"count": 1}},
                        "sections": {"data": [], "meta": {"count": 0}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "included": [
                {
                    "type": "exercise",
                    "id": "bylced",
                    "attributes": {
                        "textbookPage": 13, "number": "5",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                    "links": {"self": "http://server/exercises/bylced"},
                },
                {
                    "type": "exercise",
                    "id": "jkrudc",
                    "attributes": {
                        "textbookPage": 14, "number": "6",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["included"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "ojsbmy"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                    "links": {"self": "http://server/exercises/jkrudc"},
                },
                {
                    "type": "exercise",
                    "id": "wbqloc",
                    "attributes": {
                        "textbookPage": 12, "number": "4",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["included"][2]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][2]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                    "links": {"self": "http://server/exercises/wbqloc"},
                },
            ],
            "links": {
                "first": "http://server/textbooks?include=exercises&page%5Bnumber%5D=1",
                "last": "http://server/textbooks?include=exercises&page%5Bnumber%5D=2",
                "next": "http://server/textbooks?include=exercises&page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.get("http://server/textbooks?include=exercises&page[number]=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "textbook",
                    "id": "pkdksv",
                    "links": {"self": "http://server/textbooks/pkdksv"},
                    "attributes": {
                        "title": "Yet another title",
                        "publisher": "Yet another publisher",
                        "year": 2025,
                        "isbn": "9783161484102",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "exercises": {
                            "data": [
                                {"type": "exercise", "id": "ufefwu"},
                                {"type": "exercise", "id": "orxbzq"},
                                {"type": "exercise", "id": "ahbwey"},
                            ],
                            "meta": {"count": 3},
                        },
                        "sections": {"data": [], "meta": {"count": 0}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "included": [
                {
                    "type": "exercise",
                    "id": "ahbwey",
                    "links": {"self": "http://server/exercises/ahbwey"},
                    "attributes": {
                        "textbookPage": 17, "number": "9",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "pkdksv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "orxbzq",
                    "links": {"self": "http://server/exercises/orxbzq"},
                    "attributes": {
                        "textbookPage": 16, "number": "8",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["included"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "pkdksv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "ufefwu",
                    "links": {"self": "http://server/exercises/ufefwu"},
                    "attributes": {
                        "textbookPage": 15, "number": "7",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["included"][2]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][2]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "pkdksv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/textbooks?include=exercises&page%5Bnumber%5D=1",
                "last": "http://server/textbooks?include=exercises&page%5Bnumber%5D=2",
                "next": None,
                "prev": "http://server/textbooks?include=exercises&page%5Bnumber%5D=1",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_patch__full(self):
        textbook = self.create_model(Textbook, project=self.project, title="The title", publisher="The publisher", year=2023, isbn="9783161484100")

        payload = {
            "data": {
                "type": "textbook",
                "id": "klxufv",
                "attributes": {
                    "title": "The new title",
                    "publisher": "The new publisher",
                    "year": 2024,
                    "isbn": "9783161484101",
                },
            },
        }
        response = self.patch("http://server/textbooks/klxufv", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "klxufv",
                "links": {"self": "http://server/textbooks/klxufv"},
                "attributes": {
                    "title": "The new title",
                    "publisher": "The new publisher",
                    "year": 2024,
                    "isbn": "9783161484101",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "exercises": {"data": [], "meta": {"count": 0}},
                    "sections": {"data": [], "meta": {"count": 0}},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(Textbook), 1)
        textbook = self.get_model(Textbook, 1)
        self.assertEqual(textbook.id, 1)
        self.assertEqual(textbook.title, "The new title")
        self.assertEqual(textbook.publisher, "The new publisher")
        self.assertEqual(textbook.year, 2024)
        self.assertEqual(textbook.isbn, "9783161484101")

    def test_patch__partial(self):
        self.create_model(Textbook, project=self.project, title="The title", publisher="The publisher", year=2023, isbn="9783161484100")

        payload = {
            "data": {
                "type": "textbook",
                "id": "klxufv",
                "attributes": {
                    "title": "The new title",
                    "year": None,
                },
            },
        }
        response = self.patch("http://server/textbooks/klxufv", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "klxufv",
                "links": {"self": "http://server/textbooks/klxufv"},
                "attributes": {
                    "title": "The new title",
                    "publisher": "The publisher",
                    "year": None,
                    "isbn": "9783161484100",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "exercises": {"data": [], "meta": {"count": 0}},
                    "sections": {"data": [], "meta": {"count": 0}},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(Textbook), 1)
        textbook = self.get_model(Textbook, 1)
        self.assertEqual(textbook.id, 1)
        self.assertEqual(textbook.project, self.project)
        self.assertEqual(textbook.title, "The new title")
        self.assertEqual(textbook.publisher, "The publisher")
        self.assertIsNone(textbook.year)
        self.assertEqual(textbook.isbn, "9783161484100")

    def test_patch__read_only_project(self):
        self.create_model(Textbook, project=self.project, title="The title", publisher="The publisher", year=2023, isbn="9783161484100")

        payload = {
            "data": {
                "type": "textbook",
                "id": "klxufv",
                "relationships": {
                    "project": {"data": {"type": "project", "id": "other"}},
                },
            },
        }
        response = self.patch("http://server/textbooks/klxufv", payload)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())
        self.assertEqual(response.json(), {"detail": [{
            "input": {"data": {"id": "other", "type": "project"}},
            "loc": ["body", "data", "relationships", "project"],
            "msg": "Extra inputs are not permitted",
            "type": "extra_forbidden",
        }]})

        self.assertEqual(self.count_models(Textbook), 1)
        textbook = self.get_model(Textbook, 1)
        self.assertEqual(textbook.id, 1)
        self.assertEqual(textbook.project, self.project)
        self.assertEqual(textbook.title, "The title")
        self.assertEqual(textbook.publisher, "The publisher")
        self.assertEqual(textbook.year, 2023)
        self.assertEqual(textbook.isbn, "9783161484100")

    def test_delete__without_exercises(self):
        self.create_model(Textbook, project=self.project, title="The title", publisher="The publisher", year=2023, isbn="9783161484100")

        response = self.delete("http://server/textbooks/klxufv")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.count_models(Textbook), 0)

    def test_delete__with_exercises(self):
        textbook = self.create_model(Textbook, project=self.project, title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=12, number="4", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=13, number="5", instructions="", wording="", example="", clue="")

        response = self.delete("http://server/textbooks/klxufv")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.count_models(Textbook), 0)
        self.assertEqual(self.count_models(Exercise), 0)


class ExercisesApiTestCase(LoggedInApiTestCase):
    resources = resources
    polymorphism = polymorphism

    def setUp(self):
        super().setUp()
        self.project = self.create_model(Project, title="The project", description="Description")
        self.textbook = self.create_model(Textbook, project=self.project, title="The title")

    def test_create__minimal_without_textbook(self):
        payload = {
            "data": {
                "type": "exercise",
                "attributes": {
                    "number": "42",
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                },
            },
        }
        response = self.post("http://server/exercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "links": {"self": "http://server/exercises/wbqloc"},
                "attributes": {
                    "textbookPage": None, "number": "42",
                    "boundingRectangle": None,
                    "instructions": "", "example": "", "clue": "", "wording": "",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": None},
                    "adaptation": {"data": None},
                    "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(Exercise), 1)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertIsNone(exercise.textbook)
        self.assertIsNone(exercise.textbook_page)
        self.assertEqual(exercise.number, "42")
        self.assertEqual(exercise.instructions, "")
        self.assertEqual(exercise.example, "")
        self.assertEqual(exercise.clue, "")
        self.assertEqual(exercise.wording, "")

    def test_create__minimal_in_textbook(self):
        payload = {
            "data": {
                "type": "exercise",
                "attributes": {
                    "textbookPage": 12, "number": "42",
                    "boundingRectangle": None,
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                },
            },
        }
        response = self.post("http://server/exercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "links": {"self": "http://server/exercises/wbqloc"},
                "attributes": {
                    "textbookPage": 12, "number": "42",
                    "boundingRectangle": None,
                    "instructions": "", "example": "", "clue": "", "wording": "",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                    "adaptation": {"data": None},
                    "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(Exercise), 1)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertEqual(exercise.textbook, self.textbook)
        self.assertEqual(exercise.textbook_page, 12)
        self.assertEqual(exercise.number, "42")
        self.assertEqual(exercise.instructions, "")
        self.assertEqual(exercise.example, "")
        self.assertEqual(exercise.clue, "")
        self.assertEqual(exercise.wording, "")

    def test_create__full(self):
        payload = {
            "data": {
                "type": "exercise",
                "attributes": {
                    "textbookPage": 14, "number": "1",
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                    "boundingRectangle": {"start": {"x": 0, "y": 1}, "stop": {"x": 2, "y": 3}},
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                },
            },
        }
        response = self.post("http://server/exercises", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "links": {"self": "http://server/exercises/wbqloc"},
                "attributes": {
                    "textbookPage": 14, "number": "1",
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                    "boundingRectangle": {"start": {"x": 0, "y": 1}, "stop": {"x": 2, "y": 3}},
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                    "adaptation": {"data": None},
                    "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(Exercise), 1)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertEqual(exercise.textbook, self.textbook)
        self.assertEqual(exercise.textbook_page, 14)
        self.assertEqual(exercise.bounding_rectangle, {"start": {"x": 0, "y": 1}, "stop": {"x": 2, "y": 3}})
        self.assertEqual(exercise.number, "1")
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_get__no_include(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        response = self.get("http://server/exercises/wbqloc")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "links": {"self": "http://server/exercises/wbqloc"},
                "attributes": {
                    "textbookPage": 16, "number": "11",
                    "boundingRectangle": None,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                    "adaptation": {"data": None},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
        })

    def test_get__include_textbook(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        response = self.get("http://server/exercises/wbqloc?include=textbook")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "links": {"self": "http://server/exercises/wbqloc"},
                "attributes": {
                    "textbookPage": 16, "number": "11",
                    "boundingRectangle": None,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                    "adaptation": {"data": None},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
            "included": [
                {
                    "type": "textbook",
                    "id": "klxufv",
                    "links": {"self": "http://server/textbooks/klxufv"},
                    "attributes": {
                        "title": "The title",
                        "publisher": None, "year": None, "isbn": None,
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "exercises": {"data": [{"type": "exercise", "id": "wbqloc"}], "meta": {"count": 1}},
                        "sections": {"data": [], "meta": {"count": 0}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
        })

    def test_get__include_adaptation(self):
        exercise = self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )
        self.create_model(
            FillWithFreeTextAdaptation,
            exercise=exercise,
            placeholder="...",
        )

        response = self.get("http://server/exercises/wbqloc?include=adaptation")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "links": {"self": "http://server/exercises/wbqloc"},
                "attributes": {
                    "textbookPage": 16, "number": "11",
                    "boundingRectangle": None,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                    "adaptation": {"data": {"type": "fillWithFreeTextAdaptation", "id": "ljpupg"}},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
            "included": [
                {
                    "type": "fillWithFreeTextAdaptation",
                    "id": "ljpupg",
                    "links": {"self": "http://server/fillWithFreeTextAdaptations/ljpupg"},
                    "attributes": {
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "placeholder": "...",
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "exercise": {"data": {"id": "wbqloc", "type": "exercise"}},
                        "createdBy": {"data": {"id": "fvirvd", "type": "user"}},
                        "updatedBy": {"data": {"id": "fvirvd", "type": "user"}},
                    },
                },
            ],
        })

    # @todo Add test_get__include_adaptation_exercise(self) with include=adaptation.exercise,
    # showing the exercise is not included again, because it's the main data

    def test_list__sorted_by_default(self):
        self.expect_commits_rollbacks(2, 0)

        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=16, number="11", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="3", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="4", instructions="", wording="", example="", clue="")

        response = self.get("http://server/exercises")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "wbqloc",
                    "links": {"self": "http://server/exercises/wbqloc"},
                    "attributes": {
                        "textbookPage": 16, "number": "11",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "bylced",
                    "links": {"self": "http://server/exercises/bylced"},
                    "attributes": {
                        "textbookPage": 17, "number": "3",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/exercises?page%5Bnumber%5D=1",
                "last": "http://server/exercises?page%5Bnumber%5D=2",
                "next": "http://server/exercises?page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.get("http://server/exercises?page[number]=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "jkrudc",
                    "links": {"self": "http://server/exercises/jkrudc"},
                    "attributes": {
                        "textbookPage": 17, "number": "4",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/exercises?page%5Bnumber%5D=1",
                "last": "http://server/exercises?page%5Bnumber%5D=2",
                "next": None,
                "prev": "http://server/exercises?page%5Bnumber%5D=1",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_list__sorted_naturally(self):
        self.expect_commits_rollbacks(2, 0)

        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=16, number="11", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="3", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="4", instructions="", wording="", example="", clue="")

        response = self.get("http://server/exercises")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "wbqloc",
                    "links": {"self": "http://server/exercises/wbqloc"},
                    "attributes": {
                        "textbookPage": 16, "number": "11",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "bylced",
                    "links": {"self": "http://server/exercises/bylced"},
                    "attributes": {
                        "textbookPage": 17, "number": "3",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/exercises?page%5Bnumber%5D=1",
                "last": "http://server/exercises?page%5Bnumber%5D=2",
                "next": "http://server/exercises?page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.get("http://server/exercises?page[number]=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "jkrudc",
                    "links": {"self": "http://server/exercises/jkrudc"},
                    "attributes": {
                        "textbookPage": 17, "number": "4",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/exercises?page%5Bnumber%5D=1",
                "last": "http://server/exercises?page%5Bnumber%5D=2",
                "next": None,
                "prev": "http://server/exercises?page%5Bnumber%5D=1",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_list__include_textbook(self):
        self.expect_commits_rollbacks(2, 0)

        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=16, number="11", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="13", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="14", instructions="", wording="", example="", clue="")
        other_textbook = self.create_model(Textbook, project=self.project, title="The other title")
        self.create_model(Exercise, project=other_textbook.project, textbook=other_textbook, textbook_page=12, number="4", instructions="", wording="", example="", clue="")

        response = self.get("http://server/exercises?include=textbook")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "wbqloc",
                    "links": {"self": "http://server/exercises/wbqloc"},
                    "attributes": {
                        "textbookPage": 16, "number": "11",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "bylced",
                    "links": {"self": "http://server/exercises/bylced"},
                    "attributes": {
                        "textbookPage": 17, "number": "13",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "included": [
                {
                    "type": "textbook",
                    "id": "klxufv",
                    "links": {"self": "http://server/textbooks/klxufv"},
                    "attributes": {
                        "title": "The title",
                        "publisher": None, "year": None, "isbn": None,
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "exercises": {
                            "data": [
                                {"type": "exercise", "id": "wbqloc"},
                                {"type": "exercise", "id": "bylced"},
                                {"type": "exercise", "id": "jkrudc"},
                            ],
                            "meta": {"count": 3},
                        },
                        "sections": {"data": [], "meta": {"count": 0}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/exercises?include=textbook&page%5Bnumber%5D=1",
                "last": "http://server/exercises?include=textbook&page%5Bnumber%5D=2",
                "next": "http://server/exercises?include=textbook&page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {"pagination": {"count": 4, "page": 1, "pages": 2}},
        })

        response = self.get("http://server/exercises?include=textbook&page[number]=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "jkrudc",
                    "links": {"self": "http://server/exercises/jkrudc"},
                    "attributes": {
                        "textbookPage": 17, "number": "14",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "ufefwu",
                    "links": {"self": "http://server/exercises/ufefwu"},
                    "attributes": {
                        "textbookPage": 12, "number": "4",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "ojsbmy"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "included": [
                {
                    "type": "textbook",
                    "id": "klxufv",
                    "links": {"self": "http://server/textbooks/klxufv"},
                    "attributes": {
                        "title": "The title",
                        "publisher": None, "year": None, "isbn": None,
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "exercises": {
                            "data": [
                                {"type": "exercise", "id": "wbqloc"},
                                {"type": "exercise", "id": "bylced"},
                                {"type": "exercise", "id": "jkrudc"},
                            ],
                            "meta": {"count": 3},
                        },
                        "sections": {"data": [], "meta": {"count": 0}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "textbook",
                    "id": "ojsbmy",
                    "links": {"self": "http://server/textbooks/ojsbmy"},
                    "attributes": {
                        "title": "The other title",
                        "publisher": None, "year": None, "isbn": None,
                        "createdAt": response.json()["included"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "exercises": {
                            "data": [
                                {"type": "exercise", "id": "ufefwu"},
                            ],
                            "meta": {"count": 1},
                        },
                        "sections": {"data": [], "meta": {"count": 0}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/exercises?include=textbook&page%5Bnumber%5D=1",
                "last": "http://server/exercises?include=textbook&page%5Bnumber%5D=2",
                "next": None,
                "prev": "http://server/exercises?include=textbook&page%5Bnumber%5D=1",
            },
            "meta": {"pagination": {"count": 4, "page": 2, "pages": 2}},
        })

    def test_list__filter_by_textbook(self):
        self.expect_commits_rollbacks(2, 0)

        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=16, number="11", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="13", instructions="", wording="", example="", clue="")
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="14", instructions="", wording="", example="", clue="")
        other_textbook = self.create_model(Textbook, project=self.project, title="The other title")
        self.create_model(Exercise, project=other_textbook.project, textbook=other_textbook, textbook_page=12, number="4", instructions="", wording="", example="", clue="")

        response = self.get("http://server/exercises?filter[textbook]=klxufv")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "wbqloc",
                    "links": {"self": "http://server/exercises/wbqloc"},
                    "attributes": {
                        "textbookPage": 16, "number": "11",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "bylced",
                    "links": {"self": "http://server/exercises/bylced"},
                    "attributes": {
                        "textbookPage": 17, "number": "13",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/exercises?filter%5Btextbook%5D=klxufv&page%5Bnumber%5D=1",
                "last": "http://server/exercises?filter%5Btextbook%5D=klxufv&page%5Bnumber%5D=2",
                "next": "http://server/exercises?filter%5Btextbook%5D=klxufv&page%5Bnumber%5D=2",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.get("http://server/exercises?filter[textbook]=klxufv&page[number]=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "jkrudc",
                    "links": {"self": "http://server/exercises/jkrudc"},
                    "attributes": {
                        "textbookPage": 17, "number": "14",
                        "boundingRectangle": None,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "adaptation": {"data": None},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
            "links": {
                "first": "http://server/exercises?filter%5Btextbook%5D=klxufv&page%5Bnumber%5D=1",
                "last": "http://server/exercises?filter%5Btextbook%5D=klxufv&page%5Bnumber%5D=2",
                "next": None,
                "prev": "http://server/exercises?filter%5Btextbook%5D=klxufv&page%5Bnumber%5D=1",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_patch__full(self):
        exercise = self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )
        self.assertEqual(self.count_models(Exercise), 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertEqual(exercise.textbook, self.textbook)
        self.assertEqual(exercise.textbook_page, 16)
        self.assertEqual(exercise.number, "11")
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

        payload = {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "attributes": {
                    "instructions": "INSTRUCTIONS", "example": "EXAMPLE", "clue": "CLUE", "wording": "WORDING",
                    "boundingRectangle": {"start": {"x": 10, "y": 11}, "stop": {"x": 12, "y": 13}},
                },
            },
        }
        response = self.patch("http://server/exercises/wbqloc", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "links": {"self": "http://server/exercises/wbqloc"},
                "attributes": {
                    "textbookPage": 16, "number": "11",
                    "boundingRectangle": {"start": {"x": 10, "y": 11}, "stop": {"x": 12, "y": 13}},
                    "instructions": "INSTRUCTIONS", "example": "EXAMPLE", "clue": "CLUE", "wording": "WORDING",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                    "adaptation": {"data": None},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(Exercise), 1)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertEqual(exercise.textbook, self.textbook)
        self.assertEqual(exercise.textbook_page, 16)
        self.assertEqual(exercise.bounding_rectangle, {"start": {"x": 10, "y": 11}, "stop": {"x": 12, "y": 13}})
        self.assertEqual(exercise.number, "11")
        self.assertEqual(exercise.instructions, "INSTRUCTIONS")
        self.assertEqual(exercise.example, "EXAMPLE")
        self.assertEqual(exercise.clue, "CLUE")
        self.assertEqual(exercise.wording, "WORDING")

    def test_patch__partial(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        payload = {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "attributes": {
                    "instructions": "INSTRUCTIONS",
                },
            },
        }
        response = self.patch("http://server/exercises/wbqloc", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "links": {"self": "http://server/exercises/wbqloc"},
                "attributes": {
                    "textbookPage": 16, "number": "11",
                    "boundingRectangle": None,
                    "instructions": "INSTRUCTIONS", "example": "example", "clue": "clue", "wording": "wording",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                    "adaptation": {"data": None},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(Exercise), 1)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertEqual(exercise.textbook, self.textbook)
        self.assertEqual(exercise.textbook_page, 16)
        self.assertEqual(exercise.number, "11")
        self.assertEqual(exercise.instructions, "INSTRUCTIONS")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_patch__read_only_project(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        payload = {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "relationships": {
                    "project": {"data": {"type": "project", "id": "other"}},
                },
            },
        }
        response = self.patch("http://server/exercises/wbqloc", payload)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())
        self.assertEqual(response.json(), {"detail": [{
            "input": {"data": {"id": "other", "type": "project"}},
            "loc": ["body", "data", "relationships", "project"],
            "msg": "Extra inputs are not permitted",
            "type": "extra_forbidden",
        }]})

        self.assertEqual(self.count_models(Exercise), 1)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertEqual(exercise.textbook, self.textbook)
        self.assertEqual(exercise.textbook_page, 16)
        self.assertEqual(exercise.number, "11")
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_patch__read_only_textbook(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )
        self.create_model(Textbook, project=self.project, title="Another textbook")

        payload = {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "relationships": {
                    "textbook": {"data": {"type": "textbook", "id": "ojsbmy"}},
                },
            },
        }
        response = self.patch("http://server/exercises/wbqloc", payload)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())
        self.assertEqual(response.json(), {"detail": [{
            "input": {"data": {"type": "textbook", "id": "ojsbmy"}},
            "loc": ["body", "data", "relationships", "textbook"],
            "msg": "Extra inputs are not permitted",
            "type": "extra_forbidden",
        }]})

        self.assertEqual(self.count_models(Exercise), 1)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertEqual(exercise.textbook, self.textbook)
        self.assertEqual(exercise.textbook_page, 16)
        self.assertEqual(exercise.number, "11")
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_patch__read_only_page(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        payload = {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "attributes": {
                    "textbookPage": 42,
                },
            },
        }
        response = self.patch("http://server/exercises/wbqloc", payload)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())
        self.assertEqual(response.json(), {"detail": [{
            "input": 42,
            "loc": ["body", "data", "attributes", "textbookPage"],
            "msg": "Extra inputs are not permitted",
            "type": "extra_forbidden",
        }]})

        self.assertEqual(self.count_models(Exercise), 1)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertEqual(exercise.textbook, self.textbook)
        self.assertEqual(exercise.textbook_page, 16)
        self.assertEqual(exercise.number, "11")
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_patch__read_only_number(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        payload = {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "attributes": {
                    "number": "12",
                },
            },
        }
        response = self.patch("http://server/exercises/wbqloc", payload)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY, response.json())
        self.assertEqual(response.json(), {"detail": [{
            "input": "12",
            "loc": ["body", "data", "attributes", "number"],
            "msg": "Extra inputs are not permitted",
            "type": "extra_forbidden",
        }]})

        self.assertEqual(self.count_models(Exercise), 1)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertEqual(exercise.textbook, self.textbook)
        self.assertEqual(exercise.textbook_page, 16)
        self.assertEqual(exercise.number, "11")
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_delete(self):
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=16, number="11", instructions="", wording="", example="", clue="")
        self.assertEqual(self.count_models(Exercise), 1)

        response = self.delete("http://server/exercises/wbqloc")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")

        self.assertEqual(self.count_models(Exercise), 0)


class AdaptationsApiTestCase(LoggedInApiTestCase):
    resources = resources
    polymorphism = polymorphism

    def setUp(self):
        super().setUp()
        self.project = self.create_model(Project, title="The project", description="Description")
        self.exercise = self.create_model(Exercise, project=self.project, number="Exercise", textbook=None, textbook_page=None, instructions="", wording="", example="", clue="")

    def test_create_select_things_adaptation(self):
        payload = {
            "data": {
                "type": "selectThingsAdaptation",
                "attributes": {
                    "colors": 3,
                    "words": True,
                    "punctuation": True,
                },
                "relationships": {
                    "exercise": {"data": {"type": "exercise", "id": "wbqloc"}},
                },
            },
        }
        response = self.post("http://server/selectThingsAdaptations", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "selectThingsAdaptation",
                "id": "ugrfkh",
                "links": {"self": "http://server/selectThingsAdaptations/ugrfkh"},
                "attributes": {
                    "colors": 3,
                    "words": True,
                    "punctuation": True,
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "exercise": {"data": {"type": "exercise", "id": "wbqloc"}},
                    "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        exercise = self.get_model(Exercise, 1)
        self.assertIsInstance(exercise.adaptation, SelectThingsAdaptation)
        self.assertEqual(exercise.adaptation.colors, 3)
        self.assertTrue(exercise.adaptation.words)
        self.assertTrue(exercise.adaptation.punctuation)

    def test_create_fill_with_free_text_adaptation(self):
        payload = {
            "data": {
                "type": "fillWithFreeTextAdaptation",
                "attributes": {
                    "placeholder": "...",
                },
                "relationships": {
                    "exercise": {"data": {"type": "exercise", "id": "wbqloc"}},
                },
            },
        }
        response = self.post("http://server/fillWithFreeTextAdaptations", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "fillWithFreeTextAdaptation",
                "id": "ljpupg",
                "links": {"self": "http://server/fillWithFreeTextAdaptations/ljpupg"},
                "attributes": {
                    "placeholder": "...",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "exercise": {"data": {"type": "exercise", "id": "wbqloc"}},
                    "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        exercise = self.get_model(Exercise, 1)
        self.assertIsInstance(exercise.adaptation, FillWithFreeTextAdaptation)
        self.assertEqual(exercise.adaptation.placeholder, "...")

    def test_dont_update_adaptation(self):
        self.exercise.adaptation = self.create_model(SelectThingsAdaptation, colors=3, words=True, punctuation=True)
        self._TransactionTestCase__session.commit()

        payload = {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "attributes": {
                    "instructions": "INSTRUCTIONS",
                },
            },
        }
        response = self.patch("http://server/exercises/wbqloc", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "links": {"self": "http://server/exercises/wbqloc"},
                "attributes": {
                    "textbookPage": None, "number": "Exercise",
                    "boundingRectangle": None,
                    "instructions": "INSTRUCTIONS", "example": "", "clue": "", "wording": "",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": None},
                    "adaptation": {"data": {"type": "selectThingsAdaptation", "id": "ugrfkh"}},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        self.assertEqual(self.count_models(SelectThingsAdaptation), 1)
        exercise = self.get_model(Exercise, 1)
        self.assertEqual(exercise.adaptation, self.get_model(SelectThingsAdaptation, 1))

    def test_update_adaptation__none(self):
        self.exercise.adaptation = self.create_model(SelectThingsAdaptation, colors=3, words=True, punctuation=True)
        self._TransactionTestCase__session.commit()

        payload = {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "relationships": {
                    "adaptation": {"data": None},
                },
            },
        }
        response = self.patch("http://server/exercises/wbqloc", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "links": {"self": "http://server/exercises/wbqloc"},
                "attributes": {
                    "textbookPage": None, "number": "Exercise",
                    "boundingRectangle": None,
                    "instructions": "", "example": "", "clue": "", "wording": "",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": None},
                    "adaptation": {"data": None},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        exercise = self.get_model(Exercise, 1)
        self.assertIsNone(exercise.adaptation)

        self.assertEqual(self.count_models(SelectThingsAdaptation), 0)

    def test_update_adaptation__other_type(self):
        self.exercise.adaptation = self.create_model(SelectThingsAdaptation, colors=3, words=True, punctuation=True)
        self._TransactionTestCase__session.commit()

        payload = {
            "data": {
                "type": "fillWithFreeTextAdaptation",
                "attributes": {
                    "placeholder": "...",
                },
                "relationships": {
                    "exercise": {"data": {"type": "exercise", "id": "wbqloc"}},
                },
            },
        }
        response = self.post("http://server/fillWithFreeTextAdaptations", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "fillWithFreeTextAdaptation",
                "id": "vahdwa",
                "links": {"self": "http://server/fillWithFreeTextAdaptations/vahdwa"},
                "attributes": {
                    "placeholder": "...",
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "exercise": {"data": {"type": "exercise", "id": "wbqloc"}},
                    "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                    "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                },
            },
        })

        exercise = self.get_model(Exercise, 1)
        self.assertIsInstance(exercise.adaptation, FillWithFreeTextAdaptation)
        self.assertEqual(exercise.adaptation.placeholder, "...")

        self.assertEqual(self.count_models(SelectThingsAdaptation), 0)


class BatchingApiTestCase(LoggedInApiTestCase):
    resources = resources
    polymorphism = polymorphism

    def test_empty_batch(self):
        response = self.post("http://server/batch", {"atomic:operations": []})
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {"atomic:results": []})

    def test_create_one_projects(self):
        payload = {
            "atomic:operations": [
                {
                    "op": "add",
                    "data": {
                        "type": "project",
                        "attributes": {
                            "title": "The project",
                            "description": "Description",
                        },
                    },
                },
            ],
        }
        response = self.post("http://server/batch", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(
            response.json(),
            {
                "atomic:results": [
                    {
                        "data": {
                            "type": "project",
                            "id": "xkopqm",
                            "attributes": {
                                "description": "Description",
                                "title": "The project",
                                "createdAt": response.json()["atomic:results"][0]["data"]["attributes"]["createdAt"],
                                "updatedAt": response.json()["atomic:results"][0]["data"]["attributes"]["updatedAt"],
                            },
                            "links": {"self": "http://server/projects/xkopqm"},
                            "relationships": {
                                "exercises": {"data": [], "meta": {"count": 0}},
                                "textbooks": {"data": [], "meta": {"count": 0}},
                                "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                                "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                            },
                        },
                    },
                ],
            },
        )

    def test_create_many_projects(self):
        payload = {
            "atomic:operations": [
                {
                    "op": "add",
                    "data": {
                        "type": "project",
                        "attributes": {
                            "title": f"The project {i}",
                            "description": f"Description {i}",
                        },
                    },
                }
                for i in range(1, 10)
            ],
        }
        response = self.post("http://server/batch", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(
            response.json(),
            {
                "atomic:results": [
                    {
                        "data": {
                            "type": "project",
                            "id": ProjectsResource.sqids.encode([i]),
                            "attributes": {
                                "description": f"Description {i}",
                                "title": f"The project {i}",
                                "createdAt": response.json()["atomic:results"][i - 1]["data"]["attributes"]["createdAt"],
                                "updatedAt": response.json()["atomic:results"][i - 1]["data"]["attributes"]["updatedAt"],
                            },
                            "links": {"self": f"http://server/projects/{ProjectsResource.sqids.encode([i])}"},
                            "relationships": {
                                "exercises": {"data": [], "meta": {"count": 0}},
                                "textbooks": {"data": [], "meta": {"count": 0}},
                                "createdBy": {"data": {"type": "user", "id": "ckylfa"}},
                                "updatedBy": {"data": {"type": "user", "id": "ckylfa"}},
                            },
                        },
                    }
                    for i in range(1, 10)
                ],
            },
        )


class UnauthenticatedUseApiTestCase(ApiTestCase):
    resources = resources
    polymorphism = polymorphism

    anonymous_use_behavior = {
        # We'd prefer if none of these would commit, but that's a quest for another day.
        "/pings GET": (status.HTTP_200_OK, True),
        "/pings POST": (status.HTTP_422_UNPROCESSABLE_ENTITY, True),
        "/pings/0 DELETE": (status.HTTP_404_NOT_FOUND, False),
        "/pings/0 GET": (status.HTTP_404_NOT_FOUND, False),
        "/pings/0 PATCH": (status.HTTP_422_UNPROCESSABLE_ENTITY, True),
        "/recoveryEmailRequests POST": (status.HTTP_422_UNPROCESSABLE_ENTITY, True),
        "/token POST": (status.HTTP_422_UNPROCESSABLE_ENTITY, True),
    }

    def request(self, method, path):
        match method:
            case "get":
                return self.get(f"http://server{path}")
            case "post":
                return self.post(f"http://server{path}", {})
            case "patch":
                return self.patch(f"http://server{path}", {})
            case "delete":
                return self.delete(f"http://server{path}")
            case _:
                self.fail(f"Unsupported method: {method}")

    def test(self):
        openapi = self.api_app.openapi()

        expected_commits = 0
        expected_rollbacks = 0
        for path, operations in openapi["paths"].items():
            path = path.replace("{id}", "0")
            for method in operations.keys():
                subTest = f"{path} {method.upper()}"
                with self.subTest(subTest):
                    response = self.request(method, path)
                    expected_status_code, does_commit = self.anonymous_use_behavior.get(subTest, (status.HTTP_401_UNAUTHORIZED, False))
                    self.assertEqual(response.status_code, expected_status_code, response.json())
                    if does_commit:
                        expected_commits += 1
                    else:
                        expected_rollbacks += 1
                self.assert_commits_rollbacks(expected_commits, expected_rollbacks)

        self.expect_commits_rollbacks(expected_commits, expected_rollbacks)
