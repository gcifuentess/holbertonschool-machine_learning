#!/usr/bin/env python3
'''Intersection module'''
import numpy as np


def intersection(x, n, P, Pr):
    '''calculates the intersection of obtaining this data with
    the various hypothetical probabilities
    Args:
        x is the number of patients that develop severe side effects
        n is the total number of patients observed
        P is a 1D numpy.ndarray containing the various hypothetical
          probabilities of developing severe side effects
        Pr is a 1D numpy.ndarray containing the prior beliefs of P
    Returns: a 1D numpy.ndarray containing the intersection of obtaining x and
             n with each probability in P, respectively
    '''
    if (type(n) is not int or n <= 0):
        raise ValueError("n must be a positive integer")

    if (type(x) is not int or x < 0):
        raise ValueError("x must be an integer that is greater " +
                         "than or equal to 0")
    if (x > n):
        raise ValueError("x cannot be greater than n")

    if (type(P) is not np.ndarray or len(P.shape) != 1):
        raise TypeError("P must be a 1D numpy.ndarray")

    if (type(Pr) is not np.ndarray or Pr.shape != P.shape):
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    if (not (np.all(P >= 0) and np.all(P <= 1))):
        raise ValueError("All values in P must be in the range [0, 1]")

    if (not (np.all(Pr >= 0) and np.all(Pr <= 1))):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    if (not np.isclose(1, np.sum(Pr))):
        raise ValueError("Pr must sum to 1")

    fact = np.math.factorial
    lh = np.ndarray(P.shape)  # likelihood
    pos = ((x / n))

    for p in range(len(P)):
        lh[p] = ((fact(n) / (fact(x) * fact(n - x))) *
                 (np.power(P[p], x)) * (np.power((1 - P[p]), (n - x))))

    return lh * Pr
