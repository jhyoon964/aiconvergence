# consumers.py
# from channels.generic.websocket import WebsocketConsumer
# import base64
# import json
# class VideoConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data=None, bytes_data=None):
#         # 받은 메시지를 JSON으로 파싱
#         data = json.loads(text_data)
#         # 처리 후 다시 클라이언트에 전송 (예시)
#         self.send(text_data=json.dumps({
#             'message': data.get('message', '')
#         }))
#         # self.send(text_data=json.dumps({
#         #     'message': 'Data received'
#         # }))        
#         # # WebSocket을 통해 받은 영상 데이터를 브라우저로 전달
#         # if bytes_data:
#         #     encoded_data = base64.b64encode(bytes_data).decode("utf-8")
#         #     self.send(text_data=f"data:image/jpeg;base64,{encoded_data}")
# from channels.generic.websocket import AsyncWebsocketConsumer
# import json

# class VideoConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         # 수신 데이터 처리 및 응답
#         await self.send(text_data=json.dumps({
#             'message': data.get('message', 'No data received')
#         }))
        
import logging
from channels.generic.websocket import WebsocketConsumer

logger = logging.getLogger(__name__)
class VideoConsumer(WebsocketConsumer):
    def connect(self):
        print('connect@@@@@@@@@@@@@@@@@@')
        logger.info("WebSocket connection requested.")
        self.accept()

    def disconnect(self, close_code):
        print('disconnect@@@@@@@@@@@@@@@@@@')
        logger.info("WebSocket connection closed with code: %s", close_code)
        pass

    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data="Hello WebSocket")        