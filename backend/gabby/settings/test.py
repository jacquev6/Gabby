import os

from .common import *


SECRET_KEY = "not-a-secret"
DEBUG = True


ALLOWED_HOSTS = os.environ["GABBY_ALLOWED_HOSTS"].split(",")


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/gabby-test.sqlite3",
    },
}


EXPOSE_RESET_FOR_TESTS_URL = True


# https://github.com/adamchainz/django-cors-headers

CORS_ALLOW_ALL_ORIGINS = True