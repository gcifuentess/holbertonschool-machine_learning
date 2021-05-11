#!/usr/bin/env python3
'''Deep Neural Network module'''
import numpy as np


class DeepNeuralNetwork():
    '''defines a deep neural network performing binary classification'''

    def __init__(self, nx, layers):
        '''Deep Neuron Network constructor
        Args:
            nx: is the number of input features to the neuron
            layers: is a list representing the number of nodes in each layer
                    of the network.
                    - The first value in layers represents the number of nodes
                      in the first layer, …
        '''
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        l_prev = nx
        for i, nodes in enumerate(layers):
            if type(nodes) is not int or nodes <= 0:
                raise TypeError("layers must be a list of positive integers")
            if i > 0:
                l_prev = layers[i - 1]
            # initialize weights using He et al method:
            self.weights['W{}'.format(i + 1)] = (np.random.randn(nodes,
                                                                 l_prev)
                                                 * np.sqrt(2 / l_prev))
            # initialize biases:
            self.weights['b{}'.format(i + 1)] = np.zeros((nodes, 1))

    @property
    def L(self):
        '''L getter'''
        return self.__L

    @property
    def cache(self):
        '''cache getter'''
        return self.__cache

    @property
    def weights(self):
        '''weights getter'''
        return self.__weights

    def forward_prop(self, X):
        '''Calculates the forward propagation of the neural network
        Args:
            X: is a numpy.ndarray with shape (nx, m) that contains
               the input data.
               - nx is the number of input features to the neuron
               - m is the number of examples
        Return: the output of the neural network and the cache, respectively
        '''
        self.cache['A0'] = X
        for i in range(1, self.L + 1):
            W = self.weights['W{}'.format(i)]
            b = self.weights['b{}'.format(i)]
            A = self.cache['A{}'.format(i - 1)]
            Z = np.matmul(W, A) + b
            #  Forwar propagation with sigmoid activation function:
            self.cache['A{}'.format(i)] = 1 / (1 + np.exp(-Z))
        return self.cache['A{}'.format(i)], self.cache

    def cost(self, Y, A):
        '''Calculates the cost of the model using logistic regression
        Args:
            Y: a numpy.ndarray with shape (1, m) that contains the correct
               labels for the input data
            A: a numpy.ndarray with shape (1, m) containing the activated
               output of the neuron for each example
        Return: the cost
        '''
        part_A = Y * np.log(A)
        part_B = (1 - Y) * np.log(1.0000001 - A)
        return float((-1 / Y.shape[1]) * np.sum(part_A + part_B))

    def evaluate(self, X, Y):
        '''Evaluates the neural network’s predictions
        Args:
            X: is a numpy.ndarray with shape (nx, m) that contains
               the input data.
               - nx is the number of input features to the neuron
               - m is the number of examples
            Y: is a numpy.ndarray with shape (1, m) that contains
               the correct labels for the input data
        Return: the neuron’s prediction and the cost of the network
            - The prediction is a numpy.ndarray with shape (1, m)
              containing the predicted labels for each example
            - The label values are 1 if the output of the network
              is >= 0.5 and 0 otherwise
        '''
        A, cache = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.zeros((1, Y.shape[1]), dtype=int)
        prediction[A >= 0.5] = 1
        return prediction, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        '''Calculates one pass of gradient descent on the neural network
        Args:
            Y: is a numpy.ndarray with shape (1, m) that contains
               the correct labels for the input data
            cache: is a dictionary containing all the intermediary values
                   of the network
            alpha: is the learning rate
        Description: Updates the private attribute __weights
        Return: Nothing
        '''
        m = Y.shape[1]
        len_cache = len(cache)

        # learning for the last layer:
        Al = cache['A{}'.format(len_cache - 1)]  # last A
        A_prev = cache['A{}'.format(len_cache - 2)]  # pre last A
        dZl = Al - Y  # last dZ
        dWl = np.matmul(dZl, A_prev.T) / m  # last dW, shape (1, nodes)
        dbl = (1 / m) * np.sum(dZl, axis=1, keepdims=True)
        Wl_str = 'W{}'.format(len_cache - 1)
        Wl = self.weights[Wl_str]  # last W
        self.weights[Wl_str] = Wl - alpha * dWl  # last layer W learning
        bl_str = 'b{}'.format(len_cache - 1)
        bl = self.weights[bl_str]  # last b
        self.weights[bl_str] = bl - alpha * dbl  # last layer b learning

        #  next: learning for the rest of the layers:
        dZ = dZl
        W_next = Wl
        for i in reversed(range(1, len_cache - 1)):
            A = self.cache['A{}'.format(i)]
            A_prev = self.cache['A{}'.format(i - 1)]
            dZ = np.matmul(W_next.T, dZ) * (A * (1 - A))
            dW = (1 / m) * (np.matmul(dZ, A_prev.T))
            db = np.sum(dZ, axis=1, keepdims=True) / m
            W_c_str = 'W{}'.format(i)
            W_c = self.weights[W_c_str]  # current W
            b_c_str = 'b{}'.format(i)
            b_c = self.weights[b_c_str]  # current b
            self.weights[W_c_str] = W_c - alpha * dW
            self.weights[b_c_str] = b_c - alpha * db
            W_next = W_c

    def train(self, X, Y, iterations=5000, alpha=0.05):
        '''Trains the neural network
        Args:
            X: is a numpy.ndarray with shape (nx, m) that contains
               the input data.
               - nx is the number of input features to the neuron
               - m is the number of examples
            Y: is a numpy.ndarray with shape (1, m) that contains
               the correct labels for the input data
            iterations: is the number of iterations to train over
            alpha: is the learning rate
        Description: Updates the private attribute __weights and __cache
        Return: the evaluation of the training data after iterations
                of training have occurred
        '''
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations < 1:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        Al, cache = self.forward_prop(X)
        for i in range(iterations):
            self.gradient_descent(Y, cache, alpha)
            Al, cache = self.forward_prop(X)
        return self.evaluate(X, Y)
