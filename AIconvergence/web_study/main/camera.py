# # camera.py
# import cv2
# import os
# import logging

# logging.basicConfig(level=logging.INFO)
# class VideoCamera:
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         self.is_recording = False
#         self.video_writer = None
#         self.output_path = None

#     def __del__(self):
#         self.video.release()

#     def start_recording(self, output_filename):
#         self.output_path = os.path.join('recordings', output_filename)
#         os.makedirs('recordings', exist_ok=True)
#         logging.info(f"Starting recording: {self.output_file}")
#         # fourcc = cv2.VideoWriter_fourcc(*'XVID')
        
#         fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#         fps = int(self.video.get(cv2.CAP_PROP_FPS) or 20)
#         width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
#         height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
#         self.video_writer = cv2.VideoWriter(self.output_path, fourcc, fps, (width, height))
#         self.is_recording = True

#     def stop_recording(self):
#         self.is_recording = False
#         if self.video_writer:
#             self.video_writer.release()
#             self.video_writer = None

#     def get_frame(self):
#         success, image = self.video.read()
#         if not success:
#             logging.warning("Failed to read from camera.")
#             return b''
#         if self.is_recording and self.video_writer:
#             self.video_writer.write(image)

#         # Encode the image to JPEG
#         ret, jpeg = cv2.imencode('.jpg', image)
#         if not ret:
#             logging.error("Failed to encode image.")
#             return b''
#         return jpeg.tobytes()


# import cv2
# import os
# import logging

# logging.basicConfig(level=logging.INFO)

# class VideoCamera:
#     def __init__(self):
#         # Initialize the camera and attributes
#         self.video = cv2.VideoCapture(0)
#         self.is_recording = None
#         self.video_writer = None
#         self.output_file = None  # Make sure this attribute is initialized here

#     def __del__(self):
#         # Release the video when the object is destroyed
#         self.video.release()

#     def start_recording(self, output_filename):
#         # Ensure the recordings directory exists
#         os.makedirs('recordings', exist_ok=True)
        
#         # Set the output file path
#         self.output_file = os.path.join('recordings', output_filename)
#         logging.info(f"Starting recording: {self.output_file}")

#         # Initialize video writer with a codec and other parameters
#         fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Or use other codecs like 'mp4v'
#         fps = int(self.video.get(cv2.CAP_PROP_FPS) or 20)
#         width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
#         height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
#         self.video_writer = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height))
#         if not self.video_writer.isOpened():
#             logging.error("Video writer couldn't be opened.")
#         else:
#             logging.info("Video writer successfully initialized.")
#         self.is_recording = True

#     def stop_recording(self):
#         # Stop recording by releasing the video writer
#         self.is_recording = False
#         if self.video_writer:
#             self.video_writer.release()
#             self.video_writer = None
#         logging.info("Recording stopped.")

#     def get_frame(self):
#         success, image = self.video.read()
#         if not success:
#             logging.warning("Failed to read from camera.")
#             return b''

#         logging.info(f"Recording status: {self.is_recording}")
#         logging.info(f"Video writer is None: {self.video_writer is None}")

#         # Record the frame if recording is enabled
#         if self.is_recording and self.video_writer:
#             self.video_writer.write(image)

#         # Encode the frame to JPEG for streaming
#         ret, jpeg = cv2.imencode('.jpg', image)
#         if not ret:
#             logging.error("Failed to encode image.")
#             return b''

#         return jpeg.tobytes()



############### Original #################### 0520
# # camera.py
# import cv2
# import os
# import logging

# logging.basicConfig(level=logging.INFO)

# class VideoCamera:
#     def __init__(self):
#         # Initialize the camera and attributes
#         self.video = cv2.VideoCapture(0)
#         if not self.video.isOpened():
#             logging.error("Camera initialization failed.")
#         self.is_recording = False
#         self.video_writer = None
#         self.output_file = None

#     def __del__(self):
#         # Release the video when the object is destroyed
#         self.video.release()

#     def start_recording(self, output_filename):
#         # Ensure the recordings directory exists
#         os.makedirs('recordings', exist_ok=True)
        
#         # Set the output file path
#         self.output_file = os.path.join('recordings', output_filename)
#         logging.info(f"Starting recording: {self.output_file}")

#         # Initialize video writer with a codec and other parameters
#         fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Or use other codecs like 'mp4v'
#         fps = int(self.video.get(cv2.CAP_PROP_FPS) or 20)
#         width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
#         height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
#         self.video_writer = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height))
#         if not self.video_writer.isOpened():
#             logging.error("Video writer couldn't be opened.")
#         else:
#             logging.info("Video writer successfully initialized.")
#         self.is_recording = True

#     def stop_recording(self):
#         # Stop recording by releasing the video writer
#         self.is_recording = False
#         if self.video_writer:
#             self.video_writer.release()
#             self.video_writer = None
#         logging.info("Recording stopped.")

#     def get_frame(self):
#         success, image = self.video.read()
#         if not success:
#             logging.warning("Failed to read from camera.")
#             return b''

#         # logging.info(f"Recording status: {self.is_recording}")
#         # logging.info(f"Video writer is None: {self.video_writer is None}")

#         # Record the frame if recording is enabled
#         if self.is_recording and self.video_writer:
#             self.video_writer.write(image)

