#!/usr/bin/env python3
'''Linear Algebra - Definiteness module'''
import numpy as np


def definiteness(matrix):
    '''calculates the definiteness of a matrix:
    Args:
        matrix is a numpy.ndarray of shape (n, n) whose definiteness
               should be calculated
    Returns: the string Positive definite, Positive semi-definite,
             Negative semi-definite, Negative definite, or Indefinite.
             If matrix does not fit any of the above categories, return None
    '''
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # check if matrix is symmetric
    if (matrix.ndim < 2 or  # should be a matrix at least 2x2
            # should be a squared matrix:
            not all(dim == matrix.shape[0] for dim in matrix.shape) or
            not np.allclose(matrix, matrix.T)):  # should be symmetric
        return None

    w, v = np.linalg.eig(matrix)

    if np.all((w > 0)):
        return "Positive definite"
    elif np.all((w >= 0)):
        return "Positive semi-definite"
    elif np.all((w < 0)):
        return "Negative definite"
    elif np.all((w <= 0)):
        return "Negative semi-definite"
    else:
        return "Indefinite"
