# https://numpy.org/doc/1.18/reference/arrays.scalars.html#built-in-scalar-types


import numpy as np


def what_is_complex():
    '''
    - "np.complex_" is an alias for np.complex128 on my operating system
    - My system also has np.complex64 and np.complex256, but not np.complex192
    - I don't understand complex numbers so don't worry about it
    '''
    print(np.complex_ is np.complex64) # False
    print(np.complex_ is np.complex128) # True
    #print(np.complex_ is np.complex192) # AttributeError
    print(np.complex_ is np.complex256) # False
    cpx = np.complex_(3j)
    print(type(cpx)) # <class 'numpy.complex128'>


if __name__ == '__main__':
    what_is_complex()
