from django.db import models


class Exercise(models.Model):
    id = models.AutoField(primary_key=True)

    pdf_sha256 = models.CharField(null=False, blank=False, max_length=64)
    pdf_page = models.IntegerField(null=False)

    # Exercise 'numbers' may very well not be actual numbers
    # (e.g. single letters, or combinations of digits, letters and dots)
    # But sorting such identifiers properly requires specification and implementation,
    # so for now we assume they are indeed numbers.
    number = models.IntegerField(null=False)

    instructions = models.TextField(null=False, blank=True)
    example = models.TextField(null=False, blank=True)
    clue = models.TextField(null=False, blank=True)
    wording = models.TextField(null=False, blank=True)

    def __str__(self):
        return f"Exercice {self.number} page {self.pdf_page} in {self.pdf_sha256}"
