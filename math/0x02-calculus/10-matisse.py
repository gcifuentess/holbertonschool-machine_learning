#!/usr/bin/env python3
'''module that calculates the derivative of a polynomial'''


def poly_derivative(poly):
    '''calculates the derivative of a polynomial'''
    if type(poly) != list or len(poly) == 0:
        return None
    derivative = []
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])
    if derivative == []:
        return [0]
    return derivative
