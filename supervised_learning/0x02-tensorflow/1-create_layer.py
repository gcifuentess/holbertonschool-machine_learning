#!/usr/bin/env python3
'''tensorflow layers module'''
import tensorflow as tf


def create_layer(prev, n, activation):
    '''Creates a tensorflow layer
    Args:
              prev: is the tensor output of the previous layer
                 n: is the number of nodes in the layer to create
        activation: is the activation function that the layer should use
    Return: the tensor output of the layer
    '''
    W = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(n, activation=activation, kernel_initializer=W,
                            name='layer')
    return layer(prev)
