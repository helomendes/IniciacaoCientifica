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

def setModel(modelo):
    model = tf.keras.Sequential([
        tf.keras.layers.Rescaling(1./255),
        tf.keras.layers.Conv2D(32, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(32, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(32, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(modelo.num_classes)
        ])

    model.compile(
            optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy']
            )

    modelo.history = model.fit(
            modelo.train_ds,   # x: input data
                        # if x is a dataset, y should not be specified since targets will be obtained from x
            validation_data = modelo.val_ds,   # data on which to evaluate the loss and any model metrics
                                        # the model will not be trained on this data
            epochs=modelo.epochs
            )
    return model

def getDataset(images_dir, train_size):
    image_paths = []
    class_names = sorted([name for name in glob.glob(f'{images_dir}*/')])
    for name in class_names:
        ds = glob.glob(f'{name}/*')
        selected = random.sample(ds, train_size)
        image_paths.extend(selected)
    random.shuffle(image_paths)
    return image_paths, class_names

