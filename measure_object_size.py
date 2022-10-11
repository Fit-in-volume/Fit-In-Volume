import cv2
from object_detector import *
import numpy as np
from rembg import remove
import os 

detector = Measuring_Volume()

# input = f'C:/Users/Jay/Downloads/Fit_in_Volume/imgs/크라운산도측면.jpg'
# name = os.path.basename(input)

img_dir = 'C:/Users/Jay/Downloads/Fit_in_Volume/uploads'
files = os.listdir(img_dir)

def get_sizes(input,name):
    image = cv2.imread(input)
    parameters = cv2.aruco.DetectorParameters_create()
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_1000)
 
    corners, _, _ = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)

    int_corners = np.int0(corners)
    
    cv2.polylines(image, int_corners, True, (0, 255, 0), 5)
    
    aruco_perimeter = cv2.arcLength(corners[0], True)
    
    pixel_cm_ratio = aruco_perimeter / 16

    rembg_path = f'C:/Users/Jay/Downloads/Fit_in_Volume/rembg/Rembg_{name}'
    output = remove(image)
    cv2.imwrite(rembg_path, output)
    img = cv2.imread(rembg_path)

    contours = detector.detect_objects(img)

    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        (x, y), (h, w), angle = rect

        object_height = h / pixel_cm_ratio
        object_width = w / pixel_cm_ratio
        r_height = round(object_height,1)
        r_width = round(object_width,1)
        
        box = cv2.boxPoints(rect)
        box = np.int0(box)
    cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1) 
    cv2.polylines(image, [box], True, (255, 0, 0), 2)
    cv2.putText(image, "Height {} cm".format(r_height), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 4, (100, 400, 0), 4)
    cv2.putText(image, "Width {} cm".format(r_width), (int(x - 100), int(y + 50)), cv2.FONT_HERSHEY_PLAIN, 4, (100, 400, 0), 4)
    cv2.imshow("Image", image)
    cv2.imwrite(f"C:/Users/Jay/Downloads/Fit_in_Volume/output/Output_{name}", image)
    cv2.waitKey(0)

for item in files:
    if (img_dir+item).__contains__(".jpg" or ".png"):
        get_sizes(img_dir + item, item)