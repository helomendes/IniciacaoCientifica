import tensorflow as tf
import matplotlib.pyplot as plt
import cv2 as cv
import os

class Model:
    def __init__(self, batch_size, height, width, epochs, flip, lr, class_names):
        self.batch_size = batch_size
        # 220 * 220
        # for the CNN model images are scaled to 96x96 with a depth of 3
        self.h = height
        self.w = width
        self.epochs = epochs
        self.flip = flip
        self.lr = lr
        self.class_names = class_names
        self.history = None
        self.num_classes = len(class_names)
        self.AUTOTUNE = tf.data.AUTOTUNE

    def dataset_prep(self, train_paths, val_paths, test_paths):
        train_ds = tf.data.Dataset.from_tensor_slices(train_paths)
        val_ds = tf.data.Dataset.from_tensor_slices(val_paths)
        test_ds = tf.data.Dataset.from_tensor_slices(test_paths)

        train_ds = train_ds.shuffle(len(train_paths), reshuffle_each_iteration=False)
        val_ds = val_ds.shuffle(len(val_paths), reshuffle_each_iteration=False)
        test_ds = test_ds.shuffle(len(test_paths), reshuffle_each_iteration=False)

        self.train_ds = train_ds
        self.val_ds = val_ds
        self.test_ds = test_ds

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

    def duplicate_with_flips(self, ds):
        flipped_ds = ds.map(
                lambda img, label: (tf.image.flip_left_right(img), label),
                num_parallel_calls=self.AUTOTUNE
                )
        ds = ds.concatenate(flipped_ds)
        ds = ds.shuffle(
                buffer_size = tf.data.experimental.cardinality(ds).numpy(),
                reshuffle_each_iteration=False
                )
        return ds

    def configure_for_performance(self, ds):
        ds = ds.cache()
        ds = ds.shuffle(buffer_size=1000)
        ds = ds.batch(self.batch_size)
        ds = ds.prefetch(buffer_size=self.AUTOTUNE)
        return ds

    def process_datasets(self):
        self.train_ds = self.train_ds.map(self.process_path, num_parallel_calls=self.AUTOTUNE)
        self.val_ds = self.val_ds.map(self.process_path, num_parallel_calls=self.AUTOTUNE)
        self.test_ds = self.test_ds.map(self.process_path, num_parallel_calls=self.AUTOTUNE)

        if self.flip:
            self.train_ds = self.duplicate_with_flips(self.train_ds)
            self.val_ds = self.duplicate_with_flips(self.val_ds)
            self.test_ds = self.duplicate_with_flips(self.test_ds)

    def configure_datasets(self):
        self.train_ds = self.configure_for_performance(self.train_ds)
        self.val_ds = self.configure_for_performance(self.val_ds)
        self.test_ds = self.configure_for_performance(self.test_ds)

    def feature_extraction(self):
        # for each (img, label)
        # image color conversion rgb -> gray scale and rgb -> hsv
        # for each colour space
        # color histogram, haralick textures, hu moments

        # lets start with the train dataset

        for img, label in self.train_ds:
            r, g, b = tf.unstack(img.numpy(), axis=-1)
            r_hist = tf.histogram_fixed_width(tf.reshape(r, [-1]), [0,255], nbins=256)
            g_hist = tf.histogram_fixed_width(tf.reshape(g, [-1]), [0,255], nbins=256)
            b_hist = tf.histogram_fixed_width(tf.reshape(b, [-1]), [0,255], nbins=256)

            gray = cv.cvtColor(img.numpy(), cv.COLOR_RGB2GRAY)
            gray_hist = tf.histogram_fixed_width(tf.reshape(gray, [-1]), [0, 256], nbins = 256)

            hsv = cv.cvtColor(img.numpy(), cv.COLOR_RGB2HSV)
            h, s, v = tf.unstack(hsv, axis=-1)
            h_hist = tf.histogram_fixed_width(tf.reshape(h, [-1]), [0,255], nbins=256)

            '''
            fig = plt.figure(figsize=(15,10))

            img_norm = tf.clip_by_value(img, 0.0, 255.0) / 255.0
            fig.add_subplot(3, 2, 1)
            plt.imshow(img_norm.numpy())
            plt.axis('off')
            plt.title('RGB')

            fig.add_subplot(3, 2, 2)
            plt.plot(r_hist.numpy(), color='red', label='Red')
            plt.plot(g_hist.numpy(), color='green', label='Green')
            plt.plot(b_hist.numpy(), color='blue', label='Blue')
            plt.title('RGB Histogram')
            plt.xlabel('Pixel Intensity')
            plt.ylabel('Frequency')

            fig.add_subplot(3, 2, 3)
            plt.imshow(gray, cmap='gray')
            plt.axis('off')
            plt.title('Gray')

            fig.add_subplot(3, 2, 4)
            plt.bar(range(256), gray_hist.numpy(), width=1.0, color='gray')
            plt.title('Gray Histogram')
            plt.xlabel('Pixel Intensity')
            plt.ylabel('Frequency')

            fig.add_subplot(3, 2, 5)
            plt.imshow(hsv)
            plt.axis('off')
            plt.title('HSV')

            fig.add_subplot(3, 2, 6)
            plt.plot(h_hist.numpy())
            plt.title('RGB Histogram')
            plt.xlabel('Pixel Intensity')
            plt.ylabel('Frequency')

            plt.legend()
            plt.show()
            '''

