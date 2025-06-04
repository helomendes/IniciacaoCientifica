import os
import tensorflow as tf
from Model import Model
import utils


def main():
    config = utils.getArgs()

    images_dir = os.path.abspath(config.get('images_dir')) + '/'
    dest_dir = os.path.abspath(config.get('dest_dir')) + '/'
    size = config.get('size')
    flip = config.get('flip')
    epochs = config.get('epochs')
    lr = config.get('learning_rate')
    batches = config.get('batch_size')

    train_paths, val_paths, test_paths, class_names = utils.getDataset(images_dir, size)

    modelo = Model(batches, 220, 220, epochs, flip, lr, class_names)
    modelo.dataset_prep(train_paths, val_paths, test_paths)
    modelo.process_datasets()

    # feature extraction
    modelo.feature_extraction()

    modelo.configure_datasets()

    exit()
    ### not yet

    modelo.normalization_layer = tf.keras.layers.Rescaling(1./255)

    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomRotation(0.2),
        tf.keras.layers.RandomShear()
        ])

    model = tf.keras.Sequential([
        data_augmentation,
        tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPool2D(pool_size=3),
        tf.keras.layers.Dropout(rate=0.25),
        tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same'),
        tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPool2D(pool_size=2),
        tf.keras.layers.Dropout(rate=0.25),
        tf.keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPool2D(pool_size=2),
        tf.keras.layers.Dropout(rate=0.25),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(units=1024, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(rate=0.5),
        tf.keras.layers.Dense(units=modelo.num_classes, activation='softmax')
        ])

    model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=modelo.lr),
            loss=tf.keras.losses.SparseCategoricalCrossentropy(),
            metrics=[
                'accuracy',
                ]
            )

    print('Train')
    modelo.history = model.fit(
            modelo.train_ds,
            validation_data = modelo.val_ds,
            epochs=modelo.epochs
            )

    print('Test')
    modelo.test_results = model.evaluate(modelo.test_ds)

    utils.writeLog(modelo, model.metrics_names, dest_dir)

if __name__ == "__main__":
    main()
