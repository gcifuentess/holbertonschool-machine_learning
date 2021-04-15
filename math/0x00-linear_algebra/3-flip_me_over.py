#!/usr/bin/env python3
'''transpose of a 2D matrix module'''


def matrix_transpose(matrix):
    '''returns the transpose of a 2D matrix'''
    transpose = []
    for i in range(0, len(matrix[0])):  # loop in columns
        new_row = []
        for row in matrix:  # loop in rows
            new_row.append(row[i])
        transpose.append(new_row)
    return (transpose)
