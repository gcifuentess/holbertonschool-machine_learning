#!/usr/bin/env python3
'''Deep RNN Module'''
import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    '''performs forward propagation for a deep RNN
    Args:
        rnn_cells is a list of RNNCell instances of length l that will be used
                  for the forward propagation
            - l is the number of layers
        X is the data to be used, given as a numpy.ndarray of shape (t, m, i)
            - t is the maximum number of time steps
            - m is the batch size
            - i is the dimensionality of the data
        h_0 is the initial hidden state, given as a numpy.ndarray of shape
            (l, m, h)
            - h is the dimensionality of the hidden state

    Returns: H, Y
        - H is a numpy.ndarray containing all of the hidden states
        - Y is a numpy.ndarray containing all of the outputs
    '''
    T, m, i = X.shape
    lyr, m, h = h_0.shape
    o = rnn_cells[-1].Wy.shape[1]  # output dimension

    H = np.zeros((T + 1, lyr, m, h))
    Y = np.zeros((T, m, o))

    H[0] = h_0
    for t in range(T):
        for lyr, rnn_cell in enumerate(rnn_cells):
            h_next = H[t][lyr]
            if (lyr == 0):
                x = X[t]
            else:
                x = H[t + 1][lyr - 1]
            h_next, y = rnn_cell.forward(h_next, x)
            H[t + 1][lyr] = h_next
        Y[t] = y

    return H, Y
