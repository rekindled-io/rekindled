import hashlib
import unittest

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.emails import email_activation
from users.utils import decode_uid, encode_uid
from utils.testing_factories import UserFactory

User = get_user_model()


def authenticate_user(user, client):
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")


class UserBase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()

    def authenticate_user(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")


class UserDetailTest(UserBase):
    def setUp(self):
        super().setUp()
        self.url = reverse("user-detail", kwargs={"username": self.user.username})

    def test_get_user_when_anonymous(self):
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_check_user_email_is_invisible_when_anonymous(self):
        res = self.client.get(self.url)

        self.assertEqual(res.data["original_email"], "")

    def test_check_user_email_is_visible_when_authenticated(self):
        self.authenticate_user()
        res = self.client.get(self.url)

        self.assertEqual(res.data["original_email"], self.user.email)

    def test_check_user_password_is_hidden(self):
        res = self.client.get(self.url)
        password = res.data.get("password")

        self.assertEqual(password, None)

    def test_check_email_is_hashed(self):
        encoded_email = self.user.email.encode()
        hashed_email = hashlib.md5(encoded_email).hexdigest()
        res = self.client.get(self.url)

        self.assertEqual(res.data["hashed_email"], hashed_email)

    def test_check_profile_is_created(self):
        res = self.client.get(self.url)

        self.assertIsNotNone(res.data["profile"])

    def test_update_self_when_authenticated(self):
        self.authenticate_user()
        data = {"email": "thedon@pizzatime.tmnt"}
        self.client.patch(self.url, data)
        res = self.client.get(self.url)

        self.assertEqual(res.data["email"], data["email"])

    def test_update_user_when_anonymous(self):
        data = {"email": "thedon@pizzatime.tmnt"}
        res = self.client.patch(self.url, data)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_profile(self):
        self.authenticate_user()
        data = {"profile": {"bio": "i love big dripping pizzas"}}
        self.client.patch(self.url, data, format="json")
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["profile"]["bio"], data["profile"]["bio"])


class UserListTest(UserBase):
    def setUp(self):
        super().setUp()
        self.url = reverse("user-list")

    def test_create_new_user(self):
        data = {
            "username": "mikey",
            "password": "bigapple12am",
            "password_confirm": "bigapple12am",
            "email": "michelangelo@pizzatime.tmnt",
            "captcha": "cowabunga",
        }
        res = self.client.post(self.url, data)

        self.assertEquals(res.status_code, status.HTTP_201_CREATED)

    def test_fail_to_create_user_when_unmatched_password_confirm(self):
        data = {
            "username": "mikey",
            "password": "bigapple12am",
            "password_confirm": "bigapple12pm",
            "email": "michelangelo@pizzatime.tmnt",
            "captcha": "cowabunga",
        }
        res = self.client.post(self.url, data)

        self.assertTrue(res.data["password_confirm"])
        self.assertEquals(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view_list_when_anonymous(self):
        res = self.client.get(self.url)

        self.assertTrue(res.data["results"])


class UserMeTest(UserBase):
    def setUp(self):
        super().setUp()
        self.url = "/users/me/"

    def test_check_me_when_anonymous(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_check_me_when_authenticated(self):
        self.authenticate_user()
        res = self.client.get(self.url)
        self.assertEqual(res.data["username"], self.user.username)


class UserEmailTest(UserBase):
    def setUp(self):
        super().setUp()

    def test_send_activation_email(self):
        email = email_activation(self.user)
        email.send()

        self.assertEqual(mail.outbox[0].to[0], self.user.email)

    def test_ensure_new_user_is_inactive(self):
        self.assertEqual(self.user.email_confirmed, False)

    def test_activation_email_sent_on_user_creation(self):
        self.assertTrue(mail.outbox[0])
        self.assertIn(self.user.username, mail.outbox[0].body)

    def test_activate_user(self):
        token = default_token_generator.make_token(self.user)
        uid = encode_uid(self.user.username)
        url = reverse("users-activate", kwargs={"uid": uid, "token": token})
        successful_res = self.client.get(url)
        invalid_res = self.client.get(url)

        self.assertEqual(successful_res.data["status"], "success")
        self.assertEqual(self.user.email_confirmed, False)
        self.assertEqual(invalid_res.data["status"], "failed")

    def test_check_invalid_activation(self):
        url = reverse("users-activate", kwargs={"uid": "mike", "token": "a8b0c0d8e5"})
        res = self.client.get(url)

        self.assertEqual(res.data["status"], "failed")
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_check_email_recipient(self):
        email = email_activation(self.user)

        self.assertEqual(email.to, [self.user.email])

    def test_check_invalid_user_activation(self):
        self.authenticate_user()
        invalid_user = UserFactory()
        token = default_token_generator.make_token(invalid_user)
        uid = encode_uid(invalid_user.username)
        url = reverse("users-activate", kwargs={"uid": uid, "token": token})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data["status"], "failed")


class TestEncoding(unittest.TestCase):
    def setUp(self):
        self.user = "raphael"

    def test_encode_and_decoding_user(self):
        encoded_user_id = encode_uid(self.user)
        decoded_user_id = decode_uid(encoded_user_id)

        self.assertEqual(encoded_user_id, "cmFwaGFlbA")
        self.assertEqual(decoded_user_id, self.user)
