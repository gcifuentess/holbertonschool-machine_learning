#!/usr/bin/env python3
'''Q affinities'''
import numpy as np


def Q_affinities(Y):
    '''calculates the Q affinities
    Args:
        Y is a numpy.ndarray of shape (n, ndim) containing the low dimensional
          transformation of X
            - n is the number of points
            - ndim is the new dimensional representation of X

    Returns: Q, num
        - Q is a numpy.ndarray of shape (n, n) containing the Q affinities
        - num is a numpy.ndarray of shape (n, n) containing the numerator
              of the Q affinities
    '''
    n, ndim = Y.shape

    sum_Y = np.sum(np.square(Y), 1)
    D = np.add(np.add(-2 * np.matmul(Y, Y.T), sum_Y).T, sum_Y)
    np.fill_diagonal(D, 0)

    # see https://www.jmlr.org/papers/volume9/vandermaaten08a
    # /vandermaaten08a.pdf page 7 equation 4
    num = np.power(1 + D, -1)
    np.fill_diagonal(num, 0)
    Q = num / num.sum()

    return Q, num
