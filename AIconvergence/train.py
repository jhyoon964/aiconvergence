from ultralytics import YOLO
import cv2
import os
import urllib

os.environ['KMP_DUPLICATE_LIB_OK']='True'


if __name__ == '__main__':
    
    # model = YOLO("pretrain/yolov8l.pt")
    # model = YOLO("C:/Users/user/WP/AIconvergence/ultralytics/ultralytics/cfg/models/v8/yolov8.yaml")
    # model = YOLO("dct_all/dct_all7/weights/best.pt")
    
    # model = YOLO("C:/Users/user/WP/AIconvergence/ultralytics/kitti/kitti/weights/best.pt")
    # model = YOLO("crack600/crack_600_for_fig1/weights/augment_best.pt")
    # model = YOLO("crack600/crack_600_all_weather/weights/best.pt")
    # model = YOLO("crack600/crack_600_for_new_split/weights/best.pt")
    # model.train(cfg="ultralytics/cfg/custom.yaml")#, resume='True'
    
    
    
    
    
    model = YOLO("C:/Users/user/WP/AIconvergence/ultralytics/coco_pretrain/coco_pretrain2/weights/best.pt")
    # model = YOLO("C:/Users/user/WP/AIconvergence/ultralytics/dct_fall/dct_fire/weights/best.pt")
    # model = YOLO("C:/Users/user/WP/AIconvergence/ultralytics/ultralytics/cfg/models/v8/yolov8_convergence_dct.yaml")
    model.train(cfg="ultralytics/cfg/custom.yaml")#, resume='True'

