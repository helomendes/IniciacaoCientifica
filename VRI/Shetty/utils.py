import argparse
import csv
import os
import yaml
import glob
import random
import tensorflow as tf
from datetime import datetime

def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument('--config', help='YAML configuration file', required=True)
    args = parse.parse_args()
    try:
        with open(args.config, 'r') as file:
            config = yaml.safe_load(file)
    except Exception as ex:
        print('Unable to open configuration file')
        print(ex)
        exit()
    return config

''' 
def getDataset(images_dir, size):
    image_paths = []
    # full paths
    # when it gets the label, compares to a full path
    # they never match
    class_names = sorted([name for name in glob.glob(f'{images_dir}*/')])
    for name in class_names:
        ds = glob.glob(f'{name}/*')
        selected = random.sample(ds, size)
        image_paths.extend(selected)
    random.shuffle(image_paths)
    return image_paths, class_names
'''

def getDataset(images_dir, size):
    class_names = sorted([
        os.path.basename(os.path.normpath(name))
        for name in glob.glob(f'{images_dir}*/')
        ])

    n_training = int(0.8 * size)
    n_train = int(0.8 * n_training)
    n_val = int(0.2 * n_training)

    train_paths, val_paths, test_paths = [], [], []

    for name in class_names:
        all_images = glob.glob(f'{images_dir}{name}/*')
        selected = random.sample(all_images, size)

        train_paths.extend(selected[:n_train])
        val_paths.extend(selected[n_train:n_train+n_val])
        test_paths.extend(selected[n_train+n_val:])

    random.shuffle(train_paths)
    random.shuffle(val_paths)
    random.shuffle(test_paths)

    return train_paths, val_paths, test_paths, class_names

def getOutputName(dest_dir):
    today = datetime.today()
    today_date = today.strftime('%Y_%m_%d')
    today_time = today.strftime('%H_%M_%S')

    dest_dir = os.path.join(dest_dir, today_date)
    os.makedirs(dest_dir, exist_ok=True)

    csv_name = f'{today_time}.csv'
    csv_output = os.path.join(dest_dir, csv_name)

    return csv_output

def writeLog(modelo, dest_dir):
    csv_output = open(getOutputName(dest_dir), 'w', newline='')
    csv_writer = csv.writer(csv_output, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    header = ['Accuracy', 'Loss', 'Val Accuracy', 'Val Loss']
    csv_writer = csv.DictWriter(csv_output, fieldnames=header)
    csv_writer.writeheader()

    for i in range(modelo.epochs):
        csv_writer.writerow({
            'Accuracy': modelo.history.history['accuracy'][i],
            'Loss': modelo.history.history['loss'][i],
            'Val Accuracy': modelo.history.history['val_accuracy'][i],
            'Val Loss': modelo.history.history['val_loss'][i]
            })
