from django.conf import settings
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
import django.core.management
import django.http


urlpatterns = []

# Test-only URL. Not in 'api/...' to avoid accidentally exposing it.
if settings.EXPOSE_RESET_FOR_TESTS_URL:
    def reset_for_tests(request):
        if request.method != "POST":
            return django.http.HttpResponseNotAllowed(["POST"])
        django.core.management.call_command("flush", interactive=False)
        django.core.management.call_command("migrate", interactive=False)
        for fixture in request.GET.getlist("fixtures"):
            django.core.management.call_command("loaddata", fixture)
        return django.http.HttpResponse("OK")

    urlpatterns += [
        path('yes-im-sure', csrf_exempt(reset_for_tests)),
    ]
