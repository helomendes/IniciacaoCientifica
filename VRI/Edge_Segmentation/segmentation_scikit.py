import os
import yaml
import argparse
import numpy as np
import skimage as ski
import matplotlib.pyplot as plt
from skimage import morphology
from scipy import ndimage as ndi
from skimage.filters import sobel
from skimage.feature import canny
from skimage.color import label2rgb
from skimage.exposure import histogram

class Figure:
    def __init__(self, dest, name, headless):
        self.dest = dest
        self.name = name
        self.headless = headless

    def saveFig(self, fig, style, low=None, high=None):
        if low and high:
            fig.savefig(f'{self.dest}{self.name}_{style}_{low}_{high}.png')
        else:
            fig.savefig(f'{self.dest}{self.name}_{style}.png')

        if not self.headless:
            plt.show()
        plt.close()
        
class Segmentation:
    def __init__(self, img):
        self.img = img

    def thresholding(self, figure):
        hist, hist_centers = ski.exposure.histogram(self.img)
        low = 30 
        high = 150

        fig, axs = plt.subplots(2, 2, figsize = (10, 5))
        
        axs[0][0].imshow(self.img, cmap='gray')
        axs[0][0].set_title('')
        axs[0][0].axis('off')
        axs[0][1].plot(hist_centers, hist, lw=2)
        axs[0][1].set_title('histograms of gray values')
        axs[1][0].imshow(self.img < low, cmap = plt.cm.gray)
        axs[1][0].set_title(f'img < {low}')
        axs[1][0].set_axis_off()
        axs[1][1].imshow(self.img > high, cmap = plt.cm.gray)
        axs[1][1].set_title(f'img > {high}')
        axs[1][1].set_axis_off()
        fig.tight_layout()

        figure.saveFig(fig, 'thresholding', low, high)

    def edgeBased(self, figure):
        edges = canny(self.img)
        fill = ndi.binary_fill_holes(edges)
        clean = morphology.remove_small_objects(fill, 21)

        fig, axs = plt.subplots(1, 3, figsize = (10, 5))
        axs[0].imshow(edges, cmap=plt.cm.gray)
        axs[0].set_title('Canny detector')
        axs[0].set_axis_off()
        axs[1].imshow(fill, cmap=plt.cm.gray)
        axs[1].set_title('Filled')
        axs[1].set_axis_off()
        axs[2].imshow(clean, cmap=plt.cm.gray)
        axs[2].set_title('Cleaned')
        axs[2].set_axis_off()
        fig.tight_layout()

        figure.saveFig(fig, 'edgeBased')

    def regionBased(self, figure):
        elevation_map = sobel(self.img)

        fig, axs = plt.subplots(1, 3, figsize = (10, 5))
        axs[0].imshow(elevation_map, cmap=plt.cm.gray)
        axs[0].set_title('elevation map')
        axs[0].set_axis_off()
        
        markers = np.zeros_like(self.img)
        markers[self.img < 30] = 1
        markers[self.img > 150] = 2

        axs[1].imshow(markers, cmap=plt.cm.nipy_spectral)
        axs[1].set_title('markers')
        axs[1].set_axis_off()

        segmentation = ski.segmentation.watershed(elevation_map, markers)

        axs[2].imshow(segmentation, cmap=plt.cm.gray)
        axs[2].set_title('segmentation')
        axs[2].set_axis_off()

        figure.saveFig(fig, 'regionBased')

        self.segmentation = segmentation

    def labeling(self, figure):
        segmentation = self.segmentation
        segmentation = ndi.binary_fill_holes(segmentation - 1)
        labeled, _ = ndi.label(segmentation)
        image_label_overlay = label2rgb(labeled, image=self.img, bg_label=0)
        
        fig, axs = plt.subplots(1, 2, figsize = (10, 5))
        axs[0].imshow(self.img, cmap = plt.cm.gray)
        axs[0].contour(segmentation, [0.5], linewidths = 1.2, colors= 'y')
        axs[0].set_axis_off()
        axs[1].imshow(image_label_overlay)
        axs[1].set_axis_off()
        fig.tight_layout()
        figure.saveFig(fig, 'labeled')

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('--config')
    parse.add_argument('-c', required=False, action='store_true')
    parse.add_argument('-headless', required=False, action='store_true')
    parse.add_argument('-all', required=False, action='store_true')
    args = parse.parse_args()

    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    dest = os.path.abspath(config.get('dest_dir')) + '/'
    os.makedirs(dest, exist_ok=True)
    
    headless=False
    if args.headless:
        headless=True

    segs = []
    names = []
    if args.c:
        name = 'coins'
        names.add(name)
        img = ski.data.coins()
        seg = Segmentation(img)
        segs.add(seg)
    else:
        img_path = config.get('img')
        if not args.all:
            name = img_path.split('/')[-1][:-4]
            names.add(name)
            img = ski.io.imread(img_path, as_gray = True)
            img = ski.util.img_as_ubyte(img)
            seg = Segmentation(img)
            segs.add(seg)
        else:
            source = img_path.rsplit('/', 1)[0]
            names = [name for name in os.listdir(source)]
            imgs = [ski.io.imread(f'{source}/{img}', as_gray=True) for img in names] 
            imgs = [ski.util.img_as_ubyte(img) for img in imgs]
            segs = [Segmentation(img) for img in imgs]

    for i, seg in enumerate(segs):
        figure = Figure(dest, names[i], headless)
        seg.thresholding(figure)
        seg.edgeBased(figure)
        seg.regionBased(figure)
        seg.labeling(figure)

if __name__ == "__main__":
    main()
