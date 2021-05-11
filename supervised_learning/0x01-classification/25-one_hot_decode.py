#!/usr/bin/env python3
'''One-Hot Decode module'''
import numpy as np


def one_hot_decode(one_hot):
    '''converts a one-hot matrix into a vector of labels
    Args:
        one_hot: is a one-hot encoded numpy.ndarray with shape (classes, m)
                 - classes: is the maximum number of classes
                 - m: is the number of examples
    Return: a numpy.ndarray with shape (m, ) containing the numeric labels
            for each example, or None on failure
    '''
    if not isinstance(one_hot, np.ndarray):
        return None
    try:
        OH_d = np.where(one_hot.T == 1)[1]
        return OH_d
    except Exception:
        return None
