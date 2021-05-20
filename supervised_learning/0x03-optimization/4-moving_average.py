#!/usr/bin/env python3
'''Moving Average module'''


def moving_average(data, beta):
    '''calculates the weighted moving average of a data set
    Args:
        data is the list of data to calculate the moving average of
        beta is the weight used for the moving average
    Returns: a list containing the moving averages of data

    Important:  Uses bias correction
    '''
    v = 0
    ma = []
    for i in range(len(data)):
        v = beta * v + (1 - beta) * data[i]
        bc = v / (1 - beta ** (i + 1))
        ma.append(bc)
    return ma
