#!/usr/bin/env python3
'''Multiple Kernels module'''
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    '''performs a convolution on images using multiple kernels
    Args:
        images is a numpy.ndarray with shape (m, h, w, c) containing multiple
               images
               - m is the number of images
               - h is the height in pixels of the images
               - w is the width in pixels of the images
               - c is the number of channels in the image
        kernels is a numpy.ndarray with shape (kh, kw, c, nc) containing the
               kernels for the convolution
               - kh is the height of the kernel
               - kw is the width of the kernel
               - c is the number of channels
               - nc is the number of kernels
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
    channels = images.shape[3]
    n_kernels = kernels.shape[3]
    input_h = images.shape[1]
    input_w = images.shape[2]
    kernel_h = kernels.shape[0]
    kernel_w = kernels.shape[1]
    bias = 0  # constant for now
    stride_h = stride[0]
    stride_w = stride[1]

    # SAME padding (default); when kernel h or w is even, add 1:
    pad_top = int(((input_h - 1) * stride_h + kernel_h -
                   input_h) / 2 + (kernel_h % 2 == 0))
    pad_bottom = pad_top
    pad_left = int(((input_w - 1) * stride_w + kernel_w -
                    input_w) / 2 + (kernel_w % 2 == 0))
    pad_right = pad_left

    if padding == 'valid':
        pad_top = 0
        pad_bottom = 0
        pad_left = 0
        pad_right = 0
    elif type(padding) == tuple:
        pad_top = padding[0]
        pad_bottom = pad_top
        pad_left = padding[1]
        pad_right = pad_left

    output_h = int(np.floor((input_h + pad_top +
                             pad_bottom - kernel_h) / stride_h) + 1)
    output_w = int(np.floor((input_w + pad_left +
                             pad_right - kernel_w) / stride_w) + 1)

    output = np.zeros([m, output_h, output_w, n_kernels])  # convolution output
    images_padded = np.pad(images, [(0, 0), (pad_top, pad_bottom),
                                    (pad_left, pad_right), (0, 0)],
                           mode="constant")

    h = 0
    for i in range(0, output_h):
        w = 0
        for j in range(0, output_w):
            current = images_padded[:, h: h + kernel_h, w: w + kernel_w, :]
            # axes sum-reduction:
            # https://stackoverflow.com/questions/41870228/...
            # ...understanding-tensordot
            output[:, i, j, :] = np.tensordot(current, kernels,
                                              axes=([1, 2, 3],
                                                    [0, 1, 2])) + bias
            w += stride_w
        h += stride_h

    return output
