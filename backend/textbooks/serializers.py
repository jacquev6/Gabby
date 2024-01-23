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
        # @todo Mark read-only fields
        # Currently the next line causes a failure in POST: 'null value in column "pdf_page"'
        # read_only_fields = ("pdf_sha1", "pdf_page")
