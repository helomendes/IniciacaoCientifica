from Modelo import Model
import utils

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
#images_count = len(list(glob.glob(f'{images_dir}*/*')))

def main():
    config = utils.getArgs()

    images_dir = os.path.abspath(config.get('images_dir')) + '/'
    dest_dir = os.path.abspath(config.get('dest_dir')) + '/'
    train_size = config.get('train_size')

    image_paths, class_names = utils.getDataset(images_dir, train_size)

    modelo = Model(class_names)
    modelo.dataset_prep(image_paths)
    modelo.train_val()

    modelo.normalization_layer = tf.keras.layers.Rescaling(1./255)

    model = utils.setModel(modelo)

    utils.writeLog(modelo, dest_dir)

if __name__ == "__main__":
    main()
