#!/usr/bin/env python3
'''Pooling module'''
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    '''performs pooling on images
    Args:
        images is a numpy.ndarray with shape (m, h, w, c) containing multiple
               images
               - m is the number of images
               - h is the height in pixels of the images
               - w is the width in pixels of the images
               - c is the number of channels in the image
        kernel_shape is a numpy.ndarray with shape (kh, kw) containing the
               kernel shape for the pooling
               - kh is the height of the kernel
               - kw is the width of the kernel
        stride is a tuple of (sh, sw)
               - sh is the stride for the height of the image
               - sw is the stride for the width of the image
        mode indicates the type of pooling
             - max indicates max pooling
             - avg indicates average pooling
    Returns: a numpy.ndarray containing the convolved images
    '''
    m = images.shape[0]
    input_h = images.shape[1]
    input_w = images.shape[2]
    channels = images.shape[3]
    kernel_h = kernel_shape[0]
    kernel_w = kernel_shape[1]
    bias = 0  # constant for now
    stride_h = stride[0]
    stride_w = stride[1]

    output_h = int(np.floor((input_h - kernel_h) / stride_h) + 1)
    output_w = int(np.floor((input_w - kernel_w) / stride_w) + 1)

    output = np.zeros([m, output_h, output_w, channels])  # convolution output

    h = 0
    for i in range(output_h):
        w = 0
        for j in range(output_w):
            current = images[:, h: h + kernel_h, w: w + kernel_w, :]
            if mode == 'max':
                output[:, i, j, :] = np.amax(current, (1, 2))
            elif mode == 'avg':
                output[:, i, j, :] = np.average(current, (1, 2))
            w += stride_w
        h += stride_h

    return output
