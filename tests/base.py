import typing as t
from unittest import TestCase
from flemi import create_app
from flemi.extensions import db
from flemi.models import User


class BaseTestCase(TestCase):
    """Test case for Flemi app."""

    def setUp(self) -> None:
        """Set up test environment."""
        self.app = create_app("testing")
        self.context = self.app.test_request_context()
        self.client = self.app.test_client()
        self.context.push()
        db.drop_all()
        db.create_all()
        self.test_user = User(
            name="test",
            username="test",
            email="test@example.com"
        )
        self.test_user.set_password("password")
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self) -> None:
        """Tear down test environment."""
        db.session.remove()
        db.drop_all()
        self.context.pop()

    def set_headers(
            self, username: t.Optional[str] = "test", password: t.Optional[str] = "password"
    ):
        """Set headers for API requests."""
        response = self.client.post(
            "/auth/login",
            json={
                "username": username,
                "password": password,
            },
        )
        token = response.get_json()["auth_token"]
        self.headers = {
            "Authorization": token,
            "Accept": "application/json",
        }
