import django.conf
import django.core.management
import fastapi


django.setup()


app = fastapi.FastAPI()


# Test-only URL. Not in 'api/...' to avoid accidentally exposing it.
if django.conf.settings.EXPOSE_RESET_FOR_TESTS_URL:
    @app.post("/reset-for-tests/yes-im-sure")
    def reset_for_tests(fixtures: str = None):
        django.core.management.call_command("flush", interactive=False)
        django.core.management.call_command("migrate", interactive=False)
        if fixtures is not None:
            for fixture in fixtures.split(","):
                django.core.management.call_command("loaddata", fixture)
        return {}
