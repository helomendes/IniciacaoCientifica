import argparse
import yaml
import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

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
    img_path = imgs[-2]
    name = dest_dir + img_path.split('/')[-1].split('.')[0]
    img = cv.imread(img_path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    thresh = 125

    dic = {}
    for i in range(6):
        dic[i] = {}
        dic[i]['Name'] = None
        dic[i]['Type'] = None
        dic[i]['Image'] = None
        dic[i]['Save_name'] = None
    dic[0]['Name'] = 'Original'
    dic[1]['Name'] = 'Binário'
    dic[1]['Type'] = 0
    dic[2]['Name'] = 'Binário_Invertido'
    dic[2]['Type'] = 1
    dic[3]['Name'] = 'Truncamento'
    dic[3]['Type'] = 2
    dic[4]['Name'] = 'Threshold_para_Zero'
    dic[4]['Type'] = 3
    dic[5]['Name'] = 'Threshold_para_Zero_Invertido'
    dic[5]['Type'] = 4

    i = 0
    while i < 6:
        if dic[i]['Type'] != None:
            _, dic[i]['Image'] = cv.threshold(img_gray, thresh, 255, dic[i]['Type'])
            dic[i]['Save_name'] = name + dic[i]['Name'] + '.png'
        else:
            dic[i]['Image'] = img_gray
            dic[i]['Save_name'] = name + '.png'

        if dic[i]['Type'] == None:
            plt.figure(figsize=(15,10))
            
            plt.subplot(1, 2, 1)
            plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
            plt.title('Original', fontsize=30)
            plt.axis('off')

            plt.subplot(1, 2, 2)
            plt.imshow(dic[i]['Image'], cmap='gray')
            plt.title('Escala_Cinza', fontsize=30)
            plt.axis('off')
        
            plt.tight_layout()
            plt.savefig(dic[i]['Save_name'])

        elif dic[i]['Type'] == 2:
            plt.figure(figsize=(15,10))
            plt.subplot(1, 1, 1)
            plt.imshow(dic[i]['Image'], cmap='gray')
            plt.title(dic[i]['Name'], fontsize=30)
            plt.axis('off')
            
            plt.tight_layout()
            plt.savefig(dic[i]['Save_name'])
        else:
            _, dic[i+1]['Image'] = cv.threshold(img_gray, thresh, 255, dic[i+1]['Type'])
            dic[i+1]['Save_name'] = name + dic[i+1]['Name'] + '.png'

            plt.figure(figsize=(15,10))
            
            plt.subplot(1, 2, 1)
            plt.imshow(dic[i]['Image'], cmap='gray')
            plt.title(dic[i]['Name'], fontsize=30)
            plt.axis('off')

            plt.subplot(1, 2, 2)
            plt.imshow(dic[i+1]['Image'], cmap='gray')
            plt.title(dic[i+1]['Name'], fontsize=30)
            plt.axis('off')
        
            plt.tight_layout()
            plt.savefig(dic[i]['Save_name'])
            i += 1
        i += 1

if __name__=="__main__":
    main()
