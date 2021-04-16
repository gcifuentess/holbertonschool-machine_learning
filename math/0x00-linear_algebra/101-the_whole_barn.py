#!/usr/bin/env python3
'''module that adds two matrices'''


def add_matrices(mat1, mat2):
    '''adds two matrices'''
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)
    if shape1 != shape2:
        return None
    else:
        return in_dimension(mat1, mat2, len(shape1), shape1[0])


def matrix_shape(matrix):
    '''calculates the shape of a matrix'''
    shape = []
    dimension = matrix.copy()
    while type(dimension) == list:
        shape.append(len(dimension))
        dimension = dimension[0]
    return(shape)


def in_dimension(mat1, mat2, dim, size):
    '''recursive function'''
    arr = []
    if dim == 1:
        for i in range(0, size):
            arr.append(mat1[i] + mat2[i])
        return arr
    else:
        for i in range(0, size):
            to_size = matrix_shape(mat1[i])[0]
            arr.append(in_dimension(mat1[i], mat2[i], dim - 1, to_size))
    return arr
