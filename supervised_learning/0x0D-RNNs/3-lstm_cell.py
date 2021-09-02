#!/usr/bin/env python3
'''LSTM Cell Module'''
import numpy as np


class LSTMCell():
    '''represents an LSTM unit'''

    def __init__(self, i, h, o):
        '''LSTMCell class constructor
        Args:
            i is the dimensionality of the data
            h is the dimensionality of the hidden state
            o is the dimensionality of the outputs

        Creates the public instance attributes Wf, Wu, Wc, Wo, Wy, bf, bu, bc,
        bo, by that represent the weights and biases of the cell
            - Wf and bf are for the forget gate
            - Wu and bu are for the update gate
            - Wc and bc are for the intermediate cell state
            - Wo and bo are for the output gate
            - Wy and by are for the outputs
        '''
        self.Wf = np.random.normal(size=(i + h, h))
        self.bf = np.zeros((1, h))
        self.Wu = np.random.normal(size=(i + h, h))
        self.bu = np.zeros((1, h))
        self.Wc = np.random.normal(size=(i + h, h))
        self.bc = np.zeros((1, h))
        self.Wo = np.random.normal(size=(i + h, h))
        self.bo = np.zeros((1, h))
        self.Wy = np.random.normal(size=(h, o))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, c_prev, x_t):
        '''performs forward propagation for one time step
        Args:
            x_t is a numpy.ndarray of shape (m, i) that contains the data input
                for the cell
                - m is the batch size for the data
            h_prev is a numpy.ndarray of shape (m, h) containing the previous
                   hidden state
            c_prev is a numpy.ndarray of shape (m, h) containing the previous
                   cell state

        Returns: h_next, c_next, y
            - h_next is the next hidden state
            - c_next is the next cell state
            - y is the output of the cell
        '''
        h_x = np.concatenate(
            (h_prev, x_t),
            axis=1
        )  # shape (m, i + h)

        ft = sigmoid(
            h_x @ self.Wf + self.bf
        )  # shape (m, h)

        it = sigmoid(
            h_x @ self.Wu + self.bu
        )  # shape (m, h)

        Ct_sub = np.tanh(
            h_x @ self.Wc + self.bc
        )  # shape (m, h)

        c_next = ft * c_prev + it * Ct_sub

        ot = sigmoid(
            h_x @ self.Wo + self.bo
        )  # shape (m, h)

        h_next = ot * np.tanh(c_next)

        z = h_next @ self.Wy + self.by
        y = softmax(z)

        return h_next, c_next, y


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
