#!/usr/bin/env python3
'''module to add two matrices element-wise'''


def add_matrices2D(mat1, mat2):
    '''adds two matrices element-wise'''
    addition = []
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        for i in range(0, len(mat1)):
            new_row = []
            for j in range(0, len(mat1[0])):
                new_row.append(mat1[i][j] + mat2[i][j])
            addition.append(new_row)
    else:
        addition = None
    return(addition)