#         # Encode the frame to JPEG for streaming
#         ret, jpeg = cv2.imencode('.jpg', image)
#         if not ret:
#             logging.error("Failed to encode image.")
#             return b''

#         return jpeg.tobytes()

# # Create a global camera instance
# camera = VideoCamera()









############# YOLO #########################
import datetime
import pytz
import cv2
import os
import logging
import torch
from pathlib import Path
import sys
import time
# YOLO 경로 추가
ULTRALYTICS_PATH = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(str(ULTRALYTICS_PATH / 'ultralytics'))

# YOLO 모델 임포트
from ultralytics import YOLO
print('@@@@@@@@@@@@@@@@@@@')
logging.basicConfig(level=logging.INFO)
import random

def is_tensor_non_empty(tensor):
    # 텐서가 비어 있는지 확인
    return tensor.size(0) > 0
class VideoCamera:
    def __init__(self):
        # Initialize the camera and attributes
        self.video = cv2.VideoCapture(0)
        if not self.video.isOpened():
            logging.error("Camera initialization failed.")
        self.is_recording = False
        self.video_writer = None
        self.output_file = None
        self.last_detection_time = time.time()
        self.detection_interval = 2
        # Load YOLO model
        self.model = self.load_yolo_model()

    def __del__(self):
        # Release the video when the object is destroyed
        self.video.release()

    def load_yolo_model(self):
        # Load YOLOv5 model from ultralytics/yolov5 repository
        model = YOLO('C:/Users/user/WP/AIconvergence/ultralytics/fire/fire_test/weights/best.pt', task='detect')
        # model.eval()
        return model

    def start_recording(self, output_filename):
        # Ensure the recordings directory exists
        os.makedirs('recordings', exist_ok=True)
        
        # Set the output file path
        self.output_file = os.path.join('recordings', output_filename)
        logging.info(f"Starting recording: {self.output_file}")

        # Initialize video writer with a codec and other parameters
        # fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Or use other codecs like 'mp4v'
        fourcc = cv2.VideoWriter_fourcc(*'H264')
        fps = int(self.video.get(cv2.CAP_PROP_FPS) or 20)
        width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        self.video_writer = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height))
        if not self.video_writer.isOpened():
            logging.error("Video writer couldn't be opened.")
        else:
            logging.info("Video writer successfully initialized.")
        self.is_recording = True
    def auto_start_recording(self, is_detection):
        # Initialize the video writer and set is_recording to True if not already recording
        if is_tensor_non_empty(is_detection):
            self.last_detection_time = time.time()
            if not self.is_recording:
                kst = self.get_kst_time(self.last_detection_time)
                self.start_recording(f'auto_output_{kst}.mp4')
                self.is_recording = True
        if (not is_tensor_non_empty(is_detection)) and self.is_recording:
            current_time = time.time()
            if current_time - self.last_detection_time > self.detection_interval:
                self.stop_recording()
    def stop_recording(self):
        # Stop recording by releasing the video writer
        self.is_recording = False
        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None
        logging.info("Recording stopped.")
    def get_kst_time(self, timestamp):
        kst = pytz.timezone('Asia/Seoul')
        dt = datetime.datetime.fromtimestamp(timestamp, kst)
        return dt.strftime('%Y_%m_%d_%H_%M')
    def get_frame(self):
        success, image = self.video.read()
        if not success:
            logging.warning("Failed to read from camera.")
            return b''

        # Perform YOLO detection
        results = self.model(image)[0]
        detections = results.boxes.xywhn  # Bounding box coordinates
        # print(is_tensor_non_empty(detections))
        img_height, img_width, _ = image.shape
        # Draw bounding boxes on the image
        for det, cls in zip(results.boxes.xywhn, results.boxes.cls):
            class_id = int(cls)
            # class_id = 0
            bbox = det[:4]  # 바운딩 박스 정보: x1, y1, x2, y2
            x_center = bbox[0] * img_width
            y_center = bbox[1] * img_height
            bbox_width = bbox[2] * img_width
            bbox_height = bbox[3] * img_height
            x1 = int(x_center - bbox_width / 2)
            y1 = int(y_center - bbox_height / 2)
            x2 = int(x_center + bbox_width / 2)
            y2 = int(y_center + bbox_height / 2)
            
            label = f'{class_id}'
            if class_id ==0:
                label = 'Fire'
            plot_one_box([x1,y1,x2,y2], image, label=label, color=(0, 0, 255), line_thickness=2)

        # Record the frame if recording is enabled
        if self.is_recording and self.video_writer:
            self.video_writer.write(image)
        self.auto_start_recording(detections)
        # Encode the frame to JPEG for streaming
        ret, jpeg = cv2.imencode('.jpg', image)
        if not ret:
            logging.error("Failed to encode image.")
            return b''

        return jpeg.tobytes()

def plot_one_box(x, img, color=None, label=None, line_thickness=None):
    # Plots one bounding box on image `img`
    assert img.data.contiguous, 'Image not contiguous. Apply np.ascontiguousarray(img) to plot_one_box() input images.'
    tl = line_thickness or round(0.002 * max(img.shape[0:2])) + 1  # line thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

# Create a global camera instance
camera = VideoCamera()