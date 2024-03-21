import datetime
import time

from django.contrib.auth.models import User
from django.test import TransactionTestCase
from fastapi.testclient import TestClient
import argon2
import jwt

from main import app


class AuthenticationTestCase(TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._client = TestClient(app)

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

    def test_unauthenticated(self):
        response = self._client.get("http://server/api/authenticated-user")
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"data": None})

    def test_wrong_password(self):
        response = self._client.post("http://server/api/token", data={"username": "john", "password": "not-the-password"})
        self.assertEqual(response.status_code, 400, response.json())
        self.assertEqual(response.json(), {"detail": "Incorrect username or password"})

    def test_password_flow(self):
        response = self._client.post("http://server/api/token", data={"username": "john", "password": "password"})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self._client.get("http://server/api/authenticated-user", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"data": {"username": "john"}})

    def test_token_expiration(self):
        response = self._client.post("http://server/api/token", data={"username": "john", "password": "password", "options": '{"validity": "PT1S"}'})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self._client.get("http://server/api/authenticated-user", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"data": {"username": "john"}})

        time.sleep(1)

        response = self._client.get("http://server/api/authenticated-user", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"data": None})

    def test_token_tempered(self):
        before = datetime.datetime.now(tz=datetime.timezone.utc)
        # Request a token with 5h validity
        response = self._client.post("http://server/api/token", data={"username": "john", "password": "password", "options": '{"validity": "PT5H"}'})
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
        response = self._client.get("http://server/api/authenticated-user", headers={"Authorization": f"Bearer {tempered_token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"data": None})
