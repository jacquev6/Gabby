from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework_json_api.schemas.openapi import SchemaGenerator
from rest_framework.schemas import get_schema_view

from .views import ExerciseViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register(r"exercises", ExerciseViewSet)

urlpatterns = [
    path("", include(router.urls)),
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
