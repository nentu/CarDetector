from ultralytics import YOLO
import cv2
import json
import numpy as np


# Load YOLOv8 model (nano version)
model = YOLO("yolov8n.pt")


# Set of class names that are considered transport/vehicles
transport_classes = {"car", "motorcycle", "bus", "truck"}

# Get class names from the YOLO model
class_names = model.names


def detect_cars(frame, detect_area_list):
    """
    Detects transport vehicles in the frame and updates the detect_area_list
    to indicate if a vehicle is found in each area.
    """
    # Reset found flag for all areas
    for dp in detect_area_list:
        dp.found = False

    # Run YOLO detection
    results = model(frame, verbose=False)

    # Iterate over detected objects
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls.cpu())
            cls_name = class_names[cls_id]
            # Check if detected object is a transport class
            if cls_name in transport_classes:
                left, top, right, bottom = box.xyxy.cpu().numpy().flatten()
                # Check if center of detection area is within bounding box
                for dp in detect_area_list:
                    dp.found = dp.found or (
                        (top < dp.y < bottom) and (left < dp.x < right)
                    )
    return detect_area_list
