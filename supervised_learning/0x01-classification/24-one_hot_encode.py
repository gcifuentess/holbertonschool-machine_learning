#!/usr/bin/env python3
'''One-Hot Encode module'''
import numpy as np


def one_hot_encode(Y, classes):
    '''converts a numeric label vector into a one-hot matrix
    Args:
        Y: is a numpy.ndarray with shape (m,) containing numeric class labels
           -m is the number of examples
        classes: is the maximum number of classes found in Y
    Return: a one-hot encoding of Y with shape (classes, m), or None on failure
    '''
    m = Y.shape[0]
    OH = np.zeros((m, m), dtype=float)
    for i, value in enumerate(Y):
        OH[value][i] = 1.0
    return OH
