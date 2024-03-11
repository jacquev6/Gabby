from django.contrib import admin

from .models import Ping


@admin.register(Ping)
class PingAdmin(admin.ModelAdmin):
    pass
