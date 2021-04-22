#!/usr/bin/env python3
'''summation_i_squared module'''


def summation_i_squared(n):
    '''sumatory of i squared'''
    if (type(n) != int and type(n) != float) or n == 0:
        return None
    return int(sum(range(1, (n * n) + 1, n)))
