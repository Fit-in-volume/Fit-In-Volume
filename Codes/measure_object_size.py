import cv2
from object_detector import *
import numpy as np

# Load Aruco detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)


# Load Object Detector
detector = HomogeneousBgDetector()

# Load Image
img1 = cv2.imread("/Users/krc/Downloads/measure_object_size/imgs/box with marker1.png")
img2 = cv2.imread("/Users/krc/Downloads/measure_object_size/imgs/box with marker2.png")

def get_sizes(image):
    # Get Aruco marker
    corners, _, _ = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)

    # Draw polygon around the marker
    int_corners = np.int0(corners)
    cv2.polylines(image, int_corners, True, (0, 255, 0), 5)

    # Aruco Perimeter
    aruco_perimeter = cv2.arcLength(corners[0], True)

    # Pixel to cm ratio
    pixel_cm_ratio = aruco_perimeter / 20

    contours = detector.detect_objects(image)

    # Draw objects boundaries
    height_lists = [] 
    width_lists = []
    for cnt in contours:
        # Get rect
        rect = cv2.minAreaRect(cnt)
        (x, y), (h, w), angle = rect

        # Get Width and Height of the Objects by applying the Ratio pixel to cm
        object_height = h / pixel_cm_ratio
        object_width = w / pixel_cm_ratio
        r_height = round(object_height,1)
        r_width = round(object_width,1)
        height_lists.append(r_height)
        width_lists.append(r_width)

    print(max(height_lists), max(width_lists)) 

    # Display rectangle
    # box = cv2.boxPoints(rect)
    # box = np.int0(box)
    # cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)
    # cv2.polylines(image, [box], True, (255, 0, 0), 2)
    # cv2.putText(image, "Height {} cm".format(max(height_lists)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    # cv2.putText(image, "Width {} cm".format(max(width_lists)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    # # cv2.imwrite('new.jpg',image)
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)

    # return max(height_lists), max(width_lists)

def compare_width(img1_width, img2_width):
    if img1_width - img2_width < 0.5: 
        print(img1_height, img1_width, img2_height) 

# img1_height, img1_width = get_sizes(img1)
# img2_height, img2_width = get_sizes(img2)
# compare_width(img1_width, img2_width)   
get_sizes(img1)
get_sizes(img2)