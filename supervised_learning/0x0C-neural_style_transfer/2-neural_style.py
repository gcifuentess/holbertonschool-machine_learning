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

        if (type(alpha) not in [int, float] or alpha < 0):
            raise TypeError("alpha must be a non-negative number")

        if (type(beta) not in [int, float] or beta < 0):
            raise TypeError("beta must be a non-negative number")

        # enable eager execution:
        tf.enable_eager_execution()

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta
        self.load_model()

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

    def load_model(self):
        '''creates the model used to calculate cost'''

        style_outputs = []
        content_outputs = []

        vgg = tf.keras.applications.VGG19(
            include_top=False,
        )

        for i, layer in enumerate(vgg.layers):
            if (i == 0):
                output = vgg.input
                continue
            if (type(layer) is tf.keras.layers.MaxPooling2D):
                layer = tf.keras.layers.AveragePooling2D(
                    pool_size=layer.pool_size,
                    strides=layer.strides,
                    padding=layer.padding,
                    name=layer.name,
                )
            output = layer(output)
            layer.trainable = False
            if (layer.name in self.style_layers):
                style_outputs.append(output)
            if (layer.name == self.content_layer):
                content_outputs.append(output)

        model_outputs = style_outputs + content_outputs

        self.model = tf.keras.models.Model(vgg.input, model_outputs)

    @staticmethod
    def gram_matrix(input_layer):
        '''calculates the gram matrix of a layer
        Args:
            input_layer - an instance of tf.Tensor or tf.Variable of
                shape (1, h, w, c)containing the layer output whose gram
                matrix should be calculated
        Returns: a tf.Tensor of shape (1, c, c) containing the gram matrix of
            input_layer
        '''

        if (tf.rank(input_layer).numpy() != 4):
            raise TypeError("input_layer must be a tensor of rank 4")

        # === way 1 - one checker wrong ===
        # a = input_layer
        # gram = tf.tensordot(a, a, [[0, 1, 2], [0, 1, 2]])

        # === way 2 ===
        channels = int(input_layer.shape[-1])
        a = tf.reshape(input_layer, [-1, channels])
        gram = tf.matmul(a, a, transpose_a=True)

        # normalize gram matrix
        n = tf.cast(input_layer.shape[1] * input_layer.shape[2], tf.float32)
        gram_normalized = gram / n

        return tf.expand_dims(gram_normalized, axis=0)
