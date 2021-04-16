#!/usr/bin/env python3
'''module that adds two matrices'''
import numpy as np


def add_matrices(mat1, mat2):
    '''adds two matrices'''
    np_mat1 = np.array(mat1)
    np_mat2 = np.array(mat2)
    if np_mat1.shape != np_mat2.shape:
        return None
    else:
        return ((np_mat1 + np_mat2).tolist())
