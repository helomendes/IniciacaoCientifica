import argparse
import yaml
import os
import glob
import random
import tensorflow as tf
import math
import numpy as np

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('--config', help='YAML configuration file', required=True)
    args = parse.parse_args()
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    images_dir = os.path.abspath(config.get('images_dir')) + '/'
    train_size = config.get('train_size')

    images_count = len(list(glob.glob(f'{images_dir}*/*')))

    # 220 * 220
    # for the CNN model images are scaled to 96x96 with a depth of 3
    batch_size = 16
    h = 220
    w = 220

    AUTOTUNE = tf.data.AUTOTUNE

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

    # finer control

    list_ds = tf.data.Dataset.list_files(f'{images_dir}*/*', shuffle=False)
    list_ds = list_ds.shuffle(images_count, reshuffle_each_iteration=False)
    class_names = np.array(sorted([item.split('/')[-1] for item in glob.glob(f'{images_dir}*')]))
    num_classes = len(class_names)

    # its counting all the images, but in this experiment we will use only 700 images from the dataset
    # can I just adjust it to 700 instead of 10015?
    
    val_size = int(images_count*0.2)
    train_ds = list_ds.skip(val_size)
    val_ds = list_ds.take(val_size)

    def get_label(file_path):
        parts = tf.strings.split(file_path, os.path.sep)
        one_hot = parts[-2] == class_names
        return tf.argmax(one_hot)

    def decode_img(img):
        img = tf.io.decode_jpeg(img, channels=3)
        return tf.image.resize(img, [h, w])

    def process_path(file_path):
        label = get_label(file_path)
        img = tf.io.read_file(file_path)
        img = decode_img(img)
        return img, label

    train_ds = train_ds.map(process_path, num_parallel_calls=AUTOTUNE)
    val_ds = val_ds.map(process_path, num_parallel_calls=AUTOTUNE)

    def configure_for_performance(ds):
        ds = ds.cache()
        ds = ds.shuffle(buffer_size=1000)
        ds = ds.batch(batch_size)
        ds = ds.prefetch(buffer_size=AUTOTUNE)
        return ds

    train_ds = configure_for_performance(train_ds)
    val_ds = configure_for_performance(val_ds)

    normalization_layer = tf.keras.layers.Rescaling(1./255)

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
            train_ds,
            validation_data = val_ds,
            epochs=3
            )

if __name__ == "__main__":
    main()
