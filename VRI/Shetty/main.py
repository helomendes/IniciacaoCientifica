import os
import tensorflow as tf
from Model import Model
import utils


def main():
    config = utils.getArgs()

    images_dir = os.path.abspath(config.get('images_dir')) + '/'
    dest_dir = os.path.abspath(config.get('dest_dir')) + '/'
    size = config.get('size')

    train_paths, val_paths, test_paths, class_names = utils.getDataset(images_dir, size)

    modelo = Model(16, 220, 220, 3, class_names)
    modelo.dataset_prep(train_paths, val_paths, test_paths)
    modelo.train_val_test()

    modelo.normalization_layer = tf.keras.layers.Rescaling(1./255)

    data_augmentation = tf.keras.Sequential([
        # test other rotations
        tf.keras.layers.RandomRotation(0.2)
        # shearing
        ])

    model = tf.keras.Sequential([
        data_augmentation,
        tf.keras.layers.Rescaling(1./255),
        tf.keras.layers.Conv2D(16, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(16, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(16, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(modelo.num_classes)
        ])

    model.compile(
            optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=[
                'accuracy',
                ]
            )

    print('Train')
    modelo.history = model.fit(
            modelo.train_ds,   # x: input data
                        # if x is a dataset, y should not be specified since targets will be obtained from x
            validation_data = modelo.val_ds,   # data on which to evaluate the loss and any model metrics
                                        # the model will not be trained on this data
            epochs=modelo.epochs
            )

    print('Test')
    modelo.test_results = model.evaluate(modelo.test_ds)

    utils.writeLog(modelo, model.metrics_names, dest_dir)

if __name__ == "__main__":
    main()
