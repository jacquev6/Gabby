from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from .models import Exercise


class ExerciseTests(APITransactionTestCase):
    maxDiff = None
    reset_sequences = True  # Primary keys appear in API responses

    def test_create_minimal_exercise(self):
        payload = {"data": {
            "type": "exercise",
            "attributes": {
                "pdfSha1": "da39a3ee5e6b4b0d3255bfef95601890afd80709", "pdfPage": 12, "number": 42,
            }
        }}
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
        self.assertEqual(exercise.pdf_sha1, "da39a3ee5e6b4b0d3255bfef95601890afd80709")
        self.assertEqual(exercise.pdf_page, 12)
        self.assertEqual(exercise.number, 42)
        self.assertEqual(exercise.instructions, "")
        self.assertEqual(exercise.clue, "")
        self.assertEqual(exercise.example, "")
        self.assertEqual(exercise.wording, "")

    def test_create_full_exercise(self):
        payload = {"data": {
            "type": "exercise",
            "attributes": {
                "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 14, "number": 1,
                "instructions": "instructions", "clue": "clue", "example": "example", "wording": "wording",
            }
        }}
        response = self.client.post(reverse("exercise-list"), payload, format="vnd.api+json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            "data": {
                "type": "exercise",
                "id": "1",
                "attributes": {
                    "pdfSha1": "3f786850e387550fdab836ed7e6dc881de23001b", "pdfPage": 14, "number": 1,
                    "instructions": "instructions", "clue": "clue", "example": "example", "wording": "wording",
                },
                "links": {"self": "http://testserver/api/exercises/1"},
            },
        })

        self.assertEqual(Exercise.objects.count(), 1)
        exercise = Exercise.objects.get()
        self.assertEqual(exercise.pdf_sha1, "3f786850e387550fdab836ed7e6dc881de23001b")
        self.assertEqual(exercise.pdf_page, 14)
        self.assertEqual(exercise.number, 1)
        self.assertEqual(exercise.instructions, "instructions")
        self.assertEqual(exercise.clue, "clue")
        self.assertEqual(exercise.example, "example")
        self.assertEqual(exercise.wording, "wording")
