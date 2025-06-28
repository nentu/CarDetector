from dataclasses import dataclass
import numpy as np


# Data class to represent a detection area with center (x, y), found flag, and polygon coordinates
@dataclass
class DetectArea:
    x: int
    y: int
    found: bool
    polygone_list: np.array


detect_area_list = [
    DetectArea(
        277, 548, False, np.array([[0, 779], [0, 1097], [786, 652], [466, 572]])
    ),
    DetectArea(
        1302,
        770,
        False,
        np.array(
            [
                [885, 675],
                [252, 1130],
                [1477, 1431],
                [1583, 774],
            ]
        ),
    ),
]
