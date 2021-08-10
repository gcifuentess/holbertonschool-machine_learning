#!/usr/bin/env python3
'''Markov Chain module'''
import numpy as np


def markov_chain(P, s, t=1):
    '''Determines the probability of a markov chain being in a particular
       state after a specified number of iterations
    Args:
        P is a square 2D numpy.ndarray of shape (n, n) representing the
          transition matrix
            - P[i, j] is the probability of transitioning from state i to
                      state j
            - n is the number of states in the markov chain
        s is a numpy.ndarray of shape (1, n) representing the probability of
          starting in each state
        t is the number of iterations that the markov chain has been through

    Returns: a numpy.ndarray of shape (1, n) representing the probability of
             being in a specific state after t iterations, or None on failure
    '''
    if (type(P) is not np.ndarray or
            len(P.shape) != 2 or
            P.shape[0] != P.shape[1]):
        return None

    n = P.shape[0]

    if (type(P) is not np.ndarray or len(P.shape) != 2 or P.shape[1] != n):
        return None

    if (type(t) is not int or t < 1):
        return None

    current_state = s.copy()
    for i in range(t):
        current_state = np.matmul(current_state, P)

    return current_state
