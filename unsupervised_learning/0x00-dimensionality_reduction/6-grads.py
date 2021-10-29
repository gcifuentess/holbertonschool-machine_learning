#!/usr/bin/env python3
'''Gradients'''
import numpy as np
Q_affinities = __import__('5-Q_affinities').Q_affinities


def grads(Y, P):
    '''calculates the gradients of Y
    Args:
        Y is a numpy.ndarray of shape (n, ndim) containing the low dimensional
          transformation of X
        P is a numpy.ndarray of shape (n, n) containing the P affinities of X

    Important: Do not multiply the gradients by the scalar 4 as described in
               the paper’s equation

    Returns: (dY, Q)
        - dY is a numpy.ndarray of shape (n, ndim) containing the gradients
             of Y
        - Q is a numpy.ndarray of shape (n, n) containing the Q affinities of Y
    '''
    n, ndim = Y.shape
    Q, num = Q_affinities(Y)
    PQ_expanded = np.expand_dims(P - Q, 2)  # NxNx1
    num_expanded = np.expand_dims(num, 2)  # NxNx1
    Yi_Yj = np.expand_dims(Y, 1) - np.expand_dims(Y, 0)  # NxNx2
    dy = (PQ_expanded * Yi_Yj * num_expanded).sum(1)  # Nx2

    return dy, Q
