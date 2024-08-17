from django.urls import path
from yourapp.consumers import LLMConsumer

websocket_urlpatterns = [
    path('ws/llm/', LLMConsumer.as_asgi()),
]
