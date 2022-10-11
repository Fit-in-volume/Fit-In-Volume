import cv2
import numpy as np
from rembg import remove

class Measuring_Volume():
    def __init__(self):
        pass

    def detect_objects(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 31, 5)
           
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        objects_contours = []

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 20000:
                #cnt = cv2.approxPolyDP(cnt, 0.03*cv2.arcLength(cnt, True), True)
                objects_contours.append(cnt)
        return objects_contours