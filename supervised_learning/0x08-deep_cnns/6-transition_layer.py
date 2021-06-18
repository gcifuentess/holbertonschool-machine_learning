#!/usr/bin/env python3
'''Transition module'''
import tensorflow.keras as K


def transition_layer(X, nb_filters, compression):
    '''Builds a transition layer as described in Densely Connected
    Convolutional Networks
    Args:
        X is the output from the previous layer
        nb_filters is an integer representing the number of filters in X
        compression is the compression factor for the transition layer
    Returns: The output of the transition layer and the number of filters
             within the output, respectively
    '''
    w = K.initializers.he_normal()

    filters = int(compression * nb_filters)

    l1 = K.layers.BatchNormalization()(X)
    l1 = K.layers.Activation("relu")(l1)

    l2 = K.layers.Conv2D(filters=filters,
                         kernel_size=(1, 1),
                         padding="same",
                         kernel_initializer=w)(l1)

    l3 = K.layers.AveragePooling2D(pool_size=(2, 2),
                                   strides=2,
                                   padding="valid")(l2)

    return l3, filters
