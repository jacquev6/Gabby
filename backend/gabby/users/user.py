from typing import Annotated
import datetime
import json

from fastapi import Depends, Form, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, ConfigDict
from sqlalchemy import orm
from starlette import status
import argon2
import jwt
import sqlalchemy as sql

from fastjsonapi.sqlalchemy import set_wrapper, OrmWrapperWithStrIds, wrap

from .. import settings
from ..database_utils import OrmBase, Session, session_dependable


# Tests for this code are in an other file ('.tests') to break a circular dependency with '..testing'


class User(OrmBase):
    __tablename__ = "users"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column()
    hashed_password: orm.Mapped[str] = orm.mapped_column()

    def __init__(self, *, clear_text_password, **kwds):
        super().__init__(hashed_password=self.hash_password(clear_text_password), **kwds)

    __password_hasher = argon2.PasswordHasher()

    def hash_password(self, clear_text_password):
        return self.__password_hasher.hash(clear_text_password)

    def check_password(self, clear_text_password):
        try:
            self.__password_hasher.verify(self.hashed_password, clear_text_password)
        except argon2.exceptions.VerifyMismatchError:
            return False
        else:
            if self.__password_hasher.check_needs_rehash(self.hashed_password):
                self.hashed_password = self.hash_password(clear_text_password)
            return True


class UserModel(BaseModel):
    username: str


class UsersResource:
    singular_name = "user"
    plural_name = "users"

    Model = UserModel

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    class ItemGetter:
        def __init__(self, session: Session = Depends(session_dependable)) -> None:
            self.__session = session

        def __call__(self, id):
            return wrap(self.__session.get(User, id))


set_wrapper(User, OrmWrapperWithStrIds)


def authenticate(session, *, username, clear_text_password):
    user = session.execute(sql.select(User).filter(User.username == username)).scalar()
    if user is None:
        # Do one round of hashing to mitigate timing attacks
        User().check_password(clear_text_password)
        return None
    else:
        if user.check_password(clear_text_password):
            return user
        else:
            return None


def authentication_token_dependable(
    credentials: Annotated[OAuth2PasswordRequestForm, Depends()],
    options: Annotated[str | None, Form()] = None,
    session: Session = Depends(session_dependable),
):
    user = authenticate(session, username=credentials.username, clear_text_password=credentials.password)
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
    return jwt.encode(token, settings.SECRET_KEY, algorithm="HS256")


def optional_authenticated_user_dependable(
    token: str | None = Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False)),
    session: Session = Depends(session_dependable),
):
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
                user = session.execute(sql.select(User).filter(User.username == token["username"])).scalar()
                if user is None:
                    # User not found despite having a valid token: user was deleted => silently unauthenticated
                    return None
                else:
                    return user
            else:
                # Expired token => silently unauthenticated
                return None


def mandatory_authenticated_user_dependable(
    user: User | None = Depends(optional_authenticated_user_dependable),
):
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    else:
        return user
