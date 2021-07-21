#!/usr/bin/env python3
'''Linear Algebra - Adjugate module'''


def adjugate(matrix):
    '''calculates the adjugate matrix of a matrix
    Args:
        matrix is a list of lists whose adjugate matrix should be calculated
    Returns: the adjugate matrix of matrix
    '''
    if (type(matrix) is not list or
            matrix == [] or
            not all(type(elem) is list for elem in matrix)):
        raise TypeError("matrix must be a list of lists")

    len_mat = len(matrix)

    if not all(len(elem) == len_mat for elem in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    cofactor_mat = cofactor(matrix)

    adj_mat = []
    for elem in cofactor_mat:
        adj_mat.append(elem.copy())

    # transpose cofactor matrix:
    for i in range(len_mat):
        for j in range(len_mat):
            adj_mat[i][j] = cofactor_mat[j][i]

    return adj_mat


def cofactor(matrix):
    '''calculates the cofactor matrix of a matrix
    Args:
        matrix is a list of lists whose cofactor matrix should be calculated
    Returns: the cofactor matrix of matrix
    '''
    if (type(matrix) is not list or
            matrix == [] or
            not all(type(elem) is list for elem in matrix)):
        raise TypeError("matrix must be a list of lists")

    len_mat = len(matrix)

    if not all(len(elem) == len_mat for elem in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    cofactor_mat = minor(matrix)  # initialy the minor matrix

    for i in range(len_mat):
        for j in range(len_mat):
            if (i % 2 == 0 and j % 2 != 0 or
                    (i % 2 != 0 and j % 2 == 0)):
                cofactor_mat[i][j] *= -1

    return cofactor_mat


def minor(matrix):
    '''calculates the minor matrix of a matrix
    Args:
        matrix is a list of lists whose minor matrix should be calculated
    Returns: the minor matrix of matrix
    '''
    if (type(matrix) is not list or
            matrix == [] or
            not all(type(elem) is list for elem in matrix)):
        raise TypeError("matrix must be a list of lists")

    len_mat = len(matrix)

    if not all(len(elem) == len_mat for elem in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # minor matrix of a 1x1 matrix is [[1]]
    if (len_mat == 1):
        return [[1]]

    minor_mat = []
    for i in range(len_mat):
        minor_row = []
        for j in range(len_mat):
            # Build sub-matrix to calculate its determinant
            sub_matrix = []
            for k in range(len_mat):
                if k != i:
                    # Build a row vector. For each row of the matrix,
                    # except the row and column of the actual position (i, j)
                    row_vector = matrix[k][:j] + matrix[k][j + 1:]
                    sub_matrix.append(row_vector)
            minor_row.append(determinant(sub_matrix))
        minor_mat.append(minor_row)

    return minor_mat


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
