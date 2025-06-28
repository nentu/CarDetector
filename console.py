from main import detect_cars
from DetectArea import detect_area_list
import cv2
from datetime import timedelta
from utils import get_video_path

video_path = get_video_path()
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Get timestamp in seconds for the current frame
    frame_idx = int(cap.get(cv2.CAP_PROP_POS_FRAMES)) - 1  # zero-based index
    timestamp_sec = frame_idx / fps if fps else 0
    timestamp_str = str(timedelta(seconds=timestamp_sec))

    # Detect vehicles in the frame for each area
    detect_area_list = detect_cars(frame, detect_area_list)

    # Print detection result for each area with timestamp
    print(timestamp_str, end=":")
    print(f"Left barrier busy: {detect_area_list[0].found}", end=", ")
    print(f"Right barrier busy: {detect_area_list[1].found}")


cap.release()
