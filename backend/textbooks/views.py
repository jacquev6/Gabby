from rest_framework_json_api.views import ModelViewSet

from .models import Exercise
from .serializers import ExerciseSerializer


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filterset_fields = {
        "pdf_sha256": ["exact"],
        "pdf_page": ["exact"],
    }
