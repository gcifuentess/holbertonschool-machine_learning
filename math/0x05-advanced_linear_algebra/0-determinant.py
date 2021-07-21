#!/usr/bin/env python3
'''Linear Algebra - Determinant module'''


def determinant(matrix):
    '''calculates the determinant of a matrix
    Args:
        matrix is a list of lists whose determinant should be calculated
    Returns: the determinant of matrix
    '''
    if (type(matrix) is not list or
            matrix == [] or
            not all(type(elem) is list for elem in matrix)):
        raise TypeError("matrix must be a list of lists")

    len_mat = len(matrix)

    # determinant of cero matrix is 1
    if (len_mat == 1 and matrix[0] == []):
        return 1

    if not all(len(elem) == len_mat for elem in matrix):
        raise ValueError("matrix must be a square matrix")

    if (len_mat == 1):
        return matrix[0][0]

    if (len_mat == 2):
        return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]

    det = 0
    for i, num in enumerate(matrix[0]):
        sub_matrix = []
        for j in range(1, len_mat):
            row_vector = matrix[j][:i] + matrix[j][i + 1:]
            sub_matrix.append(row_vector)
        if i % 2 == 0:
            det += num * determinant(sub_matrix)
        else:
            det -= num * determinant(sub_matrix)

    return det
