#!/usr/bin/env python3
'''Dense Block module'''
import tensorflow.keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    '''Builds a dense block as described in Densely Connected
    Convolutional Networks
    Args:
        X is the output from the previous layer
        nb_filters is an integer representing the number of filters in X
        growth_rate is the growth rate for the dense block
        layers is the number of layers in the dense block
    Important: applied bottleneck layers used for DenseNet-B
    Returns: The concatenated output of each layer within the Dense Block
             and the number of filters within the concatenated outputs,
             respectively
    '''
    w = K.initializers.he_normal()
    concat = X

    for i in range(layers):
        l1 = K.layers.BatchNormalization()(concat)
        l1 = K.layers.Activation("relu")(l1)

        l2 = K.layers.Conv2D(filters=(4 * growth_rate),
                             kernel_size=(1, 1),
                             padding="same",
                             kernel_initializer=w)(l1)

        l3 = K.layers.BatchNormalization()(l2)
        l3 = K.layers.Activation("relu")(l3)

        l4 = K.layers.Conv2D(filters=growth_rate,
                             kernel_size=(3, 3),
                             padding="same",
                             kernel_initializer=w)(l3)

        nb_filters += growth_rate
        concat = K.layers.Concatenate()([concat, l4])

    return concat, nb_filters
