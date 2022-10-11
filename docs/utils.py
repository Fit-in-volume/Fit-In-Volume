import cv2
import numpy as np
from rembg import remove
import os 

class Measuring_Volume():
    def __init__(self):
        pass
    
    def detect_objects(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)   

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        objects_contours = []

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 2000:
                #cnt = cv2.approxPolyDP(cnt, 0.03*cv2.arcLength(cnt, True), True)
                objects_contours.append(cnt)
        return objects_contours
    def get_sizes(self, image, name):
        detector = Measuring_Volume()
        parameters = cv2.aruco.DetectorParameters_create()
        aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
        corners, _, _ = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)

        int_corners = np.int0(corners)
        
        cv2.polylines(image, int_corners, True, (0, 255, 0), 5)
        
        aruco_perimeter = cv2.arcLength(corners[0], True)

        pixel_cm_ratio = aruco_perimeter / 16
    
        contours = detector.detect_objects(image)
        height_lists = [] 
        width_lists = []
        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            (x, y), (h, w), angle = rect

            object_height = h / pixel_cm_ratio
            object_width = w / pixel_cm_ratio
            r_height = round(object_height,1)
            r_width = round(object_width,1)
            height_lists.append(r_height)
            width_lists.append(r_width)

            box = cv2.boxPoints(rect)
            box = np.int0(box)
        cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1) 
        cv2.polylines(image, [box], True, (255, 0, 0), 2)
        cv2.putText(image, "Height {} cm".format(r_height), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 4, (100, 400, 0), 4)
        cv2.putText(image, "Width {} cm".format(r_width), (int(x - 100), int(y + 50)), cv2.FONT_HERSHEY_PLAIN, 4, (100, 400, 0), 4)
        cv2.imshow("Image", image)
        cv2.imwrite(f"/Users/krc/Downloads/Fit_in_Volume/output/Output_{name}", image)
        cv2.waitKey(0)

    def compare_width(img1_width, img2_width):
        if abs(img1_width - img2_width) <= 0.5: 
            print(img1_height, img1_width, img2_height) 
