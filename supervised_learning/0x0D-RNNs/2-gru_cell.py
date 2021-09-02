#!/usr/bin/env python3
'''GRU Cell Module'''
import numpy as np


class GRUCell():
    '''represents a gated recurrent unit'''

    def __init__(self, i, h, o):
        '''GRUCell class constructor
        Args:
            i is the dimensionality of the data
            h is the dimensionality of the hidden state
            o is the dimensionality of the outputs

        Creates the public instance attributes Wz, Wr, Wh, Wy, bz, br, bh, by
        that represent the weights and biases of the cell
            - Wz and bz are for the update gate
            - Wr and br are for the reset gate
            - Wh and bh are for the intermediate hidden state
            - Wy and by are for the output
        '''
        self.Wz = np.random.normal(size=(i + h, h))
        self.bz = np.zeros((1, h))
        self.Wr = np.random.normal(size=(i + h, h))
        self.br = np.zeros((1, h))
        self.Wh = np.random.normal(size=(i + h, h))
        self.bh = np.zeros((1, h))
        self.Wy = np.random.normal(size=(h, o))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        '''performs forward propagation for one time step
        Args:
            x_t is a numpy.ndarray of shape (m, i) that contains the data input
                for the cell
                - m is the batch size for the data
            h_prev is a numpy.ndarray of shape (m, h) containing the previous
                   hidden state

        Returns: h_next, y
            - h_next is the next hidden state
            - y is the output of the cell
        '''
        h_x = np.concatenate(
            (h_prev, x_t),
            axis=1
        )  # shape (m, i + h)

        zt = sigmoid(
            h_x @ self.Wz + self.bz
        )  # shape (m, h)

        rt = sigmoid(
            h_x @ self.Wr + self.br
        )  # shape (m, h)

        h_rt = h_prev * rt  # shape (m, h)

        h_rt_x = np.concatenate(
            (h_rt, x_t),
            axis=1,
        )  # shape (m, i + h)

        h_next_sub = np.tanh(
            h_rt_x @ self.Wh + self.bh
        )  # shape (m, h)

        h_next = (1 - zt) * h_prev + zt * h_next_sub

        z = h_next @ self.Wy + self.by
        y = softmax(z)

        return h_next, y


def sigmoid(x):
    '''sigmoid activation function'''
    return 1 / (1 + np.exp(-x))


def softmax(z):
    '''softmax activation function

    Extracted from:
        https://stackoverflow.com/questions/34968722/
        how-to-implement-the-softmax-function-in-python
        by ChuckFive
    '''
    s = np.max(z, axis=1)
    s = s[:, np.newaxis]  # necessary step to do broadcasting
    e_x = np.exp(z - s)
    div = np.sum(e_x, axis=1)
    div = div[:, np.newaxis]

    return e_x / div
