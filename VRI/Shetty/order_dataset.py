import argparse
import os
import yaml
import glob
import csv
import cv2 as cv

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('--config_file', help='Path to the configuration file', required=True)
    args = parse.parse_args()

    conf = args.config_file
    with open(conf, 'r') as config_file:
        config = yaml.safe_load(config_file)

    ground_truth = os.path.abspath(config.get('ground_truth'))
    dataset_path = os.path.abspath(config.get('dataset_path')) + '/'
    destination = os.path.abspath(config.get('destination')) + '/'

    lesions = {}
    with open(ground_truth, newline='') as file:
        gt = csv.reader(file, delimiter=',', quotechar='|')
        header = next(gt)
        dx = header.index('dx')
        img = header.index('image_id')

        for row in gt:
            if row[dx] not in lesions:
                lesions[row[dx]] = []
            lesions[row[dx]].append(row[img])
    for les in lesions:
        os.makedirs(f'{destination}{les}', exist_ok=True)
    parts = ['1_part', '2_part']
    for part in parts:
        print(f'Copying images from {part}')
        for image in glob.glob(f'{dataset_path}{part}/*.jpg'):
            read_image = cv.imread(image)
            full_name = image.split('/')[-1]
            name = full_name.split('.')[0]
            for les in lesions:
                if name in lesions[les]:
                    cv.imwrite(f'{destination}{les}/{name}.JPEG', read_image)

if __name__ == "__main__":
    main()
