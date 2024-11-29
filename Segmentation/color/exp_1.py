import argparse
import os
import cv2 as cv
import matplotlib.pyplot as plt
from yaml import safe_load
from glob import glob
from skimage import io
from skimage import color

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("--config", help='Configuration file yaml type', required=True)
    args = parse.parse_args()
    with open(args.config, 'r') as file:
        config = safe_load(file)

    imgs_dir = os.path.abspath(config.get('images_dir')) + '/'
    dest_dir = os.path.abspath(config.get('destination_dir')) + '/'
    imgs = sorted(glob(f'{imgs_dir}/*'))
    for image in imgs:
        img_name = os.path.split(image)[-1]
        img_name = img_name[:-4]

        rgb = io.imread(image)[:,:,:3]
        lab = color.rgb2lab(rgb)
        gray = color.rgb2gray(rgb)
        hsv = color.rgb2hsv(rgb)

        fig = plt.figure(figsize=(10,7))
        fig.add_subplot(2,2,1)
        plt.imshow(rgb)
        plt.axis('off')
        plt.title("RGB")
        fig.add_subplot(2,2,3)
        plt.imshow(lab)
        plt.axis('off')
        plt.title("LAB")
        fig.add_subplot(2,2,2)
        plt.imshow(gray, cmap=plt.cm.gray)
        plt.axis('off')
        plt.title("GRAY")
        fig.add_subplot(2,2,4)
        plt.imshow(hsv)
        plt.axis("off")
        plt.title("HSV")
        name = img_name + '_skimage'
        plt.savefig(f'{dest_dir}{name}.jpg')

if __name__ == "__main__":
    main()
