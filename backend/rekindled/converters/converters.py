from rekindled.settings import HASHIDS


def get_hashid_settings():
    settings = {"salt": HASHIDS.get("SALT"), "min_length": HASHIDS.get("MIN_LENGTH")}

    return settings


def get_regex(settings):
    min_length = settings.get("min_length")
    if min_length:
        return f"[0-9a-zA-Z]{{{ min_length },}}"
    return "[0-9a-zA-Z]+"


HASH_ID_SETTINGS = get_hashid_settings()
HASH_ID_REGEX = get_regex(HASH_ID_SETTINGS)
