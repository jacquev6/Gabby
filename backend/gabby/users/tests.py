import datetime
import time

import argon2
from fastapi import Depends
import jwt

from .user import User, UserEmailAddress, UsersResource, ActuallyMandatoryAuthenticatedUserDependable, OptionalAuthenticatedUserDependable
from .. import testing


class AuthenticationTestCase(testing.TransactionTestCase):
    def setUp(self):
        super().setUp()
        self.create_model(User, username="john", clear_text_password="password")
        self.create_model(User, username="no-password", clear_text_password=None)
        self.expect_commits_rollbacks(0, 0)

    def test_check_password__wrong(self):
        self.assertFalse(self.get_model(User, 2).check_password("not-the-password"))

    def test_check_password__right(self):
        self.assertTrue(self.get_model(User, 2).check_password("password"))

    def test_check_password__no_password(self):
        self.assertFalse(self.get_model(User, 3).check_password("whatever"))

    def test_hashed_password(self):
        self.assertTrue(self.get_model(User, 2).hashed_password.startswith("$argon2id$v=19$m=65536,t=3,p=4$"))

    def test_rehash_password(self):
        old_password_hasher = argon2.PasswordHasher(time_cost=1, memory_cost=1024, parallelism=1)
        user = self.get_model(User, 2)
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
        def get(user: OptionalAuthenticatedUserDependable):
            if user is None:
                return None
            else:
                return {"id": user.id, "username": user.username}

        @cls.api_app.get("/mandatory-authenticated")
        def get(user: ActuallyMandatoryAuthenticatedUserDependable):
            return {"id": user.id, "username": user.username}

    def setUp(self):
        super().setUp()
        self.create_model(
            UserEmailAddress,
            user=self.create_model(User, username="john", clear_text_password="password"),
            address="john@example.com",
        )
        self.create_model(
            UserEmailAddress,
            user=self.create_model(User, username=None, clear_text_password="anonymous-1"),
            address="anonymous-1@example.com",
        )
        self.create_model(
            UserEmailAddress,
            user=self.create_model(User, username=None, clear_text_password="anonymous-2"),
            address="anonymous-2@example.com",
        )

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
        self.assertEqual(response.status_code, 403, response.json())
        self.assertEqual(response.json(), {"detail": "Incorrect username or password"})

    def test_non_existing_user(self):
        self.expect_rollback()

        response = self.api_client.post("http://server/token", data={"username": "bob", "password": "password"})
        self.assertEqual(response.status_code, 403, response.json())
        self.assertEqual(response.json(), {"detail": "Incorrect username or password"})

    def test_password_flow_using_username(self):
        self.expect_commits_rollbacks(3, 0)

        response = self.api_client.post("http://server/token", data={"username": "john", "password": "password"})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self.api_client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"id": 2, "username": "john"})

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"id": 2, "username": "john"})

    def test_password_flow_using_email_address_for_named_user(self):
        self.expect_commits_rollbacks(2, 0)

        response = self.api_client.post("http://server/token", data={"username": "john@example.com", "password": "password"})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"id": 2, "username": "john"})

    def test_password_flow_using_email_address_for_anonymous_1_user(self):
        self.expect_commits_rollbacks(2, 0)

        response = self.api_client.post("http://server/token", data={"username": "anonymous-1@example.com", "password": "anonymous-1"})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"id": 3, "username": None})

    def test_password_flow_using_email_address_for_anonymous_2_user(self):
        self.expect_commits_rollbacks(2, 0)

        response = self.api_client.post("http://server/token", data={"username": "anonymous-2@example.com", "password": "anonymous-2"})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"id": 4, "username": None})

    def test_password_flow_using_email_address_for_non_existing_user(self):
        self.expect_commits_rollbacks(0, 1)

        response = self.api_client.post("http://server/token", data={"username": "nope@example.com", "password": "password"})
        self.assertEqual(response.status_code, 403, response.json())

    def test_token_expiration(self):
        self.expect_commits_rollbacks(4, 1)

        response = self.api_client.post("http://server/token", data={"username": "john", "password": "password", "options": '{"validity": "PT1S"}'})
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        response = self.api_client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"id": 2, "username": "john"})

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {"id": 2, "username": "john"})

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

        self.delete_model(User, 2)

        response = self.api_client.get("http://server/optional-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), None)

        response = self.api_client.get("http://server/mandatory-authenticated", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 401, response.json())

    def test_token_tempered__validity(self):
        self.expect_commits_rollbacks(2, 1)

        before = datetime.datetime.now(tz=datetime.timezone.utc)
        # Request a token with longer-than-default validity
        response = self.api_client.post("http://server/token", data={"username": "john", "password": "password", "options": '{"validity": "PT24H"}'})
        after = datetime.datetime.now(tz=datetime.timezone.utc)
        self.assertEqual(response.status_code, 200, response.json())
        token = response.json()["access_token"]

        # Validity is still the default one
        token = jwt.decode(token, options={"verify_signature": False})
        valid_until = datetime.datetime.fromisoformat(token["validUntil"])
        self.assertLessEqual(before + datetime.timedelta(hours=20), valid_until)
        self.assertLessEqual(valid_until, after + datetime.timedelta(hours=20))

        self.assertEqual(token, {
            "userId": 2,
            "validUntil": valid_until.isoformat(),
        })
        # Try to set 'validUntil' in the token
        tempered_token = jwt.encode(
            {
                "userId": 2,
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

    def test_token_tempered__user_id(self):
        self.expect_commits_rollbacks(2, 1)

        response = self.api_client.post("http://server/token", data={"username": "john", "password": "password"})
        self.assertEqual(response.status_code, 200, response.json())
        token = jwt.decode(response.json()["access_token"], options={"verify_signature": False})
        valid_until = token["validUntil"]

        self.assertEqual(token, {
            "userId": 2,
            "validUntil": valid_until,
        })
        # Try to set 'userId' in the token
        tempered_token = jwt.encode(
            {
                "userId": 3,
                "validUntil": valid_until,
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


class UsersApiTestCase(testing.ApiTestCase):
    resources = [UsersResource]
    polymorphism = {}

    def setUp(self):
        super().setUp()
        self.john = self.create_model(User, username="john", clear_text_password="password")
        self.create_model(UserEmailAddress, user=self.john, address="john@example.com")
        self.john_created_at = self.john.created_at.isoformat().replace("+00:00", "Z")
        self.john_updated_at = self.john.updated_at.isoformat().replace("+00:00", "Z")
        self.anonymous = self.create_model(User, username=None, clear_text_password="anonymous")
        self.create_model(UserEmailAddress, user=self.anonymous, address="anonymous@example.com")
        self.anonymous_created_at = self.anonymous.created_at.isoformat().replace("+00:00", "Z")
        self.anonymous_updated_at = self.anonymous.updated_at.isoformat().replace("+00:00", "Z")

    def test_get_named_by_id(self):
        response = self.get("http://server/users/ckylfa")
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "user",
                "id": "ckylfa",
                "links": {
                    "self": "http://server/users/ckylfa",
                },
                "attributes": {
                    "username": "john",
                    "createdAt": self.john_created_at,
                    "updatedAt": self.john_updated_at,
                },
                "relationships": {
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
        })

    def test_get_anonymous_by_id(self):
        response = self.get("http://server/users/jahykn")
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "user",
                "id": "jahykn",
                "links": {
                    "self": "http://server/users/jahykn",
                },
                "attributes": {
                    "username": None,
                    "createdAt": self.anonymous_created_at,
                    "updatedAt": self.anonymous_updated_at,
                },
                "relationships": {
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
        })

    def test_get_named_by_current(self):
        self.expect_commits_rollbacks(2, 0)

        self.login("john", "password")
        response = self.get("http://server/users/current")
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "user",
                "id": "ckylfa",
                "links": {
                    "self": "http://server/users/ckylfa",
                },
                "attributes": {
                    "username": "john",
                    "createdAt": self.john_created_at,
                    "updatedAt": self.john_updated_at,
                },
                "relationships": {
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
        })

    def test_get_anonymous_by_current(self):
        self.expect_commits_rollbacks(2, 0)

        self.login("anonymous@example.com", "anonymous")
        response = self.get("http://server/users/current")
        self.assertEqual(response.status_code, 200, response.json())
        self.assertEqual(response.json(), {
            "data": {
                "type": "user",
                "id": "jahykn",
                "links": {
                    "self": "http://server/users/jahykn",
                },
                "attributes": {
                    "username": None,
                    "createdAt": self.anonymous_created_at,
                    "updatedAt": self.anonymous_updated_at,
                },
                "relationships": {
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "fvirvd"}},
                },
            },
        })

    def test_patch_current__username(self):
        self.expect_commits_rollbacks(2, 0)

        self.login("anonymous@example.com", "anonymous")

        payload = {
            "data": {
                "type": "user",
                "id": "current",
                "attributes": {
                    "username": "jane",
                },
            },
        }
        response = self.patch("http://server/users/current", payload)
        self.assertEqual(response.status_code, 200, response.json())
        updated_at = response.json()["data"]["attributes"]["updatedAt"]
        self.assertGreater(datetime.datetime.fromisoformat(updated_at), datetime.datetime.fromisoformat(self.anonymous_created_at))
        self.assertEqual(response.json(), {
            "data": {
                "type": "user",
                "id": "jahykn",
                "links": {
                    "self": "http://server/users/jahykn",
                },
                "attributes": {
                    "username": "jane",
                    "createdAt": self.anonymous_created_at,
                    "updatedAt": updated_at
                },
                "relationships": {
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "jahykn"}},
                },
            },
        })

    def test_patch_current__password(self):
        self.expect_commits_rollbacks(3, 0)

        self.login("anonymous@example.com", "anonymous")

        payload = {
            "data": {
                "type": "user",
                "id": "current",
                "attributes": {
                    "clearTextPassword": "new-password",
                },
            },
        }
        response = self.patch("http://server/users/current", payload)
        self.assertEqual(response.status_code, 200, response.json())
        updated_at = response.json()["data"]["attributes"]["updatedAt"]
        self.assertGreater(datetime.datetime.fromisoformat(updated_at), datetime.datetime.fromisoformat(self.anonymous_created_at))
        self.assertEqual(response.json(), {
            "data": {
                "type": "user",
                "id": "jahykn",
                "links": {
                    "self": "http://server/users/jahykn",
                },
                "attributes": {
                    "username": None,
                    "createdAt": self.anonymous_created_at,
                    "updatedAt": updated_at
                },
                "relationships": {
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "jahykn"}},
                },
            },
        })

        self.login("anonymous@example.com", "new-password")

    def test_patch_current__unauthenticated(self):
        self.expect_rollback()

        payload = {
            "data": {
                "type": "user",
                "id": "current",
                "attributes": {
                    "username": "jane",
                },
            },
        }
        response = self.patch("http://server/users/current", payload)
        self.assertEqual(response.status_code, 401, response.json())
        self.assertEqual(response.json(), {"detail": "Invalid or expired token"})

    def test_patch_by_id__self(self):
        self.expect_commits_rollbacks(2, 0)

        self.login("anonymous@example.com", "anonymous")

        payload = {
            "data": {
                "type": "user",
                "id": "current",
                "attributes": {
                    "username": "jane",
                },
            },
        }
        response = self.patch("http://server/users/jahykn", payload)
        self.assertEqual(response.status_code, 200, response.json())
        updated_at = response.json()["data"]["attributes"]["updatedAt"]
        self.assertGreater(datetime.datetime.fromisoformat(updated_at), datetime.datetime.fromisoformat(self.anonymous_created_at))
        self.assertEqual(response.json(), {
            "data": {
                "type": "user",
                "id": "jahykn",
                "links": {
                    "self": "http://server/users/jahykn",
                },
                "attributes": {
                    "username": "jane",
                    "createdAt": self.anonymous_created_at,
                    "updatedAt": updated_at
                },
                "relationships": {
                    "createdBy": {"data": {"type": "user", "id": "fvirvd"}},
                    "updatedBy": {"data": {"type": "user", "id": "jahykn"}},
                },
            },
        })

    def test_patch_by_id__someone_else(self):
        self.expect_commits_rollbacks(1, 1)

        self.login("anonymous@example.com", "anonymous")

        payload = {
            "data": {
                "type": "user",
                "id": "current",
                "attributes": {
                    "username": "jane",
                },
            },
        }
        response = self.patch("http://server/users/ckylfa", payload)
        self.assertEqual(response.status_code, 403, response.json())
        self.assertEqual(response.json(), {'detail': 'You can only edit your own user'})
