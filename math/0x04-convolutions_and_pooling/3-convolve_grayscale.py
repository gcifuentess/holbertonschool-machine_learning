#!/usr/bin/env python3
'''Strided Convolution module'''
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
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
        padding is either a tuple of (ph, pw), ‘same’, or ‘valid’
                - if ‘same’, performs a same convolution
                - if ‘valid’, performs a valid convolution
                - if a tuple:
                    * ph is the padding for the height of the image
                    * pw is the padding for the width of the image
                Important: the image will be padded with 0’s
        stride is a tuple of (sh, sw)
               - sh is the stride for the height of the image
               - sw is the stride for the width of the image
    Returns: a numpy.ndarray containing the convolved images
    '''
    m = images.shape[0]
    input_h = images.shape[1]
    input_w = images.shape[2]
    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]
    bias = 0  # constant for now
    stride_h = stride[0]
    stride_w = stride[1]

    if padding == 'valid':
        pad_top = 0
        pad_bottom = 0
        pad_left = 0
        pad_right = 0
        output_h = (input_h - kernel_h) // stride_h + 1
        output_w = (input_w - kernel_w) // stride_w + 1
    elif padding == 'same':
        pad_top = kernel_h // 2
        pad_bottom = pad_top
        pad_left = kernel_w // 2
        pad_right = pad_left
        output_h = (input_h // stride_h)
        output_w = (input_w // stride_w)
    elif type(padding) == tuple:
        pad_top = padding[0]
        pad_bottom = pad_top
        pad_left = padding[1]
        pad_right = pad_left
        output_h = (input_h + pad_top +
                    pad_bottom - kernel_h) // stride_h + 1
        output_w = (input_w + pad_left +
                    pad_right - kernel_w) // stride_w + 1

    output = np.zeros([m, output_h, output_w])  # convolution output
    images_padded = np.pad(images, [(0, 0), (pad_top, pad_bottom),
                                    (pad_left, pad_right)], mode="constant")

    h = 0
    for i in range(0, output_h):
        w = 0
        for j in range(0, output_w):
            current = images_padded[:, h: h + kernel_h, w: w + kernel_w]
            # axes sum-reduction:
            # https://stackoverflow.com/questions/41870228/...
            # ...understanding-tensordot
            output[:, i, j] = np.tensordot(current, kernel,
                                           axes=([1, 2], [0, 1])) + bias
            w += stride_w
        h += stride_h

    return output
