import os

from .common import *


# Deployment checklist
# https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SILENCED_SYSTEM_CHECKS = [
    # @todo(Project management, soon) Understand and consider re-enabling these checks
    "security.W004",  # You have not set a value for the SECURE_HSTS_SECONDS setting. If your entire site is served only over SSL, you may want to consider setting a value and enabling HTTP Strict Transport Security. Be sure to read the documentation first; enabling HSTS carelessly can cause serious, irreversible problems.
    "security.W008",  # Your SECURE_SSL_REDIRECT setting is not set to True. Unless your site should be available over both SSL and non-SSL connections, you may want to either set this setting True or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.
]


SECRET_KEY = os.environ["GABBY_SECRET_KEY"]
assert len(SECRET_KEY) > 50, "The secret key is too short"  # Required by './manage.py check --deploy'
DEBUG = False


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


EXPOSE_RESET_FOR_TESTS_URL = os.environ.get("GABBY_EXPOSE_RESET_FOR_TESTS_URL") == "yes-i-m-sure--it-s-not-really-prod"


# @todo(Project management, soon) Make sure I'm notified by e-mail on 500s
# @todo(Project management, soon) Make sure I'm notified by e-mail on exceptions during backup
