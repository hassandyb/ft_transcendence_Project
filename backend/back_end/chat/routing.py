# chat/routing.py
from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    re_path(r'wss/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    # path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]