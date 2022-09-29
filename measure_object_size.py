import cv2
from object_detector import *
import numpy as np
from rembg import remove
import os 
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
detector = Measuring_Volume()

img_path = "/Users/krc/Downloads/Fit_in_Volume/imgs"
input = f"{img_path}/물병1.jpg"
name = os.path.basename(input)
input_path = f'/Users/krc/Downloads/Fit_in_Volume/imgs/{name}'
output_path = f'/Users/krc/Downloads/Fit_in_Volume/rembg/Rembg_{name}'

input = cv2.imread(input_path)
output = remove(input)
cv2.imwrite(output_path, output)

img = cv2.imread(output_path)

def get_sizes(image):
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
    cv2.putText(image, "Height {} cm".format(r_width), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 4, (100, 400, 0), 4)
    cv2.putText(image, "Width {} cm".format(r_height), (int(x - 100), int(y + 50)), cv2.FONT_HERSHEY_PLAIN, 4, (100, 400, 0), 4)
    cv2.imshow("Image", image)
    cv2.imwrite(f"/Users/krc/Downloads/Fit_in_Volume/output/Output_{name}", image)
    cv2.waitKey(0)

# def compare_width(img1_width, img2_width):
#     if img1_width - img2_width < 0.5: 
#         print(img1_height, img1_width, img2_height) 

# img1_height, img1_width = get_sizes(img1)
# img2_height, img2_width = get_sizes(img2)
# compare_width(img1_width, img2_width)   
# get_sizes(img1)
# get_sizes(img2)

get_sizes(img)
