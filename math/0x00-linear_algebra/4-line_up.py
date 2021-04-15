#!/usr/bin/env python3
'''module to add two arrays element-wise'''


def add_arrays(arr1, arr2):
    '''adds two arrays element-wise'''
    addition = []
    if len(arr1) == len(arr2):
        for i in range(0, len(arr1)):
            addition.append(arr1[i] + arr2[i])
    else:
        addition = None
    return(addition)
