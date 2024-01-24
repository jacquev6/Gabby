from rest_framework_json_api import serializers

from .models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            "pdf_sha1", "pdf_page",
            "number",
            "url",
            "instructions", "example", "clue", "wording",
        )

    # https://stackoverflow.com/questions/22124555 has many answers;
    # I chose the approach described in https://stackoverflow.com/a/50842440/905845
    def validate_pdf_sha1(self, value):
        if self.instance and value != self.instance.pdf_sha1:
            raise serializers.ValidationError("pdfSha1 is immutable once set")
        return value

    def validate_pdf_page(self, value):
        if self.instance and value != self.instance.pdf_page:
            raise serializers.ValidationError("pdfPage is immutable once set")
        return value

    def validate_number(self, value):
        if self.instance and value != self.instance.number:
            raise serializers.ValidationError("number is immutable once set")
        return value
