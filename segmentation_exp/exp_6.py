import argparse
from yaml import safe_load
import os
from glob import glob
import cv2 as cv

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='Configuration YAML file')
args = parser.parse_args()

with open(args.config, 'r') as file:
    config = safe_load(file)

imgs_dir = os.path.abspath(config.get('images_dir')) + '/'
dest_dir = os.path.abspath(config.get('destination_dir')) + '/'

imgs = sorted(glob(f'{imgs_dir}/*'))
for image in imgs:
    img = cv.imread(image)
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    #img_threshold = cv.inRange(img_hsv, )
    cv.imshow('Original Image', img)
    #cv.imshow('inRange', img_threshold)
    cv.waitKey()

