#!/usr/bin/env python3
'''tensorflow batch normalization module'''
import tensorflow as tf
import numpy as np


def create_batch_norm_layer(prev, n, activation):
    '''creates a batch normalization layer for a neural network in tensorflow
    Args:
        prev is the activated output of the previous layer
        n is the number of nodes in the layer to be created
    activation is the activation function that should be used on the
                   output of the layer
    Returns: a tensor of the activated output for the layer
    '''
    w = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(n, kernel_initializer=w, name="norm_layer")
    mean, var = tf.nn.moments(layer(prev), axes=0)
    beta = tf.Variable(tf.zeros(n), trainable=True)
    gamma = tf.Variable(tf.ones(n), trainable=True)
    epsilon = 1e-8
    norm = tf.nn.batch_normalization(x=layer(prev),
                                     mean=mean,
                                     variance=var,
                                     offset=beta,
                                     scale=gamma,
                                     variance_epsilon=epsilon,
                                     name="batch_norm")
    return activation(norm)
