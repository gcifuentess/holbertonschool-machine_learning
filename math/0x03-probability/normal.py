#!/usr/bin/env python3
'''normal distribution module'''


class Normal():
    '''normal distribution class'''

    def __init__(self, data=None, mean=0., stddev=1.):
        '''Constructor
        Args:
            data: is a list of the data to be used to estimate the distribution
            mean: is the mean of the distribution
            stddev: is the standard deviation of the distribution
        '''

        self.data = data
        if data is None:
            self.mean = mean
            self.stddev = stddev
        else:
            self.mean = sum(data) / len(data)
            n = len(data)
            z = 0
            for i in range(n):
                z += (data[i] - self.mean) ** 2
            self.stddev = (z / n) ** (1 / 2)

    @property
    def data(self):
        '''data getter'''
        return self.__data

    @data.setter
    def data(self, dataset):
        '''data setter'''
        if dataset is None:
            pass
        elif type(dataset) is not list:
            raise TypeError("data must be a list")
        elif len(dataset) < 2:
            raise ValueError("data must contain multiple values")
        self.__data = dataset

    @property
    def mean(self):
        '''mean getter'''
        return self.__mean

    @mean.setter
    def mean(self, value):
        '''mean setter'''
        self.__mean = float(value)

    @property
    def stddev(self):
        '''stddev getter'''
        return self.__stddev

    @stddev.setter
    def stddev(self, value):
        '''stddev setter'''
        if value > 0:
            self.__stddev = float(value)
        else:
            raise ValueError("stddev must be a positive value")

    def z_score(self, x):
        '''Calculates the z-score of a given x-value
        Args:
            x: is the x-value
        Returns: the z-score of x
        '''
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        '''Calculates the x-value of a given z-score
        Args:
            z: is the z-score
        Returns: the x-value of z
        '''
        return (z * self.stddev) + self.mean
