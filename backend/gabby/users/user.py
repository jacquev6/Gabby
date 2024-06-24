from contextlib import contextmanager
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

from .. import api_models
from .. import settings
from ..api_utils import get_item, save_item
from ..database_utils import OrmBase, SessionDependable, Session
from ..wrapping import make_sqids, set_wrapper, orm_wrapper_with_sqids, unwrap, wrap


# Tests for this code are in an other file ('.tests') to break a circular dependency with '..testing'

# https://stackoverflow.com/a/17576095/905845
class WriteOnlyProperty(object):
    def __init__(self, func):
        self.func = func

    def __set__(self, obj, value):
        return self.func(obj, value)


class User(OrmBase):
    __tablename__ = "users"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    # Can't use 'CreatedUpdatedByAtMixin' because of circular dependency
    created_at: orm.Mapped[datetime.datetime] = orm.mapped_column(sql.DateTime(timezone=True), server_default=sql.func.now())
    created_by_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey("users.id"))
    created_by: orm.Mapped['User'] = orm.relationship(foreign_keys=[created_by_id], remote_side=[id], post_update=True)
    updated_at: orm.Mapped[datetime.datetime] = orm.mapped_column(sql.DateTime(timezone=True), server_default=sql.func.now(), onupdate=sql.func.now())
    updated_by_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey("users.id"))
    updated_by: orm.Mapped['User'] = orm.relationship(foreign_keys=[updated_by_id], remote_side=[id], post_update=True)

    username: orm.Mapped[str | None] = orm.mapped_column()
    hashed_password: orm.Mapped[str | None] = orm.mapped_column()

    email_addresses: orm.Mapped[list['UserEmailAddress']] = orm.relationship("UserEmailAddress", back_populates="user")

    __table_args__ = (
        # NEVER allow '@' in usernames, to avoid confusion with email addresses
        sql.CheckConstraint("regexp_like(username, '^[-_A-Za-z0-9]+$')", name="check_username"),
    )

    def __init__(self, *, clear_text_password=None, **kwds):
        super().__init__(hashed_password=self.hash_password(clear_text_password), **kwds)

    @WriteOnlyProperty
    def clear_text_password(self, value):
        self.hashed_password = self.hash_password(value)

    __password_hasher = argon2.PasswordHasher()

    @classmethod
    def hash_password(cls, clear_text_password):
        if clear_text_password is None:
            return None
        else:
            return cls.__password_hasher.hash(clear_text_password)

    def check_password(self, clear_text_password):
        if self.hashed_password is None:
            return False
        else:
            try:
                self.__password_hasher.verify(self.hashed_password, clear_text_password)
            except argon2.exceptions.VerifyMismatchError:
                return False
            else:
                if self.__password_hasher.check_needs_rehash(self.hashed_password):
                    self.hashed_password = self.hash_password(clear_text_password)
                return True


class UserEmailAddress(OrmBase):
    __tablename__ = "user_email_addresses"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    user_id: orm.Mapped[int] = orm.mapped_column(sql.ForeignKey("users.id", ondelete="CASCADE"))
    user: orm.Mapped[User] = orm.relationship("User", back_populates="email_addresses")
    address: orm.Mapped[str] = orm.mapped_column(unique=True)


def authenticate(session, *, username, clear_text_password):
    if "@" in username:
        user = session.execute(sql.select(User).join(UserEmailAddress).filter(UserEmailAddress.address == username)).scalar()
    else:
        user = session.execute(sql.select(User).filter(User.username == username)).scalar()
    if user is None:
        # Do one round of hashing to mitigate timing attacks
        User.hash_password(clear_text_password)
        return None
    else:
        if user.check_password(clear_text_password):
            return user
        else:
            return None


def make_access_token(user: User, validity: datetime.timedelta):
    valid_until = datetime.datetime.now(tz=datetime.timezone.utc) + validity
    token = {
        "userId": user.id,
        "validUntil": valid_until.isoformat(),
    }
    return (jwt.encode(token, settings.SECRET_KEY, algorithm="HS256"), valid_until)


def authentication_dependable(
    session: SessionDependable,
    credentials: Annotated[OAuth2PasswordRequestForm, Depends()],
    options: Annotated[str | None, Form()] = None,
):
    user = authenticate(session, username=credentials.username, clear_text_password=credentials.password)
    if user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect username or password")

    default_validity = datetime.timedelta(hours=20)  # Require login every morning, and token expires during the night
    class Options(BaseModel):
        model_config = ConfigDict(extra="forbid")

        validity: datetime.timedelta = default_validity

    options = Options(**({} if options is None else json.loads(options)))
    options.validity = min(options.validity, default_validity)
    (access_token, valid_until) = make_access_token(user, options.validity)
    return {
        "access_token": access_token,
        "valid_until": valid_until,
        "token_type": "bearer",
    }


AuthenticationDependable = Annotated[dict, Depends(authentication_dependable)]


def get_optional_user_from_token(session: Session, token: str | None):
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
            if datetime.datetime.now(tz=datetime.timezone.utc) > datetime.datetime.fromisoformat(token["validUntil"]):
                # Expired token => silently unauthenticated
                return None
            else:
                user = session.get(User, token["userId"])
                if user is None:
                    # User not found despite having a valid token: user was deleted => silently unauthenticated
                    return None
                else:
                    return user


def optional_auth_bearer_dependable(
    session: SessionDependable,
    token: Annotated[str | None, Depends(OAuth2PasswordBearer(tokenUrl="token", auto_error=False))],
):
    return get_optional_user_from_token(session, token)


OptionalAuthBearerDependable = Annotated[User | None, Depends(optional_auth_bearer_dependable)]


def mandatory_auth_bearer_dependable(user: OptionalAuthBearerDependable):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    else:
        return user


MandatoryAuthBearerDependable = Annotated[User, Depends(mandatory_auth_bearer_dependable)]


class UsersResource:
    singular_name = "user"
    plural_name = "users"

    Model = api_models.User

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    sqids = make_sqids(singular_name)

    def get_item(
        self,
        id,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        if id == "current":
            return wrap(authenticated_user)
        else:
            return get_item(session, User, UsersResource.sqids.decode(id)[0])

    @contextmanager
    def save_item(
        self,
        item,
        session: SessionDependable,
        authenticated_user: MandatoryAuthBearerDependable,
    ):
        if unwrap(item) != authenticated_user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only edit your own user")
        yield
        item.updated_by = authenticated_user
        save_item(session, item)


set_wrapper(User, orm_wrapper_with_sqids(UsersResource.sqids))
