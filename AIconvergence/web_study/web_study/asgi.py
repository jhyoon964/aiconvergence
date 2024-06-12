"""
ASGI config for web_study project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
# web_study/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from web_study.consumers import VideoConsumer
print('!!!!!!!!!!!!!!@!!!!!!!!!!!!')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_study.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/video/", VideoConsumer.as_asgi()),
        ])
    ),
})








# import os

# from django.core.asgi import get_asgi_application

# # from . import routing
# from web_study.routing import websocket_urlpatterns

# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from web_study.consumers import VideoConsumer  # WebSocket을 처리할 Consumer를 추가
# from django.urls import path

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_study.settings')

# # # # application = get_asgi_application()
# # application = ProtocolTypeRouter({
# #     "http": get_asgi_application(),
# #     "websocket": URLRouter(
# #         websocket_urlpatterns
# #     ),
# # })
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     # "websocket": URLRouter([
#     #     path("ws/video/", VideoConsumer.as_asgi()),
#     # ]),
#     "websocket": AuthMiddlewareStack(
#         URLRouter([
#             # WebSocket URL을 여기에 추가하세요
#             # routing.websocket_urlpatterns
#             path("ws/video/", VideoConsumer.as_asgi()),
#         ])
#     ),
# })











# import os
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.core.asgi import get_asgi_application
# from web_study.routing import websocket_urlpatterns

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_study.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             websocket_urlpatterns
#         )
#     ),
# })