from django.urls import re_path
from .consumers import OCPPConsumer


websocket_urlpatterns = [
    re_path(r"ws/ocpp/$", OCPPConsumer.as_asgi()),
]