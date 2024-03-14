from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework_json_api.schemas.openapi import SchemaGenerator
from rest_framework.schemas import get_schema_view

from .views import PdfFileViewSet, PdfFileNamingViewSet, ProjectViewSet, TextbookViewSet, SectionViewSet, ExerciseViewSet, ExtractionEventViewSet
from .views import extraction_report_view


# @todo(Project management, later): Migrate schema generation to DRF-spectacular
# (See deprecation notice on top of https://www.django-rest-framework.org/api-guide/schemas/)

# @todo(Project management, later): Save the schema to a file on startup (to make changes more explicit)

router = routers.DefaultRouter(trailing_slash=False)
router.register("pdfFiles", PdfFileViewSet)
router.register("pdfFileNamings", PdfFileNamingViewSet)
router.register("projects", ProjectViewSet)
router.register("textbooks", TextbookViewSet)
router.register("sections", SectionViewSet)
router.register("exercises", ExerciseViewSet)
router.register("extractionEvents", ExtractionEventViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("project-<int:project_id>-extraction-report.json", extraction_report_view, name="extraction-report"),
    path(
        "schema",
        get_schema_view(
            title="Gabby API",
            description="API for inclusive textbook exercises.",
            version="0.1.0",
            generator_class=SchemaGenerator,
        ),
        name="openapi-schema",
    ),
    path(
        "swagger/",
        TemplateView.as_view(
            template_name="swagger.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger",
    ),
]
