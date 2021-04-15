#!/usr/bin/env python3
'''module to concatenate two matrices along a specific axis'''


def cat_matrices2D(mat1, mat2, axis=0):
    '''concatenates two matrices along a specific axis'''
    concat = []
    for row in mat1:
        concat.append(row.copy())
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        for row in mat2:
            concat.append(row.copy())
    elif axis == 1 and len(mat1) == len(mat2):
        for i in range(0, len(mat1)):
            for j in range(0, len(mat2[i])):
                concat[i].append(mat2[i][j])
    else:
        concat = None
    return (concat)
