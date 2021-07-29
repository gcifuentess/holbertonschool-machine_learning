#!/usr/bin/env python3
'''Continuous Posterior module'''
from scipy import special


def posterior(x, n, p1, p2):
    '''calculates the posterior probability that the probability of developing
    severe side effects falls within a specific range given the data
    Args:
        x is the number of patients that develop severe side effects
        n is the total number of patients observed
        p1 is the lower bound on the range
        p2 is the upper bound on the range

    Important: it is assumed the prior beliefs of p follow a uniform distrib

    Returns: the posterior probability that p is within the range [p1, p2]
             given x and n
    '''
    if (type(n) is not int or n <= 0):
        raise ValueError("n must be a positive integer")

    if (type(x) is not int or x < 0):
        raise ValueError("x must be an integer that is greater " +
                         "than or equal to 0")
    if (x > n):
        raise ValueError("x cannot be greater than n")

    if ((not isinstance(p1, float)) or p1 < 0 or p2 > 1):
        raise TypeError("p1 must be a float in the range [0, 1]")

    if ((not isinstance(p2, float)) or p2 < 0 or p2 > 1):
        raise TypeError("p2 must be a float in the range [0, 1]")

    if (p2 <= p1):
        raise ValueError("p2 must be greater than p1")

    beta1 = special.btdtr(x + 1, n - x + 1, p1)
    beta2 = special.btdtr(x + 1, n - x + 1, p2)

    return beta2 - beta1
