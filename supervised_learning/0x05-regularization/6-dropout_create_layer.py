#!/usr/bin/env python3
'''Create a Layer with Dropout tensorflow module'''
import tensorflow as tf


def dropout_create_layer(prev, n, activation, keep_prob):
    '''creates a layer of a neural network using dropout
    Args:
        prev is a tensor containing the output of the previous layer
        n is the number of nodes the new layer should contain
        activation is the activation function that should be used on the layer
        keep_prob is the probability that a node will be kept
    Returns: the output of the new layer
    '''
    w = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(n,
                            activation=activation,
                            kernel_initializer=w)
    rate = 1 - keep_prob
    dropout = tf.layers.Dropout(rate)
    return dropout(layer(prev))
