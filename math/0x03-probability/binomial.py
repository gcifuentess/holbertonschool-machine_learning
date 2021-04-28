#!/usr/bin/env python3
'''binomial distribution module'''


class Binomial():
    '''Binomial distribution class'''

    def __init__(self, data=None, n=1, p=0.5):
        '''Constructor
        Args:
            data: is a list of the data to be used to estimate the distribution
            n: is the number of Bernoulli trials
            p: is the probability of a success
        '''
        self.data = data
        if self.data is None:
            self.n = n
            self.p = p
        else:
            # Theorical:  mean = n * p, var = n * p * q and q = 1 - p
            len_data = len(self.data)
            mean = sum(self.data) / len_data
            z = 0
            for i in range(len_data):
                z += (self.data[i] - mean) ** 2
            var = z / len_data
            q = var / mean
            p = 1 - q
            self.n = round(mean / p)
            self.p = mean / self.n

    @property
    def n(self):
        '''n getter'''
        return self.__n

    @n.setter
    def n(self, value):
        '''n setter'''
        if value > 0:
            self.__n = int(value)
        else:
            raise ValueError("n must be a positive value")

    @property
    def p(self):
        '''p getter'''
        return self.__p

    @p.setter
    def p(self, value):
        '''p setter'''
        if value > 0 and value < 1:
            self.__p = float(value)
        else:
            raise ValueError("p must be greater than 0 and less than 1")

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
            k: is the number of successes
        Returns: the PMF value for k
        '''
        if k < 0:
            return 0

        factorial_n = self.n
        for i in reversed(range(1, self.n)):
            factorial_n *= i

        if k == 0:
            factorial_k = 1
        else:
            factorial_k = k
            for i in reversed(range(1, k)):
                factorial_k *= i

        factorial_n_k = (self.n - k)
        for i in reversed(range(1, (self.n - k))):
            factorial_n_k *= i

        bin_coef = factorial_n / (factorial_k * factorial_n_k)
        return (bin_coef * (self.p ** k) * ((1 - self.p) ** (self.n - k)))

    def cdf(self, k):
        '''Calculates the value of the CDF for a given number of successes
        Args:
            k: is the number of successes
        Returns: the CDF value for k
        '''
        # Hint:
        # https://www.itl.nist.gov/div898/handbook/eda/section3/eda366i.htm
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
