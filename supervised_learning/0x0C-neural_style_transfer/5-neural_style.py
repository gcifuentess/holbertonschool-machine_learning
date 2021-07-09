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
        self.generate_features()

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
            size=[int(h * scale), int(w * scale)],
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
        a = input_layer

        if (not (isinstance(a, tf.Tensor) or isinstance(a, tf.Variable))
                or tf.rank(a).numpy() != 4):
            raise TypeError("input_layer must be a tensor of rank 4")

        # === way 1 ===
        gram = tf.tensordot(a, a, [[0, 1, 2], [0, 1, 2]])

        # === way 2 ===
        # channels = int(a.shape[-1])
        # a_ = tf.reshape(a, [-1, channels])
        # gram = tf.matmul(a_, a_, transpose_a=True)

        # normalize gram matrix
        n = tf.cast(a.shape[1] * a.shape[2], tf.float32)
        gram_normalized = gram / n

        return tf.expand_dims(gram_normalized, axis=0)

    def generate_features(self):
        '''extracts the features used to calculate neural style cost'''

        # Preprocess images
        # expects input in [0,1] so image is multiplied by 255
        p_style_image = tf.keras.applications.vgg19.preprocess_input(
            self.style_image * 255,
        )
        p_content_image = tf.keras.applications.vgg19.preprocess_input(
            self.content_image * 255,
        )

        n_style_layers = len(self.style_layers)
        style_features = self.model(p_style_image)[:n_style_layers]

        self.content_feature = self.model(p_content_image)[n_style_layers:][0]
        self.gram_style_features = [self.gram_matrix(style_feature)
                                    for style_feature in style_features]

    def layer_style_cost(self, style_output, gram_target):
        '''Calculates the style cost for a single layer
        Args:
            style_output - tf.Tensor of shape (1, h, w, c) containing the layer
                style output of the generated image
            gram_target - tf.Tensor of shape (1, c, c) the gram matrix of the
                target style output for that layer
        Returns: the layer’s style cost
        '''
        if (not (isinstance(style_output, tf.Tensor) or
                 isinstance(style_output, tf.Variable)) or
                tf.rank(style_output).numpy() != 4):
            raise TypeError("style_output must be a tensor of rank 4")

        channels = style_output.shape[-1]

        if (not (isinstance(gram_target, tf.Tensor) or
                 isinstance(gram_target, tf.Variable)) or
                tf.rank(gram_target).numpy() != 3 or
                gram_target.shape != (1, channels, channels)):
            raise TypeError("gram_target must be a tensor of "
                            "shape [1, {}, {}]".format(channels, channels))

        gram_style = self.gram_matrix(style_output)

        return tf.reduce_mean(tf.square(gram_style - gram_target))

    def style_cost(self, style_outputs):
        '''Calculates the style cost for generated image
        Args:
            style_outputs - a list of tf.Tensor style outputs for the
                generated image
        Returns: the style cost
        '''
        len_style_layers = len(self.style_layers)

        if (len(style_outputs) != len_style_layers):
            raise TypeError("style_outputs must be a list with a "
                            "length of {}".format(len_style_layers))

        weight = 1.0 / float(len_style_layers)
        weighted_layer_style_costs = []

        gram_targets = self.gram_style_features

        for i, s_output in enumerate(style_outputs):
            weighted_layer_style_costs.append(
                self.layer_style_cost(s_output, gram_targets[i]) * weight
            )

        return tf.add_n(weighted_layer_style_costs)
