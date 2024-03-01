from rest_framework_json_api.views import ModelViewSet

from .models import Ping
from .serializers import PingSerializer


class PingViewSet(ModelViewSet):
    queryset = Ping.objects.order_by("id")
    serializer_class = PingSerializer
