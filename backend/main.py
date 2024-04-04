import json

import django
django.setup()  # Required before importing any module that uses the Django ORM

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import django.conf
import django.contrib.auth
import django.core.management
import jinja2

from fastjsonapi import make_jsonapi_router
from fastjsonapi.django import AuthenticationToken
from opinion_ping.resources import PingsResource
from textbooks.models import Project, Exercise
from textbooks.resources import PdfFilesResource, PdfFileNamingsResource, ProjectsResource, TextbooksResource, SectionsResource, ExercisesResource, ExtractionEventsResource
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

@app.get("/api/project-{project_id}-extraction-report.json")
def extraction_report(project_id: int):
    return make_extraction_report(project_id)

env = jinja2.Environment(
    loader=jinja2.PackageLoader("textbooks"),
)
template = env.get_template("adapted.html")

@app.get("/api/project-{project_id}.html")
def export_project(project_id: int):
    project = Project.objects.get(id=project_id)
    exercises = []
    for exercise in project.exercises.all():
        try:
            adapted = exercise.adapted
        except Exercise.adapted.RelatedObjectDoesNotExist:
            pass
        else:
            exercises.append({
                "number": exercise.number,
                "textbookPage": exercise.textbook_page,
                "instructions": exercise.instructions,
                "wording": exercise.wording,
                "adaptation": adapted.make_adaptation_dict(),
            })
    data = json.dumps({
        "exercises": {str(k): v for k, v in enumerate(exercises)}
    }).replace("\\", "\\\\").replace('"', "\\\"")
    print(data)
    return HTMLResponse(template.render(data=data))

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
        superuser = User.objects.filter(username="admin").first()
        if superuser is None:
            superuser = User.objects.create_superuser(
                "admin",
                email="admin@localhost",
                password="password",
            )
        if fixtures is not None:
            for fixture in fixtures.split(","):
                django.core.management.call_command("loaddata", fixture)
        return {}
