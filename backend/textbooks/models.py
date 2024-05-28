from django.core.validators import RegexValidator
from django.db import models
from polymorphic.models import PolymorphicModel

from . import parsing
from . import renderable


# @todo(Feature, later) Add timestamps (created_at, modified_at, etc.) and user ids (created_by, modified_by, etc.) to all models

class PdfFile(models.Model):
    sha256 = models.CharField(
        primary_key=True,
        null=False, blank=False,
        max_length=64,
        validators=[RegexValidator(r'^[0-9a-f]{64}$')],
    )

    bytes_count = models.IntegerField(null=False)
    pages_count = models.IntegerField(null=False)

    @property
    def id(self):
        return self.sha256

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


class PdfFileNaming(models.Model):
    pdf_file = models.ForeignKey(PdfFile, on_delete=models.CASCADE, related_name="namings")

    name = models.CharField(null=False, blank=False, max_length=255)
    # Could have other fields, e.g. the user who named it

    class Meta:
        constraints = [
            models.UniqueConstraint(
                "pdf_file", "name",
                name="unique_naming",
            ),
        ]


class Project(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Project '{self.title}'"


class Textbook(models.Model):
    id = models.AutoField(primary_key=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="textbooks")

    class Meta:
        constraints = [
            # Seemingly redondent (as 'id' is unique by itself), but required to add the "fat" foreign key in 'migrations/0003_initial_patch.py'
            models.UniqueConstraint(
                "id", "project",
                name="unique_id_and_project_id",
            ),
        ]

    title = models.CharField(null=False, blank=False, max_length=255)
    publisher = models.CharField(null=True, blank=True, max_length=255)  # De-normalized
    year = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(
        null=True, blank=True,
        max_length=25, # Max length as of 2024 is 13, established in 2007, so this should be future-proof
        validators=[RegexValidator(r'[0-9]')],
    )

    def __str__(self):
        return f'Textbook "{self.title}" by {self.publisher} ({self.year}) with ISBN {self.isbn}'

    def short_str(self):
        return f'"{self.title}" by {self.publisher} ({self.year})'


class Section(models.Model):
    id = models.AutoField(primary_key=True)

    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE, related_name="sections")
    pdf_file = models.ForeignKey(PdfFile, on_delete=models.CASCADE, related_name="sections")

    textbook_start_page = models.IntegerField(null=False)
    pdf_file_start_page = models.IntegerField(null=False)
    pages_count = models.IntegerField(null=False)

    def __str__(self):
        return f"Pages {self.textbook_start_page}-{self.textbook_start_page+self.pages_count-1} of {self.textbook.short_str()} in {self.pdf_file.short_str()}"


class Adaptation(PolymorphicModel):
    id = models.AutoField(primary_key=True)

    def make_adapted(self):
        return renderable.AdaptedExercise(
            number=self.exercise.number,
            textbook_page=self.exercise.textbook_page,
            instructions=self.make_adapted_instructions(),
            wording=self.make_adapted_wording(),
        )

    def to_generic_adaptation(self):
        return GenericAdaptation(
            exercise=Exercise(
                project=None,
                textbook=self.exercise.textbook,
                textbook_page=self.exercise.textbook_page,
                number=self.exercise.number,
                instructions=self.make_adapted_instructions().to_generic(),
                wording=self.make_adapted_wording().to_generic(),
            ),
        )


class GenericAdaptation(Adaptation):
    generic = models.TextField(null=False)

    def make_adapted_instructions(self):
        return parsing.parse_generic_section(self.exercise.instructions)

    def make_adapted_wording(self):
        return parsing.parse_generic_section(self.exercise.wording)


class Exercise(models.Model):
    id = models.AutoField(primary_key=True)

    project = models.ForeignKey(Project, null=False, on_delete=models.CASCADE, related_name="exercises")

    # @todo Review normalization:
    # - textbook and textbook_page must be "consistently null" (cf. constraint below), so maybe they'd be better in a dedicated table?
    # - bounding_rectangle make sense only if textbook_page falls within a section, but this is not currently enforced
    # - we'll soon need to add rectangles for instructions, wording, etc.
    textbook = models.ForeignKey(Textbook, null=True, on_delete=models.CASCADE, related_name="exercises")
    textbook_page = models.IntegerField(null=True)
    bounding_rectangle = models.JSONField(null=True)

    # Custom collation: https://dba.stackexchange.com/a/285230
    number = models.CharField(null=False, db_collation="textbooks_exercise_number")

    class Meta:
        ordering = ("textbook", "textbook_page", "number")
        constraints = [
            models.UniqueConstraint(
                "textbook", "textbook_page", "number",
                name="unique_exercise",
            ),
            models.CheckConstraint(
                check=models.Q(textbook=None, textbook_page=None) | models.Q(textbook__isnull=False, textbook_page__isnull=False),
                name="textbook_and_page_consistently_null",
            ),
        ]

    instructions = models.TextField(null=False, blank=True)
    wording = models.TextField(null=False, blank=True)
    example = models.TextField(null=False, blank=True)
    clue = models.TextField(null=False, blank=True)

    adaptation = models.OneToOneField(Adaptation, on_delete=models.SET_NULL, null=True, related_name="exercise")

    def __str__(self):
        assert((self.textbook is None) == (self.textbook_page is None))
        if self.textbook:
            return f"Exercise '{self.number}' page {self.textbook_page} of {self.textbook.short_str()}"
        else:
            return f"Exercise '{self.number}'"


