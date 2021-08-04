#!/usr/bin/env python3
'''PDF module'''
import numpy as np


def pdf(X, m, S):
    '''calculates the probability density function of a Gaussian distribution
    Args:
        X is a numpy.ndarray of shape (n, d) containing the data points whose
          PDF should be evaluated
        m is a numpy.ndarray of shape (d,) containing the mean of the
          distribution
        S is a numpy.ndarray of shape (d, d) containing the covariance of the
          distribution
    Returns: P, or None on failure
        - P is a numpy.ndarray of shape (n,) containing the PDF values for each
            data point
    Important: All values in P should have a minimum value of 1e-300
    '''
    if (type(X) is not np.ndarray or len(X.shape) != 2):
        return None

    n, d = X.shape

    if (type(m)is not np.ndarray or m.shape != (d,)):
        return None

    if (type(S)is not np.ndarray or S.shape != (d, d)):
        return None

    cov_det = np.linalg.det(S)
    const = 1 / (((2 * np.pi) ** (d / 2)) * (cov_det ** (1 / 2)))
    potence = ((X - m) @ np.linalg.inv(S) @ (X - m).T) * (- 1 / 2)
    P = const * np.exp(potence)
    P = P[np.diag_indices_from(P)]  # extract the diagonal

    return P
