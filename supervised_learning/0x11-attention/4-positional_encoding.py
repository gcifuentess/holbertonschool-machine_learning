#!/usr/bin/env python3
'''Positional Encoding module'''
import numpy as np


def positional_encoding(max_seq_len, dm):
    '''calculates the positional encoding for a transformer
    Args:
        max_seq_len is an integer representing the maximum sequence length
        dm is the model depth

    Returns: a numpy.ndarray of shape (max_seq_len, dm) containing the
             positional encoding vectors
    '''
    PE = np.zeros((max_seq_len, dm))
    even = np.array([x for x in range(0, dm, 2)])
    pos = np.arange(max_seq_len)

    PE[:, ::2] = np.sin(pos[:, np.newaxis] / np.power(10000, even / dm))
    PE[:, 1::2] = np.cos(pos[:, np.newaxis] / np.power(10000, even / dm))

    return PE
