from django.contrib.auth import login, logout, user_logged_in, user_logged_out
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


def encode_uid(value):
    return force_str(urlsafe_base64_encode(force_bytes(value)))


def decode_uid(value):
    return force_str(urlsafe_base64_decode(value))
