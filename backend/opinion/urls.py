from django.contrib import admin
from django.urls import path, include

from opinion_ping.urls import urlpatterns as opinion_ping


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(opinion_ping)),
]
