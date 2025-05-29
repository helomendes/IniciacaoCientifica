import tensorflow as tf
import os

class Model:
    def __init__(self, batch_size, height, width, epochs, class_names):
        self.batch_size = batch_size
        # 220 * 220
        # for the CNN model images are scaled to 96x96 with a depth of 3
        self.h = height
        self.w = width
        self.epochs = epochs
        self.history = None
        self.class_names = class_names
        self.num_classes = len(class_names)
        self.AUTOTUNE = tf.data.AUTOTUNE

    '''
    def dataset_prep(self, image_paths):
        # finer control

        #list_ds = tf.data.Dataset.list_files(image_paths, shuffle=False)
        list_ds = tf.data.Dataset.from_tensor_slices(image_paths)
        list_ds = list_ds.shuffle(training_size, reshuffle_each_iteration=False)

        # this is slicing from the same image_paths list
        # the validation is just a shuffled subset of the training set, not independet
        # the model sees the exact same images during training and validation
        self.train_ds = list_ds.skip(val_size)
        self.val_ds = list_ds.take(val_size)
    '''

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

    def configure_for_performance(self, ds):
        ds = ds.cache()
        ds = ds.shuffle(buffer_size=1000)
        ds = ds.batch(self.batch_size)
        ds = ds.prefetch(buffer_size=self.AUTOTUNE)
        return ds

    def train_val_test(self):
        self.train_ds = self.train_ds.map(self.process_path, num_parallel_calls=self.AUTOTUNE)
        self.val_ds = self.val_ds.map(self.process_path, num_parallel_calls=self.AUTOTUNE)
        self.test_ds = self.test_ds.map(self.process_path, num_parallel_calls=self.AUTOTUNE)

        self.train_ds = self.configure_for_performance(self.train_ds)
        self.val_ds = self.configure_for_performance(self.val_ds)
        self.test_ds = self.configure_for_performance(self.test_ds)

    def dataAugmentation(img):
        flip_image = tf.image.flip_left_right(img)
        return flip_image
