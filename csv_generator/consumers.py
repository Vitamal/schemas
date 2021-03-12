import json
from channels.generic.websocket import WebsocketConsumer


class SchemasConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        self.schema_id = None
        super().__init__(*args, **kwargs)

    def connect(self):
        self.schema_id = self.scope['url_route']['kwargs']['schema_id']
        self.accept()

    def disconnect(self, close_code):
        print("disconnected", close_code)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        generated_file_id = text_data_json['generated_file.id']

        self.send(text_data=json.dumps({
            'generated_file_id': generated_file_id
        }))
