#!/usr/bin/env python3
'''Inception Block module'''
import tensorflow.keras as K


def inception_block(A_prev, filters):
    '''builds an inception block as described in
    Going Deeper with Convolutions (2014):
    Args:
        A_prev is the output from the previous layer
        filters is a tuple or list containing F1, F3R, F3, F5R, F5, FPP,
                respectively:
                - F1 is the number of filters in the 1x1 convolution
                - F3R is the number of filters in the 1x1 convolution before
                      the 3x3 convolution
                - F3 is the number of filters in the 3x3 convolution
                - F5R is the number of filters in the 1x1 convolution before
                      the 5x5 convolution
                - F5 is the number of filters in the 5x5 convolution
                - FPP is the number of filters in the 1x1 convolution after
                      the max pooling
        Important: All convolutions inside the inception block  use a
                   rectified linear activation (ReLU)
    Returns: the concatenated output of the inception block
    '''
    F1, F3R, F3, F5R, F5, FPP = filters
    w = K.initializers.he_normal(seed=None)
    l1x1 = K.layers.Conv2D(filters=F1,
                           kernel_size=(1, 1),
                           padding="same",
                           activation="relu",
                           kernel_initializer=w)(A_prev)

    l3x3 = K.layers.Conv2D(filters=F3R,
                           kernel_size=(1, 1),
                           padding="same",
                           activation="relu",
                           kernel_initializer=w)(A_prev)

    l3x3 = K.layers.Conv2D(filters=F3,
                           kernel_size=(3, 3),
                           padding="same",
                           activation="relu",
                           kernel_initializer=w)(l3x3)

    l5x5 = K.layers.Conv2D(filters=F5R,
                           kernel_size=(1, 1),
                           padding="same",
                           activation="relu",
                           kernel_initializer=w)(A_prev)

    l5x5 = K.layers.Conv2D(filters=F5,
                           kernel_size=(5, 5),
                           padding="same",
                           activation="relu",
                           kernel_initializer=w)(l5x5)

    lpooling = K.layers.MaxPool2D(pool_size=(2, 2),
                                  strides=(1, 1),
                                  padding='same')(A_prev)

    lpooling = K.layers.Conv2D(filters=FPP,
                               kernel_size=(1, 1),
                               padding="same",
                               activation="relu",
                               kernel_initializer=w)(lpooling)

    return(K.layers.Concatenate()([l1x1, l3x3, l5x5, lpooling]))
