from django.urls import register_converter
from hashids import Hashids

from .converters import HASH_ID_REGEX, HASH_ID_SETTINGS

hashids = Hashids(**HASH_ID_SETTINGS)


class HashidsConverter:
    regex = HASH_ID_REGEX

    @staticmethod
    def encode_id(id):
        return hashids.encode(id)

    @staticmethod
    def decode_id(id):
        decoded_values = hashids.decode(id)

        if len(decoded_values) != 1:
            raise ValueError
        return decoded_values[0]

    def to_python(self, value: str):
        return HashidsConverter.decode_id(value)

    def to_url(self, value):
        return HashidsConverter.encode_id(value)


url_converters = {"hashids": HashidsConverter}


def register_custom_url_converters():
    for name, klass in url_converters.items():
        register_converter(klass, name)
