from django.db import models


class Exercise(models.Model):
    id = models.AutoField(primary_key=True)

    pdf_sha1 = models.CharField(null=False, blank=False, max_length=40)
    pdf_page = models.IntegerField(null=False)

    number = models.TextField(null=False)

    instructions = models.TextField(null=True, default=None)
    example = models.TextField(null=True, default=None)
    clue = models.TextField(null=True, default=None)
    wording = models.TextField(null=True, default=None)
