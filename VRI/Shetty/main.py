import argparse
import yaml
import os
import glob
import random
import tensorflow as tf
import math
import numpy as np

# NORMAL TRAINING
'''
    train_full = tf.keras.utils.image_dataset_from_directory(
            images_dir,
            validation_split = 0.2,
            subset="training",
            seed=123,
            image_size = (h, w),
            batch_size = batch_size)

    num_batches = math.ceil(train_size/batch_size)
    train_ds = train_full.take(num_batches)

    val_ds = tf.keras.utils.image_dataset_from_directory(
            images_dir,
            validation_split = 0.2,
            subset="validation",
            seed=123,
            image_size = (h, w),
            batch_size = batch_size)

    num_classes = len(val_ds.class_names)
    class_names = val_ds.class_names

    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
'''

def getDataset(images_dir, train_size):
    image_paths = []
    class_names = sorted([name for name in glob.glob(f'{images_dir}*/')])
    for name in class_names:
        ds = glob.glob(f'{name}/*')
        selected = random.sample(ds, train_size)
        image_paths.extend(selected)
    random.shuffle(image_paths)
    return image_paths, len(image_paths), class_names

class Model:
    def __init__(self, image_paths, image_count, class_names):
        self.batch_size = 16
        # 220 * 220
        # for the CNN model images are scaled to 96x96 with a depth of 3
        self.h = 220
        self.w = 220
        self.AUTOTUNE = tf.data.AUTOTUNE
        self.image_paths = image_paths
        self.images_count = image_count
        self.class_names = class_names

    def dataset_prep(self):
        # finer control
        list_ds = tf.data.Dataset.list_files(self.image_paths, shuffle=False)
        list_ds = list_ds.shuffle(self.images_count, reshuffle_each_iteration=False)

        val_size = int(self.images_count*0.2)
        self.train_ds = list_ds.skip(val_size)
        self.val_ds = list_ds.take(val_size)

    def get_label(self, file_path):
        parts = tf.strings.split(file_path, os.path.sep)
        one_hot = parts[-2] == self.class_names
        return tf.argmax(one_hot)

    def decode_img(self, img):
        img = tf.io.decode_jpeg(img, channels=3)
        return tf.image.resize(img, [self.h, self.w])

    def process_path(self, file_path):
        label = self.get_label(file_path)
        img = tf.io.read_file(file_path)
        img = self.decode_img(img)
        return img, label

    def configure_for_performance(self, ds):
        ds = ds.cache()
        ds = ds.shuffle(buffer_size=1000)
        ds = ds.batch(self.batch_size)
        ds = ds.prefetch(buffer_size=self.AUTOTUNE)
        return ds

    def train_val(self):
        self.train_ds = self.train_ds.map(self.process_path, num_parallel_calls=self.AUTOTUNE)
        self.val_ds = self.val_ds.map(self.process_path, num_parallel_calls=self.AUTOTUNE)

        self.train_ds = self.configure_for_performance(self.train_ds)
        self.val_ds = self.configure_for_performance(self.val_ds)

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('--config', help='YAML configuration file', required=True)
    args = parse.parse_args()
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    images_dir = os.path.abspath(config.get('images_dir')) + '/'
    train_size = config.get('train_size')

    image_paths, images_count, class_names = getDataset(images_dir, train_size)
    num_classes = len(class_names)

    #images_count = len(list(glob.glob(f'{images_dir}*/*')))

    modelo = Model(image_paths, images_count, class_names)
    modelo.dataset_prep()
    modelo.train_val()

    modelo.normalization_layer = tf.keras.layers.Rescaling(1./255)

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
        tf.keras.layers.Dense(num_classes)
        ])

    model.compile(
            optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy']
            )

    model.fit(
            modelo.train_ds,   # x: input data
                        # if x is a dataset, y should not be specified since targets will be obtained from x
            validation_data = modelo.val_ds,   # data on which to evaluate the loss and any model metrics
                                        # the model will not be trained on this data
            epochs=3
            )

if __name__ == "__main__":
    main()
