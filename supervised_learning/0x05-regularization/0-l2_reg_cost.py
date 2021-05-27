#!/usr/bin/env python3
'''L2 Regularization Cost module'''
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    '''calculates the cost of a neural network with L2 regularization
    Args:
        cost is the cost of the network without L2 regularization
        lambtha is the regularization parameter
        weights is a dictionary of the weights and biases (numpy.ndarrays) of
                the neural network
        L is the number of layers in the neural network
        m is the number of data points used
    Returns: the cost of the network accounting for L2 regularization
    '''
    l2_reg = 0
    for i in range(1, L + 1):
        W = weights['W{}'.format(i)]
        sqrt_norm = np.multiply(W, W)
        l2_reg += np.sum(sqrt_norm)
    return cost + (lambtha / (2 * m)) * l2_reg
