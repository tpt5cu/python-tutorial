# https://docs.python.org/3/tutorial/floatingpoint.html#representation-error - Python floating point internals
# https://numpy.org/doc/1.18/reference/arrays.scalars.html#built-in-scalar-types


import numpy as np


def what_is_float():
    '''
    - Python's "float" type has 53 bits of precision
        - "Almost all machines today (November 2000) use IEEE-754 floating point arithmetic, and almost all platforms map Python floats to IEEE-754
          "double precision". 754 doubles contain 53 bits of precision"
        - However, when "float" is used as an arg/kwarg for the "dtype" parameter, it is equivalent to "np.float_". Confusing!
    - "np.float_" is an alias for a real underlying NumPy scalar type
        - The value of the alias depends on the operating system
            - On my system, "np.float_" creates an object whose class is "numpy.float64"
                - "np.int_" has the same precision as ...?
        - If I want some size other than those specified by the aliases, I'll have to use a class with an explicit size, e.g. np.int32
    - My system has numpy.float128 but not numpy.float96
    '''
    print(np.float_ is np.float64) # True
    scalar = np.float_(10)
    print(type(scalar)) # <class 'numpy.float64'>
    #scalar = np.float8(10)
    scalar = np.float16(10)
    print(type(scalar)) # <class 'numpy.float16'>
    scalar = np.float32(10)
    print(type(scalar)) # <class 'numpy.float32'>
    #scalar = np.float96(10) # AttributeError
    scalar = np.float128(10)


if __name__ == '__main__':
    what_is_float()
