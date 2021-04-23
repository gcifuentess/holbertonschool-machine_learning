#!/usr/bin/env python3
'''summation_i_squared module'''


def summation_i_squared(n):
    '''sumatory of i squared'''
    if (type(n) != int and type(n) != float) or n < 1:
        return None
    # Summs of powers Faulhaber's formula:
    return int((n * (n + 1) * (2 * n + 1)) / 6)
