from rest_framework_json_api import serializers

from .models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            "pdf_sha256", "pdf_page",
            "number",
            "url",
            "instructions", "example", "clue", "wording",
        )

    # https://stackoverflow.com/questions/22124555 has many answers;
    # I chose the approach described in https://stackoverflow.com/a/50842440/905845
    def validate_pdf_sha256(self, value):
        if len(value) != 64:
            raise serializers.ValidationError("pdfSha256 must be 64 characters long")
        for c in value:
            if c not in "0123456789abcdef":
                raise serializers.ValidationError(f"pdfSha256 must be a hexadecimal string (it contains a '{c}')")
        if self.instance and value != self.instance.pdf_sha256:
            raise serializers.ValidationError("pdfSha256 is immutable once set")
        return value

    def validate_pdf_page(self, value):
        if self.instance and value != self.instance.pdf_page:
            raise serializers.ValidationError("pdfPage is immutable once set")
        return value

    def validate_number(self, value):
        if self.instance and value != self.instance.number:
            raise serializers.ValidationError("number is immutable once set")
        return value
