from django.test import TransactionTestCase
from django.db.utils import IntegrityError

from .models import Project, Textbook, Exercise


class ExerciseTests(TransactionTestCase):
    def setUp(self):
        self.project = Project.objects.create(title="Project")
        self.textbook = Textbook.objects.create(project=self.project, title="Textbook")

    def test_create(self):
        e = Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="5")
        self.assertEqual(e.project, self.project)
        self.assertEqual(e.textbook, self.textbook)
        self.assertEqual(e.textbook_page, 5)
        self.assertEqual(e.number, "5")

    def test_create_without_textbook(self):
        e = Exercise.objects.create(project=self.project, textbook=None, textbook_page=None, number="5")
        self.assertEqual(e.project, self.project)
        self.assertIsNone(e.textbook)
        self.assertIsNone(e.textbook_page)
        self.assertEqual(e.number, "5")

    def test_create_duplicate(self):
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="5")
        with self.assertRaises(IntegrityError):
            Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="5")

    def test_create_near_duplicates(self):
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="A")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="a")

    def test_create_with_textbook_but_without_textbook_page(self):
        with self.assertRaises(IntegrityError):
            Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=None, number="5")

    def test_create_with_textbook_page_but_without_textbook(self):
        with self.assertRaises(IntegrityError):
            Exercise.objects.create(project=self.project, textbook=None, textbook_page=5, number="5")

    def test_create_without_project(self):
        with self.assertRaises(IntegrityError):
            Exercise.objects.create(project=None, textbook=self.textbook, textbook_page=5, number="5")

    def test_create_with_inconsistent_project(self):
        other_project = Project.objects.create(title="Other project")
        # Implemented using a "fat" foreign key added outside Django's ORM, in 'migrations/0003_initial_patch.py'
        with self.assertRaises(IntegrityError):
            Exercise.objects.create(project=other_project, textbook=self.textbook, textbook_page=5, number="5")

    def test_ordering(self):
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="5.b")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="5.a")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="12")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="A12")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="A1")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=5, number="2")
        Exercise.objects.create(project=self.project, textbook=None, textbook_page=None, number="4")
        Exercise.objects.create(project=self.project, textbook=None, textbook_page=None, number="Some text")
        Exercise.objects.create(project=self.project, textbook=None, textbook_page=None, number="Some other text")
        Exercise.objects.create(project=self.project, textbook=None, textbook_page=None, number="Other text")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=1, number="1")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=1, number="Bob")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=1, number="10")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=1, number="Alice")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=1, number="03")
        Exercise.objects.create(project=self.project, textbook=self.textbook, textbook_page=1, number="2")
        self.assertEqual(
            [
                (bool(exercise.textbook), exercise.textbook_page, exercise.number)
                for exercise in Exercise.objects.order_by("textbook_page", "number")
            ],
            [
                (True, 1, "1"),
                (True, 1, "2"),
                (True, 1, "03"),
                (True, 1, "10"),
                (True, 1, "Alice"),
                (True, 1, "Bob"),
                (True, 5, "2"),
                (True, 5, "5.a"),
                (True, 5, "5.b"),
                (True, 5, "12"),
                (True, 5, "A1"),
                (True, 5, "A12"),
                (False, None, "4"),
                (False, None, "Other text"),
                (False, None, "Some other text"),
                (False, None, "Some text"),
            ],
        )
