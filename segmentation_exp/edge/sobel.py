import cv2 as cv
import os
import argparse
import yaml
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

class Image:
    def __init__(self, img):
        self.original = img
        self.gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        self.blur = cv.GaussianBlur(self.gray, (3,3), 0) 
        
    def applyKernel(self, flag):
        if flag == 0:
            kernel = [[-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]]
        elif flag == 1:
            kernel = [[-1, -2, -1],
                      [0, 0, 0],
                      [1, 2, 1]]
        else:
            return self.blur
        
        aux = np.zeros(self.blur.shape)
        for i, row in enumerate(self.blur):
            if i+2 < self.blur.shape[0]:
                for j, value in enumerate(row):
                    if j+2 < self.blur.shape[1]:
                        soma = 0
                        for k in range(3):
                            for l in range(3):
                                soma += int(self.blur[i+k][j+l]) * kernel[k][l]
                        aux[i+1][j+1] = soma
        return aux
    
    def sobel(self):
        my_gx = self.applyKernel(0)
        my_gy = self.applyKernel(1)
        my_g = np.sqrt(my_gx**2+my_gy**2)
        gx = cv.Sobel(self.blur, cv.CV_64F, 1, 0, ksize=3)
        gy = cv.Sobel(self.blur, cv.CV_64F, 0, 1, ksize=3)
        g = np.sqrt(gx**2+gy**2)

        self.my_gx = np.uint8(255*np.abs(my_gx)/np.max(my_gx))
        self.my_gy = np.uint8(255*np.abs(my_gy)/np.max(my_gy))
        self.my_g = np.uint8(255*my_g/np.max(my_g))
        self.gx = np.uint8(255*np.abs(gx)/np.max(gx))
        self.gy = np.uint8(255*np.abs(gy)/np.max(gy))
        self.g = np.uint8(255*g/np.max(g))

    def saveFig(self, name):
        plt.figure(figsize=(15,10))

        plt.subplot(3,3,1)
        plt.imshow(self.original)
        plt.title('Original Image')
        plt.axis('off')

        plt.subplot(3,3,2)
        plt.imshow(self.gray, cmap='gray')
        plt.title('Gray Image')
        plt.axis('off')

        plt.subplot(3,3,3)
        plt.imshow(self.blur, cmap='gray')
        plt.title('Blurred Image')
        plt.axis('off')

        plt.subplot(3,3,4)
        plt.imshow(self.my_gx, cmap='gray', vmin=0, vmax=255)
        plt.title('My Gradient in X Direction')
        plt.axis('off')

        plt.subplot(3,3,5)
        plt.imshow(self.my_gy, cmap='gray', vmin=0, vmax=255)
        plt.title('My Gradient in Y Direction')
        plt.axis('off')

        plt.subplot(3,3,6)
        plt.imshow(self.my_g, cmap='gray', vmin=0, vmax=255)
        plt.title('My Sobel Edge Detection')
        plt.axis('off')

        plt.subplot(3,3,7)
        plt.imshow(self.gx, cmap='gray', vmin=0, vmax=255)
        plt.title('Gradient in X Direction')
        plt.axis('off')

        plt.subplot(3,3,8)
        plt.imshow(self.gy, cmap='gray', vmin=0, vmax=255)
        plt.title('Gradient in Y Direction')
        plt.axis('off')

        plt.subplot(3,3,9)
        plt.imshow(self.g, cmap='gray', vmin=0, vmax=255)
        plt.title('Sobel Edge Detection')
        plt.axis('off')

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
    for image in images:
        name = dest_dir + image.split('/')[-1]
        img = Image(cv.imread(image))
        img.sobel()
        img.saveFig(name)
        del img

if __name__ == "__main__":
    main()

