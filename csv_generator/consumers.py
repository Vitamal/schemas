import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class SchemasConsumer(WebsocketConsumer):

    # def connect(self):
    #     self.accept()

    def __init__(self, *args, **kwargs):
        self.schema_id = None
        self.group_name = None
        super().__init__(*args, **kwargs)

    def connect(self):
        self.group_name = 'generator'
        self.schema_id = self.scope['url_route']['kwargs']['schema_id']

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    # def disconnect(self, close_code):
    #     pass

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #
    #     self.send(text_data=json.dumps({
    #         'message': message
    #     }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        generated_file_id = text_data_json['generated_file_id']
        print('8888888888888888', text_data)
        print('self.group_name,', self.group_name)

        # # Send message to room group
        # async_to_sync(self.channel_layer.group_send)(
        #     self.group_name,
        #     {
        #         'type': 'pr_status_message',
        #         'generated_file_id': generated_file_id,
        #     }
        # )

    # Receive message from room group
    def task_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    # # Receive message from room group
    # def pr_status_message(self, event):
    #     generated_file_id = event['generated_file_id']
    #     generated_file_status = event['generated_file_status']
    #
    #     # Send message to WebSocket
    #     self.send(text_data=json.dumps({
    #         'generated_file_id': generated_file_id,
    #          'generated_file_status': generated_file_status
    #     }))
