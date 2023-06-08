from importlib.resources import path
from unittest.mock import patch
from . import consumers
from django.urls import path


websocket_urlpatterns = [
    path('ws/sc/<str:group_name>/',consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/<str:group_name>/',consumers.MyAsyncConsumer.as_asgi()),
]