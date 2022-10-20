import cv2
import numpy as np
from rembg import remove
import os 

class Measuring_Volume():
    def __init__(self):
        pass

    def detect_objects(self, image):


        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 31, 5)
           
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        objects_contours = []
        areas = []

        for cnt in contours:
            # area = cv2.contourArea(cnt)
            # areas.append(area)
                #cnt = cv2.approxPolyDP(cnt, 0.03*cv2.arcLength(cnt, True), True)
            objects_contours.append([cnt])
        # max_index = areas.index(max(areas))
        object_contours = objects_contours[-1]
        return object_contours

detector = Measuring_Volume()
def image_xy(image):
    max_y, max_x, rgb = image.shape
    total_xy = max_y * max_x
    return [max_y, max_x, total_xy]

def object_areas(image):
    y, x, total = image_xy(image)
    x_area = int((x) * (2/3))
    object_area = image[:, :x_area, :]
    return object_area

def marker_areas(image):
    y, x, total = image_xy(image)
    x_area = int((x) * (2/3))
    marker_area = image[:, x_area:, :]
    return marker_area

def get_sizes(input,name):
    print(name)
    image = cv2.imread(input)

    marker_area = marker_areas(image)
    object_area = object_areas(image)
    
    parameters = cv2.aruco.DetectorParameters_create()
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_1000)

    corners, _, _ = cv2.aruco.detectMarkers(marker_area, aruco_dict, parameters=parameters)

    int_corners = np.int0(corners)
    
    cv2.polylines(marker_area, int_corners, True, (0, 255, 0), 5)
    
    aruco_perimeter = cv2.arcLength(corners[0], True)
    
    pixel_cm_ratio = aruco_perimeter / 16

    # rembg_path = f'/Users/krc/Downloads/Fit_in_Volume/rembg/Rembg_{name}'
    # output = remove(image)
    # cv2.imwrite(rembg_path, output)
    # img = cv2.imread(rembg_path)

    output = remove(object_area)
    contours = detector.detect_objects(output)

    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect
        if int(angle) < 45: 
            object_width = w / pixel_cm_ratio
            object_height = h / pixel_cm_ratio
        else:
            object_width = h / pixel_cm_ratio
            object_height = w / pixel_cm_ratio
        r_width = round(object_width,1)
        r_height = round(object_height,1)
        print(r_width,r_height)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
    
    cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1) 
    cv2.polylines(image, [box], True, (255, 0, 0), 2)
    # y, x, total = image_xy(image)
    # text_area = np.zeros((y+200, x, 3))
    # text_area[0:y, 0:x] = image
    cv2.putText(image, "Width {} cm".format(r_width), (100, 200), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 0), 7)
    cv2.putText(image, "Height {} cm".format(r_height), (1000, 200), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 0), 7)
    cv2.imshow("Image", image)
    cv2.imwrite(f"/Users/krc/Downloads/Fit_in_Volume/imgs/new/output/Output_{name}", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # return r_width, r_height

def compare_width(img1_width,img1_height, img2_width, img2_height):
    if abs(img1_width - img2_width) <= 1.0: 
        width = round(((img1_width + img2_width) / 2), 1)
        height = img1_height
        depth = img2_height
        return f"가로 : {width}\t\t 세로 : {height}\t\t 높이 : {depth}"  

def get_circumference(img1_width, img1_height):
    circumference = round((img1_width * 3.14),1)
    height = img1_height
    return f"원주 : {circumference}\t\t 지름 : {img1_width}\t\t 세로 : {height}"