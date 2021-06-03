#!/usr/bin/env python3
'''Convolution with Padding module'''
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    '''performs a convolution on grayscale images with custom padding
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
        padding is a tuple of (ph, pw)
                - ph is the padding for the height of the image
                - pw is the padding for the width of the image
    Important: the image will be padded with 0’s
    Returns: a numpy.ndarray containing the convolved images
    '''
    m = images.shape[0]
    input_h = images.shape[1]
    input_w = images.shape[2]
    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]
    bias = 0  # constant for now
    pad_top = padding[0]
    pad_bottom = pad_top
    pad_left = padding[1]
    pad_right = pad_left
    output_h = input_h + pad_top + pad_bottom - kernel_h + 1
    output_w = input_w + pad_left + pad_right - kernel_w + 1

    output = np.zeros([m, output_h, output_w])  # convolution output
    images_padded = np.pad(images, [(0, 0), (pad_top, pad_bottom),
                                    (pad_left, pad_right)], mode="constant")

    for h in range(output_h):
        for w in range(output_w):
            current = images_padded[:, h: h + kernel_h, w: w + kernel_w]
            # axes sum-reduction:
            # https://stackoverflow.com/questions/41870228/...
            # ...understanding-tensordot
            output[:, h, w] = np.tensordot(current, kernel,
                                           axes=([1, 2], [0, 1])) + bias
    return output
