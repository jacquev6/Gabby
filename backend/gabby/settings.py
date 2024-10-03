import logging
import os


ROOT_URL = os.environ["GABBY_ROOT_URL"]
assert not ROOT_URL.endswith("/")

DATABASE_URL = os.environ["GABBY_DATABASE_URL"]
SECRET_KEY = os.environ["GABBY_SECRET_KEY"]
DATABASE_BACKUPS_URL = os.environ["GABBY_DATABASE_BACKUPS_URL"]
assert not DATABASE_BACKUPS_URL.endswith("/")

DEBUG = os.environ.get("GABBY_DEBUG", "false") == "true"
EXPOSE_RESET_FOR_TESTS_URL = os.environ.get("GABBY_EXPOSE_RESET_FOR_TESTS_URL", "false") == "true"

GENERIC_DEFAULT_API_PAGE_SIZE = int(os.environ.get("GABBY_GENERIC_DEFAULT_API_PAGE_SIZE", 20))

if not DEBUG:
    assert len(SECRET_KEY) > 50

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO

MAIL_SENDER = os.environ["GABBY_MAIL_SENDER"]
SMTP_HOST = os.environ["GABBY_SMTP_HOST"]
SMTP_PORT = int(os.environ["GABBY_SMTP_PORT"])
SMTP_USER = os.environ["GABBY_SMTP_USER"]
SMTP_PASSWORD = os.environ["GABBY_SMTP_PASSWORD"]
