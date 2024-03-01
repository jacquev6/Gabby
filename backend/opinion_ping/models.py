from django.db.models import Model, DateTimeField


class Ping(Model):
    created_at = DateTimeField(auto_now_add=True)
