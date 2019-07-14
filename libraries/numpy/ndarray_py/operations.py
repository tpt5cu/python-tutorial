import numpy as np


def type_check():
    ary = np.array([1, 1, 1])
    print(isinstance(ary, np.ndarray)) # True


def subtraction():
    """Subtraction is done element-wise. If two ndarrays have different dimensions, a ValueError is raised. The exception is ndarray and scalar subtraction."""
    # Element-wise subtraction
    minuends = np.array([5, 5, 5])
    subtrahends = np.array([2, 2, 2])
    differences = minuends - subtrahends
    print(differences) # [3, 3, 3]
    print(type(differences)) # <type 'numpy.ndarray'>
    # Incompatible shapes
    #minuends = np.array([2, 2, 2])
    #subtrahends = np.array([11, 6])
    #differences = minuends - subtrahends
    #print(differences)
    # ndarray and scalar
    minuends = np.array([6, 6, 6])
    print(minuends - 12) # [-6, -6, -6]


def absolute_deviation():
    """numpy.absolute() calculates the absolute values of every element in an ndarray."""
    data = np.array([5, 5, 5])
    mean = np.array([1, 1, 1])
    absolute_values = np.absolute(mean - data)
    print(absolute_values) # [4, 4, 4]
    print(np.sum(absolute_values)) # 12
    print(type(absolute_deviation)) # <type 'numpy.ndarray'>


if __name__ == "__main__":
    #type_check()
    subtraction()
    #absolute_deviation()