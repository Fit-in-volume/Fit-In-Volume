import cv2
from utils import *
import numpy as np
from rembg import remove
import os 

detector = Measuring_Volume()

img_dir = '/Users/krc/Downloads/Fit_in_Volume/imgs/new/imgs/'
files = os.listdir(img_dir)
if os.path.exists(img_dir+'.DS_Store'):
    os.remove(img_dir+'.DS_Store')

# Case1: product is rectangle
# Get two different width and height and compare width to identify whether it is same product
# And return width height depth(as second image's height)
# Case2: product is cylinder 
# Return width and height
# Case3: neither 
# Print error message

if __name__ == "__main__":
    if len(files) == 1 :
        for i in range(len(files)):
            if (img_dir+files[i]).__contains__(".jpg" or ".png"):
                globals()[f'img{i+1}_width'], globals()[f'img{i+1}_height'] = get_sizes(img_dir + files[i], files[i])
        print(compare_width(img1_width, img2_width))
    elif len(files) == 2 : 
        for i in range(len(files)):
            if (img_dir+files[i]).__contains__(".jpg" or ".png"):
                globals()[f'img{i+1}_width'], globals()[f'img{i+1}_height'] = get_sizes(img_dir + files[i], files[i])
        print(f"가로 : {img1_width}\n 세로 : {img1_height}")
    else : 
        print("ERROR : Pls restart the app")

# Test code : get all the files in a folder
if __name__ == "__main__":
    for item in files:
        if (img_dir+item).__contains__(".jpg" or ".jpeg" or ".png"):
            get_sizes(img_dir + item, item)