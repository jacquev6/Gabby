import json

from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from fastjsonapi import make_jsonapi_router

from . import database_utils
from . import settings
from .fixtures import load as load_fixtures
from .projects import Project, ProjectsResource
from .exercises import Exercise
from .users import authentication_token_dependable
from . import api_resources


app = FastAPI(
    # We want '/reset-...' to be at the root, so can't use root_path="/api", so we have to specify these individually:
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    make_session=database_utils.SessionMaker(database_utils.create_engine(settings.DATABASE_URL)),
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
        resources=api_resources.resources,
        polymorphism=api_resources.polymorphism,
    ),
    prefix="/api",
)

@app.get("/api/project-{project_id}-extraction-report.json")
def extraction_report(project_id: str, session: database_utils.Session = Depends(database_utils.session_dependable)):
    project = session.get(Project, ProjectsResource.sqids.decode(project_id)[0])
    return {
        "project": {
            "title": project.title,
            "textbooks": [
                {
                    "title": textbook.title,
                    "exercises": [
                        {
                            "page": exercise.textbook_page,
                            "number": exercise.number,
                            "events": [
                                json.loads(event.event)
                                for event in exercise.extraction_events
                            ],
                        }
                        for exercise in session.query(Exercise).filter_by(project=project, textbook=textbook).order_by(Exercise.textbook_page, Exercise.number)
                    ],
                }
                for textbook in project.textbooks
            ],
        },
    }

@app.get("/api/project-{project_id}.html")
def export_project(project_id: str, session: database_utils.Session = Depends(database_utils.session_dependable)):
    project = session.get(Project, ProjectsResource.sqids.decode(project_id)[0])
    exercises = []
    for exercise in project.exercises:
        if exercise.adaptation is not None:
            exercises.append(exercise.adaptation.make_adapted().model_dump())
    data = json.dumps(dict(
        projectId=project.id,
        exercises=exercises,
    )).replace("\\", "\\\\").replace('"', "\\\"")
    with open("gabby/templates/adapted/index.html") as f:
        template = f.read()
    return HTMLResponse(
        content=template.replace("{{ data }}", data),
        headers={
            "Content-Type": "text/html",
            "Content-Disposition": f'attachment; filename="{project.title}.html"',
        },
    )

@app.post("/api/token")
def login(access_token: str = Depends(authentication_token_dependable)):
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

# Test-only URL. Not in 'api/...' to avoid accidentally exposing it.
if settings.EXPOSE_RESET_FOR_TESTS_URL:
    @app.post("/reset-for-tests/yes-im-sure")
    def reset_for_tests(fixtures: str = None, session: database_utils.Session = Depends(database_utils.session_dependable)):
        load_fixtures(session, [] if fixtures is None else fixtures.split(","))
        return {}


if settings.DEBUG:
    with open("openapi.json", "w") as file:
        json.dump(app.openapi(), file, indent=2, sort_keys=True)
        file.write("\n")
