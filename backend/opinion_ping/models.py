from django.db.models import Model, DateTimeField, TextField, ForeignKey, SET_NULL


class Ping(Model):
    created_at = DateTimeField(auto_now_add=True)
    prev = ForeignKey('self', null=True, on_delete=SET_NULL, related_name='next')
    message = TextField(null=True, max_length=16)
