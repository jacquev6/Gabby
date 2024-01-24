from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from .models import Exercise


class ExerciseTests(APITransactionTestCase):
    maxDiff = None
    reset_sequences = True  # Primary keys appear in API responses

    def test_create__minimal(self):
        payload = {
            "data": {
                "type": "exercise",
                "id": None,
                "attributes": {
                    "pdfSha1": "da39a3ee5e6b4b0d3255bfef95601890afd80709", "pdfPage": 12, "number": 42,
                },
            },
        }
        response = self.client.post(reverse("exercise-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "pdfSha1": "da39a3ee5e6b4b0d3255bfef95601890afd80709", "pdfPage": 12, "number": 42,
                    "instructions": "", "clue": "", "example": "", "wording": "",
                },
                "links": {"self": "http://testserver/api/exercises/1"},
            },
        })

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.pdf_sha1, "da39a3ee5e6b4b0d3255bfef95601890afd80709")
        self.assertEqual(exercise.pdf_page, 12)
        self.assertEqual(exercise.number, 42)
        self.assertEqual(exercise.instructions, "")
        self.assertEqual(exercise.example, "")
        self.assertEqual(exercise.clue, "")
        self.assertEqual(exercise.wording, "")

    def test_create__full(self):
        payload = {
            "data": {
                "type": "exercise",
                "id": None,
                "attributes": {
                    "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 14, "number": 1,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                },
            },
        }
        response = self.client.post(reverse("exercise-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 14, "number": 1,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                },
                "links": {"self": "http://testserver/api/exercises/1"},
            },
        })

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.pdf_sha1, "3f786850e387550fdab836ed7e6dc881de23001b")
        self.assertEqual(exercise.pdf_page, 14)
        self.assertEqual(exercise.number, 1)
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_get(self):
        Exercise.objects.create(
            pdf_sha1="3f786850e387550fdab836ed7e6dc881de23001b",
            pdf_page=16,
            number=11,
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )

        response = self.client.get(reverse("exercise-detail", args=[1]), format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 16, "number": 11,
                    "instructions": "instructions", "example": "example", "clue": "clue", "wording": "wording",
                },
                "links": {"self": "http://testserver/api/exercises/1"},
            },
        })

    def test_list(self):
        Exercise.objects.create(pdf_sha1="3f786850e387550fdab836ed7e6dc881de23001b", pdf_page=16, number=11)
        Exercise.objects.create(pdf_sha1="3f786850e387550fdab836ed7e6dc881de23001b", pdf_page=17, number=13)
        Exercise.objects.create(pdf_sha1="3f786850e387550fdab836ed7e6dc881de23001b", pdf_page=17, number=14)

        response = self.client.get(reverse("exercise-list"), format="vnd.api+json", QUERY_STRING="sort=pdfSha1,pdfPage,number")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "1",
                    "attributes": {
                        "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 16, "number": 11,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "links": {"self": "http://testserver/api/exercises/1"},
                },
                {
                    "type": "exercise",
                    "id": "2",
                    "attributes": {
                        "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 17, "number": 13,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "links": {"self": "http://testserver/api/exercises/2"},
                },
            ],
            "links": {
                "first": "http://testserver/api/exercises?page%5Bnumber%5D=1&sort=pdfSha1%2CpdfPage%2Cnumber",
                "last": "http://testserver/api/exercises?page%5Bnumber%5D=2&sort=pdfSha1%2CpdfPage%2Cnumber",
                "next": "http://testserver/api/exercises?page%5Bnumber%5D=2&sort=pdfSha1%2CpdfPage%2Cnumber",
                "prev": None,
            },
            "meta": {"pagination": {"count": 3, "page": 1, "pages": 2}},
        })

        response = self.client.get(reverse("exercise-list"), format="vnd.api+json", QUERY_STRING="page[number]=2&sort=pdfSha1,pdfPage,number")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "data": [
                {
                    "type": "exercise",
                    "id": "3",
                    "attributes": {
                        "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 17, "number": 14,
                        "instructions": "", "example": "", "clue": "", "wording": "",
                    },
                    "links": {"self": "http://testserver/api/exercises/3"},
                },
            ],
            "links": {
                "first": "http://testserver/api/exercises?page%5Bnumber%5D=1&sort=pdfSha1%2CpdfPage%2Cnumber",
                "last": "http://testserver/api/exercises?page%5Bnumber%5D=2&sort=pdfSha1%2CpdfPage%2Cnumber",
                "next": None,
                "prev": "http://testserver/api/exercises?page%5Bnumber%5D=1&sort=pdfSha1%2CpdfPage%2Cnumber",
            },
            "meta": {"pagination": {"count": 3, "page": 2, "pages": 2}},
        })

    def test_patch__full(self):
        exercise = Exercise.objects.create(
            pdf_sha1="3f786850e387550fdab836ed7e6dc881de23001b",
            pdf_page=16,
            number=11,
            instructions="instructions",
            example="example",
            clue="clue",
            wording="wording",
        )
        self.assertEqual(Exercise.objects.count(), 1)
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.pdf_sha1, "3f786850e387550fdab836ed7e6dc881de23001b")
        self.assertEqual(exercise.pdf_page, 16)
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
                    "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 16, "number": 11,
                    "instructions": "INSTRUCTIONS", "example": "EXAMPLE", "clue": "CLUE", "wording": "WORDING",
                },
            },
        }
        response = self.client.patch(reverse("exercise-detail", args=[1]), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 16, "number": 11,
                    "instructions": "INSTRUCTIONS", "example": "EXAMPLE", "clue": "CLUE", "wording": "WORDING",
                },
                "links": {"self": "http://testserver/api/exercises/1"},
            },
        })

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.pdf_sha1, "3f786850e387550fdab836ed7e6dc881de23001b")
        self.assertEqual(exercise.pdf_page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "INSTRUCTIONS")
        self.assertEqual(exercise.example, "EXAMPLE")
        self.assertEqual(exercise.clue, "CLUE")
        self.assertEqual(exercise.wording, "WORDING")

    def test_patch__partial(self):
        Exercise.objects.create(
            pdf_sha1="3f786850e387550fdab836ed7e6dc881de23001b",
            pdf_page=16,
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 16, "number": 11,
                    "instructions": "INSTRUCTIONS", "example": "example", "clue": "clue", "wording": "wording",
                },
                "links": {"self": "http://testserver/api/exercises/1"},
            },
        })

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.pdf_sha1, "3f786850e387550fdab836ed7e6dc881de23001b")
        self.assertEqual(exercise.pdf_page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "INSTRUCTIONS")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_patch__read_only_pdf_sha1(self):
        Exercise.objects.create(
            pdf_sha1="3f786850e387550fdab836ed7e6dc881de23001b",
            pdf_page=16,
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
                    "pdfSha1": "foobar",
                },
            },
        }
        response = self.client.patch(reverse("exercise-detail", args=[1]), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'errors': [{'code': 'invalid',
             'detail': 'pdfSha1 is immutable once set',
             'source': {'pointer': '/data/attributes/pdfSha1'},
             'status': '400'}
        ]})

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.pdf_sha1, "3f786850e387550fdab836ed7e6dc881de23001b")
        self.assertEqual(exercise.pdf_page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_patch__read_only_pdf_page(self):
        Exercise.objects.create(
            pdf_sha1="3f786850e387550fdab836ed7e6dc881de23001b",
            pdf_page=16,
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
                    "pdfPage": 42,
                },
            },
        }
        response = self.client.patch(reverse("exercise-detail", args=[1]), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'errors': [{'code': 'invalid',
             'detail': 'pdfPage is immutable once set',
             'source': {'pointer': '/data/attributes/pdfPage'},
             'status': '400'}
        ]})

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.pdf_sha1, "3f786850e387550fdab836ed7e6dc881de23001b")
        self.assertEqual(exercise.pdf_page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_patch__read_only_number(self):
        Exercise.objects.create(
            pdf_sha1="3f786850e387550fdab836ed7e6dc881de23001b",
            pdf_page=16,
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
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'errors': [{'code': 'invalid',
             'detail': 'number is immutable once set',
             'source': {'pointer': '/data/attributes/number'},
             'status': '400'}
        ]})

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.id, 1)
        self.assertEqual(exercise.pdf_sha1, "3f786850e387550fdab836ed7e6dc881de23001b")
        self.assertEqual(exercise.pdf_page, 16)
        self.assertEqual(exercise.number, 11)
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.wording, "wording")

    def test_delete(self):
        Exercise.objects.create(
            pdf_sha1="3f786850e387550fdab836ed7e6dc881de23001b",
            pdf_page=16,
            number=11,
        )
        self.assertEqual(Exercise.objects.count(), 1)

        response = self.client.delete(reverse("exercise-detail", args=[1]), format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")

        self.assertEqual(Exercise.objects.count(), 0)
