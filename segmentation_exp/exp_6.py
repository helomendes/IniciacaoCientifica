import argparse
from yaml import safe_load
import os
from glob import glob
import cv2 as cv
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='Configuration YAML file')
args = parser.parse_args()

with open(args.config, 'r') as file:
    config = safe_load(file)

imgs_dir = os.path.abspath(config.get('images_dir')) + '/'
dest_dir = os.path.abspath(config.get('destination_dir')) + '/'

color = np.uint8([[[122, 142, 150]]])
hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)
frst = hsv_color[0][0][0]
hsv_lower = np.array([frst - 10, 100, 100])
hsv_upper = np.array([frst + 10, 255, 255])

imgs = sorted(glob(f'{imgs_dir}/*'))
for image in imgs:
    img = cv.imread(image)
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(img_hsv, hsv_lower, hsv_upper)
    res = cv.bitwise_and(img, img, mask=mask)
    nocolor = cv.bitwise_and(img, img, mask=cv.bitwise_not(mask).astype(np.uint8))
    #cv.imshow('Original Image', res)
    cv.imshow('Image', res)
    
    cv.waitKey()

