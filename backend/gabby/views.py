import django.core.management
import django.http


def reset_for_tests(request):
    if request.method != "POST":
        return django.http.HttpResponseNotAllowed(["POST"])
    django.core.management.call_command("flush", interactive=False)
    django.core.management.call_command("migrate", interactive=False)
    for fixture in request.GET.getlist("fixtures"):
        django.core.management.call_command("loaddata", fixture)
    # django.core.management.call_command("loaddata", "test-exercises")
    return django.http.HttpResponse("OK")
