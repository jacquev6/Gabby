import django.conf
import django.core.management
import fastapi
from fastapi.middleware.cors import CORSMiddleware

from fastjsonapi import make_jsonapi_router
django.setup()  # Required before importing any module that uses the Django ORM
from opinion_ping.resources import PingsResource
from textbooks.resources import PdfFilesResource, PdfFileNamingsResource, ProjectsResource, TextbooksResource, SectionsResource, ExercisesResource, ExtractionEventsResource


app = fastapi.FastAPI(
    # We want '/reset-...' to be at the root, so can't use root_path="/api", so we have to specify these individually:
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    make_jsonapi_router([
        PingsResource(),
        PdfFilesResource(),
        PdfFileNamingsResource(),
        ProjectsResource(),
        TextbooksResource(),
        SectionsResource(),
        ExercisesResource(),
        ExtractionEventsResource(),
    ]),
    prefix="/api",
)

# Test-only URL. Not in 'api/...' to avoid accidentally exposing it.
if django.conf.settings.EXPOSE_RESET_FOR_TESTS_URL:
    @app.post("/reset-for-tests/yes-im-sure")
    def reset_for_tests(fixtures: str = None):
        django.core.management.call_command("flush", interactive=False)
        django.core.management.call_command("migrate", interactive=False)
        if fixtures is not None:
            for fixture in fixtures.split(","):
                django.core.management.call_command("loaddata", fixture)
        return {}
