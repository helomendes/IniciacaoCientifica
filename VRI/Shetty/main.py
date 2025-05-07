import argparse
import yaml
import os
import glob
import random
import tensorflow as tf
import math

def main():
    # receive the images
    parse = argparse.ArgumentParser()
    parse.add_argument('--config', help='YAML configuration file', required=True)
    args = parse.parse_args()
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    images_dir = os.path.abspath(config.get('images_dir')) + '/'
    train_size = config.get('train_size')

    # 220 * 220
    # for the CNN model images are scaled to 96x96 with a depth of 3
    batch_size = 16
    h = 220
    w = 220

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

    # RGB values are [0, 255] range
    # make your input values small
    # standardize values to [0, 1] range
    normalization_layer = tf.keras.layers.Rescaling(1./255)

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    

if __name__ == "__main__":
    main()
