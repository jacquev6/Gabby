from django.contrib import admin
from django.urls import path, include

from opinion_ping.urls import urlpatterns as opinion_ping
from textbooks.urls import urlpatterns as textbooks


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(textbooks)),
    path('api/', include(opinion_ping)),
]
