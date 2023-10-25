from django.urls import path , re_path
from channels.routing import ProtocolTypeRouter, URLRouter

from .consumers import ChatConsumer

websocket_urlpatterns = [
   re_path(r'^ws/(?P<token>\w+)/$', ChatConsumer.as_asgi()),
]   


