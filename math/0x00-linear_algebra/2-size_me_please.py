#!/usr/bin/env python3


def matrix_shape(matrix):
    '''calculates the shape of a matrix'''
    shape = []
    dimension = matrix.copy()
    while type(dimension) == list:
        shape.append(len(dimension))
        dimension = dimension[0]
    return(shape)
