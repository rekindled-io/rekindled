from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from utils.testing_factories import UserFactory

User = get_user_model()


def authenticate_user(user, client):
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")


class BaseUserTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()


class UserDetailViewTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.url = reverse("user-detail", kwargs={"username": self.user.username})

    def test_get_user_detail(self):
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_user_when_anonymous(self):
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_check_user_email_is_invisible_when_anonymous(self):
        res = self.client.get(self.url)

        self.assertEqual(res.data["original_email"], "")

    def test_update_profile(self):
        authenticate_user(self.user, self.client)
        data = {"profile": {"bio": "griffith did nothing wrong"}}
        self.client.patch(self.url, data, format="json")
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["profile"]["bio"], data["profile"]["bio"])


class TestUserListView(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.url = reverse("user-list")

    def test_view_when_anonymous(self):
        res = self.client.get(self.url)

        self.assertTrue(res.data)
