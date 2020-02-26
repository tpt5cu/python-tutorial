# https://stackoverflow.com/questions/9452775/converting-numpy-dtypes-to-native-python-types/11389998


import numpy as np


def int64_to_int():
    '''Is is really as simple as calling <ndarray>.tolist()? It appear so'''
    numbers = np.array([1, 2, 3, 4])
    print(type(numbers)) # <class 'numpy.ndarray'>
    print(numbers.dtype) # int64
    print(type(numbers[0])) # <class 'numpy.int64'>
    #numbers = numbers.item() # ValueError: can only convert an array of size 1 to a Python scalar
    numbers = numbers.tolist()
    print(type(numbers)) # <class 'list'>
    print(type(numbers[0])) # <class 'int'>


def float64_to_float():
    numbers = np.array([1.1, 2.2, 3.3, 4.4])
    print(type(numbers)) # <class 'numpy.ndarray'>
    print(numbers.dtype) # int64
    print(type(numbers[0])) # <class 'numpy.float64'>
    numbers = numbers.tolist()
    print(type(numbers)) # <class 'list'>
    print(type(numbers[0])) # <class 'float'>


if __name__ == '__main__':
    #int64_to_int()
    float64_to_float()