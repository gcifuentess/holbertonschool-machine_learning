#!/usr/bin/env python3
'''module that calculates the integral of a polynomial'''


def poly_integral(poly, C=0):
    '''calculates the integral of a polynomial'''
    if type(poly) != list or len(poly) == 0 or type(C) != int:
        return None
    if len(poly) == 1:
        return [C]
    integral = [C]
    for i in range(0, len(poly)):
        if type(poly[i]) != int and type(poly[i]) != float:
            return None
        coeficient = poly[i] / (i + 1)
        if coeficient - int(coeficient) == 0:
            coeficient = int(coeficient)
        integral.append(coeficient)
    while integral[-1] == 0 and len(integral) > 1:
        integral.pop()
    return integral
