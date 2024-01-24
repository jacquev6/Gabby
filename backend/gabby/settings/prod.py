import os

from .common import *


# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = os.environ["DJANGO_ALLOWED_HOSTS"].split(",")


REST_FRAMEWORK["PAGE_SIZE"] = 20
