from rest_framework_json_api.views import ModelViewSet

from .models import PdfFile, PdfFileNaming, Textbook, Section, Exercise
from .serializers import PdfFileSerializer, PdfFileNamingSerializer, TextbookSerializer, SectionSerializer, ExerciseSerializer


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
    filterset_fields = {
        "pdf_file__sha256": ["exact"],
    }


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.order_by("id")
    serializer_class = ExerciseSerializer
    filterset_fields = {
        "textbook": ["exact"],
        "page": ["exact"],
    }
