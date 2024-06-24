import dataclasses
import datetime
import re
import unittest.mock
import uuid

from fastapi import BackgroundTasks, Depends
import jwt
import sqlalchemy as sql

from .. import mailing
from .. import settings
from .. import testing
from ..api_models import RecoveryEmailRequest
from ..database_utils import Session, SessionDependable
from .user import User, UserEmailAddress, make_access_token, WanabeMandatoryAuthenticatedUserDependable


@dataclasses.dataclass
class RecoveryEmailRequestItem:
    id: str


def maybe_send_recovery_email(session: Session, address: str, language: str):
    user = session.execute(sql.select(User).join(UserEmailAddress).filter(UserEmailAddress.address == address)).scalar()
    if user is not None:
        token = make_access_token(user, datetime.timedelta(hours=1))[0]
        link = f"{settings.ROOT_URL}/reset-password/{address}/{token}"
        if language == "fr":
            subject = "MALIN - récupération de mot de passe"
            body = f"Vous avez demandé à réinitialiser votre mot de passe. Cliquez sur ce lien pour continuer: {link}. Lien valable une heure."
        else:
            subject = "MALIN - password recovery"
            body = f"You requested to reset your password. Click on this link to continue: {link}. Link valid for one hour."
        mailing.send_mail(address, subject, body)


class RecoveryEmailRequestsResource:
    singular_name = "recovery_email_request"
    plural_name = "recovery_email_requests"

    Model = RecoveryEmailRequest

    default_page_size = settings.GENERIC_DEFAULT_API_PAGE_SIZE

    def create_item(
        self,
        address: str,
        language: str,
        session: SessionDependable,
        background_tasks: BackgroundTasks,
    ):
        background_tasks.add_task(maybe_send_recovery_email, session, address, language)
        return RecoveryEmailRequestItem(id=uuid.uuid4().hex)

    def get_item(
        self,
        id,
        authenticated_user: WanabeMandatoryAuthenticatedUserDependable,
    ):
        return None


class RecoveryEmailRequestsApiTestCase(testing.ApiTestCase):
    resources = [RecoveryEmailRequestsResource()]
    polymorphism = {}

    def setUp(self):
        super().setUp()
        self.create_model(UserEmailAddress, user=self.create_model(User, clear_text_password="password"), address="john@example.com")

    def test_existing_user(self):
        payload = {
            "data": {
                "type": "recovery_email_requests",
                "attributes": {
                    "address": "john@example.com",
                    "language": "en",
                },
            },
        }
        before = datetime.datetime.now(tz=datetime.timezone.utc)
        with unittest.mock.patch("gabby.mailing.send_mail") as send_mail:
            response = self.post("http://server/recoveryEmailRequests", payload)
        after = datetime.datetime.now(tz=datetime.timezone.utc)
        self.assertEqual(response.status_code, 201, response.json())
        ident = response.json()["data"]["id"]
        self.assertEqual(response.json(), {
            "data": {
                "type": "recoveryEmailRequest",
                "id": ident,
                "links": {"self": f"http://server/recoveryEmailRequests/{ident}"},
            }
        })

        send_mail.assert_called_once()
        args = send_mail.call_args.args
        self.assertEqual(len(args), 3)
        self.assertEqual(args[0], "john@example.com")
        self.assertEqual(args[1], "MALIN - password recovery")
        m = re.fullmatch(
            r"You requested to reset your password\. Click on this link to continue: http://localhost:8080/reset-password/john@example.com/(.*)\. Link valid for one hour\.",
            args[2],
        )
        self.assertTrue(m)
        token = jwt.decode(m.group(1), options={"verify_signature": False})
        valid_until = datetime.datetime.fromisoformat(token["validUntil"])
        self.assertLessEqual(before + datetime.timedelta(hours=1), valid_until)
        self.assertLessEqual(valid_until, after + datetime.timedelta(hours=1))
        self.assertEqual(token, {
            "userId": 2,
            "validUntil": valid_until.isoformat(),
        })

    def test_non_existing_user(self):
        payload = {
            "data": {
                "type": "recovery_email_requests",
                "attributes": {
                    "address": "not-john@example.com",
                    "language": "en",
                },
            },
        }
        with unittest.mock.patch("gabby.mailing.send_mail") as send_mail:
            response = self.post("http://server/recoveryEmailRequests", payload)
        self.assertEqual(response.status_code, 201, response.json())
        ident = response.json()["data"]["id"]
        self.assertEqual(response.json(), {
            "data": {
                "type": "recoveryEmailRequest",
                "id": ident,
                "links": {"self": f"http://server/recoveryEmailRequests/{ident}"},
            }
        })

        send_mail.assert_not_called()
