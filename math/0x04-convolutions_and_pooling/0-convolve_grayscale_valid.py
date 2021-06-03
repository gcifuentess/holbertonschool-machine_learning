#!/usr/bin/env python3
'''Valid Convolution module'''
import numpy as np


def convolve_grayscale_valid(images, kernel):
    '''performs a valid convolution on grayscale images
    Args:
        images is a numpy.ndarray with shape (m, h, w) containing multiple
               grayscale images
               - m is the number of images
               - h is the height in pixels of the images
               - w is the width in pixels of the images
        kernel is a numpy.ndarray with shape (kh, kw) containing the kernel
               for the convolution
               - kh is the height of the kernel
               - kw is the width of the kernel
    Returns: a numpy.ndarray containing the convolved images
    '''
    m = images.shape[0]
    input_h = images.shape[1]
    input_w = images.shape[2]
    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]
    # strides = (1, 1)  # constant for now
    bias = 0  # constant for now
    # output_h = int(floor(float(input_h - kernel_h + 1) / float(strides[0])))
    # output_w = int(floor(float(input_w - kernel_w + 1) / float(strides[1])))
    output_h = input_h - kernel_h + 1
    output_w = input_w - kernel_w + 1

    output = np.zeros([m, output_h, output_w])  # convolution output

    for h in range(output_h):
        for w in range(output_w):
            current = images[:, h: h + kernel_h, w: w + kernel_w]
            # axes sum-reduction:
            # https://stackoverflow.com/questions/41870228/...
            # ...understanding-tensordot
            output[:, h, w] = np.tensordot(current, kernel,
                                           axes=([1, 2], [0, 1])) + bias
    return output
