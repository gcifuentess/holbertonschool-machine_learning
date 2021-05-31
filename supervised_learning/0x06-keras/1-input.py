#!/usr/bin/env python3
'''Input module'''
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    '''builds a neural network with the Keras library
    Args:
        nx is the number of input features to the network
        layers is a list containing the number of nodes in each layer of the
               network
        activations is a list containing the activation functions used for
                    each layer of the network
        lambtha is the L2 regularization parameter
        keep_prob is the probability that a node will be kept for dropout
    Returns: the keras model
    '''
    w = K.initializers.VarianceScaling(mode="fan_avg")
    regularizer = K.regularizers.l2(lambtha)
    inputs = K.Input(shape=(nx,))
    dense_layers = []
    for i in range(len(layers)):
        if i == 0:
            x = inputs
        else:
            x = dense_layers[i - 1]
        layer = K.layers.Dense(units=layers[i],
                               activation=activations[i],
                               kernel_initializer=w,
                               kernel_regularizer=regularizer)(x)
        if i < len(layers) - 1:
            dropout = K.layers.Dropout(1 - keep_prob)(layer)
            dense_layers.append(dropout)
        else:
            outputs = layer
    return K.Model(inputs=inputs, outputs=outputs)
