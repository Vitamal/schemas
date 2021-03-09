from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/generator/(?P<schema_id>\w+)/$', consumers.SchemasConsumer.as_asgi()),
]
