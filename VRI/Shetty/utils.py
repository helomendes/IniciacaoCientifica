import argparse
import csv
import json
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

    json_name = f'{today_time}.json'
    json_output = os.path.join(dest_dir, json_name)

    return json_output

def writeLog(modelo, metrics, dest_dir):
    history = modelo.history.history
    # maybe use a train and validation accuracy/loss mean?
    test_list = [[metric, val] for metric, val in zip(metrics, modelo.test_results)]

    dictionary = {
            "batch_size": modelo.batch_size,
            "size": [modelo.h, modelo.w],
            "epochs": modelo.epochs,
            "learning_rate": modelo.lr,
            "flip": modelo.flip,
            "train": {
                "accuracy": history['accuracy'],
                "loss": history['loss']
                },
            "val": {
                "accuracy": history['val_accuracy'],
                "loss": history['val_loss']
                },
            }
    if "test" not in dictionary:
        dictionary["test"] = {}
    for item in test_list:
        dictionary["test"][item[0]] = item[1]
    
    json_obj = json.dumps(dictionary, indent=4)
    with open(getOutputName(dest_dir), 'w') as file:
        file.write(json_obj)
