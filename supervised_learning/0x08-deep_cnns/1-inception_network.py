#!/usr/bin/env python3
'''Inception Network module'''
import tensorflow.keras as K
inception_block = __import__('0-inception_block').inception_block


def inception_network():
    '''builds the inception network as described in Going Deeper with
    Convolutions (2014)
    Important:
        - input data must have shape (224, 224, 3)
        - All convolutions inside and outside the inception block
          use a rectified linear activation (ReLU)
    Returns: a keras model
    '''
    inception3a = [64, 96, 128, 16, 32, 32]
    inception3b = [128, 128, 192, 32, 96, 64]
    inception4a = [192, 96, 208, 16, 48, 64]
    inception4b = [160, 112, 224, 24, 64, 64]
    inception4c = [128, 128, 256, 24, 64, 64]
    inception4d = [112, 144, 288, 32, 64, 64]
    inception4e = [256, 160, 320, 32, 128, 128]
    inception5a = [256, 160, 320, 32, 128, 128]
    inception5b = [384, 192, 384, 48, 128, 128]

    w = K.initializers.he_normal(seed=None)

    inputs = K.Input(shape=(224, 224, 3))

    l1 = K.layers.Conv2D(filters=64,
                         kernel_size=(7, 7),
                         strides=(2, 2),
                         padding="same",
                         activation="relu",
                         kernel_initializer=w)(inputs)

    l2 = K.layers.MaxPool2D(pool_size=(3, 3),
                            strides=2,
                            padding="same")(l1)

    l3 = K.layers.Conv2D(filters=64,
                         kernel_size=(1, 1),
                         strides=1,
                         padding="same",
                         activation="relu",
                         kernel_initializer=w)(l2)

    l3 = K.layers.Conv2D(filters=192,
                         kernel_size=(3, 3),
                         strides=1,
                         padding="same",
                         activation="relu",
                         kernel_initializer=w)(l3)

    l4 = K.layers.MaxPool2D(pool_size=(3, 3),
                            strides=2,
                            padding="same")(l3)

    l5 = inception_block(l4, inception3a)

    l6 = inception_block(l5, inception3b)

    l7 = K.layers.MaxPool2D(pool_size=(3, 3),
                            strides=2,
                            padding="same")(l6)

    l8 = inception_block(l7, inception4a)

    l9 = inception_block(l8, inception4b)

    l10 = inception_block(l9, inception4c)

    l11 = inception_block(l10, inception4d)

    l12 = inception_block(l11, inception4e)

    l13 = K.layers.MaxPool2D(pool_size=(3, 3),
                             strides=2,
                             padding="same")(l12)

    l14 = inception_block(l13, inception5a)

    l15 = inception_block(l14, inception5b)

    l16 = K.layers.AveragePooling2D(pool_size=(7, 7),
                                    strides=1,
                                    padding="valid")(l15)

    l17 = K.layers.Dropout(.4)(l16)

    l18 = K.layers.Dense(units=1000,
                         activation="softmax",
                         kernel_initializer=w)(l17)

    return K.Model(inputs=inputs, outputs=l18)
