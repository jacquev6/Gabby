from django.urls import include, path
from rest_framework import routers

from .views import PingViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register("pings", PingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
