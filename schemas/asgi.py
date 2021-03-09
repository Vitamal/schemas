"""
ASGI config for schemas project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

import csv_generator.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schemas.project.settingsproxy')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            csv_generator.routing.websocket_urlpatterns
        )
    ),
})
