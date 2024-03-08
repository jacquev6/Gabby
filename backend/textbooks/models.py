from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Model
from django.db.models import CharField, ForeignKey, IntegerField, TextField, AutoField
from django.db.models import CASCADE


# @todo(Feature, later) Add timestamps (created_at, modified_at, etc.) and user ids (created_by, modified_by, etc.) to all models

class PdfFile(Model):
    sha256 = CharField(
        primary_key=True,
        null=False, blank=False,
        max_length=64,
        validators=[RegexValidator(r'^[0-9a-f]{64}$')],
    )

    bytes_count = IntegerField(null=False)
    pages_count = IntegerField(null=False)

    def __str__(self):
        if self.namings:
            names = ", ".join(naming.name for naming in self.namings.all())
            return f"PDF file with sha256={self.sha256[0:8]}... known as {names}"
        else:
            return f"PDF file with sha256={self.sha256[0:8]}..."

    def short_str(self):
        if self.namings:
            return self.namings.first().name
        else:
            return f"PDF file with sha256={self.sha256[0:8]}..."


class PdfFileNaming(Model):
    pdf_file = ForeignKey(PdfFile, on_delete=models.CASCADE, related_name="namings")

    name = CharField(null=False, blank=False, max_length=255)
    # Could have other fields, e.g. the user who named it

    class Meta:
        unique_together = ["pdf_file", "name"]


class Project(Model):
    id = AutoField(primary_key=True)

    title = CharField(null=True, blank=False, max_length=255)
    description = TextField(null=True, blank=False)

    def __str__(self):
        return f"Project '{self.title}'"


class Textbook(Model):
    id = AutoField(primary_key=True)

    project = ForeignKey(Project, on_delete=CASCADE, related_name="textbooks")

    title = CharField(null=False, blank=False, max_length=255)
    publisher = CharField(null=True, blank=False, max_length=255)  # De-normalized
    year = IntegerField(null=True)
    isbn = CharField(
        null=True, blank=False,
        max_length=25, # Max length as of 2024 is 13, established in 2007, so this should be future-proof
        validators=[RegexValidator(r'[0-9]')],
    )

    def __str__(self):
        return f'Textbook "{self.title}" by {self.publisher} ({self.year}) with ISBN {self.isbn}'

    def short_str(self):
        return f'"{self.title}" by {self.publisher} ({self.year})'


class TextbookExercise(Model):
    id = AutoField(primary_key=True)

    textbook = ForeignKey(Textbook, on_delete=CASCADE, related_name="exercises")
    page = IntegerField(null=False)
    # Exercise 'numbers' may very well not be actual numbers
    # (e.g. single letters, or combinations of digits, letters and dots)
    # But sorting such identifiers properly requires specification and implementation,
    # so for now we assume they are indeed numbers.
    number = IntegerField(null=False)

    class Meta:
        unique_together = ["textbook", "page", "number"]

    def __str__(self):
        return f"Exercise {self.number} page {self.page} in {self.textbook.short_str()}"


class Section(Model):
    id = AutoField(primary_key=True)

    textbook = ForeignKey(Textbook, on_delete=models.CASCADE, related_name="sections")
    pdf_file = ForeignKey(PdfFile, on_delete=models.CASCADE, related_name="sections")

    textbook_start_page = IntegerField(null=False)
    pdf_file_start_page = IntegerField(null=False)
    pages_count = IntegerField(null=False)

    def __str__(self):
        return f"Pages {self.textbook_start_page}-{self.textbook_start_page+self.pages_count-1} of {self.textbook.short_str()} in {self.pdf_file.short_str()}"


class Exercise(Model):
    id = AutoField(primary_key=True)

    project = models.ForeignKey(Project, null=False, on_delete=models.CASCADE, related_name="exercises")

    # Morally, these two fields are exclusive, but this is not enforced
    textbook_exercise = models.ForeignKey(TextbookExercise, null=True, default=None, on_delete=models.SET_NULL, related_name="exercise")
    title = CharField(null=False, blank=True, max_length=255)

    instructions = TextField(null=False, blank=True)
    example = TextField(null=False, blank=True)
    clue = TextField(null=False, blank=True)
    wording = TextField(null=False, blank=True)

    def __str__(self):
        if self.textbook_exercise:
            return f"{self.textbook_exercise}, extracted"
        else:
            return f"Exercice '{self.title}'"


class ExtractionEvent(Model):
    id = AutoField(primary_key=True)

    exercise = ForeignKey(Exercise, on_delete=CASCADE, related_name="extraction_events")
    event = TextField(null=False, blank=False)  # Free form for the backend, defined by the frontend
