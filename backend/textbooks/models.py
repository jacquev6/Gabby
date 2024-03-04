from django.core.validators import RegexValidator
from django.db.models import Model
from django.db.models import CharField, ForeignKey, IntegerField, TextField, AutoField
from django.db.models import CASCADE, PROTECT


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
    pdf_file = ForeignKey(PdfFile, on_delete=CASCADE, related_name="namings")

    name = CharField(null=False, blank=False, max_length=255)
    # Could have other fields, e.g. the user who named it

    class Meta:
        unique_together = ["pdf_file", "name"]


class Textbook(Model):
    id = AutoField(primary_key=True)

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


class Section(Model):
    id = AutoField(primary_key=True)

    textbook = ForeignKey(Textbook, on_delete=CASCADE, related_name="sections")
    pdf_file = ForeignKey(PdfFile, on_delete=CASCADE, related_name="sections")

    textbook_start_page = IntegerField(null=False)
    pdf_file_start_page = IntegerField(null=False)
    pages_count = IntegerField(null=False)

    def __str__(self):
        return f"Pages {self.textbook_start_page}-{self.textbook_start_page+self.pages_count-1} of {self.textbook.short_str()} in {self.pdf_file.short_str()}"


class Exercise(Model):
    id = AutoField(primary_key=True)

    textbook = ForeignKey(Textbook, on_delete=PROTECT, related_name="exercises")
    page = IntegerField(null=False)
    # Exercise 'numbers' may very well not be actual numbers
    # (e.g. single letters, or combinations of digits, letters and dots)
    # But sorting such identifiers properly requires specification and implementation,
    # so for now we assume they are indeed numbers.
    number = IntegerField(null=False)

    class Meta:
        unique_together = ["textbook", "page", "number"]

    instructions = TextField(null=False, blank=True)
    example = TextField(null=False, blank=True)
    clue = TextField(null=False, blank=True)
    wording = TextField(null=False, blank=True)

    def __str__(self):
        return f"Exercice {self.number} page {self.page} in {self.textbook.short_str()}"
