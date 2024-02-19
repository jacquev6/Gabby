import os

from .common import *


SECRET_KEY = "not-a-secret"
DEBUG = True


ALLOWED_HOSTS = os.environ["GABBY_ALLOWED_HOSTS"].split(",")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'api/static/'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["GABBY_DB_NAME"],
        "USER": os.environ["GABBY_DB_USER"],
        "PASSWORD": os.environ["GABBY_DB_PASSWORD"],
        "HOST": os.environ["GABBY_DB_HOST"],
    },
}
