from rest_framework_json_api import serializers

from .models import Ping


class PingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ping
        fields = (
            "url",
            "created_at",
        )
