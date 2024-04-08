from typing import Annotated
import argon2
import datetime
import functools
import json
import time

from django.conf import settings
from django.contrib.auth import authenticate
from django.db import models
from django.test import TransactionTestCase
from fastapi import Depends, FastAPI, Form, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.testclient import TestClient
from pydantic import BaseModel, ConfigDict
from starlette import status
import django.contrib.auth
import jwt


User = django.contrib.auth.get_user_model()


class DjangoOrmWrapper:
    __slots__ = ["_wrapped"]

    def __init__(self, wrapped):
        self._wrapped = wrapped

    @property
    def id(self):
        return str(self._wrapped.id)

    def __getattr__(self, name):
        attr = getattr(self._wrapped, name)
        if attr.__class__.__name__ == "RelatedManager":
            return [wrap(item) for item in attr.all()]
        elif isinstance(attr, models.Model):
            return wrap(attr)
        else:
            return attr

    def __setattr__(self, name, value):
        if name == "_wrapped":
            super().__setattr__(name, value)
        else:
            attr = getattr(self._wrapped, name)
            if attr.__class__.__name__ == "RelatedManager":
                attr.set([unwrap(v) for v in value])
            elif isinstance(value, DjangoOrmWrapper):
                setattr(self._wrapped, name, unwrap(value))
            else:
                setattr(self._wrapped, name, value)


@functools.cache
def make_wrapper(type):
    class Wrapper(DjangoOrmWrapper):
        pass

    Wrapper.__name__ = type.__name__ + "Wrapper"

    return Wrapper


def wrap(o):
    assert o is not None
    return make_wrapper(o.__class__)(o)


def unwrap(wrapper):
    return None if wrapper is None else wrapper._wrapped


default_page_size = django.conf.settings.REST_FRAMEWORK["PAGE_SIZE"]



class UserModel(BaseModel):
    username: str


class UserResource:
    singular_name = "user"
    plural_name = "users"

    Model = UserModel

    default_page_size = default_page_size

    class ItemGetter:
        def __call__(self, id):
            try:
                return wrap(User.objects.get(id=id))
            except User.DoesNotExist:
                return None


def make_authentication_token(
    credentials: Annotated[OAuth2PasswordRequestForm, Depends()],
    options: Annotated[str | None, Form()] = None,
):
    user = authenticate(username=credentials.username, password=credentials.password)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")

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
    return jwt.encode(token, django.conf.settings.SECRET_KEY, algorithm="HS256")

AuthenticationToken = Annotated[str, Depends(make_authentication_token)]


def get_optional_authenticated_user(token: Annotated[str | None, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))]):
    if token is None:
        # No token => unauthenticated
        return None
    else:
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.exceptions.InvalidTokenError:
            # Corrupted token => silently unauthenticated
            return None
        else:
            if datetime.datetime.now(tz=datetime.timezone.utc) < datetime.datetime.fromisoformat(token["validUntil"]):
                return User.objects.get(username=token["username"])
            else:
                # Expired token => silently unauthenticated
                return None

OptionalAuthenticatedUser = Annotated[User | None, Depends(get_optional_authenticated_user)]


def get_mandatory_authenticated_user(token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=True))]):
    assert token is not None
    user = get_optional_authenticated_user(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    else:
        return user

MandatoryAuthenticatedUser = Annotated[User, Depends(get_mandatory_authenticated_user)]


class AuthenticationTestCase(TransactionTestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.__app = FastAPI()

        @cls.__app.post("/token")
        def login(access_token: AuthenticationToken):
            return {
                "access_token": access_token,
                "token_type": "bearer",
            }

        @cls.__app.get("/optional-authenticated")
        def get(authenticated_user: OptionalAuthenticatedUser = None):
            if authenticated_user is None:
                return None
            else:
                return {"username": authenticated_user.username}

        @cls.__app.get("/mandatory-authenticated")
        def get(authenticated_user: MandatoryAuthenticatedUser):
            return {"username": authenticated_user.username}

        cls.__client = TestClient(cls.__app)

    def setUp(self):
        User.objects.create_user(username="john", password="password")

    def test_credentials(self):
        user = User.objects.get(username="john")

        # We currently verify passwords using Django:
        self.assertTrue(user.check_password("password"))
        self.assertFalse(user.check_password("not-the-password"))

        # We could verify stored passwords this way if we ever decommission Django:
        self.assertEqual(user.password[:6], "argon2")
        ph = argon2.PasswordHasher()
        ph.verify(user.password[6:], "password")
        with self.assertRaises(argon2.exceptions.VerifyMismatchError):
            ph.verify(user.password[6:], "not-the-password")

    def test_rehash_password(self):
        ph = argon2.PasswordHasher(time_cost=1, memory_cost=1024, parallelism=1)
        user = User.objects.get(username="john")
        user.password = "argon2" + ph.hash("password")  # Do not use .set_password() as it would hash the hash
        user.save()

        self.assertTrue(user.password.startswith("argon2$argon2id$v=19$m=1024,t=1,p=1$"))
        self.assertTrue(user.check_password("password"))  # Triggers a re-hash
        self.assertTrue(user.password.startswith("argon2$argon2id$v=19$m=102400,t=2,p=8$"))

    def test_unauthenticated__ok_on_optional(self):
        response = self.__client.get("http://server/optional-authenticated")
        self.assertEqual(response.status_code, 200, response.json())
        self.assertIsNone(response.json())

    def test_unauthenticated__error_on_mandatory(self):
        response = self.__client.get("http://server/mandatory-authenticated")
        self.assertEqual(response.status_code, 401, response.json())

    def test_wrong_password(self):
        response = self.__client.post("http://server/token", data={"username": "john", "password": "not-the-password"})
        self.assertEqual(response.status_code, 400, response.json())
        self.assertEqual(response.json(), {"detail": "Incorrect username or password"})

    def test_password_flow(self):
        response = self.__client.post("http://server/token", data={"username": "john", "password": "password"})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self.__client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"username": "john"})

        response = self.__client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"username": "john"})

    def test_token_expiration(self):
        response = self.__client.post("http://server/token", data={"username": "john", "password": "password", "options": '{"validity": "PT1S"}'})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self.__client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"username": "john"})

        response = self.__client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"username": "john"})

        time.sleep(1)

        response = self.__client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), None)

        response = self.__client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 401, response.json())

    def test_token_tempered(self):
        before = datetime.datetime.now(tz=datetime.timezone.utc)
        # Request a token with 5h validity
        response = self.__client.post("http://server/token", data={"username": "john", "password": "password", "options": '{"validity": "PT5H"}'})
        after = datetime.datetime.now(tz=datetime.timezone.utc)
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        # Validity is still 1h
        token = jwt.decode(token, options={"verify_signature": False})
        valid_until = datetime.datetime.fromisoformat(token["validUntil"])
        self.assertLessEqual(before + datetime.timedelta(hours=1), valid_until)
        self.assertLessEqual(valid_until, after + datetime.timedelta(hours=1))

        self.assertEqual(token, {
            "username": "john",
            "validUntil": valid_until.isoformat(),
        })
        # Try to set 'validUntil' in the token
        tempered_token = jwt.encode(
            {
                "username": "john",
                "validUntil": (valid_until + datetime.timedelta(hours=24)).isoformat(),
            },
            "not-the-secret",
            algorithm="HS256",
        )

        # Be detected
        response = self.__client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {tempered_token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), None)

        response = self.__client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {tempered_token}"})
        self.assertEqual(response.status_code, 401, response.json())
