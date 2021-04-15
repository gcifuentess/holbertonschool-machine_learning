'''
module that performs element-wise addition, subtraction, multiplication,
and division
'''


def np_elementwise(mat1, mat2):
    '''
    performs element-wise addition, subtraction, multiplication,
    and division
    '''
    add = mat1 + mat2
    sub = mat1 - mat2
    mult = mat1 * mat2
    div = mat1 / mat2
    return ((add, sub, mult, div))
