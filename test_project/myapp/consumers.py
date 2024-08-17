from channels.generic.websocket import AsyncWebsocketConsumer
import json
import requests
from rest_framework_simplejwt.authentication import JWTAuthentication
from channels.db import database_sync_to_async

class LLMConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        token = self.scope['query_string'].decode().split('=')[1]
        user = await self.authenticate_token(token)
        if user is not None:
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        pass

    @database_sync_to_async
    def authenticate_token(self, token):
        try:
            auth = JWTAuthentication()
            validated_token = auth.get_validated_token(token)
            return auth.get_user(validated_token)
        except:
            return None

    async def receive(self, text_data):
        data = json.loads(text_data)
        prompt = data['prompt']

        response = requests.post(
            f"{self.scope['settings'].LANGFLOW_URL}/agent/prompt",
            json={'prompt': prompt}
        )

        await self.send(text_data=json.dumps({
            'response': response.json()
        }))
