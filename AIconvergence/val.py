from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionValidator

from multiprocessing import freeze_support
# Load a model
# model = YOLO('yolov8n.pt')  # load an official model
# model = YOLO('/crack600/crack_600_new_label/weights/best.pt', data='/ultralytics/cfg/datasets/crack600.yaml')  # load a custom model



# model = YOLO('C:/Users/user/WP/ultra_2/crack600/crack_600_new_label/weights/best.pt')  # load a custom model
# # Validate the model   , data='/ultralytics/cfg/datasets/crack600_rain.yaml'model=

# metrics = model.val()  # no arguments needed, dataset and settings remembered
# metrics.box.map    # map50-95
# metrics.box.map50  # map50


# def run():    
#     freeze_support()
#     # model = YOLO("fall_detection/fall_test4/weights/best.pt", task='detect')  # load a custom model
#     model = YOLO("other_fire/other_fire_test/weights/best.pt", task='detect')  # load a custom model
#     ##, data='/ultralytics/cfg/datasets/crack600.yaml'
#     # Validate the model
#     # model.load("crack600/crack_600_new_label/weights/best.pt")
#     # model.load("crack600/crack_600_for_fig1/weights/non_augment_best.pt")
#     model.load("other_fire/other_fire_test/weights/best.pt")
#     metrics = model.val(data='ultralytics/cfg/datasets/other_fire.yaml', batch=1)  # no arguments needed, dataset and settings remembered
#     metrics.box.map    # map50-95
#     metrics.box.map50  # map50
#     metrics.box.map75  # map75
#     metrics.box.maps   # a list contains map50-95 of each category
# if __name__ == '__main__':
#     run()


def run():    
    freeze_support()
    model = YOLO("dct_only_fire/dct_only_fire/weights/best.pt", task='detect')  # load a custom model
    # model = YOLO("C:/Users/user/WP/AIconvergence/ultralytics/kitti2d/kitti2dis/weights/best.pt", task='detect')  # load a custom model
    # model = YOLO("C:/Users/user/WP/AIconvergence/ultralytics/kitti2d/kitti2dis/weights/best.pt", task='detect')  # load a custom model
    ##, data='/ultralytics/cfg/datasets/crack600.yaml'
    # Validate the model
    # model.load("crack600/crack_600_new_label/weights/best.pt")
    # model.load("crack600/crack_600_for_fig1/weights/non_augment_best.pt")
    model.load("dct_only_fire/dct_only_fire/weights/best.pt")
    # model.load("C:/Users/user/WP/AIconvergence/ultralytics/kitti2d/kitti2dis/weights/best.pt")
    # model.load("C:/Users/user/WP/AIconvergence/ultralytics/kitti2d/kitti2dis/weights/best.pt")
    metrics = model.val(data='ultralytics/cfg/datasets/fire.yaml', batch=1)  # no arguments needed, dataset and settings remembered
    metrics.box.map    # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps   # a list contains map50-95 of each category
if __name__ == '__main__':
    run()

