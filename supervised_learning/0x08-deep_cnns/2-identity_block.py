#!/usr/bin/env python3
'''Identity Block module'''
import tensorflow.keras as K


def identity_block(A_prev, filters):
    '''Builds an identity block as described in Deep Residual Learning for
    Image Recognition (2015)
    Args:
        A_prev is the output from the previous layer
        filters is a tuple or list containing F11, F3, F12, respectively:
                - F11 is the number of filters in the first 1x1 convolution
                - F3 is the number of filters in the 3x3 convolution
                - F12 is the number of filters in the second 1x1 convolution
    Important: All convolutions inside the inception block  use a
               rectified linear activation (ReLU)
    Returns: the activated output of the projection block
    '''
    F11, F3, F12 = filters
    w = K.initializers.he_normal(seed=None)

    l1 = K.layers.Conv2D(filters=F11,
                         kernel_size=(1, 1),
                         padding="same",
                         kernel_initializer=w)(A_prev)

    l2 = K.layers.BatchNormalization()(l1)
    l2 = K.layers.Activation("relu")(l2)

    l3 = K.layers.Conv2D(filters=F3,
                         kernel_size=(3, 3),
                         padding="same",
                         kernel_initializer=w)(l2)

    l4 = K.layers.BatchNormalization()(l3)
    l4 = K.layers.Activation("relu")(l4)

    l5 = K.layers.Conv2D(filters=F12,
                         kernel_size=(1, 1),
                         padding="same",
                         kernel_initializer=w)(l4)

    l6 = K.layers.BatchNormalization()(l5)

    l7 = K.layers.Add()([l6, A_prev])

    return K.layers.Activation("relu")(l7)
