from django.contrib.auth.models import User


# There is no 'User.objects.get_or_create_superuser'
superuser = User.objects.filter(username="gabby").first()
if superuser is None:
    superuser = User.objects.create_superuser(
        "gabby",
        email="gabby@localhost",
        password="password",
    )
