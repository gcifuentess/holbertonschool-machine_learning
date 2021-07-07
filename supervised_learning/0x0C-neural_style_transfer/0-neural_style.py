#!/usr/bin/env python3
'''Neural Style Transfer Module'''
import numpy as np
import tensorflow as tf


class NST():
    '''class to perform tasks for neural style transfer'''

    style_layers = [
        'block1_conv1',
        'block2_conv1',
        'block3_conv1',
        'block4_conv1',
        'block5_conv1'
    ]
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        '''class constructor
        Args:
            style_image - the image used as a style reference, stored as a
                numpy.ndarray
            content_image - the image used as a content reference, stored as a
                numpy.ndarray
            alpha - the weight for content cost
            beta - the weight for style cost
        '''

        if (type(style_image) is not np.ndarray or
                style_image.ndim != 3 or
                style_image.shape[2] != 3):
            raise TypeError("style_image must be a numpy.ndarray "
                            "with shape (h, w, 3)")

        if (type(content_image) is not np.ndarray or
                content_image.ndim != 3 or
                content_image.shape[2] != 3):
            raise TypeError("content_image must be a numpy.ndarray "
                            "with shape (h, w, 3)")

        print("alpha", type(alpha))
        if (alpha < 0 or type(alpha) not in [int, float]):
            raise ValueError("alpha must be a non-negative number")

        print("beta", type(beta))
        if (beta < 0 or type(beta) not in [int, float]):
            raise ValueError("beta must be a non-negative number")

        # enable eager execution:
        tf.enable_eager_execution()

        self.style_image = NST.scale_image(style_image)
        self.content_image = NST.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

    @staticmethod
    def scale_image(image):
        '''rescales an image such that its pixels values are between
               0 and 1 and its largest side is 512 pixels
        Args:
            image - a numpy.ndarray of shape (h, w, 3) containing the
                image to be scaled
        Returns: the scaled image
        '''
        if (type(image) is not np.ndarray or
                image.ndim != 3 or
                image.shape[2] != 3):
            raise TypeError("image must be a numpy.ndarray "
                            "with shape (h, w, 3)")

        # image scale:
        max_dim = 512
        h, w, _ = image.shape
        scale = max_dim / max(h, w)

        # batch dimension
        image = np.expand_dims(image, axis=0)

        # resize image
        image_t = tf.image.resize_bicubic(
            images=image,
            size=[round(h * scale), round(w * scale)],
        )

        # normalize image:
        image_t = image_t / 255
        image_t = tf.clip_by_value(image_t, 0, 1)

        return image_t
