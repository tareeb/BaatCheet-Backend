import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter , get_default_application
import chat.routing
import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')
django.setup()
application = ProtocolTypeRouter({ 'http' : get_asgi_application(),
                                  
                                  
                     "websocket": AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns)), 
                     
                     })

application = get_default_application()
