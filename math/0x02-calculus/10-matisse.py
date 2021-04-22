#!/usr/bin/env python3
'''module that calculates the derivative of a polynomial'''


def poly_derivative(poly):
    '''calculates the derivative of a polynomial'''
    if type(poly) != list or len(poly) <= 1:
        return [0]
    derivative = []
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])
    return derivative