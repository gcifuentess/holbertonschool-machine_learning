#!/usr/bin/env python3
'''Cost'''
import numpy as np


def cost(P, Q):
    '''calculates the cost of the t-SNE transformation
    Args:
        P is a numpy.ndarray of shape (n, n) containing the P affinities
        Q is a numpy.ndarray of shape (n, n) containing the Q affinities

    Important: Watch out for division by 0 errors! Take the minimum of all
               values in p and q with almost 0 (ex. 1e-12)

    Returns: C, the cost of the transformation
    '''
    P = np.where(P == np.amin(P), 1e-12, P)
    Q = np.where(Q == np.amin(Q), 1e-12, Q)

    return (P * np.log(P / Q)).sum()
