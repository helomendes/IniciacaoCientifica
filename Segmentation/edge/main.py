import cv2 as cv
import copy
import os
import argparse
import yaml
import matplotlib.pyplot as plt
from glob import glob
from Image import Image
from EdgeDetection import EdgeDetection

def saveFigs(figs, name, which):
    plt.figure(figsize=(15,10))

    for i, fig in enumerate(figs):
        plt.subplot(2,3,i+1)
        attr = getattr(figs[i], which)
        plt.imshow(attr, cmap='gray')
        plt.title('')
        plt.axis('off')
    
    name += f"_{which}.jpg"
    plt.savefig(name)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help="Configuration YAML file")
    args = parser.parse_args()

    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)
    
    imgs_dir = os.path.abspath(config.get('images_dir')) + '/'
    dest_dir = os.path.abspath(config.get('dest_dir')) + '/'
    os.makedirs(dest_dir, exist_ok=True)

    images = sorted(glob(f'{imgs_dir}/*'))
    figs = []
    name_all = dest_dir + "all_images"
    for image in images:
        name = dest_dir + image.split('/')[-1]
        img = Image(cv.imread(image))
        alg = EdgeDetection(img)
        alg.detectEdges()
        img.saveFig(name, alg)
        figs.append(copy.copy(alg))
        del img
    for method in ("sobel", "canny", "laplacian", "prewitt", "robertsCross", "scharr"):
        saveFigs(figs, name_all, method)

if __name__ == "__main__":
    main()

