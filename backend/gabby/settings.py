import os


DATABASE_URL = os.environ["GABBY_DATABASE_URL"]
SECRET_KEY = os.environ["GABBY_SECRET_KEY"]

DEBUG = os.environ.get("GABBY_DEBUG", "false") == "true"
EXPOSE_RESET_FOR_TESTS_URL = os.environ.get("GABBY_EXPOSE_RESET_FOR_TESTS_URL", "false") == "true"

GENERIC_DEFAULT_API_PAGE_SIZE = int(os.environ.get("GABBY_GENERIC_DEFAULT_API_PAGE_SIZE", 20))
