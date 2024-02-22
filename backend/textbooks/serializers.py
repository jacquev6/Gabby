from rest_framework_json_api import serializers

from .models import PdfFile, PdfFileNaming, Textbook, Section, Exercise


class PdfFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PdfFile
        fields = (
            "url",
            "sha256", "bytes_count", "pages_count",
            "namings", "sections",
        )

    included_serializers = {
        "namings": 'textbooks.serializers.PdfFileNamingSerializer',
        "sections": 'textbooks.serializers.SectionSerializer',
    }

class PdfFileNamingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PdfFileNaming
        fields = (
            "url",
            "name",
            "pdf_file",
        )

    included_serializers = {
        "pdf_file": 'textbooks.serializers.PdfFileSerializer',
    }


class TextbookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Textbook
        fields = (
            "url",
            "title", "publisher", "year", "isbn",
            "exercises", "sections",
        )

    included_serializers = {
        "exercises": 'textbooks.serializers.ExerciseSerializer',
        "sections": 'textbooks.serializers.SectionSerializer',
    }


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = (
            "url",
            "textbook_start_page", "pdf_file_start_page", "pages_count",
            "textbook", "pdf_file",
        )

    included_serializers = {
        "textbook": TextbookSerializer,
        "pdf_file": PdfFileSerializer,
    }


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            "url",
            "page", "number",
            "instructions", "example", "clue", "wording",
            "textbook",
        )

    included_serializers = {
        "textbook": TextbookSerializer,
    }

    # https://stackoverflow.com/questions/22124555 has many answers;
    # I chose the approach described in https://stackoverflow.com/a/50842440/905845
    def validate_textbook(self, value):
        if self.instance and value != self.instance.textbook:
            raise serializers.ValidationError("'textbook' is immutable once set.")
        return value

    def validate_page(self, value):
        if self.instance and value != self.instance.page:
            raise serializers.ValidationError("'page' is immutable once set.")
        return value

    def validate_number(self, value):
        if self.instance and value != self.instance.number:
            raise serializers.ValidationError("'number' is immutable once set.")
        return value
