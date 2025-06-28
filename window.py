from main import detect_cars
from DetectArea import detect_area_list
import cv2
from utils import get_video_path, draw_detections

video_path = get_video_path()
cap = cv2.VideoCapture(video_path)

# OpenCV window setup
cv2.namedWindow("res", cv2.WND_PROP_FULLSCREEN)

# Main video processing loop
while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video
    # Detect vehicles in the frame for each area
    detect_area_list = detect_cars(frame, detect_area_list)

    frame = draw_detections(frame, detect_area_list)

    # Display the frame with overlays
    cv2.imshow("res", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
