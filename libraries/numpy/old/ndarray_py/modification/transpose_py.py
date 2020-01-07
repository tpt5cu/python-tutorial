"""
https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
"""


import numpy as np


def set_to_transpose():
    """
    <ndarray>.T (which is equivalent to <ndarray>.transpose()) returns a VIEW of the original array. Thus, setting an ndarray to be its tranposition
    indeed changes the original array. Fortunately, it seems that <ndarray>.T is calculated at invocation time, so I can get the original array back
    by getting the transpose of the transposition!
    """
    data = [
        [50, 1, 6],
        [27, 45, 0],
        [1000, 19, 0.5],
        [1, 356.6, 8]
    ]
    ary = np.array(data)
    print(ary)
    print("")
    print(ary.T)
    print("")
    ary = ary.T
    print(ary)
    print("")
    print(ary.T)
    print("")


if __name__ == "__main__":
    set_to_transpose()