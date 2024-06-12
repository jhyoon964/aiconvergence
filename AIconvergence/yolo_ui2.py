import threading
from PyQt5.QtCore import pyqtSignal, QObject
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog
from PyQt5 import uic
import cv2
import time
from ultralytics import YOLO
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, Qt,QDateTime

class DetectionThread(QThread):
    alert_signal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.detection_active = True
        self.model = YOLO('fire/fire_test/weights/best.pt', task='detect')
        self.cap = cv2.VideoCapture(0)
        
        
    def run(self):
        while self.detection_active:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            detections = self.model(frame)
            detected = any(detections)
            self.alert_signal.emit(detected)
            
            time.sleep(1)  # 30fps에 맞춰 지연

    def stop(self):
        self.detection_active = False
        self.cap.release()
        self.wait()
        
    
class AppController:
    def __init__(self):
        self.detection_thread = DetectionThread()
        # self.detection_thread.alert_signal.connect(self.handle_detection)

    def start_detection(self):
        self.detection_thread.start()

    def stop_detection(self):
        self.detection_thread.stop()


controller = AppController()



class MainUI(QMainWindow):
    def __init__(self, stacked_widget, controller):
        super().__init__()
        self.ui = uic.loadUi("Main2.ui", self)
        self.stacked_widget = stacked_widget
        self.Map_button.clicked.connect(self.gotoFirst)
        self.Road_button.clicked.connect(self.gotoFirst1)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)  # 1초마다 업데이트        
        
        
        self.controller = controller
        self.controller.detection_thread.alert_signal.connect(self.handle_detection)
        self.setMinimumSize(900, 1500)  # 최소 크기 설정
        self.setMaximumSize(900, 1500)  # 최대 크기 설정
        
    def update_clock(self):
        current_time = QDateTime.currentDateTime().toString('현재 시간\nhh:mm:ss')
        self.ui.time_label.setStyleSheet("color: white;")
        self.ui.time_label.setText(current_time)
                
    def gotoFirst(self):
        self.stacked_widget.setCurrentIndex(1)  # 첫 번째 화면으로 전환
    def gotoFirst1(self):
        self.stacked_widget.setCurrentIndex(2)  # 첫 번째 화면으로 전환
    def handle_detection(self, detected):
        if detected:
            self.setStyleSheet("background-color: red;")
        else:
            self.setStyleSheet("background-color: black;")



