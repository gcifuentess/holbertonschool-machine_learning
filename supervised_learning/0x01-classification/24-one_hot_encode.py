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
    if type(classes) is not int or classes < 1:
        return None
    try:
        m = Y.shape[0]
    except e:
        return None
    OH = np.zeros((classes, m), dtype=float)
    OH[Y, np.arange(Y.size)] = 1
    return OH
