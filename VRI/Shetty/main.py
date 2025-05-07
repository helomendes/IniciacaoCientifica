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

    batch_size = 32
    h = 220
    w = 220
    num_batches = math.ceil(train_size/batch_size)

    train_full = tf.keras.utils.image_dataset_from_directory(
            images_dir,
            validation_split = 0.2,
            subset="training",
            seed=123,
            image_size = (h, w),
            batch_size = batch_size)
    train_ds = train_full.take(num_batches)

    total_images = sum([len(files) for r, d, files in os.walk(images_dir)])
    print(total_images)

    # for the CNN model images are scaled to 96x96 with a depth of 3

if __name__ == "__main__":
    main()
