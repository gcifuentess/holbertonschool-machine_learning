#!/usr/bin/env python3
'''summation_i_squared module'''
import numpy as np


def summation_i_squared(n):
    '''sumatory of i squared'''
    if (type(n) != int and type(n) != float) or n < 1:
        return None
    sequence = np.array(range(1, n + 1)) ** 2
    return int(sum(sequence, 0))
