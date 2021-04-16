#!/usr/bin/env python3
'''module that slices a matrix along specific axes'''


def np_slice(matrix, axes={}):
    '''slices a matrix along specific axes'''
    to_slice = [slice(None)] * matrix.ndim
    for key, value in axes.items():
        to_slice[key] = slice(*value)
    return (matrix[tuple(to_slice)].copy())
