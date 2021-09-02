#!/usr/bin/env python3
'''Bidirectional RNN module'''
import numpy as np


def bi_rnn(bi_cell, X, h_0, h_t):
    '''performs forward propagation for a bidirectional RNN
    Args:
        bi_cell is an instance of BidirectinalCell that will be used for the
                forward propagation
        X is the data to be used, given as a numpy.ndarray of shape (t, m, i)
            - t is the maximum number of time steps
            - m is the batch size
            - i is the dimensionality of the data
        h_0 is the initial hidden state in the forward direction, given as a
            numpy.ndarray of shape (m, h)
            - h is the dimensionality of the hidden state
        h_t is the initial hidden state in the backward direction, given as a
            numpy.ndarray of shape (m, h)

    Returns: H, Y
        - H is a numpy.ndarray containing all of the concatenated hidden states
        - Y is a numpy.ndarray containing all of the outputs
    '''
    T, m, i = X.shape
    _, h = h_0.shape
    Hp = np.zeros((T, m, h))
    Hn = np.zeros((T, m, h))

    for t in range(T):
        if (t == 0):
            h_prev = h_0
        else:
            h_prev = Hn[t - 1]
        Hn[t] = bi_cell.forward(h_prev, X[t])

    for t in reversed(range(T)):
        if (t == T - 1):
            h_next = h_t
        else:
            h_next = Hp[t + 1]
        Hp[t] = bi_cell.backward(h_next, X[t])

    H = np.concatenate(
        (Hn, Hp),
        axis=2,
    )

    Y = bi_cell.output(H)

    return H, Y
