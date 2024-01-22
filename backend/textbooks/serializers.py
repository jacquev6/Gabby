from rest_framework_json_api import serializers

from .models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            "pdf_sha1", "pdf_page",
            "number",
            "instructions", "example", "clue", "wording",
        )
        read_only_fields = ("pdf_sha1", "pdf_page")
