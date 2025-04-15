import argparse
import yaml
import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def compute_cumulative_hist(norm_hist):
    return np.cumsum(norm_hist)

def compute_entropy(norm_hist):
    entropy = np.where(norm_hist > 0, - norm_hist * np.log(norm_hist), 0)
    return np.cumsum(entropy)

def compute_threshold(norm_hist):
    cumu_hist = compute_cumulative_hist(norm_hist)
    entropy_vals = compute_entropy(norm_hist)
    entropy_255 = entropy_vals[-1]

    f_values = np.zeros(256)

    for t in range(255):
        if cumu_hist[t] > 0 and cumu_hist[t] < 1:
            max_cumu_t = np.max(cumu_hist[:t+1])
            max_cumu_t_next = np.max(cumu_hist[t+1:])

            f1 = (entropy_vals[t] / entropy_255) * (np.log(cumu_hist[t]) / np.log(max_cumu_t))
            f2 = ( 1 - (entropy_vals[t] / entropy_255)) * (np.log(1 - cumu_hist[t]) / np.log(max_cumu_t_next))

        f_values[t] = f1+f2

    return np.argmax(f_values)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help="Configuration YAML file")
    args = parser.parse_args()
    
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    imgs_dir = os.path.abspath(config.get('images_dir')) + '/'
    dest_dir = os.path.abspath(config.get('dest_dir')) + '/'
    os.makedirs(dest_dir, exist_ok=True)

    imgs = sorted([f'{imgs_dir}{img}' for img in os.listdir(imgs_dir)])

    img = cv.imread(imgs[-2], cv.IMREAD_GRAYSCALE)
    hist = cv.calcHist(img, [0], None, [256], [0, 256]).flatten()
    norm_hist = hist / hist.sum()

    

    #threshold = compute_threshold(norm_hist)
    #_, binary_image = cv.threshold(img, threshold, 255, cv.THRESH_BINARY)

    #print('Threshold: ', threshold)

    plt.figure(figsize=(15,10))
    
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    '''
    plt.subplot(2, 2, 2)
    plt.imshow(binary_image, cmap='gray')
    plt.title('Binary Image')
    plt.axis('off')
    '''

    plt.subplot(2,2,3)
    plt.plot(hist, color='black', label='Histogram')
    plt.title('Original Histogram')
    plt.xlabel('Gray Level')
    plt.ylabel('Pixel Count')
    plt.legend()

    plt.subplot(2,2,4)
    plt.plot(norm_hist, color='red', label='Normalization')
    plt.title('Normalized Histogram')
    plt.xlabel('Gray Level')
    plt.ylabel('Pixel Count')
    plt.legend()

    #plt.savefig(f'{dest_dir}binaryimage.png')
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    main()
