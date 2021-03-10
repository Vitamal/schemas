import json
from channels.generic.websocket import AsyncWebsocketConsumer


class SchemasConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.shema_id = self.scope['url_route']['kwargs']['schema_id']
        await self.accept()

    async def disconnect(self, close_code):
        print("disconnected", close_code)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
