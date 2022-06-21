from pathlib import Path
from datetime import timedelta


import environ

BASE_DIR = Path(__file__).resolve().parent.parent

LOCALHOSTS = ["*localhost:*", "*"]

env = environ.Env(
    DEBUG=(bool, False),
    PROD=(bool, False),
    ALLOWED_HOSTS=(list, LOCALHOSTS),
    CORS_WHITELIST=(list, LOCALHOSTS),
    CSRF_WHITELIST=(list, LOCALHOSTS),
    HASHID_SALT=(str, "DEV"),
)
env.read_env()

#############################
# General
#############################

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG", False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.User"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "django_filters",
    "corsheaders",
    "users",
    "games",
    "handles",
    "kindles",
    "notifications",
    "keen",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "rekindled.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rekindled.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CAPTCHA_SECRET_KEY = env(
    "CAPTCHA_SECRET_KEY", default="6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
)

#############################
# Security
#############################

CORS_ORIGIN_WHITELIST = env.list("CORS_WHITELIST")
CORS_ALLOW_CREDENTIALS = True

#############################
# Internationalization
#############################

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

#############################
# Static files
#############################

STATIC_ROOT = str(BASE_DIR / "static")
STATIC_URL = "/static/"

MEDIA_ROOT = str(BASE_DIR / "media")
MEDIA_URL = "/media/"

##########################
# Email
##########################

if DEBUG:
    # Send emails to memory for testing
    EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

EMAIL = {
    "FROM": env("DJANGO_FROM_EMAIL", default="noreply@example.com"),
    "REPLY_TO": env.list("DJANGO_REPLY_TO_EMAIL", default=["noreply@example.com"]),
}

EMAIL_HOST = env("EMAIL_HOST", default="localhost")
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="rekindled")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="password123")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#############################
# simplejwt
#############################

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "UPDATE_LAST_LOGIN": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

#############################
# REST Framework
#############################

DEFAULT_RENDERER_CLASSES = ("rest_framework.renderers.JSONRenderer",)

if DEBUG:
    DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + (
        "rest_framework.renderers.BrowsableAPIRenderer",
    )

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_RENDERER_CLASSES": DEFAULT_RENDERER_CLASSES,
    "DEFAULT_PAGINATION_CLASS": "rekindled.pagination.CustomPagination",
}

#############################
# hashids
#############################

HASHIDS = {"SALT": env("HASHID_SALT", "DEV"), "MIN_LENGTH": 11}
