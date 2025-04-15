import argparse
from yaml import safe_load
import os
from glob import glob
import cv2 as cv
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='Configuration YAML file')
args = parser.parse_args()

with open(args.config, 'r') as file:
    config = safe_load(file)

imgs_dir = os.path.abspath(config.get('images_dir')) + '/'
dest_dir = os.path.abspath(config.get('destination_dir')) + '/'
imgs = sorted(glob(f'{imgs_dir}/*'))

for image in imgs:
    img_name = os.path.split(image)[-1][:-4]
    img = cv.imread(image)
    #img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ###### LOGARITHMIC TRANSFORMATION #####

    '''
    c = 1
    log_transformed = c * np.log(1 + img)
    c_1 = np.array(log_transformed, dtype = np.uint8)

    c = 25
    log_transformed = c * np.log(1 + img)
    c_25 = np.array(log_transformed, dtype = np.uint8)

    c = 50
    log_transformed = c * np.log(1 + img)
    c_50 = np.array(log_transformed, dtype = np.uint8)

    c = 75
    log_transformed = c * np.log(1 + img)
    c_75 = np.array(log_transformed, dtype = np.uint8)

    c = 150
    log_transformed = c * np.log(1 + img)
    c_150 = np.array(log_transformed, dtype = np.uint8)

    c = 255/(np.log(1 + np.int16(np.max(img))))
    log_transformed = c * np.log(1 + img)
    c_perfect = np.array(log_transformed, dtype = np.uint8)
    
    titles = ['Original', 'C = 1', 'C = 25', 'C = 50', 'C = 75', 'C = 150', 'Perfect C']
    images = [img, c_1, c_25, c_50, c_75, c_150, c_perfect]

    for i in range(7):
        plt.subplot(3, 3, i+1)
        plt.imshow(images[i], plt.cm.gray)
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    #plt.show()
    plt.savefig(f'{dest_dir}/logtransform_{img_name}.jpg')
    '''

    ##### POWER-LAW (GAMMA) TRANSFORMATION ######

    '''
    
    i = 1
    plt.subplot(3,3,i)
    plt.imshow(img, plt.cm.gray)
    plt.title('Original')
    plt.axis('off')

    for gamma in [0.1, 0.5, 1.2, 2.2]:
        i += 1
        gamma_corrected = np.array(255*(img/255) ** gamma, dtype=np.uint8)
        plt.subplot(3,3,i)
        plt.imshow(gamma_corrected, plt.cm.gray)
        plt.title(f'Gamma {gamma}')
        plt.axis('off')
    #plt.show()
    plt.savefig(f'{dest_dir}/gammatransform_{img_name}.jpg')

    '''
