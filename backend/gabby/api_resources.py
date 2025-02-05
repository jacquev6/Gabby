from fastapi import HTTPException
from starlette import status

from . import deltas
from .api_models import PdfRectangle, Point, SyntheticError, Adaptation
from .exercises import Exercise, ExercisesResource
from .parsed_exercises import ParsedExercisesResource
from .pdfs import PdfFile, PdfFileNaming, PdfFilesResource, PdfFileNamingsResource
from .pings import PingsResource
from .projects import Project, ProjectsResource
from .testing import ApiTestCase, LoggedInApiTestCase
from .textbooks import Textbook, Section, TextbooksResource, SectionsResource
from .users import UsersResource
from .users.recovery import RecoveryEmailRequestsResource


class SyntheticErrorsResource:
    singular_name = "synthetic_error"
    plural_name = "synthetic_errors"

    Model = SyntheticError

    default_page_size = 1

    def get_item(self, id):
        raise HTTPException(status_code=int(id), detail="Synthetic error")


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
    ParsedExercisesResource(),
    SyntheticErrorsResource(),
]


polymorphism = {
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
        self.expect_one_more_commit()

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
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=16, number="11", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=17, number="13", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

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
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=16, number="11", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=17, number="13", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["included"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                        "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                        "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                    },
                },
            ],
        })

    def test_list(self):
        self.expect_commits_rollbacks(2, 0)

        textbook = self.create_model(Textbook, project=self.project, title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=12, number="4", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=13, number="5", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        textbook = self.create_model(Textbook, project=self.project, title="Another title", publisher="Another publisher", year=2024, isbn="9783161484101")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=14, number="6", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        textbook = self.create_model(Textbook, project=self.project, title="Yet another title", publisher="Yet another publisher", year=2025, isbn="9783161484102")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=15, number="7", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=16, number="8", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=17, number="9", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

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
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=12, number="4", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=13, number="5", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        textbook = self.create_model(Textbook, project=self.project, title="Another title", publisher="Another publisher", year=2024, isbn="9783161484101")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=14, number="6", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        textbook = self.create_model(Textbook, project=self.project, title="Yet another title", publisher="Yet another publisher", year=2025, isbn="9783161484102")
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=15, number="7", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=16, number="8", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=17, number="9", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["included"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "ojsbmy"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["included"][2]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][2]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["included"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "pkdksv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["included"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "pkdksv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["included"][2]["attributes"]["createdAt"],
                        "updatedAt": response.json()["included"][2]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "pkdksv"}},
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
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=12, number="4", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, textbook=textbook, project=textbook.project, textbook_page=13, number="5", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

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
                    "rectangles": [],
                    "instructions": [{"insert": "\n", "attributes": {}}],
                    "example": [{"insert": "\n", "attributes": {}}],
                    "clue": [{"insert": "\n", "attributes": {}}],
                    "wording": [{"insert": "\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
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
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "textbook": {"data": None},
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
        self.assertEqual(exercise.instructions, [deltas.InsertOp(insert="\n", attributes={})])
        self.assertEqual(exercise.example, [deltas.InsertOp(insert="\n", attributes={})])
        self.assertEqual(exercise.clue, [deltas.InsertOp(insert="\n", attributes={})])
        self.assertEqual(exercise.wording, [deltas.InsertOp(insert="\n", attributes={})])

    def test_create__minimal_in_textbook(self):
        payload = {
            "data": {
                "type": "exercise",
                "attributes": {
                    "textbookPage": 12, "number": "42",
                    "rectangles": [],
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
                    "rectangles": [],
                    "instructions": [{"insert": "\n", "attributes": {}}],
                    "example": [{"insert": "\n", "attributes": {}}],
                    "clue": [{"insert": "\n", "attributes": {}}],
                    "wording": [{"insert": "\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
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
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
        self.assertEqual(exercise.instructions, [deltas.InsertOp(insert="\n", attributes={})])
        self.assertEqual(exercise.example, [deltas.InsertOp(insert="\n", attributes={})])
        self.assertEqual(exercise.clue, [deltas.InsertOp(insert="\n", attributes={})])
        self.assertEqual(exercise.wording, [deltas.InsertOp(insert="\n", attributes={})])

    def test_create__full(self):
        payload = {
            "data": {
                "type": "exercise",
                "attributes": {
                    "textbookPage": 14, "number": "1",
                    "instructions": [{"insert": "instructions\n", "attributes": {}}],
                    "example": [{"insert": "example\n", "attributes": {}}],
                    "clue": [{"insert": "clue\n", "attributes": {}}],
                    "wording": [{"insert": "wording\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "adaptation": {
                        "kind": "generic",
                        "wording_paragraphs_per_pagelet": 2,
                        "single_item_per_paragraph": False,
                        "placeholder_for_fill_with_free_text": None,
                        "items": None,
                        "items_are_selectable": None,
                        "items_are_boxed": False,
                        "items_have_mcq_beside": False,
                        "items_have_mcq_below": False,
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                    "rectangles": [
                        {
                            "pdf_sha256": "sha256",
                            "pdf_page": 42,
                            "coordinates": "pdfjs",
                            "start": {"x": 10, "y": 20},
                            "stop": {"x": 30, "y": 40},
                            "text": "text",
                            "role": "instructions",
                        },
                    ],
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
                    "instructions": [{"insert": "instructions\n", "attributes": {}}],
                    "example": [{"insert": "example\n", "attributes": {}}],
                    "clue": [{"insert": "clue\n", "attributes": {}}],
                    "wording": [{"insert": "wording\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "adaptation": {
                        "kind": "generic",
                        "wording_paragraphs_per_pagelet": 2,
                        "single_item_per_paragraph": False,
                        "placeholder_for_fill_with_free_text": None,
                        "items": None,
                        "items_are_selectable": None,
                        "items_are_boxed": False,
                        "items_have_mcq_beside": False,
                        "items_have_mcq_below": False,
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                    "rectangles": [
                        {
                            "pdf_sha256": "sha256",  # @todo Rename to 'pdfSha256'
                            "pdf_page": 42,  # @todo Rename to 'pdfPage'
                            "coordinates": "pdfjs",
                            "start": {"x": 10, "y": 20},
                            "stop": {"x": 30, "y": 40},
                            "text": "text",
                            "role": "instructions",
                        },
                    ],
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
        self.assertEqual(exercise.number, "1")
        self.assertEqual(exercise.instructions, [deltas.InsertOp(insert="instructions\n", attributes={})])
        self.assertEqual(exercise.example, [deltas.InsertOp(insert="example\n", attributes={})])
        self.assertEqual(exercise.clue, [deltas.InsertOp(insert="clue\n", attributes={})])
        self.assertEqual(exercise.wording, [deltas.InsertOp(insert="wording\n", attributes={})])
        self.assertEqual(
            exercise.rectangles,
            [
                PdfRectangle(
                    pdf_sha256="sha256",
                    pdf_page=42,
                    coordinates="pdfjs",
                    start=Point(x=10, y=20),
                    stop=Point(x=30, y=40),
                    text="text",
                    role="instructions",
                ),
            ],
        )

    def test_get__no_include(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions=[deltas.InsertOp(insert="instructions\n", attributes={})],
            example=[deltas.InsertOp(insert="example\n", attributes={})],
            clue=[deltas.InsertOp(insert="clue\n", attributes={})],
            wording=[deltas.InsertOp(insert="wording\n", attributes={})],
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
                    "rectangles": [],
                    "instructions": [{"insert": "instructions\n", "attributes": {}}],
                    "example": [{"insert": "example\n", "attributes": {}}],
                    "clue": [{"insert": "clue\n", "attributes": {}}],
                    "wording": [{"insert": "wording\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
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
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
            instructions=[deltas.InsertOp(insert="instructions\n", attributes={})],
            example=[deltas.InsertOp(insert="example\n", attributes={})],
            clue=[deltas.InsertOp(insert="clue\n", attributes={})],
            wording=[deltas.InsertOp(insert="wording\n", attributes={})],
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
                    "rectangles": [],
                    "instructions": [{"insert": "instructions\n", "attributes": {}}],
                    "example": [{"insert": "example\n", "attributes": {}}],
                    "clue": [{"insert": "clue\n", "attributes": {}}],
                    "wording": [{"insert": "wording\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
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
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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

    def test_get__with_adaptation(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions=[deltas.InsertOp(insert="instructions\n", attributes={})],
            example=[deltas.InsertOp(insert="example\n", attributes={})],
            clue=[deltas.InsertOp(insert="clue\n", attributes={})],
            wording=[deltas.InsertOp(insert="wording\n", attributes={})],
            adaptation=Adaptation(
                kind="fill-with-free-text",
                wording_paragraphs_per_pagelet=None,
                single_item_per_paragraph=False,
                placeholder_for_fill_with_free_text="...",
                items=None,
                items_are_selectable=None,
                items_are_boxed=False,
                items_have_mcq_beside=False,
                items_have_mcq_below=False,
                show_arrow_before_mcq_fields=False,
                show_mcq_choices_by_default=False,
            ),
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
                    "rectangles": [],
                    "instructions": [{"insert": "instructions\n", "attributes": {}}],
                    "example": [{"insert": "example\n", "attributes": {}}],
                    "clue": [{"insert": "clue\n", "attributes": {}}],
                    "wording": [{"insert": "wording\n", "attributes": {}}],
                    "textReference": [{"insert": "\n", "attributes": {}}],
                    "adaptation": {
                        "kind": "fill-with-free-text",
                        "wording_paragraphs_per_pagelet": None,
                        "single_item_per_paragraph": False,
                        "placeholder_for_fill_with_free_text": "...",
                        "items": None,
                        "items_are_selectable": None,
                        "items_are_boxed": False,
                        "items_have_mcq_beside": False,
                        "items_have_mcq_below": False,
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
        })

    # @todo Add test_get__include_adaptation_exercise(self) with include=adaptation.exercise,
    # showing the exercise is not included again, because it's the main data

    def test_list__sorted_by_default(self):
        self.expect_commits_rollbacks(2, 0)

        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=16, number="11", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="3", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="4", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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

        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=16, number="11", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="3", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="4", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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

        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=16, number="11", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="13", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="14", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        other_textbook = self.create_model(Textbook, project=self.project, title="The other title")
        self.create_model(Exercise, project=other_textbook.project, textbook=other_textbook, textbook_page=12, number="4", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "ojsbmy"}},
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

        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=16, number="11", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="13", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=17, number="14", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        other_textbook = self.create_model(Textbook, project=self.project, title="The other title")
        self.create_model(Exercise, project=other_textbook.project, textbook=other_textbook, textbook_page=12, number="4", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)

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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][1]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][1]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
                        "rectangles": [],
                        "instructions": [{"insert": "\n", "attributes": {}}],
                        "example": [{"insert": "\n", "attributes": {}}],
                        "clue": [{"insert": "\n", "attributes": {}}],
                        "wording": [{"insert": "\n", "attributes": {}}],
                        "textReference": [{"insert": "\n", "attributes": {}}],
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
                            "show_arrow_before_mcq_fields": False,
                            "show_mcq_choices_by_default": False,
                        },
                        "createdAt": response.json()["data"][0]["attributes"]["createdAt"],
                        "updatedAt": response.json()["data"][0]["attributes"]["updatedAt"],
                    },
                    "relationships": {
                        "project": {"data": {"type": "project", "id": "xkopqm"}},
                        "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
            instructions=[deltas.InsertOp(insert="instructions\n", attributes={})],
            example=[deltas.InsertOp(insert="example\n", attributes={})],
            clue=[deltas.InsertOp(insert="clue\n", attributes={})],
            wording=[deltas.InsertOp(insert="wording\n", attributes={})],
            text_reference=[deltas.InsertOp(insert="reference\n", attributes={})],
            rectangles=[PdfRectangle(
                pdf_sha256="sha256",
                pdf_page=42,
                coordinates="pdfjs",
                start=Point(x=10, y=20),
                stop=Point(x=30, y=40),
                text="text",
                role="instructions",
            )],
        )
        self.assertEqual(self.count_models(Exercise), 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.project, self.project)
        self.assertEqual(exercise.textbook, self.textbook)
        self.assertEqual(exercise.textbook_page, 16)
        self.assertEqual(exercise.number, "11")
        self.assertEqual(exercise.instructions, [deltas.InsertOp(insert="instructions\n", attributes={})])
        self.assertEqual(exercise.example, [deltas.InsertOp(insert="example\n", attributes={})])
        self.assertEqual(exercise.clue, [deltas.InsertOp(insert="clue\n", attributes={})])
        self.assertEqual(exercise.wording, [deltas.InsertOp(insert="wording\n", attributes={})])
        self.assertEqual(exercise.text_reference, [deltas.InsertOp(insert="reference\n", attributes={})])
        self.assertEqual(
            exercise.rectangles,
            [
                PdfRectangle(
                    pdf_sha256="sha256",
                    pdf_page=42,
                    coordinates="pdfjs",
                    start=Point(x=10, y=20),
                    stop=Point(x=30, y=40),
                    text="text",
                    role="instructions",
                ),
            ],
        )

        payload = {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "attributes": {
                    "instructions": [{"insert": "INSTRUCTIONS\n", "attributes": {}}],
                    "example": [{"insert": "EXAMPLE\n", "attributes": {}}],
                    "clue": [{"insert": "CLUE\n", "attributes": {}}],
                    "wording": [{"insert": "WORDING\n", "attributes": {}}],
                    "textReference": [{"insert": "REFERENCE\n", "attributes": {}}],
                    "rectangles": [
                        {
                            "pdf_sha256": "sha256",
                            "pdf_page": 42,
                            "coordinates": "pdfjs",
                            "start": {"x": 10, "y": 20},
                            "stop": {"x": 30, "y": 40},
                            "text": "text",
                            "role": "instructions",
                        },
                        {
                            "pdf_sha256": "sha256",
                            "pdf_page": 42,
                            "coordinates": "pdfjs",
                            "start": {"x": 100, "y": 200},
                            "stop": {"x": 300, "y": 400},
                            "text": "text 2",
                            "role": "instructions",
                        },
                    ],
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
                    "instructions": [{"insert": "INSTRUCTIONS\n", "attributes": {}}],
                    "example": [{"insert": "EXAMPLE\n", "attributes": {}}],
                    "clue": [{"insert": "CLUE\n", "attributes": {}}],
                    "wording": [{"insert": "WORDING\n", "attributes": {}}],
                    "textReference": [{"insert": "REFERENCE\n", "attributes": {}}],
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
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                    "rectangles": [
                        {
                            "pdf_sha256": "sha256",  # @todo Rename to 'pdfSha256'
                            "pdf_page": 42,  # @todo Rename to 'pdfPage'
                            "coordinates": "pdfjs",
                            "start": {"x": 10, "y": 20},
                            "stop": {"x": 30, "y": 40},
                            "text": "text",
                            "role": "instructions",
                        },
                        {
                            "pdf_sha256": "sha256",
                            "pdf_page": 42,
                            "coordinates": "pdfjs",
                            "start": {"x": 100, "y": 200},
                            "stop": {"x": 300, "y": 400},
                            "text": "text 2",
                            "role": "instructions",
                        },
                    ],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
        self.assertEqual(exercise.instructions, [deltas.InsertOp(insert="INSTRUCTIONS\n", attributes={})])
        self.assertEqual(exercise.example, [deltas.InsertOp(insert="EXAMPLE\n", attributes={})])
        self.assertEqual(exercise.clue, [deltas.InsertOp(insert="CLUE\n", attributes={})])
        self.assertEqual(exercise.wording, [deltas.InsertOp(insert="WORDING\n", attributes={})])
        self.assertEqual(exercise.text_reference, [deltas.InsertOp(insert="REFERENCE\n", attributes={})])
        self.assertEqual(
            exercise.rectangles,
            [
                PdfRectangle(
                    pdf_sha256="sha256",
                    pdf_page=42,
                    coordinates="pdfjs",
                    start=Point(x=10, y=20),
                    stop=Point(x=30, y=40),
                    text="text",
                    role="instructions",
                ),
                PdfRectangle(
                    pdf_sha256="sha256",
                    pdf_page=42,
                    coordinates="pdfjs",
                    start=Point(x=100, y=200),
                    stop=Point(x=300, y=400),
                    text="text 2",
                    role="instructions",
                ),
            ],
        )

    def test_patch__partial(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions=[deltas.InsertOp(insert="instructions\n", attributes={})],
            example=[deltas.InsertOp(insert="example\n", attributes={})],
            clue=[deltas.InsertOp(insert="clue\n", attributes={})],
            wording=[deltas.InsertOp(insert="wording\n", attributes={})],
            text_reference=[deltas.InsertOp(insert="reference\n", attributes={})],
        )

        payload = {
            "data": {
                "type": "exercise",
                "id": "wbqloc",
                "attributes": {
                    "instructions": [{"insert": "INSTRUCTIONS\n", "attributes": {}}],
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
                    "rectangles": [],
                    "instructions": [{"insert": "INSTRUCTIONS\n", "attributes": {}}],
                    "example": [{"insert": "example\n", "attributes": {}}],
                    "clue": [{"insert": "clue\n", "attributes": {}}],
                    "wording": [{"insert": "wording\n", "attributes": {}}],
                    "textReference": [{"insert": "reference\n", "attributes": {}}],
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
                        "show_arrow_before_mcq_fields": False,
                        "show_mcq_choices_by_default": False,
                    },
                    "createdAt": response.json()["data"]["attributes"]["createdAt"],
                    "updatedAt": response.json()["data"]["attributes"]["updatedAt"],
                },
                "relationships": {
                    "project": {"data": {"type": "project", "id": "xkopqm"}},
                    "textbook": {"data": {"type": "textbook", "id": "klxufv"}},
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
        self.assertEqual(exercise.instructions, [deltas.InsertOp(insert="INSTRUCTIONS\n", attributes={})])
        self.assertEqual(exercise.example, [deltas.InsertOp(insert="example\n", attributes={})])
        self.assertEqual(exercise.clue, [deltas.InsertOp(insert="clue\n", attributes={})])
        self.assertEqual(exercise.wording, [deltas.InsertOp(insert="wording\n", attributes={})])
        self.assertEqual(exercise.text_reference, [deltas.InsertOp(insert="reference\n", attributes={})])

    def test_patch__read_only_project(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions=[deltas.InsertOp(insert="instructions\n", attributes={})],
            example=[deltas.InsertOp(insert="example\n", attributes={})],
            clue=[deltas.InsertOp(insert="clue\n", attributes={})],
            wording=[deltas.InsertOp(insert="wording\n", attributes={})],
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
        self.assertEqual(exercise.instructions, [deltas.InsertOp(insert="instructions\n", attributes={})])
        self.assertEqual(exercise.example, [deltas.InsertOp(insert="example\n", attributes={})])
        self.assertEqual(exercise.clue, [deltas.InsertOp(insert="clue\n", attributes={})])
        self.assertEqual(exercise.wording, [deltas.InsertOp(insert="wording\n", attributes={})])

    def test_patch__read_only_textbook(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions=[deltas.InsertOp(insert="instructions\n", attributes={})],
            example=[deltas.InsertOp(insert="example\n", attributes={})],
            clue=[deltas.InsertOp(insert="clue\n", attributes={})],
            wording=[deltas.InsertOp(insert="wording\n", attributes={})],
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
        self.assertEqual(exercise.instructions, [deltas.InsertOp(insert="instructions\n", attributes={})])
        self.assertEqual(exercise.example, [deltas.InsertOp(insert="example\n", attributes={})])
        self.assertEqual(exercise.clue, [deltas.InsertOp(insert="clue\n", attributes={})])
        self.assertEqual(exercise.wording, [deltas.InsertOp(insert="wording\n", attributes={})])

    def test_patch__read_only_page(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions=[deltas.InsertOp(insert="instructions\n", attributes={})],
            example=[deltas.InsertOp(insert="example\n", attributes={})],
            clue=[deltas.InsertOp(insert="clue\n", attributes={})],
            wording=[deltas.InsertOp(insert="wording\n", attributes={})],
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
        self.assertEqual(exercise.instructions, [deltas.InsertOp(insert="instructions\n", attributes={})])
        self.assertEqual(exercise.example, [deltas.InsertOp(insert="example\n", attributes={})])
        self.assertEqual(exercise.clue, [deltas.InsertOp(insert="clue\n", attributes={})])
        self.assertEqual(exercise.wording, [deltas.InsertOp(insert="wording\n", attributes={})])

    def test_patch__read_only_number(self):
        self.create_model(
            Exercise,
            textbook=self.textbook,
            project=self.textbook.project,
            textbook_page=16,
            number="11",
            instructions=[deltas.InsertOp(insert="instructions\n", attributes={})],
            example=[deltas.InsertOp(insert="example\n", attributes={})],
            clue=[deltas.InsertOp(insert="clue\n", attributes={})],
            wording=[deltas.InsertOp(insert="wording\n", attributes={})],
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
        self.assertEqual(exercise.instructions, [deltas.InsertOp(insert="instructions\n", attributes={})])
        self.assertEqual(exercise.example, [deltas.InsertOp(insert="example\n", attributes={})])
        self.assertEqual(exercise.clue, [deltas.InsertOp(insert="clue\n", attributes={})])
        self.assertEqual(exercise.wording, [deltas.InsertOp(insert="wording\n", attributes={})])

    def test_delete(self):
        self.create_model(Exercise, project=self.textbook.project, textbook=self.textbook, textbook_page=16, number="11", instructions=deltas.empty, wording=deltas.empty, example=deltas.empty, clue=deltas.empty)
        self.assertEqual(self.count_models(Exercise), 1)

        response = self.delete("http://server/exercises/wbqloc")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")

        self.assertEqual(self.count_models(Exercise), 0)


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

    def test_create_two_textbooks_with_same_pdf__pdf_first(self):
        project = self.create_model(Project, title="The project", description="Description")
        textbook = self.create_model(Textbook, project=project, title="First textbook")
        pdfFile = self.create_model(PdfFile, sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c", bytes_count=0, pages_count=2)
        self.create_model(PdfFileNaming, name="test.pdf", pdf_file=pdfFile)
        self.create_model(Section, pdf_file_start_page=1, pages_count=2, textbook_start_page=1, pdf_file=pdfFile, textbook=textbook)

        payload = {
            "atomic:operations": [
                {"op":"add","data":{"type":"pdfFile","lid":"pdf","attributes":{"sha256":"f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c","bytesCount":0,"pagesCount":2},"relationships":{}}},
                {"op":"add","data":{"type":"pdfFileNaming","attributes":{"name":"test.pdf"},"relationships":{"pdfFile":{"data":{"type":"pdfFile","lid":"pdf"}}}}},
                {"op":"add","data":{"type":"textbook","lid":"tb","attributes":{"title":"Second textbook"},"relationships":{"project":{"data":{"type":"project","id":"xkopqm"}}}}},
                {"op":"add","data":{"type":"section","attributes":{"pdfFileStartPage":1,"pagesCount":2,"textbookStartPage":1},"relationships":{"pdfFile":{"data":{"type":"pdfFile","lid":"pdf"}},"textbook":{"data":{"type":"textbook","lid":"tb"}}}}},
            ],
        }
        response = self.post("http://server/batch", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        self.assertEqual(self.count_models(Textbook), 2)
        self.assertEqual(self.count_models(PdfFile), 1)
        self.assertEqual(self.count_models(PdfFileNaming), 2)
        self.assertEqual(self.count_models(Section), 2)

    def test_create_two_textbooks_with_same_pdf__textbook_first(self):
        project = self.create_model(Project, title="The project", description="Description")
        textbook = self.create_model(Textbook, project=project, title="First textbook")
        pdfFile = self.create_model(PdfFile, sha256="f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c", bytes_count=0, pages_count=2)
        self.create_model(PdfFileNaming, name="test.pdf", pdf_file=pdfFile)
        self.create_model(Section, pdf_file_start_page=1, pages_count=2, textbook_start_page=1, pdf_file=pdfFile, textbook=textbook)

        payload = {
            "atomic:operations": [
                {"op":"add","data":{"type":"textbook","lid":"tb","attributes":{"title":"Second textbook"},"relationships":{"project":{"data":{"type":"project","id":"xkopqm"}}}}},
                {"op":"add","data":{"type":"pdfFile","lid":"pdf","attributes":{"sha256":"f8e399a0130a4ec30821821664972e7ad3cf94bc7335db13c1d381494427707c","bytesCount":0,"pagesCount":2},"relationships":{}}},
                {"op":"add","data":{"type":"pdfFileNaming","attributes":{"name":"test.pdf"},"relationships":{"pdfFile":{"data":{"type":"pdfFile","lid":"pdf"}}}}},
                {"op":"add","data":{"type":"section","attributes":{"pdfFileStartPage":1,"pagesCount":2,"textbookStartPage":1},"relationships":{"pdfFile":{"data":{"type":"pdfFile","lid":"pdf"}},"textbook":{"data":{"type":"textbook","lid":"tb"}}}}},
            ],
        }
        # There was a bug where this request got a 400 claiming that the section's textbook was null.
        # This was due to the rollback in the PdfsResource it failed to add the PDF: that rollback also rollbacked the addition of the textbook.
        # This was fixed by using a nested transaction in the PdfsResource.
        response = self.post("http://server/batch", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

        self.assertEqual(self.count_models(Textbook), 2)
        self.assertEqual(self.count_models(PdfFile), 1)
        self.assertEqual(self.count_models(PdfFileNaming), 2)
        self.assertEqual(self.count_models(Section), 2)


class UnauthenticatedUseApiTestCase(ApiTestCase):
    resources = resources
    polymorphism = polymorphism

    anonymous_use_behavior = {
        # We'd prefer if none of these would commit, but that's a quest for another day.
        "/pings GET": (status.HTTP_200_OK, True, False),
        "/pings POST": (status.HTTP_422_UNPROCESSABLE_ENTITY, True, False),
        "/pings/404 DELETE": (status.HTTP_404_NOT_FOUND, False, True),
        "/pings/404 GET": (status.HTTP_404_NOT_FOUND, False, True),
        "/pings/404 PATCH": (status.HTTP_422_UNPROCESSABLE_ENTITY, True, False),
        "/recoveryEmailRequests POST": (status.HTTP_422_UNPROCESSABLE_ENTITY, True, False),
        "/token POST": (status.HTTP_422_UNPROCESSABLE_ENTITY, True, False),
        "/syntheticErrors/404 GET": (status.HTTP_404_NOT_FOUND, False, False),
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
            path = path.replace("{id}", "404")
            for method in operations.keys():
                subTest = f"{path} {method.upper()}"
                with self.subTest(subTest):
                    response = self.request(method, path)
                    expected_status_code, does_commit, does_rollback = self.anonymous_use_behavior.get(subTest, (status.HTTP_401_UNAUTHORIZED, False, True))
                    self.assertEqual(response.status_code, expected_status_code, response.json())
                    if does_commit:
                        expected_commits += 1
                    if does_rollback:
                        expected_rollbacks += 1
                self.assert_commits_rollbacks(expected_commits, expected_rollbacks)

        self.expect_commits_rollbacks(expected_commits, expected_rollbacks)