class ExtractionEvent(models.Model):
    id = models.AutoField(primary_key=True)

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="extraction_events")
    event = models.TextField(null=False, blank=False)  # Free form for the backend, defined by the frontend


class SelectThingsAdaptation(Adaptation):
    punctuation = models.BooleanField(null=False)
    words = models.BooleanField(null=False)
    colors = models.IntegerField(null=False)

    def make_adapted_instructions(self):
        if self.colors > 1:
            colors = range(1, self.colors + 1)
            parse = parsing.SectionParser(
                {f"sel{color}": r""" "|" STR """ for color in colors},
                type(
                    "InstructionsTransformer",
                    (parsing.SectionTransformer,),
                    {
                        f"sel{color}_tag": (lambda c: staticmethod(lambda args: renderable.SelectedText(text=args[0], color=c, colors=self.colors)))(color)
                        for color in colors
                    },
                )(),
            )
            section = parse(self.exercise.instructions)
            tokens = []
            for color in colors:
                if color != 1:
                    tokens.append(renderable.Whitespace())
                tokens.append(renderable.SelectedClicks(color=color, colors=self.colors))
            section.paragraphs.append(renderable.Paragraph(sentences=[renderable.Sentence(tokens=tokens)]))

            return section
        else:
            return parsing.parse_plain_section(self.exercise.instructions)

    class WordingTransformer(parsing.SectionTransformer):
        def __init__(self, words, punctuation, colors):
            self.select_words = words
            self.select_punctuation = punctuation
            self.colors = colors

        def word(self, args):
            if self.select_words:
                return renderable.SelectableText(text=args[0], colors=self.colors)
            else:
                return renderable.PlainText(text=args[0])

        def punctuation(self, args):
            if self.select_punctuation:
                return renderable.SelectableText(text=args[0], colors=self.colors)
            else:
                return renderable.PlainText(text=args[0])

    def make_adapted_wording(self):
        parse = parsing.SectionParser({}, self.WordingTransformer(self.words, self.punctuation, self.colors))
        return parse(self.exercise.wording)


class FillWithFreeTextAdaptation(Adaptation):
    placeholder = models.CharField(null=False, blank=False, max_length=10)

    def make_adapted_instructions(self):
        return parsing.parse_plain_section(self.exercise.instructions)

    class WordingTransformer(parsing.SectionTransformer):
        def placeholder_tag(self, args):
            return renderable.FreeTextInput()

    def make_adapted_wording(self):
        parse = parsing.SectionParser({"placeholder": ""}, self.WordingTransformer())
        return parse(self.exercise.wording.replace(self.placeholder, "{placeholder}"))


class MultipleChoicesAdaptation(Adaptation):
    placeholder = models.CharField(null=False, blank=False, max_length=10)

    class InstructionsTransformer(parsing.SectionTransformer):
        def __init__(self):
            self.choices = []

        def choice_tag(self, args):
            self.choices.append(args[0])
            return renderable.PlainText(text=args[0])

    def make_adapted_instructions(self):
        parse = parsing.SectionParser({"choice": r""" "|" STR """}, self.InstructionsTransformer())
        return parse(self.exercise.instructions)

    class WordingTransformer(parsing.SectionTransformer):
        def __init__(self, choices):
            self.choices = choices

        def placeholder_tag(self, args):
            return renderable.MultipleChoicesInput(choices=self.choices)

    def make_adapted_wording(self):
        choices_gatherer = self.InstructionsTransformer()
        parsing.SectionParser({"choice": r""" "|" STR """}, choices_gatherer)(self.exercise.instructions)
        parse = parsing.SectionParser({"placeholder": ""}, self.WordingTransformer(choices_gatherer.choices))
        return parse(self.exercise.wording.replace(self.placeholder, "{placeholder}"))
