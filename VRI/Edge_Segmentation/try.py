import cv2 as cv
import copy
import os
import argparse
import yaml
import matplotlib.pyplot as plt
from glob import glob
from Image import Image
from EdgeDetection import EdgeDetection

def saveFig(img, alg, name):
    '''
    plt.figure(figsize=(15,10))

    plt.subplot(1,2,1)
    plt.imshow(img.rgb)
    plt.title('Imagem Original', fontsize=30)
    plt.axis('off')

    
    plt.subplot(1,2,2)
    plt.imshow(img.gray, cmap='gray')
    plt.title('Escala Cinza', fontsize=30)
    plt.axis('off')

    plt.tight_layout()
    plt.savefig(name)
    '''

    plt.figure(figsize=(15,10))

    plt.subplot(1,2,1)
    plt.imshow(img.gray, cmap='gray')
    plt.title('Escala Cinza', fontsize=30)
    plt.axis('off')

    
    plt.subplot(1,2,2)
    plt.imshow(alg.laplacian, cmap='gray', vmin=0, vmax=255)
    plt.title('Detecção Laplacian', fontsize=30)
    plt.axis('off')

    name += f"_Laplacian_compare.jpg"
    plt.tight_layout()
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
    for i in images:
        if 'BO097Osteoide3' in i:
            image = i
            break
    name = dest_dir + image.split('/')[-1]
    img = Image(cv.imread(image))
    alg = EdgeDetection(img)
    alg.laplacian()
    saveFig(img, alg, name) 

if __name__ == "__main__":
    main()

