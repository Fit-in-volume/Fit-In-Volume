import cv2
from utils import *
import numpy as np
from rembg import remove
import os 


detector = Measuring_Volume()

img_path = "/Users/krc/Downloads/Fit_in_Volume/imgs"
input = f"{img_path}/밴드2.jpg"
name = os.path.basename(input)
input_path = f'/Users/krc/Downloads/Fit_in_Volume/imgs/{name}'
output_path = f'/Users/krc/Downloads/Fit_in_Volume/rembg/Rembg_{name}'

input = cv2.imread(input_path)
output = remove(input)
cv2.imwrite(output_path, output)

img = cv2.imread(output_path)

detector.get_sizes(img, name)