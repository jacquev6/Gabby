from .common import *


SECRET_KEY = "not-a-secret"
DEBUG = True
ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "gabby",
        "USER": "gabby",
        "PASSWORD": "password",
        "HOST": "db",
    },
}
