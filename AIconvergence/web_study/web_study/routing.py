# # routing.py
# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/video/', consumers.VideoConsumer.as_asgi()),
# ]


from django.urls import path
from web_study.consumers import VideoConsumer
# from web_study import consumers
from channels.routing import ProtocolTypeRouter, URLRouter
print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
websocket_urlpatterns = [
    path('ws/video/', VideoConsumer.as_asgi()),  # WebSocket URL과 컨슈머 연결
]
# websocket_urlpatterns = [
#     path('ws/video/', consumers.as_asgi()),  # WebSocket URL과 컨슈머 연결
# ]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})