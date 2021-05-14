#!/usr/bin/env python3
'''tensorflow forward propagation module'''
import tensorflow as tf


def forward_prop(x, layer_sizes=[], activations=[]):
    '''creates the forward propagation graph for the neural network
    Args:
                  x: is the placeholder for the input data
        layer_sizes: is a list containing the number of nodes in each layer
                     of the network
        activations: is a list containing the activation functions for each
                     layer of the network
    Return: the prediction of the network in tensor form
    '''
    create_layer = __import__('1-create_layer').create_layer
    current_x = x
    for i in range(len(layer_sizes)):
        current_x = create_layer(current_x, layer_sizes[i], activations[i])
    return current_x
