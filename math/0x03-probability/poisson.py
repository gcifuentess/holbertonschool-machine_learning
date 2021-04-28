#!/usr/bin/env python3
'''poisson distribution module'''


class Poisson():
    '''Poisson distribution function class'''

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

    def pmf(self, k):
        '''Calculates the value of the PMF for a given number of successes
        Args:
            k: is the number of “successes”. if out of range, return 0

        Returns: PMF value for k
        '''
        e = 2.7182818285
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        x = k
        for i in reversed(range(1, k)):
            x *= i
        return ((e ** -self.lambtha) * (self.lambtha ** k)) / x

    def cdf(self, k):
        '''Calculates the value of the CDF for a given number of successes
        Args:
            k: is the number of “successes”. if out of range, return 0
        Returns: CDF value for k
        '''
        e = 2.7182818285
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0

        z = 0
        for i in range(floor(k) + 1):
            x = i
            if i == 0:
                x = 1
            else:
                for j in reversed(range(1, i)):
                    x *= j
            z += (self.lambtha ** i) / x
        return (e ** -self.lambtha) * z


def floor(number):
    '''Gives as output the greatest integer less than or equal to number
    Args:
        number: any Real number
    Returns: the floor number
             -For example,floor(2.4) = 2
    '''
    return int(number)