form_class = uic.loadUiType("map2.ui")[0]
class SecondUI(QDialog, form_class):
    def __init__(self, stacked_widget, controller):
        super().__init__()
        self.setupUi(self)
        self.stacked_widget = stacked_widget
        self.controller = controller
        self.controller.detection_thread.alert_signal.connect(self.handle_detection)
        self.back_button.clicked.connect(self.gotoSecond)
        self.dlabel_1.setPixmap(QPixmap())  # 초기에는 빈 이미지 또는 숨김 처리
        self.dlabel_2.setPixmap(QPixmap())  # 초기에는 빈 이미지 또는 숨김 처리
        self.dlabel_3.setPixmap(QPixmap())  # 초기에는 빈 이미지 또는 숨김 처리
        self.dlabel_1.hide()
        self.dlabel_2.hide()
        self.dlabel_3.hide()        
        self.btn_1_1.clicked.connect(self.defbtn_1_1)
        self.btn_2_1.clicked.connect(self.defbtn_2_1)
        self.btn_3_1.clicked.connect(self.defbtn_3_1)
        self.t_btn.clicked.connect(self.def_t_btn)
        
    def defbtn_2_1(self):
        pixmap_1 = QPixmap("2_1_1.jpg")  # 이미지 경로
        scaled_pixmap_1 = pixmap_1.scaled(self.dlabel_1.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.dlabel_1.setPixmap(scaled_pixmap_1)        
        self.dlabel_1.show()  # 이미지가 숨겨져 있었다면 표시
        pixmap_2 = QPixmap("new_2_1.png")  # 이미지 경로
        scaled_pixmap_2 = pixmap_2.scaled(self.dlabel_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.dlabel_2.setPixmap(scaled_pixmap_2)        
        self.dlabel_2.show()  # 이미지가 숨겨져 있었다면 표시
        self.dlabel_3.setText("웰빙과자전문점 바삭바삭 '맛나당'입니다.\n총 60여가지 Haccp인증 뻥튀기, 옛날과자,유기농아기과자, \n세계과자, 국내산 누룽지, 어포튀각, 종합전병세트등을 \n판매하고 있습니다.")
        self.dlabel_3.setStyleSheet("color: white; font-size: 25px;")
        self.dlabel_3.show()  # 텍스트 라벨을 보이게 함
    def defbtn_1_1(self):
        pixmap_1 = QPixmap("1_1_1.jpg")  # 이미지 경로
        scaled_pixmap_1 = pixmap_1.scaled(self.dlabel_1.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.dlabel_1.setPixmap(scaled_pixmap_1)        
        self.dlabel_1.show()  # 이미지가 숨겨져 있었다면 표시
        pixmap_2 = QPixmap("new_1_1.png")  # 이미지 경로
        scaled_pixmap_2 = pixmap_2.scaled(self.dlabel_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.dlabel_2.setPixmap(scaled_pixmap_2)        
        self.dlabel_2.show()  # 이미지가 숨겨져 있었다면 표시
        self.dlabel_3.setText("감사합니다.\n금남로 지하상가 코리아 안경 입니다.")
        self.dlabel_3.setStyleSheet("color: white; font-size: 25px;")
        self.dlabel_3.show()  # 텍스트 라벨을 보이게 함
    def defbtn_3_1(self):
        pixmap_1 = QPixmap("3_1_1.jpg")  # 이미지 경로
        scaled_pixmap_1 = pixmap_1.scaled(self.dlabel_1.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.dlabel_1.setPixmap(scaled_pixmap_1)        
        self.dlabel_1.show()  # 이미지가 숨겨져 있었다면 표시
        pixmap_2 = QPixmap("3_1.png")  # 이미지 경로
        scaled_pixmap_2 = pixmap_2.scaled(self.dlabel_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.dlabel_2.setPixmap(scaled_pixmap_2)        
        self.dlabel_2.show()  # 이미지가 숨겨져 있었다면 표시
        self.dlabel_3.setText("만남의 광장")
        self.dlabel_3.setStyleSheet("color: white; font-size: 25px;")
        self.dlabel_3.show()  # 텍스트 라벨을 보이게 함        
    def def_t_btn(self):
        pixmap_1 = QPixmap("t_image.jpg")  # 이미지 경로
        scaled_pixmap_1 = pixmap_1.scaled(self.dlabel_1.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.dlabel_1.setPixmap(scaled_pixmap_1)        
        self.dlabel_1.show()  # 이미지가 숨겨져 있었다면 표시
        pixmap_2 = QPixmap("new_t_map.png")  # 이미지 경로
        scaled_pixmap_2 = pixmap_2.scaled(self.dlabel_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.dlabel_2.setPixmap(scaled_pixmap_2)        
        self.dlabel_2.show()  # 이미지가 숨겨져 있었다면 표시
        self.dlabel_3.setText("화장실")
        self.dlabel_3.setStyleSheet("color: white; font-size: 25px;")
        self.dlabel_3.show()  # 텍스트 라벨을 보이게 함
                
        
        
                        
    def gotoSecond(self):
        self.stacked_widget.setCurrentIndex(0)
    def handle_detection(self, detected):
        if detected:
            self.setStyleSheet("background-color: red;")
        else:
            self.setStyleSheet("background-color: black;")    



form_class1 = uic.loadUiType("Road_guide2.ui")[0]
class ThirdUI(QMainWindow, form_class1):
    def __init__(self, stacked_widget, controller):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi("Road_guide.ui", self)
        self.stacked_widget = stacked_widget
        self.label.setPixmap(QPixmap("new_map.png").scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        # self.label.setPixmap(QPixmap())  # 초기에는 빈 이미지 또는 숨김 처리
        # self.label.hide()
        self.back_button.clicked.connect(self.gotoThird0)
        self.r1_button.clicked.connect(self.gotoThird1)
        self.r2_button.clicked.connect(self.gotoThird2)
        self.r3_button.clicked.connect(self.gotoThird3)
        self.r4_button.clicked.connect(self.gotoThird4)
        self.r5_button.clicked.connect(self.gotoThird5)
        self.r6_button.clicked.connect(self.gotoThird6)
        self.r7_button.clicked.connect(self.gotoThird7)
        self.r8_button.clicked.connect(self.gotoThird8)
        self.r9_button.clicked.connect(self.gotoThird9)
        self.controller = controller
        self.controller.detection_thread.alert_signal.connect(self.handle_detection)    
        
        
    def gotoThird0(self):
        self.stacked_widget.setCurrentIndex(0)  # 두 번째 화면으로 전환
    def gotoThird1(self):
        pixmap = QPixmap("new_exit1.png")  # 이미지 경로
        scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.label.setPixmap(scaled_pixmap)        
        self.label.show()  # 이미지가 숨겨져 있었다면 표시
        QTimer.singleShot(3000, self.hide_image)  # 3000ms 후에 hide_image 함수 호출      

    def gotoThird2(self):
        pixmap = QPixmap("new_exit2.png")  # 이미지 경로
        scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.label.setPixmap(scaled_pixmap)        
        self.label.show()  # 이미지가 숨겨져 있었다면 표시
        QTimer.singleShot(3000, self.hide_image)  # 3000ms 후에 hide_image 함수 호출      
    def gotoThird3(self):
        pixmap = QPixmap("new_exit3.png")  # 이미지 경로
        scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.label.setPixmap(scaled_pixmap)        
        self.label.show()  # 이미지가 숨겨져 있었다면 표시
        QTimer.singleShot(3000, self.hide_image)  # 3000ms 후에 hide_image 함수 호출
    def gotoThird4(self):
        pixmap = QPixmap("new_exit4.png")  # 이미지 경로
        scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.label.setPixmap(scaled_pixmap)        
        self.label.show()  # 이미지가 숨겨져 있었다면 표시
        QTimer.singleShot(3000, self.hide_image)  # 3000ms 후에 hide_image 함수 호출
    def gotoThird5(self):
        pixmap = QPixmap("new_exit5.png")  # 이미지 경로
        scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.label.setPixmap(scaled_pixmap)        
        self.label.show()  # 이미지가 숨겨져 있었다면 표시
        QTimer.singleShot(3000, self.hide_image)  # 3000ms 후에 hide_image 함수 호출
    def gotoThird6(self):
        pixmap = QPixmap("new_exit6.png")  # 이미지 경로
        scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.label.setPixmap(scaled_pixmap)        
        self.label.show()  # 이미지가 숨겨져 있었다면 표시
        QTimer.singleShot(3000, self.hide_image)  # 3000ms 후에 hide_image 함수 호출
    def gotoThird7(self):
        pixmap = QPixmap("new_exit7.png")  # 이미지 경로
        scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.label.setPixmap(scaled_pixmap)        
        self.label.show()  # 이미지가 숨겨져 있었다면 표시
        QTimer.singleShot(3000, self.hide_image)  # 3000ms 후에 hide_image 함수 호출
    def gotoThird8(self):
        pixmap = QPixmap("new_exit8.png")  # 이미지 경로
        scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 라벨 크기에 맞게 이미지 스케일링
        self.label.setPixmap(scaled_pixmap)        
        self.label.show()  # 이미지가 숨겨져 있었다면 표시
        QTimer.singleShot(3000, self.hide_image)  # 3000ms 후에 hide_image 함수 호출
    def gotoThird9(self):
        print('clicked third9')
        
    def hide_image(self):
        self.label.setPixmap(QPixmap("new_map.png").scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        # self.label.setPixmap(QPixmap())  # 빈 이미지로 설정하거나
        # self.label.hide()  # 라벨 숨김        
    def handle_detection(self, detected):
        if detected:
            self.setStyleSheet("background-color: red;")
        else:
            self.setStyleSheet("background-color: black;")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    controller = AppController()

    main_ui = MainUI(stacked_widget, controller)
    second_ui = SecondUI(stacked_widget, controller)
    third_ui = ThirdUI(stacked_widget, controller)

    stacked_widget.addWidget(main_ui)
    stacked_widget.addWidget(second_ui)
    stacked_widget.addWidget(third_ui)

    stacked_widget.show()
    controller.start_detection()
    
    def on_app_exit():
        controller.stop_detection()
        app.quit()

    app.aboutToQuit.connect(on_app_exit)
    sys.exit(app.exec_())

