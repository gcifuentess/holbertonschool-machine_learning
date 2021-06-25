#!/usr/bin/env python3
'''Transfer Knowledge module'''
import tensorflow.keras as K


def preprocess_data(X, Y):
    '''pre-processes the data for a model
    Args:
        X is a numpy.ndarray of shape (m, 32, 32, 3) containing the CIFAR 10
          data, where m is the number of data points
        Y is a numpy.ndarray of shape (m,) containing the CIFAR 10 labels for X
    Returns: X_p, Y_p
             - X_p is a numpy.ndarray containing the preprocessed X
             - Y_p is a numpy.ndarray containing the preprocessed Y
    '''
    # Densenet data preprocessing
    X_p = K.applications.densenet.preprocess_input(
        X,
        data_format="channels_last",
    )

    # One-hot encode for labels
    Y_p = K.utils.to_categorical(Y)

    return X_p, Y_p


if __name__ == "__main__":

    # Download cifar10 training dataset
    (x_train, y_train), (x_test, y_test) = K.datasets.cifar10.load_data()
    x_train, y_train = preprocess_data(x_train, y_train)
    x_test, y_test = preprocess_data(x_test, y_test)

    # Using DenseNet121 as base_model
    base_model = K.applications.DenseNet121(
        include_top=False,
        weights="imagenet",
        input_tensor=None,
        input_shape=(224, 224, 3),
        pooling=None,
        classes=10,
    )

    # Freeze the base_model
    base_model.trainable = False

    # Create new model on top
    inputs = K.Input(shape=(32, 32, 3))

    # Adding new layers
    resize_l = K.layers.Lambda(
        lambda x: K.backend.resize_images(
            x=x,
            height_factor=(224 / 32),
            width_factor=(224 / 32),
            data_format="channels_last",
        ),
        output_shape=(224, 224, 3),
    )(inputs)

    x = base_model(resize_l, training=False)
    x = K.layers.AveragePooling2D(
        pool_size=(7, 7),
        strides=1,
        padding="valid",
    )(x)

    x = K.layers.GlobalAveragePooling2D()(x)

    outputs = K.layers.Dense(
        units=10,
        activation="softmax",
    )(x)

    model = K.Model(inputs, outputs)
    model.summary()
    model.compile(
        optimizer=K.optimizers.Adam(),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    model.fit(
        x=x_train,
        y=y_train,
        epochs=20,
        validation_data=(x_test, y_test),
    )

    # Unfreeze the base_model. Note that it keeps running in inference mode
    # since we passed `training=False` when calling it. This means that
    # the batchnorm layers will not update their batch statistics.
    # This prevents the batchnorm layers from undoing all the training
    # we've done so far.
    base_model.trainable = True

    model.summary()
    model.compile(
        optimizer=K.optimizers.Adam(1e-5),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    model.fit(
        x=x_train,
        y=y_train,
        epochs=10,
        validation_data=(x_test, y_test),
    )

    model.save("cifar10.h5")
