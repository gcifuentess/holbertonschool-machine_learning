#!/usr/bin/env python3
'''Bidirectional Cell Backward'''
import numpy as np


class BidirectionalCell():
    '''represents a bidirectional cell of an RNN'''

    def __init__(self, i, h, o):
        '''RNNCell class constructor
        Args:
            i is the dimensionality of the data
            h is the dimensionality of the hidden state
            o is the dimensionality of the outputs

        Creates the public instance attributes Whf, Whb, Wy, bhf, bhb, by
        that represent the weights and biases of the cell
            - Whf and bhf are for the hidden states in the forward direction
            - Whb and bhb are for the hidden states in the backward direction
            - Wy and by are for the outputs
        '''
        self.Whf = np.random.normal(size=(i + h, h))
        self.bhf = np.zeros((1, h))
        self.Whb = np.random.normal(size=(i + h, h))
        self.bhb = np.zeros((1, h))
        self.Wy = np.random.normal(size=(h + h, o))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        '''calculates the hidden state in the forward direction for one time
           step
        Args:
            x_t is a numpy.ndarray of shape (m, i) that contains the data input
                for the cell
                - m is the batch size for the data
            h_prev is a numpy.ndarray of shape (m, h) containing the previous
                   hidden state

        Returns: h_next, the next hidden state
        '''
        h_next = np.tanh(
            np.concatenate(
                (h_prev, x_t),
                axis=1
            ) @ self.Whf + self.bhf
        )

        return h_next

    def backward(self, h_next, x_t):
        '''calculates the hidden state in the backward direction for one time
           step
        Args:
            x_t is a numpy.ndarray of shape (m, i) that contains the data input
                for the cell
                - m is the batch size for the data
            h_next is a numpy.ndarray of shape (m, h) containing the next
                   hidden state

        Returns: h_pev, the previous hidden state
        '''
        h_prev = np.tanh(
            np.concatenate(
                (h_next, x_t),
                axis=1
            ) @ self.Whb + self.bhb
        )

        return h_prev

    def output(self, H):
        '''calculates all outputs for the RNN
        Args:
            H is a numpy.ndarray of shape (t, m, 2 * h) that contains the
              concatenated hidden states from both directions, excluding their
              initialized states
                - t is the number of time steps
                - m is the batch size for the data
                - h is the dimensionality of the hidden states

        Returns: Y, the outputs
        '''
        T = H.shape[0]
        Y = []
        for t in range(T):
            z = H[t] @ self.Wy + self.by
            Y.append(softmax(z))

        return np.array(Y)


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
