#!/usr/bin/env python3
'''Bidirectional Cell Forward'''
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
