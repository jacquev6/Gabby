from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from .models import PdfFile, Textbook, Section, Exercise


class PdfFileTests(APITransactionTestCase):
    maxDiff = None
    reset_sequences = True  # Primary keys appear in API responses

    def test_create(self):
        payload = {
            "data": {
                "type": "pdfFile",
                "attributes": {
                    "sha256": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                    "bytesCount": 123456789, "pagesCount": 42,
                },
                "relationships": {"namings": {"data": []}, "sections": {"data": []}},
            },
        }
        response = self.client.post(reverse("pdffile-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "pdfFile",
                "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                "links": {"self": "http://testserver/api/pdfFiles/87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                "attributes": {
                    "sha256": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                    "bytesCount": 123456789, "pagesCount": 42,
                },
                "relationships": {
                    "sections": {"data": [], "meta": {"count": 0}},
                    "namings": {"data": [], "meta": {"count": 0}},
                },
            },
        })

        self.assertEqual(PdfFile.objects.count(), 1)
        pdf_file = PdfFile.objects.get()
        self.assertEqual(pdf_file.sha256, "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7")
        self.assertEqual(pdf_file.bytes_count, 123456789)
        self.assertEqual(pdf_file.pages_count, 42)

    def test_create__short_sha256(self):
        payload = {
            "data": {
                "type": "pdfFile",
                "attributes": {
                    "sha256": "0263829989b6fd954f7",
                    "bytesCount": 123456789, "pagesCount": 42,
                },
                "relationships": {"namings": {"data": []}, "sections": {"data": []}},
            },
        }
        response = self.client.post(reverse("pdffile-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
        self.assertEqual(response.json(), {"errors": [{"code": "invalid",
             "detail": "Enter a valid value.",
             "source": {"pointer": "/data/attributes/sha256"},
             "status": "400"}
        ]})

        self.assertEqual(PdfFile.objects.count(), 0)

    def test_create__bad_sha256(self):
        payload = {
            "data": {
                "type": "pdfFile",
                "attributes": {
                    "sha256": "0263829989b6fd954f72baaf2fc64bc2e2f01d692d4de72986ea808f6e99813x",
                    "bytesCount": 123456789, "pagesCount": 42,
                },
                "relationships": {"namings": {"data": []}, "sections": {"data": []}},
            },
        }
        response = self.client.post(reverse("pdffile-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
        self.assertEqual(response.json(), {"errors": [{"code": "invalid",
             "detail": "Enter a valid value.",
             "source": {"pointer": "/data/attributes/sha256"},
             "status": "400"}
        ]})

        self.assertEqual(Exercise.objects.count(), 0)

    def test_get(self):
        pdf_file = PdfFile.objects.create(sha256="87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7", bytes_count=123456789, pages_count=42)
        pdf_file.namings.create(name="amazing.pdf")

        response = self.client.get(reverse("pdffile-detail", args=["87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"]), format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "pdfFile",
                "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                "links": {"self": "http://testserver/api/pdfFiles/87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                "attributes": {
                    "sha256": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                    "bytesCount": 123456789, "pagesCount": 42,
                },
                "relationships": {
                    "namings": {"data": [{"type": "pdfFileNaming", "id": "1"}], "meta": {"count": 1}},
                    "sections": {"data": [], "meta": {"count": 0}},
                },
            },
        })

    def test_get__include_namings(self):
        pdf_file = PdfFile.objects.create(sha256="87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7", bytes_count=123456789, pages_count=42)
        pdf_file.namings.create(name="amazing.pdf")
        pdf_file.namings.create(name="alias.pdf")

        response = self.client.get(reverse("pdffile-detail", args=["87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"]), format="vnd.api+json", QUERY_STRING="include=namings")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "pdfFile",
                "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                "links": {"self": "http://testserver/api/pdfFiles/87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                "attributes": {
                    "sha256": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
                    "bytesCount": 123456789, "pagesCount": 42,
                },
                "relationships": {
                    "namings": {
                        "data": [
                            {"type": "pdfFileNaming", "id": "1"},
                            {"type": "pdfFileNaming", "id": "2"},
                        ],
                        "meta": {"count": 2},
                    },
                    "sections": {"data": [], "meta": {"count": 0}},
                },
            },
            "included": [
                {
                    "type": "pdfFileNaming",
                    "id": "1",
                    "links": {"self": "http://testserver/api/pdfFileNamings/1"},
                    "attributes": {
                        "name": "amazing.pdf",
                    },
                    "relationships": {
                        "pdfFile": {
                            "data": {"type": "pdfFile", "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                        },
                    },
                },
                {
                    "type": "pdfFileNaming",
                    "id": "2",
                    "links": {"self": "http://testserver/api/pdfFileNamings/2"},
                    "attributes": {
                        "name": "alias.pdf",
                    },
                    "relationships": {
                        "pdfFile": {
                            "data": {"type": "pdfFile", "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                        },
                    },
                },
            ],
        })


class TextbookTests(APITransactionTestCase):
    maxDiff = None
    reset_sequences = True

    def test_create__minimal(self):
        payload = {
            "data": {
                "type": "textbook",
                "attributes": {
                    "title": "The title",
                },
                "relationships": {"exercises": {"data": []}, "sections": {"data": []}},
            },
        }
        response = self.client.post(reverse("textbook-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "1",
                "links": {"self": "http://testserver/api/textbooks/1"},
                "attributes": {
                    "title": "The title",
                    "publisher": None, "year": None, "isbn": None,
                },
                "relationships": {
                    "exercises": {"data": [], "meta": {"count": 0}},
                    "sections": {"data": [], "meta": {"count": 0}},
                },
            },
        })

        self.assertEqual(Textbook.objects.count(), 1)
        textbook = Textbook.objects.get()
        self.assertEqual(textbook.id, 1)
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
                "relationships": {"exercises": {"data": []}, "sections": {"data": []}},
            },
        }
        response = self.client.post(reverse("textbook-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "1",
                "links": {"self": "http://testserver/api/textbooks/1"},
                "attributes": {
                    "title": "The title",
                    "publisher": "The publisher",
                    "year": 2023,
                    "isbn": "9783161484100",
                },
                "relationships": {
                    "exercises": {"data": [], "meta": {"count": 0}},
                    "sections": {"data": [], "meta": {"count": 0}},
                },
            },
        })

        self.assertEqual(Textbook.objects.count(), 1)
        textbook = Textbook.objects.get()
        self.assertEqual(textbook.id, 1)
        self.assertEqual(textbook.title, "The title")
        self.assertEqual(textbook.publisher, "The publisher")
        self.assertEqual(textbook.year, 2023)
        self.assertEqual(textbook.isbn, "9783161484100")

    def test_get(self):
        textbook = Textbook.objects.create(title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        textbook.exercises.create(page=16, number=11)
        textbook.exercises.create(page=17, number=13)

        response = self.client.get(reverse("textbook-detail", args=[1]), format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "1",
                "links": {"self": "http://testserver/api/textbooks/1"},
                "attributes": {
                    "title": "The title",
                    "publisher": "The publisher",
                    "year": 2023,
                    "isbn": "9783161484100",
                },
                "relationships": {
                    "exercises": {
                        "data": [
                            {"type": "exercise", "id": "1"},
                            {"type": "exercise", "id": "2"},
                        ],
                        "meta": {"count": 2},
                    },
                    "sections": {"data": [], "meta": {"count": 0}},
                },
            },
        })

    def test_get__include_exercises(self):
        textbook = Textbook.objects.create(title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        textbook.exercises.create(page=16, number=11)
        textbook.exercises.create(page=17, number=13)

        response = self.client.get(reverse("textbook-detail", args=[1]), format="vnd.api+json", QUERY_STRING="include=exercises")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "1",
                "links": {"self": "http://testserver/api/textbooks/1"},
                "attributes": {
                    "title": "The title",
                    "publisher": "The publisher",
                    "year": 2023,
                    "isbn": "9783161484100",
                },
                "relationships": {
                    "exercises": {
                        "data": [
                            {"type": "exercise", "id": "1"},
                            {"type": "exercise", "id": "2"},
                        ],
                        "meta": {"count": 2},
                    },
                    "sections": {"data": [], "meta": {"count": 0}},
                },
            },
            "included": [
                {
                    "type": "exercise",
                    "id": "1",
                    "links": {"self": "http://testserver/api/exercises/1"},
                    "attributes": {
                        "page": 16, "number": 11,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "2",
                    "links": {"self": "http://testserver/api/exercises/2"},
                    "attributes": {
                        "page": 17, "number": 13,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
            ],
        })

    def test_get__omit_relationships(self):
        textbook = Textbook.objects.create(title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        textbook.exercises.create(page=16, number=11)
        textbook.exercises.create(page=17, number=13)

        response = self.client.get(reverse("textbook-detail", args=[1]), format="vnd.api+json", QUERY_STRING="fields[textbook]=title,publisher,year,isbn")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "1",
                "links": {"self": "http://testserver/api/textbooks/1"},
                "attributes": {
                    "title": "The title",
                    "publisher": "The publisher",
                    "year": 2023,
                    "isbn": "9783161484100",
                },
            },
        })

    def test_list(self):
        textbook = Textbook.objects.create(title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        textbook.exercises.create(page=12, number=4)
        textbook.exercises.create(page=13, number=5)
        textbook = Textbook.objects.create(title="Another title", publisher="Another publisher", year=2024, isbn="9783161484101")
        textbook.exercises.create(page=14, number=6)
        textbook = Textbook.objects.create(title="Yet another title", publisher="Yet another publisher", year=2025, isbn="9783161484102")
        textbook.exercises.create(page=15, number=7)
        textbook.exercises.create(page=16, number=8)
        textbook.exercises.create(page=17, number=9)

        response = self.client.get(reverse("textbook-list"), format="vnd.api+json", QUERY_STRING="sort=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "textbook",
                    "id": "2",
                    "links": {"self": "http://testserver/api/textbooks/2"},
                    "attributes": {
                        "title": "Another title",
                        "publisher": "Another publisher",
                        "year": 2024,
                        "isbn": "9783161484101",
                    },
                    "relationships": {
                        "exercises": {"data": [{"type": "exercise", "id": "3"}], "meta": {"count": 1}},
                        "sections": {"data": [], "meta": {"count": 0}},
                    },
                },
                {
                    "type": "textbook",
                    "id": "1",
                    "links": {"self": "http://testserver/api/textbooks/1"},
                    "attributes": {
                        "title": "The title",
                        "publisher": "The publisher",
                        "year": 2023,
                        "isbn": "9783161484100",
                    },
                    "relationships": {
                        "exercises": {"data": [{"type": "exercise", "id": "1"}, {"type": "exercise", "id": "2"}], "meta": {"count": 2}},
                        "sections": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/textbooks?page%5Bnumber%5D=1&sort=title",
                "last": "http://testserver/api/textbooks?page%5Bnumber%5D=2&sort=title",
                "next": "http://testserver/api/textbooks?page%5Bnumber%5D=2&sort=title",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.client.get(reverse("textbook-list"), format="vnd.api+json", QUERY_STRING="page[number]=2&sort=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "textbook",
                    "id": "3",
                    "links": {"self": "http://testserver/api/textbooks/3"},
                    "attributes": {
                        "title": "Yet another title",
                        "publisher": "Yet another publisher",
                        "year": 2025,
                        "isbn": "9783161484102",
                    },
                    "relationships": {
                        "exercises": {"data": [{"type": "exercise", "id": "4"}, {"type": "exercise", "id": "5"}, {"type": "exercise", "id": "6"}], "meta": {"count": 3}},
                        "sections": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/textbooks?page%5Bnumber%5D=1&sort=title",
                "last": "http://testserver/api/textbooks?page%5Bnumber%5D=2&sort=title",
                "next": None,
                "prev": "http://testserver/api/textbooks?page%5Bnumber%5D=1&sort=title",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_list__include_exercises(self):
        textbook = Textbook.objects.create(title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        textbook.exercises.create(page=12, number=4)
        textbook.exercises.create(page=13, number=5)
        textbook = Textbook.objects.create(title="Another title", publisher="Another publisher", year=2024, isbn="9783161484101")
        textbook.exercises.create(page=14, number=6)
        textbook = Textbook.objects.create(title="Yet another title", publisher="Yet another publisher", year=2025, isbn="9783161484102")
        textbook.exercises.create(page=15, number=7)
        textbook.exercises.create(page=16, number=8)
        textbook.exercises.create(page=17, number=9)

        response = self.client.get(reverse("textbook-list"), format="vnd.api+json", QUERY_STRING="include=exercises&sort=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "textbook",
                    "id": "2",
                    "links": {"self": "http://testserver/api/textbooks/2"},
                    "attributes": {
                        "title": "Another title",
                        "publisher": "Another publisher",
                        "year": 2024,
                        "isbn": "9783161484101",
                    },
                    "relationships": {
                        "exercises": {"data": [{"type": "exercise", "id": "3"}], "meta": {"count": 1}},
                        "sections": {"data": [], "meta": {"count": 0}},
                    },
                },
                {
                    "type": "textbook",
                    "id": "1",
                    "links": {"self": "http://testserver/api/textbooks/1"},
                    "attributes": {
                        "title": "The title",
                        "publisher": "The publisher",
                        "year": 2023,
                        "isbn": "9783161484100",
                    },
                    "relationships": {
                        "exercises": {"data": [{"type": "exercise", "id": "1"}, {"type": "exercise", "id": "2"}], "meta": {"count": 2}},
                        "sections": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "included": [
                {
                    "type": "exercise",
                    "id": "1",
                    "attributes": {
                        "page": 12, "number": 4,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"id": "1", "type": "textbook"}},
                    },
                    "links": {"self": "http://testserver/api/exercises/1"},
                },
                {
                    "type": "exercise",
                    "id": "2",
                    "attributes": {
                        "page": 13, "number": 5,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"id": "1", "type": "textbook"}},
                    },
                    "links": {"self": "http://testserver/api/exercises/2"},
                },
                {
                    "type": "exercise",
                    "id": "3",
                    "attributes": {
                        "page": 14, "number": 6,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"id": "2", "type": "textbook"}},
                    },
                    "links": {"self": "http://testserver/api/exercises/3"},
                },
            ],
            "links": {
                "first": "http://testserver/api/textbooks?include=exercises&page%5Bnumber%5D=1&sort=title",
                "last": "http://testserver/api/textbooks?include=exercises&page%5Bnumber%5D=2&sort=title",
                "next": "http://testserver/api/textbooks?include=exercises&page%5Bnumber%5D=2&sort=title",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.client.get(reverse("textbook-list"), format="vnd.api+json", QUERY_STRING="include=exercises&page[number]=2&sort=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "textbook",
                    "id": "3",
                    "links": {"self": "http://testserver/api/textbooks/3"},
                    "attributes": {
                        "title": "Yet another title",
                        "publisher": "Yet another publisher",
                        "year": 2025,
                        "isbn": "9783161484102",
                    },
                    "relationships": {
                        "exercises": {"data": [{"type": "exercise", "id": "4"}, {"type": "exercise", "id": "5"}, {"type": "exercise", "id": "6"}], "meta": {"count": 3}},
                        "sections": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "included": [
                {
                    "type": "exercise",
                    "id": "4",
                    "attributes": {
                        "page": 15, "number": 7,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"id": "3", "type": "textbook"}},
                    },
                    "links": {"self": "http://testserver/api/exercises/4"},
                },
                {
                    "type": "exercise",
                    "id": "5",
                    "attributes": {
                        "page": 16, "number": 8,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"id": "3", "type": "textbook"}},
                    },
                    "links": {"self": "http://testserver/api/exercises/5"},
                },
                {
                    "type": "exercise",
                    "id": "6",
                    "attributes": {
                        "page": 17, "number": 9,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"id": "3", "type": "textbook"}},
                    },
                    "links": {"self": "http://testserver/api/exercises/6"},
                },
            ],
            "links": {
                "first": "http://testserver/api/textbooks?include=exercises&page%5Bnumber%5D=1&sort=title",
                "last": "http://testserver/api/textbooks?include=exercises&page%5Bnumber%5D=2&sort=title",
                "next": None,
                "prev": "http://testserver/api/textbooks?include=exercises&page%5Bnumber%5D=1&sort=title",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_list__omit_relationships(self):
        textbook = Textbook.objects.create(title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
        textbook.exercises.create(page=12, number=4)
        textbook.exercises.create(page=13, number=5)
        textbook = Textbook.objects.create(title="Another title", publisher="Another publisher", year=2024, isbn="9783161484101")
        textbook.exercises.create(page=14, number=6)
        textbook = Textbook.objects.create(title="Yet another title", publisher="Yet another publisher", year=2025, isbn="9783161484102")
        textbook.exercises.create(page=15, number=7)
        textbook.exercises.create(page=16, number=8)
        textbook.exercises.create(page=17, number=9)

        response = self.client.get(reverse("textbook-list"), format="vnd.api+json", QUERY_STRING="fields[textbook]=title,publisher,year,isbn&sort=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "textbook",
                    "id": "2",
                    "links": {"self": "http://testserver/api/textbooks/2"},
                    "attributes": {
                        "title": "Another title",
                        "publisher": "Another publisher",
                        "year": 2024,
                        "isbn": "9783161484101",
                    },
                },
                {
                    "type": "textbook",
                    "id": "1",
                    "links": {"self": "http://testserver/api/textbooks/1"},
                    "attributes": {
                        "title": "The title",
                        "publisher": "The publisher",
                        "year": 2023,
                        "isbn": "9783161484100",
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/textbooks?fields%5Btextbook%5D=title%2Cpublisher%2Cyear%2Cisbn&page%5Bnumber%5D=1&sort=title",
                "last": "http://testserver/api/textbooks?fields%5Btextbook%5D=title%2Cpublisher%2Cyear%2Cisbn&page%5Bnumber%5D=2&sort=title",
                "next": "http://testserver/api/textbooks?fields%5Btextbook%5D=title%2Cpublisher%2Cyear%2Cisbn&page%5Bnumber%5D=2&sort=title",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.client.get(reverse("textbook-list"), format="vnd.api+json", QUERY_STRING="fields[textbook]=title,publisher,year,isbn&page[number]=2&sort=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "textbook",
                    "id": "3",
                    "links": {"self": "http://testserver/api/textbooks/3"},
                    "attributes": {
                        "title": "Yet another title",
                        "publisher": "Yet another publisher",
                        "year": 2025,
                        "isbn": "9783161484102",
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/textbooks?fields%5Btextbook%5D=title%2Cpublisher%2Cyear%2Cisbn&page%5Bnumber%5D=1&sort=title",
                "last": "http://testserver/api/textbooks?fields%5Btextbook%5D=title%2Cpublisher%2Cyear%2Cisbn&page%5Bnumber%5D=2&sort=title",
                "next": None,
                "prev": "http://testserver/api/textbooks?fields%5Btextbook%5D=title%2Cpublisher%2Cyear%2Cisbn&page%5Bnumber%5D=1&sort=title",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_patch__full(self):
        Textbook.objects.create(title="The title", publisher="The publisher", year=2023, isbn="9783161484100")

        payload = {
            "data": {
                "type": "textbook",
                "id": "1",
                "attributes": {
                    "title": "The new title",
                    "publisher": "The new publisher",
                    "year": 2024,
                    "isbn": "9783161484101",
                },
            },
        }
        response = self.client.patch(reverse("textbook-detail", args=[1]), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "1",
                "links": {"self": "http://testserver/api/textbooks/1"},
                "attributes": {
                    "title": "The new title",
                    "publisher": "The new publisher",
                    "year": 2024,
                    "isbn": "9783161484101",
                },
                "relationships": {
                    "exercises": {"data": [], "meta": {"count": 0}},
                    "sections": {"data": [], "meta": {"count": 0}},
                },
            },
        })

        self.assertEqual(Textbook.objects.count(), 1)
        textbook = Textbook.objects.get()
        self.assertEqual(textbook.id, 1)
        self.assertEqual(textbook.title, "The new title")
        self.assertEqual(textbook.publisher, "The new publisher")
        self.assertEqual(textbook.year, 2024)
        self.assertEqual(textbook.isbn, "9783161484101")

    def test_patch__partial(self):
        Textbook.objects.create(title="The title", publisher="The publisher", year=2023, isbn="9783161484100")

        payload = {
            "data": {
                "type": "textbook",
                "id": "1",
                "attributes": {
                    "title": "The new title",
                    "year": None,
                },
            },
        }
        response = self.client.patch(reverse("textbook-detail", args=[1]), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "textbook",
                "id": "1",
                "links": {"self": "http://testserver/api/textbooks/1"},
                "attributes": {
                    "title": "The new title",
                    "publisher": "The publisher",
                    "year": None,
                    "isbn": "9783161484100",
                },
                "relationships": {
                    "exercises": {"data": [], "meta": {"count": 0}},
                    "sections": {"data": [], "meta": {"count": 0}},
                },
            },
        })

        self.assertEqual(Textbook.objects.count(), 1)
        textbook = Textbook.objects.get()
        self.assertEqual(textbook.id, 1)
        self.assertEqual(textbook.title, "The new title")
        self.assertEqual(textbook.publisher, "The publisher")
        self.assertIsNone(textbook.year)
        self.assertEqual(textbook.isbn, "9783161484100")

    def test_delete__without_exercises(self):
        Textbook.objects.create(title="The title", publisher="The publisher", year=2023, isbn="9783161484100")

        response = self.client.delete(reverse("textbook-detail", args=[1]), format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Textbook.objects.count(), 0)

    # @todo(Feature, now) Catch the exception and enable this test
    # def test_delete__with_exercises(self):
    #     textbook = Textbook.objects.create(title="The title", publisher="The publisher", year=2023, isbn="9783161484100")
    #     textbook.exercises.create(page=16, number=11)
    #     textbook.exercises.create(page=17, number=13)

    #     response = self.client.delete(reverse("textbook-detail", args=[1]), format="vnd.api+json")
    #     self.assertEqual(response.status_code, status.HTTP_409_CONFLICT, response.json())
    #     self.assertEqual(Textbook.objects.count(), 1)
    #     self.assertEqual(Exercise.objects.count(), 2)


class ExerciseTests(APITransactionTestCase):
    maxDiff = None
    reset_sequences = True

    def setUp(self):
        self.textbook = Textbook.objects.create(title="The title")

    def test_create__minimal(self):
        payload = {
            "data": {
                "type": "exercise",
                "attributes": {
                    "page": 12, "number": 42,
                },
                "relationships": {
                    "extractionEvents": {"data": []},
                    "textbook": {"data": {"type": "textbook", "id": "1"}},
                },
            },
        }
        response = self.client.post(reverse("exercise-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "links": {"self": "http://testserver/api/exercises/1"},
                "attributes": {
                    "page": 12, "number": 42,
                    "instructions": "", "example": "", "clue": "", "wording": "",
                },
                "relationships": {
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {
                        "data": {
                            "type": "textbook",
                            "id": "1",
                        },
                    },
                },
            },
        })

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.textbook.id, 1)
        self.assertEqual(exercise.page, 12)
        self.assertEqual(exercise.number, 42)
        self.assertEqual(exercise.instructions, "")
        self.assertEqual(exercise.example, "")
        self.assertEqual(exercise.clue, "")
        self.assertEqual(exercise.wording, "")

    def test_create__full(self):
        payload = {
            "data": {
                "type": "exercise",
                "attributes": {
                    "page": 14, "number": 1,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                },
                "relationships": {
                    "extractionEvents": {"data": []},
                    "textbook": {"data": {"type": "textbook", "id": "1"}},
                },
            },
        }
        response = self.client.post(reverse("exercise-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "links": {"self": "http://testserver/api/exercises/1"},
                "attributes": {
                    "page": 14, "number": 1,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                },
                "relationships": {
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {
                        "data": {
                            "type": "textbook",
                            "id": "1",
                        },
                    },
                },
            },
        })

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.textbook.id, 1)
        self.assertEqual(exercise.page, 14)
        self.assertEqual(exercise.number, 1)
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_get(self):
        self.textbook.exercises.create(
            page=16,
            number=11,
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        response = self.client.get(reverse("exercise-detail", args=[1]), format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "links": {"self": "http://testserver/api/exercises/1"},
                "attributes": {
                    "page": 16, "number": 11,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                },
                "relationships": {
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "1"}},
                },
            },
        })

    def test_get__include_textbook(self):
        self.textbook.exercises.create(
            page=16,
            number=11,
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        response = self.client.get(reverse("exercise-detail", args=[1]), format="vnd.api+json", QUERY_STRING="include=textbook")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "links": {"self": "http://testserver/api/exercises/1"},
                "attributes": {
                    "page": 16, "number": 11,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                },
                "relationships": {
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "1"}},
                },
            },
            "included": [
                {
                    "type": "textbook",
                    "id": "1",
                    "links": {"self": "http://testserver/api/textbooks/1"},
                    "attributes": {
                        "title": "The title",
                        "publisher": None, "year": None, "isbn": None,
                    },
                    "relationships": {
                        "exercises": {"data": [{"type": "exercise", "id": "1"}], "meta": {"count": 1}},
                        "sections": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
        })

    def test_list(self):
        self.textbook.exercises.create(page=16, number=11)
        self.textbook.exercises.create(page=17, number=13)
        self.textbook.exercises.create(page=17, number=14)

        response = self.client.get(reverse("exercise-list"), format="vnd.api+json", QUERY_STRING="sort=textbook,page,number")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "1",
                    "links": {"self": "http://testserver/api/exercises/1"},
                    "attributes": {
                        "page": 16, "number": 11,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "2",
                    "links": {"self": "http://testserver/api/exercises/2"},
                    "attributes": {
                        "page": 17, "number": 13,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/exercises?page%5Bnumber%5D=1&sort=textbook%2Cpage%2Cnumber",
                "last": "http://testserver/api/exercises?page%5Bnumber%5D=2&sort=textbook%2Cpage%2Cnumber",
                "next": "http://testserver/api/exercises?page%5Bnumber%5D=2&sort=textbook%2Cpage%2Cnumber",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.client.get(reverse("exercise-list"), format="vnd.api+json", QUERY_STRING="page[number]=2&sort=textbook,page,number")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "3",
                    "links": {"self": "http://testserver/api/exercises/3"},
                    "attributes": {
                        "page": 17, "number": 14,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/exercises?page%5Bnumber%5D=1&sort=textbook%2Cpage%2Cnumber",
                "last": "http://testserver/api/exercises?page%5Bnumber%5D=2&sort=textbook%2Cpage%2Cnumber",
                "next": None,
                "prev": "http://testserver/api/exercises?page%5Bnumber%5D=1&sort=textbook%2Cpage%2Cnumber",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_list__include_textbook(self):
        self.textbook.exercises.create(page=16, number=11)
        self.textbook.exercises.create(page=17, number=13)
        self.textbook.exercises.create(page=17, number=14)
        Textbook.objects.create(title="The other title").exercises.create(page=12, number=4)

        response = self.client.get(reverse("exercise-list"), format="vnd.api+json", QUERY_STRING="include=textbook&sort=textbook,page,number")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "1",
                    "links": {"self": "http://testserver/api/exercises/1"},
                    "attributes": {
                        "page": 16, "number": 11,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "2",
                    "links": {"self": "http://testserver/api/exercises/2"},
                    "attributes": {
                        "page": 17, "number": 13,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
            ],
            "included": [
                {
                    "type": "textbook",
                    "id": "1",
                    "links": {"self": "http://testserver/api/textbooks/1"},
                    "attributes": {
                        "title": "The title",
                        "publisher": None, "year": None, "isbn": None,
                    },
                    "relationships": {
                        "exercises": {
                            "data": [
                                {"type": "exercise", "id": "1"},
                                {"type": "exercise", "id": "2"},
                                {"type": "exercise", "id": "3"},
                            ],
                            "meta": {"count": 3},
                        },
                        "sections": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/exercises?include=textbook&page%5Bnumber%5D=1&sort=textbook%2Cpage%2Cnumber",
                "last": "http://testserver/api/exercises?include=textbook&page%5Bnumber%5D=2&sort=textbook%2Cpage%2Cnumber",
                "next": "http://testserver/api/exercises?include=textbook&page%5Bnumber%5D=2&sort=textbook%2Cpage%2Cnumber",
                "prev": None,
            },
            "meta": {"pagination": {"count": 4, "page": 1, "pages": 2}},
        })

        response = self.client.get(reverse("exercise-list"), format="vnd.api+json", QUERY_STRING="include=textbook&page[number]=2&sort=textbook,page,number")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "3",
                    "links": {"self": "http://testserver/api/exercises/3"},
                    "attributes": {
                        "page": 17, "number": 14,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "4",
                    "links": {"self": "http://testserver/api/exercises/4"},
                    "attributes": {
                        "page": 12, "number": 4,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "2"}},
                    },
                },
            ],
            "included": [
                {
                    "type": "textbook",
                    "id": "1",
                    "links": {"self": "http://testserver/api/textbooks/1"},
                    "attributes": {
                        "title": "The title",
                        "publisher": None, "year": None, "isbn": None,
                    },
                    "relationships": {
                        "exercises": {
                            "data": [
                                {"type": "exercise", "id": "1"},
                                {"type": "exercise", "id": "2"},
                                {"type": "exercise", "id": "3"},
                            ],
                            "meta": {"count": 3},
                        },
                        "sections": {"data": [], "meta": {"count": 0}},
                    },
                },
                {
                    "type": "textbook",
                    "id": "2",
                    "links": {"self": "http://testserver/api/textbooks/2"},
                    "attributes": {
                        "title": "The other title",
                        "publisher": None, "year": None, "isbn": None,
                    },
                    "relationships": {
                        "exercises": {
                            "data": [
                                {"type": "exercise", "id": "4"},
                            ],
                            "meta": {"count": 1},
                        },
                        "sections": {"data": [], "meta": {"count": 0}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/exercises?include=textbook&page%5Bnumber%5D=1&sort=textbook%2Cpage%2Cnumber",
                "last": "http://testserver/api/exercises?include=textbook&page%5Bnumber%5D=2&sort=textbook%2Cpage%2Cnumber",
                "next": None,
                "prev": "http://testserver/api/exercises?include=textbook&page%5Bnumber%5D=1&sort=textbook%2Cpage%2Cnumber",
            },
            "meta": {"pagination": {"count": 4, "page": 2, "pages": 2}},
        })

    def test_list__filter_by_textbook(self):
        self.textbook.exercises.create(page=16, number=11)
        self.textbook.exercises.create(page=17, number=13)
        self.textbook.exercises.create(page=17, number=14)
        Textbook.objects.create(title="The other title").exercises.create(page=12, number=4)

        response = self.client.get(reverse("exercise-list"), format="vnd.api+json", QUERY_STRING="sort=textbook,page,number&filter[textbook]=1")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "1",
                    "links": {"self": "http://testserver/api/exercises/1"},
                    "attributes": {
                        "page": 16, "number": 11,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
                {
                    "type": "exercise",
                    "id": "2",
                    "links": {"self": "http://testserver/api/exercises/2"},
                    "attributes": {
                        "page": 17, "number": 13,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/exercises?filter%5Btextbook%5D=1&page%5Bnumber%5D=1&sort=textbook%2Cpage%2Cnumber",
                "last": "http://testserver/api/exercises?filter%5Btextbook%5D=1&page%5Bnumber%5D=2&sort=textbook%2Cpage%2Cnumber",
                "next": "http://testserver/api/exercises?filter%5Btextbook%5D=1&page%5Bnumber%5D=2&sort=textbook%2Cpage%2Cnumber",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.client.get(reverse("exercise-list"), format="vnd.api+json", QUERY_STRING="filter[textbook]=1&page[number]=2&sort=textbook,page,number")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "3",
                    "links": {"self": "http://testserver/api/exercises/3"},
                    "attributes": {
                        "page": 17, "number": 14,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"type": "textbook", "id": "1"}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/exercises?filter%5Btextbook%5D=1&page%5Bnumber%5D=1&sort=textbook%2Cpage%2Cnumber",
                "last": "http://testserver/api/exercises?filter%5Btextbook%5D=1&page%5Bnumber%5D=2&sort=textbook%2Cpage%2Cnumber",
                "next": None,
                "prev": "http://testserver/api/exercises?filter%5Btextbook%5D=1&page%5Bnumber%5D=1&sort=textbook%2Cpage%2Cnumber",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_patch__full(self):
        exercise = self.textbook.exercises.create(
            page=16,
            number=11,
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )
        self.assertEqual(Exercise.objects.count(), 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.textbook.id, 1)
        self.assertEqual(exercise.page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

        payload = {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "page": 16, "number": 11,
                    "instructions": "INSTRUCTIONS", "example": "EXAMPLE", "clue": "CLUE", "wording": "WORDING",
                },
            },
        }
        response = self.client.patch(reverse("exercise-detail", args=[1]), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "links": {"self": "http://testserver/api/exercises/1"},
                "attributes": {
                    "page": 16, "number": 11,
                    "instructions": "INSTRUCTIONS", "example": "EXAMPLE", "clue": "CLUE", "wording": "WORDING",
                },
                "relationships": {
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "1"}},
                },
            },
        })

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.textbook.id, 1)
        self.assertEqual(exercise.page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "INSTRUCTIONS")
        self.assertEqual(exercise.example, "EXAMPLE")
        self.assertEqual(exercise.clue, "CLUE")
        self.assertEqual(exercise.wording, "WORDING")

    def test_patch__partial(self):
        self.textbook.exercises.create(
            page=16,
            number=11,
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        payload = {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "instructions": "INSTRUCTIONS",
                },
            },
        }
        response = self.client.patch(reverse("exercise-detail", args=[1]), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "links": {"self": "http://testserver/api/exercises/1"},
                "attributes": {
                    "page": 16, "number": 11,
                    "instructions": "INSTRUCTIONS", "example": "example", "clue": "clue", "wording": "wording",
                },
                "relationships": {
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "1"}},
                },
            },
        })

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.textbook.id, 1)
        self.assertEqual(exercise.page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "INSTRUCTIONS")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_patch__read_only_textbook(self):
        self.textbook.exercises.create(
            page=16,
            number=11,
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )
        Textbook.objects.create(title="Another textbook")

        payload = {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "textbook": {"type": "textbook", "id": "2"},
                },
            },
        }
        response = self.client.patch(reverse("exercise-detail", args=[1]), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
        self.assertEqual(response.json(), {"errors": [{"code": "invalid",
             "detail": "'textbook' is immutable once set.",
             "source": {"pointer": "/data/relationships/textbook"},
             "status": "400"}
        ]})

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.textbook.id, 1)
        self.assertEqual(exercise.page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_patch__read_only_page(self):
        self.textbook.exercises.create(
            page=16,
            number=11,
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        payload = {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "page": 42,
                },
            },
        }
        response = self.client.patch(reverse("exercise-detail", args=[1]), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
        self.assertEqual(response.json(), {"errors": [{"code": "invalid",
             "detail": "'page' is immutable once set.",
             "source": {"pointer": "/data/attributes/page"},
             "status": "400"}
        ]})

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.textbook.id, 1)
        self.assertEqual(exercise.page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_patch__read_only_number(self):
        self.textbook.exercises.create(
            page=16,
            number=11,
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        payload = {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "number": 12,
                },
            },
        }
        response = self.client.patch(reverse("exercise-detail", args=[1]), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
        self.assertEqual(response.json(), {"errors": [{"code": "invalid",
             "detail": "'number' is immutable once set.",
             "source": {"pointer": "/data/attributes/number"},
             "status": "400"}
        ]})

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.textbook.id, 1)
        self.assertEqual(exercise.page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_delete(self):
        self.textbook.exercises.create(page=16, number=11)
        self.assertEqual(Exercise.objects.count(), 1)

        response = self.client.delete(reverse("exercise-detail", args=[1]), format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")

        self.assertEqual(Exercise.objects.count(), 0)


class RealisticUseTests(APITransactionTestCase):
    maxDiff = None
    reset_sequences = True

    def setUp(self):
        pdf_file = PdfFile.objects.create(sha256="0000000000000000000000000000000000000000000000000000000000000000", bytes_count=1234, pages_count=10)
        pdf_file.namings.create(name="not-so-amazing.pdf")
        textbook = Textbook.objects.create(title="Dull title")
        Section.objects.create(textbook=textbook, pdf_file=pdf_file, pdf_file_start_page=1, textbook_start_page=10, pages_count=35)

        pdf_file = PdfFile.objects.create(sha256="87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7", bytes_count=2354, pages_count=42)
        pdf_file.namings.create(name="amazing.pdf")
        textbook = Textbook.objects.create(title="The title")
        Section.objects.create(textbook=textbook, pdf_file=pdf_file, pdf_file_start_page=3, textbook_start_page=5, pages_count=35)
        textbook.exercises.create(page=16, number=11, instructions="instructions", example="example", clue="clue", wording="wording")

    def test_load_existing_pdf(self):
        # Input: the user just loaded a PDF in the GUI and it has computed its sha256
        sha256 = "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"

        # First request: get the associated section(s) and textbook(s)
        response = self.client.get(reverse("section-list"), format="vnd.api+json", QUERY_STRING=f"include=textbook&filter[pdf_file.sha256]={sha256}")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "section",
                    "id": "2",
                    "links": {"self": "http://testserver/api/sections/2"},
                    "attributes": {"pagesCount": 35, "pdfFileStartPage": 3, "textbookStartPage": 5},
                    "relationships": {
                        "pdfFile": {
                            "data": {"type": "pdfFile", "id": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7"},
                        },
                        "textbook": {
                            "data": {"id": "2", "type": "textbook"},
                        },
                    },
                },
            ],
            "included": [
                {
                    "type": "textbook",
                    "id": "2",
                    "links": {"self": "http://testserver/api/textbooks/2"},
                    "attributes": {"isbn": None, "publisher": None, "title": "The title", "year": None},
                    "relationships": {
                        "exercises": {"data": [{"id": "1", "type": "exercise"}], "meta": {"count": 1}},
                        "sections": {"data": [{"id": "2", "type": "section"}], "meta": {"count": 1}},
                    },
                },
            ],
            "links": {
                "first": "http://testserver/api/sections?filter%5Bpdf_file.sha256%5D=87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7&include=textbook&page%5Bnumber%5D=1",
                "last": "http://testserver/api/sections?filter%5Bpdf_file.sha256%5D=87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7&include=textbook&page%5Bnumber%5D=1",
                "next": None,
                "prev": None,
            },
            "meta": {"pagination": {"count": 1, "page": 1, "pages": 1}}
        })

        # The GUI displays the associated textbook(s) to the user
        # The user clicks on the textbook they want, the GUI displays the first page of the first matching section

        # Second request: get the exercises on that page
        response = self.client.get(reverse("exercise-list"), format="vnd.api+json", QUERY_STRING="filter[textbook]=2&filter[page]=5")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [],
            "links": {
                "first": "http://testserver/api/exercises?filter%5Bpage%5D=5&filter%5Btextbook%5D=2&page%5Bnumber%5D=1",
                "last": "http://testserver/api/exercises?filter%5Bpage%5D=5&filter%5Btextbook%5D=2&page%5Bnumber%5D=1",
                "next": None,
                "prev": None,
            },
            "meta": {"pagination": {"count": 0, "page": 1, "pages": 1}},
        })

        # User navigates to another page

        response = self.client.get(reverse("exercise-list"), format="vnd.api+json", QUERY_STRING="filter[textbook]=2&filter[page]=16")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "1",
                    "links": {"self": "http://testserver/api/exercises/1"},
                    "attributes": {
                        "page": 16, "number": 11,
                        "instructions": "instructions", "clue": "clue", "example": "example", "wording": "wording",
                    },
                    "relationships": {
                        "extractionEvents": {"data": [], "meta": {"count": 0}},
                        "textbook": {"data": {"id": "2", "type": "textbook"}},
                    },
                }
            ],
            "links": {
                "first": "http://testserver/api/exercises?filter%5Bpage%5D=16&filter%5Btextbook%5D=2&page%5Bnumber%5D=1",
                "last": "http://testserver/api/exercises?filter%5Bpage%5D=16&filter%5Btextbook%5D=2&page%5Bnumber%5D=1",
                "next": None,
                "prev": None,
            },
            "meta": {"pagination": {"count": 1, "page": 1, "pages": 1}},
        })

        # User creates a new exercise

        payload = {
            "data": {
                "type": "exercise",
                "attributes": {
                    "page": 16, "number": 12,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                },
                "relationships": {
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "2"}},
                },
            },
        }
        response = self.client.post(reverse("exercise-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "2",
                "links": {"self": "http://testserver/api/exercises/2"},
                "attributes": {
                    "page": 16, "number": 12,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                },
                "relationships": {
                    "extractionEvents": {"data": [], "meta": {"count": 0}},
                    "textbook": {"data": {"type": "textbook", "id": "2"}},
                },
            },
        })

        self.assertEqual(Exercise.objects.count(), 2)
