#!/usr/bin/env python3
'''module that concatenates two arrays'''


def cat_arrays(arr1, arr2):
    '''concatenates two arrays'''
    concat = arr1.copy()
    for element in arr2:
        concat.append(element)
    return concat
