#!/usr/bin/env python3
'''Recurrent Neural Network Model'''
import numpy as np


class RNNCell():
    '''represents a cell of a simple RNN'''

    def __init__(self, i, h, o):
        '''RNNCell class constructor
        Args:
            i is the dimensionality of the data
            h is the dimensionality of the hidden state
            o is the dimensionality of the outputs

        Creates the public instance attributes Wh, Wy, bh, by that represent
        the weights and biases of the cell
            - Wh and bh are for the concatenated hidden state and input data
            - Wy and by are for the output

        '''
        self.Wh = np.random.normal(size=(i + h, h))
        self.bh = np.zeros((1, h))
        self.Wy = np.random.normal(size=(h, o))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        '''performs forward propagation for one time step
        Args:
            x_t is a numpy.ndarray of shape (m, i) that contains the data input
                for the cell
                - m is the batche size for the data
            h_prev is a numpy.ndarray of shape (m, h) containing the previous
                   hidden state

        Returns: h_next, y
            - h_next is the next hidden state
            - y is the output of the cell
        '''
        h_next = np.tanh(
            np.concatenate(
                (h_prev, x_t),
                axis=1
            ) @ self.Wh + self.bh
        )

        z = h_next @ self.Wy + self.by
        y = softmax(z)

        return h_next, y


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
