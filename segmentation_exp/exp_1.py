import argparse
import os
import cv2 as cv
import matplotlib.pyplot as plt
from yaml import safe_load
from glob import glob

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("--config", help='Configuration file yaml type', required=True)
    args = parse.parse_args()
    with open(args.config, 'r') as file:
        config = safe_load(file)

    imgs_dir = os.path.abspath(config.get('images_dir')) + '/'
    imgs = sorted(glob(f'{imgs_dir}/*'))
    for image in imgs:
        plt.imshow(image)

if __name__ == "__main__":
    main()
