#!/usr/bin/env python3
'''Forward Propagation with Dropout module'''
import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    '''conducts forward propagation using Dropout
    Args:
        X is a numpy.ndarray of shape (nx, m) containing the input data for
          the network
            nx is the number of input features
            m is the number of data points
        weights is a dictionary of the weights and biases of the neural network
        L the number of layers in the network
        keep_prob is the probability that a node will be kept
    Returns: a dictionary containing the outputs of each layer and the dropout
             mask used on each layer
    Important: All layers except the last uses the tanh activation function
               The last layer uses the softmax activation function
    '''
    cache = {}
    cache['A0'] = X
    for i in range(1, L + 1):
        W = weights['W{}'.format(i)]
        b = weights['b{}'.format(i)]
        A = cache['A{}'.format(i - 1)]
        Z = np.matmul(W, A) + b
        # Forward propagation:
        if i < L:
            # with tanh activation function:
            _A = (2 / (1 + np.exp(-2 * Z))) - 1
            D = np.random.rand(_A.shape[0], _A.shape[1]) < keep_prob
            _A = np.multiply(_A, D)  # dropout
            cache['A{}'.format(i)] = _A / keep_prob  # inverted dropout
            cache['D{}'.format(i)] = D * 1
        else:
            # with softmax activation function:
            T = np.exp(Z)
            cache['A{}'.format(i)] = T / np.sum(T, axis=0)
    return cache
