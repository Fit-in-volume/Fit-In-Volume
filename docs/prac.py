import cv2
from object_detector import *
import numpy as np
from rembg import remove
import os 
image = cv2.imread("/Users/krc/Downloads/Fit_in_Volume/rembg/Rembg_자두2.jpg")

parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_1000)

corners, _, _ = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)

int_corners = np.int0(corners)

cv2.polylines(image, int_corners, True, (0, 255, 0), 5)

aruco_perimeter = cv2.arcLength(corners[0], True)
print(aruco_perimeter)