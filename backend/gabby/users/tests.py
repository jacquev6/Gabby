import datetime
import time

import argon2
from fastapi import Depends
import jwt

from .user import User, optional_authenticated_user_dependable, mandatory_authenticated_user_dependable
from .. import testing


class AuthenticationTestCase(testing.TransactionTestCase):
    def setUp(self):
        super().setUp()
        self.create_model(User, username="john", clear_text_password="password")
        self.expect_commits_rollbacks(0, 0)

    def test_check_password__wrong(self):
        self.assertFalse(self.get_model(User, 1).check_password("not-the-password"))

    def test_check_password__right(self):
        self.assertTrue(self.get_model(User, 1).check_password("password"))

    def test_hashed_password(self):
        self.assertTrue(self.get_model(User, 1).hashed_password.startswith("$argon2id$v=19$m=65536,t=3,p=4$"))

    def test_rehash_password(self):
        old_password_hasher = argon2.PasswordHasher(time_cost=1, memory_cost=1024, parallelism=1)
        user = self.get_model(User, 1)
        user.hashed_password = old_password_hasher.hash("password")

        self.assertTrue(user.hashed_password.startswith("$argon2id$v=19$m=1024,t=1,p=1$"))
        self.assertTrue(user.check_password("password"))  # Triggers a re-hash
        self.assertTrue(user.hashed_password.startswith("$argon2id$v=19$m=65536,t=3,p=4$"))


class AuthenticationApiTestCase(testing.ApiTestCase):
    resources = []
    polymorphism = {}

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        @cls.api_app.get("/optional-authenticated")
        def get(user: User | None = Depends(optional_authenticated_user_dependable)):
            if user is None:
                return None
            else:
                return {"username": user.username}

        @cls.api_app.get("/mandatory-authenticated")
        def get(user: User = Depends(mandatory_authenticated_user_dependable)):
            return {"username": user.username}

    def setUp(self):
        super().setUp()
        self.create_model(User, username="john", clear_text_password="password")

    def test_unauthenticated__ok_on_optional(self):
        response = self.api_client.get("http://server/optional-authenticated")
        self.assertEqual(response.status_code, 200, response.json())
        self.assertIsNone(response.json())

    def test_unauthenticated__error_on_mandatory(self):
        self.expect_rollback()

        response = self.api_client.get("http://server/mandatory-authenticated")
        self.assertEqual(response.status_code, 401, response.json())

    def test_wrong_password(self):
        self.expect_rollback()

        response = self.api_client.post("http://server/token", data={"username": "john", "password": "not-the-password"})
        self.assertEqual(response.status_code, 400, response.json())
        self.assertEqual(response.json(), {"detail": "Incorrect username or password"})

    def test_password_flow(self):
        self.expect_commits_rollbacks(3, 0)

        response = self.api_client.post("http://server/token", data={"username": "john", "password": "password"})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self.api_client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"username": "john"})

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"username": "john"})

    def test_token_expiration(self):
        self.expect_commits_rollbacks(4, 1)

        response = self.api_client.post("http://server/token", data={"username": "john", "password": "password", "options": '{"validity": "PT1S"}'})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self.api_client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"username": "john"})

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"username": "john"})

        time.sleep(1)

        response = self.api_client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), None)

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 401, response.json())

    def test_user_deletion(self):
        self.expect_commits_rollbacks(2, 1)

        response = self.api_client.post("http://server/token", data={"username": "john", "password": "password"})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        self.delete_model(User, 1)

        response = self.api_client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), None)

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 401, response.json())

    def test_token_tempered(self):
        self.expect_commits_rollbacks(2, 1)

        before = datetime.datetime.now(tz=datetime.timezone.utc)
        # Request a token with 5h validity
        response = self.api_client.post("http://server/token", data={"username": "john", "password": "password", "options": '{"validity": "PT5H"}'})
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
        response = self.api_client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {tempered_token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), None)

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {tempered_token}"})
        self.assertEqual(response.status_code, 401, response.json())
