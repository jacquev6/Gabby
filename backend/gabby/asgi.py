import datetime
import json
import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import fastapi

from fastjsonapi import make_jsonapi_router
import fastjsonapi.openapi_utils

from . import api_resources
from . import database_utils
from . import settings
from .database_utils import SessionDependable
from .fixtures import load as load_fixtures
from .projects import Project, ProjectsResource
from .users import AuthenticationDependable, MandatoryAuthTokenDependable
from .users.user import get_optional_user_id_from_token


if os.environ.get("GABBY_UNITTESTING", "false") != "true":
    logging.basicConfig(level=settings.LOGGING_LEVEL)

logger = logging.getLogger(__name__)
logger.info("Gabby API starting up")
logger.debug("Debug logs are enabled")


app = FastAPI(
    # We want '/reset-...' to be at the root, so can't use root_path="/api", so we have to specify these individually:
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    make_session=database_utils.SessionMaker(database_utils.create_engine(settings.DATABASE_URL)),
)


app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


app.include_router(make_jsonapi_router(resources=api_resources.resources, polymorphism=api_resources.polymorphism, batching=True), prefix="/api")


@app.middleware("http")
async def log_requests_and_responses(request: fastapi.Request, call_next):
    if (request.method, request.url.path) in [
        ("POST", "/api/token"),  # Don't log clear-text passwords
        ("POST", "/api/parsedExercises"),  # Reduce volumes of logs of low interest
    ]:
        return await call_next(request)
    else:
        authorization_header = request.headers.get("authorization")
        if authorization_header is not None and authorization_header.startswith("Bearer "):
            user = get_optional_user_id_from_token(authorization_header[len("Bearer ") :])
        else:
            user = None
        body = await request.body()
        response = await call_next(request)
        # @todo Learn about log formatting (to add date automatically)
        # @todo Learn about structured logging (to keep fields structured)
        logger.info(f"{datetime.datetime.now()} user_id={user} {request.method} {request.url} {body} -> {response.status_code}")
        return response


@app.get("/api/project-{project_id}.html")
def export_project(project_id: str, session: SessionDependable, authenticated_user: MandatoryAuthTokenDependable, download: bool = True):
    project = session.get(Project, ProjectsResource.sqids.decode(project_id)[0])
    data = (
        json.dumps(dict(projectId=project.id, exercises=[exercise.make_adapted().model_dump(exclude_unset=True) for exercise in project.exercises]))
        .replace("\\", "\\\\")
        .replace('"', '\\"')
    )
    with open("gabby/templates/adapted/index.html") as f:
        template = f.read()

    headers = {"Content-Type": "text/html"}
    if download:
        headers["Content-Disposition"] = f'attachment; filename="{project.title}.html"'

    return HTMLResponse(content=template.replace("{{ data }}", data), headers=headers)


@app.post("/api/token")
def login(authentication: AuthenticationDependable):
    return authentication


# Test-only URL. Not in 'api/...' to avoid accidentally exposing it.
if settings.EXPOSE_RESET_FOR_TESTS_URL:

    @app.post("/reset-for-tests/yes-im-sure")
    def reset_for_tests(session: SessionDependable, fixtures: str = None):
        load_fixtures(session, [] if fixtures is None else fixtures.split(","))
        return {}


if settings.DEBUG:
    with open("openapi.json", "w") as file:
        json.dump(fastjsonapi.openapi_utils.stabilize(app.openapi()), file, indent=2, sort_keys=True)
        file.write("\n")
