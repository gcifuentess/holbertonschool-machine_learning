#!/usr/bin/env python3
'''poisson distribution module'''


class Poisson():
    '''Poisson distribution function class'''

    def __init__(self, data=None, lambtha=1.):
        '''Constructor
        @data: is a list of the data to be used to estimate the distribution
        @lambtha: is the expected number of occurences in a given time frame
        '''

        self.data = data
        if self.data is None:
            self.lambtha = lambtha
        else:
            self.lambtha = sum(self.data) / len(self.data)

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
