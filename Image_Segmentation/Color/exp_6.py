import argparse
from yaml import safe_load
import os
from glob import glob
import cv2 as cv
import numpy as np
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='Configuration YAML file')
args = parser.parse_args()

with open(args.config, 'r') as file:
    config = safe_load(file)

imgs_dir = os.path.abspath(config.get('images_dir')) + '/'
dest_dir = os.path.abspath(config.get('destination_dir')) + '/'

color = np.uint8([[config.get('color')]])
hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)
frst = hsv_color[0][0][0]
hsv_lower = np.array([frst - 5, 100, 150])
hsv_upper = np.array([frst + 5, 255, 255])

hsv = hsv_color[0][0]
code = f'{hsv[0]}_{hsv[1]}_{hsv[2]}'

color = np.uint8([[[88, 91, 118]]])
hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)
frst = hsv_color[0][0][0]
hsv_lower_2 = np.array([frst - 3, 80, 120])
hsv_upper_2 = np.array([frst + 3, 255, 255])

imgs = sorted(glob(f'{imgs_dir}/*'))
asw = input('Save?')
for image in imgs:
    img_name = os.path.split(image)[-1][:-4]
    img = cv.imread(image) 
    img = cv.resize(img, (0,0), None, .50, .50)
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask1 = cv.inRange(img_hsv, hsv_lower, hsv_upper)
    mask2 = cv.inRange(img_hsv, hsv_lower_2, hsv_upper_2)
    mask = cv.bitwise_or(mask1, mask2)
    res = cv.bitwise_and(img, img, mask=mask)
    nocolor = cv.bitwise_and(img, img, mask=cv.bitwise_not(mask).astype(np.uint8))

    mask_3_channel = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    numpy_horizontal_1 = np.hstack((img, mask_3_channel))
    numpy_horizontal_2 = np.hstack((res, nocolor))
    numpy_vertical = np.vstack((numpy_horizontal_1, numpy_horizontal_2))

    cv.imshow('Np Vertical', numpy_vertical)
    cv.waitKey()
    if asw == 'y' or asw == 'Y':
        today = datetime.now()
        save_dir = f'{dest_dir}/{code}'
        os.makedirs(save_dir, exist_ok=True)
        cv.imwrite(f'{save_dir}/{img_name}.jpg', numpy_vertical)
