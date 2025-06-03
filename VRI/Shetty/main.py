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
    modelo.train_val_test()

    modelo.normalization_layer = tf.keras.layers.Rescaling(1./255)

    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomRotation(0.2),
        tf.keras.layers.RandomShear()
        ])

    model = tf.keras.Sequential([
        data_augmentation,
        # 32 filters, 3x3 filter size, ReLU activation, same padding, followed by batch normalization
        # batch normalization?
        tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', padding='same'),
        # 3x3 pool size to reduce image spatial dimensions quickly from 96x96 to 32x32
        tf.keras.layers.MaxPool2D(pool_size=3),
        # 0.25 Neurons
        tf.keras.layers.Dropout(rate=0.25),
        # 64 filters, 3x3 filter size, ReLU activation, same padding
        tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same'),
        # 64 filters, 3x3 filter size, ReLU activation, following the same padding, batch normalization is performed
        # batch normalization?
        tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same'),
        # 2x2 pool size
        tf.keras.layers.MaxPool2D(pool_size=2),
        # 0.25 Neurons
        tf.keras.layers.Dropout(rate=0.25),
        # 128 filters, 3x3 filter size, ReLU activation, following the same padding, batch normalization is performed
        # batch normalization?
        tf.keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'),
        # 128 filters, 3x3 filter size, ReLU activation, same padding followed by batch normalization
        # batch normalization?
        tf.keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'),
        # 2x2 pool size
        tf.keras.layers.MaxPool2D(pool_size=2),
        # 0.25 Neurons
        tf.keras.layers.Dropout(rate=0.25),
        # flatten
        tf.keras.layers.Flatten(),
        # 1024 Units, ReLU activation, and batch normalization
        # batch normalization?
        tf.keras.layers.Dense(units=1024, activation='relu'),
        # 0.5 Neurons
        tf.keras.layers.Dropout(rate=0.5),
        # 7 units, softmax activation
        # softmax?
        tf.keras.layers.Dense(units=modelo.num_classes)
        ])

    model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=modelo.lr),
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
