#!/usr/bin/env python3
'''Gradient Descent with L2 Regularization'''
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    '''updates the weights and biases of a neural network using gradient
    descent with L2 regularization
    Args:
        Y is a one-hot numpy.ndarray of shape (classes, m) that contains the
          correct labels for the data
        classes is the number of classes
        m is the number of data points
        weights is a dictionary of the weights and biases of the neural network
        cache is a dictionary of the outputs of each layer of the neural
              network
        alpha is the learning rate
        lambtha is the L2 regularization parameter
        L is the number of layers of the network
    Returns: Nothing. The weights and biases of the network should be updated
             in place
    Important: The neural network uses tanh activations on each layer except
               the last, which uses a softmax activation
    '''
    m = Y.shape[1]
    len_cache = len(cache)

    # learning for the last layer:
    Al = cache['A{}'.format(len_cache - 1)]  # last A
    A_prev = cache['A{}'.format(len_cache - 2)]  # pre last A
    dZl = Al - Y  # last dZ
    dWl = np.matmul(dZl, A_prev.T) / m  # last dW, shape (1, nodes)
    dbl = (1 / m) * np.sum(dZl, axis=1, keepdims=True)
    Wl_str = 'W{}'.format(len_cache - 1)
    Wl = weights[Wl_str]  # last W
    weights[Wl_str] = Wl - alpha * dWl  # last layer W learning
    bl_str = 'b{}'.format(len_cache - 1)
    bl = weights[bl_str]  # last b
    weights[bl_str] = bl - alpha * dbl  # last layer b learning

    #  next: learning for the rest of the layers:
    dZ = dZl
    W_next = Wl
    for i in reversed(range(1, len_cache - 1)):
        A = cache['A{}'.format(i)]
        A_prev = cache['A{}'.format(i - 1)]
        dZ = np.matmul(W_next.T, dZ) * (1 - A ** 2)
        dW = (1 / m) * (np.matmul(dZ, A_prev.T))
        db = np.sum(dZ, axis=1, keepdims=True) / m
        W_c_str = 'W{}'.format(i)
        W_c = weights[W_c_str]  # current W
        b_c_str = 'b{}'.format(i)
        b_c = weights[b_c_str]  # current b
        weights[W_c_str] = W_c - (alpha * lambtha / m) * W_c - alpha * dW
        weights[b_c_str] = b_c - alpha * db
        W_next = W_c
