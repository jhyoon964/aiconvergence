# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog
# from PyQt5 import uic

# form_class = uic.loadUiType("map.ui")[0]
# class MainUI(QDialog, form_class):
#     def __init__(self, stacked_widget):
#         super().__init__()
#         self.setupUi(self)  # 오타 수정: setipUi -> setupUi
#         self.stacked_widget = stacked_widget
#         self.pushButton_3.clicked.connect(self.gotoSecond)


#     def gotoSecond(self):
#         self.stacked_widget.setCurrentIndex(1)  # 두 번째 화면으로 전환

# class SecondUI(QMainWindow):
#     def __init__(self, stacked_widget):
#         super().__init__()
#         uic.loadUi("Main.ui", self)
#         self.stacked_widget = stacked_widget
#         self.Map_button.clicked.connect(self.gotoFirst)
#         self.Road_button.clicked.connect(self.gotoFirst1)

#     def gotoFirst(self):
#         self.stacked_widget.setCurrentIndex(0)  # 첫 번째 화면으로 전환
#     def gotoFirst1(self):
#         self.stacked_widget.setCurrentIndex(2)  # 첫 번째 화면으로 전환
#         # print('Clicked Road')
#         # self.stacked_widget.setCurrentIndex(0)  # 첫 번째 화면으로 전환    
# form_class1 = uic.loadUiType("Road_guide.ui")[0]
# class ThridUI(QMainWindow, form_class1):
#     def __init__(self, stacked_widget):
#         super().__init__()
#         self.setupUi(self)
#         # uic.loadUi("Road_guide.ui", self)
#         self.stacked_widget = stacked_widget
#         self.back_button.clicked.connect(self.gotoThird0)
#         self.r1_button.clicked.connect(self.gotoThird1)
#         self.r2_button.clicked.connect(self.gotoThird2)
#         self.r3_button.clicked.connect(self.gotoThird3)
#         self.r4_button.clicked.connect(self.gotoThird4)
#         self.r5_button.clicked.connect(self.gotoThird5)
#         self.r6_button.clicked.connect(self.gotoThird6)
#         self.r7_button.clicked.connect(self.gotoThird7)
#         self.r8_button.clicked.connect(self.gotoThird8)
#         self.r9_button.clicked.connect(self.gotoThird9)
#     def gotoThird0(self):
#         self.stacked_widget.setCurrentIndex(1)  # 두 번째 화면으로 전환
#     def gotoThird1(self):
#         print('clicked third1')
#     def gotoThird2(self):
#         print('clicked third2')
#     def gotoThird3(self):
#         print('clicked third3')
#     def gotoThird4(self):
#         print('clicked third4')
#     def gotoThird5(self):
#         print('clicked third5')
#     def gotoThird6(self):
#         print('clicked third6')
#     def gotoThird7(self):
#         print('clicked third7')
#     def gotoThird8(self):
#         print('clicked third8')
#     def gotoThird9(self):
#         print('clicked third9')
    


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     stacked_widget = QStackedWidget()

#     # MainUI 인스턴스를 생성할 때 form_class 인자를 제거
#     main_ui = MainUI(stacked_widget)
#     second_ui = SecondUI(stacked_widget)
#     third_ui = ThridUI(stacked_widget)

#     stacked_widget.addWidget(main_ui)  # 첫 번째 화면 추가
#     stacked_widget.addWidget(second_ui)  # 두 번째 화면 추가
#     stacked_widget.addWidget(third_ui)  # 두 번째 화면 추가

#     stacked_widget.show()
#     sys.exit(app.exec_())


import threading
from PyQt5.QtCore import pyqtSignal, QObject
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog
from PyQt5 import uic
import cv2
import time
from ultralytics import YOLO

from PyQt5.QtCore import QThread, pyqtSignal

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
form_class = uic.loadUiType("map.ui")[0]
class MainUI(QDialog, form_class):
    def __init__(self, stacked_widget, controller):
        super().__init__()
        self.setupUi(self)
        self.stacked_widget = stacked_widget
        self.controller = controller
        self.controller.detection_thread.alert_signal.connect(self.handle_detection)
        self.pushButton_3.clicked.connect(self.gotoSecond)
    def gotoSecond(self):
        self.stacked_widget.setCurrentIndex(1)
    def handle_detection(self, detected):
        if detected:
            self.setStyleSheet("background-color: red;")
        else:
            self.setStyleSheet("")    



class SecondUI(QMainWindow):
    def __init__(self, stacked_widget, controller):
        super().__init__()
        uic.loadUi("Main.ui", self)
        self.stacked_widget = stacked_widget
        self.Map_button.clicked.connect(self.gotoFirst)
        self.Road_button.clicked.connect(self.gotoFirst1)
        self.controller = controller
        self.controller.detection_thread.alert_signal.connect(self.handle_detection)
        
        
    def gotoFirst(self):
        self.stacked_widget.setCurrentIndex(0)  # 첫 번째 화면으로 전환
    def gotoFirst1(self):
        self.stacked_widget.setCurrentIndex(2)  # 첫 번째 화면으로 전환
    def handle_detection(self, detected):
        if detected:
            self.setStyleSheet("background-color: red;")
        else:
            self.setStyleSheet("")

form_class1 = uic.loadUiType("Road_guide.ui")[0]
class ThirdUI(QMainWindow, form_class1):
    def __init__(self, stacked_widget, controller):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi("Road_guide.ui", self)
        self.stacked_widget = stacked_widget
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
        self.stacked_widget.setCurrentIndex(1)  # 두 번째 화면으로 전환
    def gotoThird1(self):
        print('clicked third1')
    def gotoThird2(self):
        print('clicked third2')
    def gotoThird3(self):
        print('clicked third3')
    def gotoThird4(self):
        print('clicked third4')
    def gotoThird5(self):
        print('clicked third5')
    def gotoThird6(self):
        print('clicked third6')
    def gotoThird7(self):
        print('clicked third7')
    def gotoThird8(self):
        print('clicked third8')
    def gotoThird9(self):
        print('clicked third9')
    def handle_detection(self, detected):
        if detected:
            self.setStyleSheet("background-color: red;")
        else:
            self.setStyleSheet("")
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

