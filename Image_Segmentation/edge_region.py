import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from skimage.feature import canny, sobel
from skimage import data, morphology
from skimage.color import rgb2gray

def main():
    plt.rcParams["figure.figsize"] = (12,8)
    rocket = data.rocket()
    rocket_wh = rgb2gray(rocket)

    edges = canny(rocket_wh)
    plt.imshow(edges, interpolation='gaussian')
    plt.title('canny detector')

    fill_im = nd.binary_fill_holes(edges)
    plt.imshow(fill_im)
    plt.title('Region Filling')

    elevation_map = sobel(rocket_wh)
    plt.imshow(elevation_map)

    markers = np.zeros_like(rocket_wh)
    markers[rocket_wh < 0.1171875] = 1
    markers[rocket_wh > 0.5859375] = 2
    
    plt.imshow(markers)
    plt.title('markers')

    segmentation = morphology.watershed(elevation_map, markers)

    plt.imshow(segmentation)
    plt.title('watershed segmentation')

    segmentation = nd.binary_fill_holes(segmentation - 1)
    label_rock, _ = nd.label(segmentation)

    image_label_overlay = label2rgb(label_rock, image=rocket_wh)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 16), sharey = True)
    ax1.imshow(rocket_wh)
    ax1.contour(segmentation, [0.8], linewidths = 1.8, colors = 'w')
    ax2.imshow(image_label_overlay)

    fig.subplots_adjust(**margins)

if __name__=="__main__":
    main()
