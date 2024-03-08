from rest_framework_json_api.views import ModelViewSet

from .models import PdfFile, PdfFileNaming, Textbook, Section, TextbookExercise, Project, Exercise, ExtractionEvent
from .serializers import PdfFileSerializer, PdfFileNamingSerializer, TextbookSerializer, SectionSerializer, TextbookExerciseSerializer, ProjectSerializer, ExerciseSerializer, ExtractionEventSerializer



class PdfFileViewSet(ModelViewSet):
    queryset = PdfFile.objects.order_by("sha256")
    serializer_class = PdfFileSerializer


class PdfFileNamingViewSet(ModelViewSet):
    queryset = PdfFileNaming.objects.order_by("id")
    serializer_class = PdfFileNamingSerializer


class TextbookViewSet(ModelViewSet):
    queryset = Textbook.objects.order_by("id")
    serializer_class = TextbookSerializer


class SectionViewSet(ModelViewSet):
    queryset = Section.objects.order_by("id")
    serializer_class = SectionSerializer


class TextbookExerciseViewSet(ModelViewSet):
    queryset = TextbookExercise.objects.order_by("id")
    serializer_class = TextbookExerciseSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.order_by("id")
    serializer_class = ProjectSerializer


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.order_by("id")
    serializer_class = ExerciseSerializer
    filterset_fields = {
        "textbook_exercise__textbook": ["exact"],
        "textbook_exercise__page": ["exact"],
    }


class ExtractionEventViewSet(ModelViewSet):
    queryset = ExtractionEvent.objects.order_by("id")
    serializer_class = ExtractionEventSerializer
    filterset_fields = {
        "exercise": ["exact"],
    }
