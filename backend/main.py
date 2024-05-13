import json

import django
django.setup()  # Required before importing any module that uses the Django ORM

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import django.conf
import django.contrib.auth
import django.core.management

from fastjsonapi import make_jsonapi_router
from fastjsonapi.django import AuthenticationToken, make_wrapper
from opinion_ping.resources import PingsResource
from textbooks.models import Project, SelectThingsAdaptation, FillWithFreeTextAdaptation
from textbooks.resources import PdfFilesResource, PdfFileNamingsResource, ProjectsResource, TextbooksResource, SectionsResource, ExercisesResource, ExtractionEventsResource
from textbooks.resources import SelectThingsAdaptationsResource, FillWithFreeTextAdaptationsResource
from textbooks.resources import AdaptedExerciseResource
from textbooks.views import make_extraction_report


User = django.contrib.auth.get_user_model()

app = FastAPI(
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
    make_jsonapi_router(
        resources=[
            PingsResource(),
            PdfFilesResource(),
            PdfFileNamingsResource(),
            ProjectsResource(),
            TextbooksResource(),
            SectionsResource(),
            ExercisesResource(),
            ExtractionEventsResource(),
            SelectThingsAdaptationsResource(),
            FillWithFreeTextAdaptationsResource(),
            AdaptedExerciseResource(),
        ],
        polymorphism={
            make_wrapper(SelectThingsAdaptation): "select_things_adaptation",
            make_wrapper(FillWithFreeTextAdaptation): "fill_with_free_text_adaptation",
        },
    ),
    prefix="/api",
)

@app.get("/api/project-{project_id}-extraction-report.json")
def extraction_report(project_id: int):
    return make_extraction_report(project_id)

@app.get("/api/project-{project_id}.html")
def export_project(project_id: int):
    project = Project.objects.get(id=project_id)
    exercises = {}
    for exercise in project.exercises.all():
        if exercise.adaptation is not None:
            exercises[exercise.id] = exercise.adaptation.make_adapted().model_dump()
    data = json.dumps(dict(
        projectId=project.id,
        exercises=exercises,
    )).replace("\\", "\\\\").replace('"', "\\\"")
    with open("textbooks/templates/adapted/index.html") as f:
        template = f.read()
    return HTMLResponse(
        content=template.replace("{{ data }}", data),
        headers={
            "Content-Type": "text/html",
            "Content-Disposition": f'attachment; filename="{project.title}.html"',
        },
    )

@app.post("/api/token")
def login(access_token: AuthenticationToken):
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

# Test-only URL. Not in 'api/...' to avoid accidentally exposing it.
if django.conf.settings.EXPOSE_RESET_FOR_TESTS_URL:
    @app.post("/reset-for-tests/yes-im-sure")
    def reset_for_tests(fixtures: str = None):
        django.core.management.call_command("flush", interactive=False)
        django.core.management.call_command("migrate", interactive=False)
        django.core.management.call_command("loaddata", "test-users")
        if fixtures is not None:
            for fixture in fixtures.split(","):
                django.core.management.call_command("loaddata", fixture)
        return {}

if django.conf.settings.DEBUG:
    with open("openapi.json", "w") as file:
        json.dump(app.openapi(), file, indent=2, sort_keys=True)
        file.write("\n")
