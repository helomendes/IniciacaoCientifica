import argparse
import os
import cv2 as cv
import matplotlib.pyplot as plt
from yaml import safe_load
from glob import glob
from skimage import io, color

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
        img_name = os.path.split(image)[-2]

        bgr_img = cv.imread(image)
        rgb_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2RGB)
        gray_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2GRAY)

        rgb = io.imread(image)
        lab = color.rgb2lab(rgb_img)
        gray = color.rgb2gray(rgb_img)
        
        fig = plt.figure(figsize=(10,7))
        fig.add_subplot(2,2,1)
        plt.imshow(bgr_img)
        plt.axis('off')
        plt.title("BGR")
        fig.add_subplot(2,2,2)
        plt.imshow(rgb_img)
        plt.axis('off')
        plt.title("RGB")
        fig.add_subplot(2,2,3)
        plt.imshow(gray_img, cmap=plt.cm.gray)
        plt.axis('off')
        plt.title("GRAY")
        plt.savefig(f'{dest_dir}/{img_name}.jpg')
        print(f'{dest_dir}/{img_name}.jpg')
        plt.show()

        #cv.imshow('image test', img)
        #cv.waitKey(0)
        #cv.destroyAllWindows()

if __name__ == "__main__":
    main()
