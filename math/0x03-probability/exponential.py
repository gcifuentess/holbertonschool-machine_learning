#!/usr/bin/env python3
'''exponential distribution module'''


class Exponential:
    '''Exponential distribution class'''

    def __init__(self, data=None, lambtha=1.):
        '''Constructor
        Args:
            data: is a list of the data to be used to estimate the distribution
            lambtha: is the expected number of occurences in a given time frame
        '''

        self.data = data
        if self.data is None:
            self.lambtha = lambtha
        else:
            self.lambtha = 1 / (sum(self.data) / len(self.data))

    @property
    def lambtha(self):
        '''lambtha getter'''
        return self.__lambtha

    @lambtha.setter
    def lambtha(self, value):
        '''lambtha setter'''
        if value > 0:
            self.__lambtha = float(value)
        else:
            raise ValueError("lambtha must be a positive value")

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

    def pdf(self, x):
        '''Calculates the value of the PDF for a given number of successes
        Args:
            x: the time period

        Returns: the PDF value for x
        '''
        e = 2.7182818285
        if x < 0:
            return 0
        return self.lambtha * e ** (-1 * self.lambtha * x)

    def cdf(self, x):
        '''Calculates the value of the CDF for a given number of successes
        Args:
            x: the time period

        Returns: the PDF value for x
        '''

        e = 2.7182818285
        if x < 0:
            return 0
        return (1 - e ** (-1 * self.lambtha * x))
