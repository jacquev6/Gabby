import os

from .common import *


# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


SECRET_KEY = os.environ["GABBY_SECRET_KEY"]
DEBUG = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = 'static/'


ALLOWED_HOSTS = os.environ["GABBY_ALLOWED_HOSTS"].split(",")


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


REST_FRAMEWORK["PAGE_SIZE"] = 20
