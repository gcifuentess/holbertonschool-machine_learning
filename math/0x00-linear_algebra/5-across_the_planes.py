#!/usr/bin/env python3
'''module to add two matrices element-wise'''


def add_matrices2D(mat1, mat2):
    '''adds two matrices element-wise'''

    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)
    addition = []
    if shape1 == shape2:
        for i in range(0, len(mat1)):
            new_row = []
            for j in range(0, len(mat1[0])):
                new_row.append(mat1[i][j] + mat2[i][j])
            addition.append(new_row)
    else:
        addition = None
    return(addition)


def matrix_shape(matrix):
    '''calculates the shape of a matrix'''
    shape = []
    dimension = matrix.copy()
    while type(dimension) == list:
        shape.append(len(dimension))
        dimension = dimension[0]
    return(shape)
