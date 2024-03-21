import datetime
import json
from typing import Annotated

import django
django.setup()  # Required before importing any module that uses the Django ORM

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from fastapi import Depends, FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, ConfigDict
import django.conf
import django.core.management
import jwt

from fastjsonapi import make_jsonapi_router
from opinion_ping.resources import PingsResource
from textbooks.resources import PdfFilesResource, PdfFileNamingsResource, ProjectsResource, TextbooksResource, SectionsResource, ExercisesResource, ExtractionEventsResource
from textbooks.views import make_extraction_report


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


@app.post("/api/token")
def login(
    credentials: Annotated[OAuth2PasswordRequestForm, Depends()],
    options: Annotated[str | None, Form()] = None,
):
    user = authenticate(username=credentials.username, password=credentials.password)
    if user is None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    default_validity = datetime.timedelta(hours=1)
    class Options(BaseModel):
        model_config = ConfigDict(extra="forbid")

        validity: datetime.timedelta = default_validity

    options = Options(**({} if options is None else json.loads(options)))
    options.validity = min(options.validity, default_validity)
    token = {
        "username": user.username,
        "validUntil": (datetime.datetime.now(tz=datetime.timezone.utc) + options.validity).isoformat(),
    }
    return {
        "access_token": jwt.encode(token, django.conf.settings.SECRET_KEY, algorithm="HS256"),
        "token_type": "bearer",
    }

def inject_authenticated_user(token: Annotated[str | None, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))]):
    if token is None:
        # No token => unauthenticated
        return None
    else:
        try:
            token = jwt.decode(token, django.conf.settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.exceptions.InvalidTokenError:
            # Corrupted token => silently unauthenticated
            return None
        else:
            if datetime.datetime.now(tz=datetime.timezone.utc) < datetime.datetime.fromisoformat(token["validUntil"]):
                return User.objects.get(username=token["username"])
            else:
                # Expired token => silently unauthenticated
                return None

AuthenticatedUser = Annotated[User | None, Depends(inject_authenticated_user)]

@app.get("/api/authenticated-user")
def get_authenticated_user(authenticated_user: AuthenticatedUser):
    if authenticated_user is None:
        return {
            "data": None,
        }
    else:
        return {
            "data": {
                "username": authenticated_user.username,
            },
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
