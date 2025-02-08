import sys
import argparse
import os

sys.path.append(r'/root/YOLO-Pothole') # Path

from ultralytics import YOLO

def main(opt):
    yaml = opt.cfg
    model = YOLO(yaml) 

    model.info()

    # 实例分割训练
    results = model.train(
        data='ultralytics-main/ultralytics/cfg/datasets/Pothole-seg.yaml', 
        epochs=300, 
        imgsz=640,  
        batch=16
        )

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, default= 'ultralytics-main/ultralytics/cfg/models/v8/yolov8-seg.yaml', help='initial weights path')
    # parser.add_argument('--cfg', type=str, default= 'ultralytics-main/ultralytics/cfg/models/11/yolo11-seg.yaml', help='initial weights path')
    parser.add_argument('--weights', type=str, default='', help='')

    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)