from .common import *


SECRET_KEY = "not-so-secret"

DEBUG = True

ALLOWED_HOSTS = ["localhost", "fanout"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db",
        "USER": "admin",
        "PASSWORD": "password",
        "HOST": "db",
    },
}

EXPOSE_RESET_FOR_TESTS_URL = True

DBBACKUP_STORAGE = "django.core.files.storage.FileSystemStorage"
DBBACKUP_STORAGE_OPTIONS = {"location": "/app/dev-env/backups/"}
