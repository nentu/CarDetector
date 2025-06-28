from main import detect_cars
from DetectArea import detect_area_list
import cv2
import sys
import os
from tqdm import tqdm
from utils import get_video_path, draw_detections

video_path = get_video_path()

cap = cv2.VideoCapture(video_path)


# Get video properties for writer
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Output file name
output_path = "output_" + os.path.basename(video_path)
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Get total frame count for progress bar
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Main video processing loop with progress bar
for _ in tqdm(range(total_frames), desc="Processing video"):
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Detect vehicles in the frame for each area
    detect_area_list = detect_cars(frame, detect_area_list)

    frame = draw_detections(frame, detect_area_list)

    # Write the processed frame to the output video
    out.write(frame)

# Release resources
cap.release()
out.release()
print(f"Processed video saved as: {output_path}")
