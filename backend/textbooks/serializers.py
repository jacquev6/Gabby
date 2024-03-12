from rest_framework_json_api import serializers

from .models import PdfFile, PdfFileNaming, Project, Textbook, Section, Exercise, ExtractionEvent


# @todo(Project management, soon) Use https://sqids.org/python for auto-increment ids

class PdfFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfFile
        fields = (
            "url",
            "sha256", "bytes_count", "pages_count",
            "namings", "sections",
        )

    included_serializers = {
        "namings": "textbooks.serializers.PdfFileNamingSerializer",
        "sections": "textbooks.serializers.SectionSerializer",
    }


class PdfFileNamingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfFileNaming
        fields = (
            "url",
            "name",
            "pdf_file",
        )

    included_serializers = {
        "pdf_file": "textbooks.serializers.PdfFileSerializer",
    }


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "url",
            "title", "description",
            "textbooks", "exercises",
        )

    included_serializers = {
        "textbooks": "textbooks.serializers.TextbookSerializer",
        "exercises": "textbooks.serializers.ExerciseSerializer",
    }


class TextbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textbook
        fields = (
            "url",
            "title", "publisher", "year", "isbn",
            "project", "exercises", "sections",
        )

    included_serializers = {
        "project": "textbooks.serializers.ProjectSerializer",
        "exercises": "textbooks.serializers.ExerciseSerializer",
        "sections": "textbooks.serializers.SectionSerializer",
    }


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = (
            "url",
            "textbook_start_page", "pdf_file_start_page", "pages_count",
            "textbook", "pdf_file",
        )

    included_serializers = {
        "textbook": "textbooks.serializers.TextbookSerializer",
        "pdf_file": "textbooks.serializers.PdfFileSerializer",
    }


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            "url",
            "textbook_page", "number",
            "instructions", "example", "clue", "wording",
            "project", "textbook", "extraction_events",
        )

    included_serializers = {
        "project": "textbooks.serializers.ProjectSerializer",
        "textbook": "textbooks.serializers.TextbookSerializer",
        "extraction_events": "textbooks.serializers.ExtractionEventSerializer",
    }

    # https://stackoverflow.com/questions/22124555 has many answers;
    # I chose the approach described in https://stackoverflow.com/a/50842440/905845
    def validate_textbook(self, value):
        if self.instance and value != self.instance.textbook:
            raise serializers.ValidationError("\"textbook\" is immutable once set.")
        return value

    def validate_textbook_page(self, value):
        if self.instance and value != self.instance.textbook_page:
            raise serializers.ValidationError("\"textbook_page\" is immutable once set.")
        return value

    def validate_number(self, value):
        if self.instance and value != self.instance.number:
            raise serializers.ValidationError("\"number\" is immutable once set.")
        return value


class ExtractionEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractionEvent
        fields = (
            "url",
            "event",
            "exercise",
        )

    included_serializers = {
        "exercise": ExerciseSerializer,
    }
