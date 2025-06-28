import os
import sys
from main import detect_cars
import cv2


def get_video_path():
    # Default video file path
    video_path = "cvtest.avi"
    # Use the first argument as the video path if provided
    if len(sys.argv) > 1:
        video_path = sys.argv[1]
    if not os.path.isfile(video_path):
        print("Invalid video path: ", video_path)
        exit(1)
    return video_path


def draw_detections(frame, detect_area_list):
    # Draw polygons for each detection area, color based on detection
    for da in detect_area_list:
        color = [(0, 0, 255), (0, 255, 0)][da.found]  # Red if not found, green if found
        cv2.polylines(
            frame, [da.polygone_list], isClosed=not da.found, color=color, thickness=3
        )
    return frame
