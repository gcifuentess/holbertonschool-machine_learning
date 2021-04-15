#!/usr/bin/env python3
'''module to perform matrix multiplication'''


def mat_mul(mat1, mat2):
    '''performs matrix multiplication'''
    mult = []
    if len(mat1[0]) == len(mat2):
        for i in range(0, len(mat1)):
            new_row = []
            for j in range(0, len(mat2[0])):
                sum = 0
                for k in range(0, len(mat1[0])):
                    sum += mat1[i][k] * mat2[k][j]
                new_row.append(sum)
            mult.append(new_row)
    else:
        mult = None
    return (mult)
