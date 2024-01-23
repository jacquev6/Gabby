from django.db import models


class Exercise(models.Model):
    id = models.AutoField(primary_key=True)

    pdf_sha1 = models.CharField(null=False, blank=False, max_length=40)
    pdf_page = models.IntegerField(null=False)

    number = models.TextField(null=False, blank=False)

    instructions = models.TextField(null=False, blank=True)
    example = models.TextField(null=False, blank=True)
    clue = models.TextField(null=False, blank=True)
    wording = models.TextField(null=False, blank=True)

    def __str__(self):
        return f"Exercice {self.number} page {self.pdf_page} in {self.pdf_sha1}"
