# https://docs.python.org/2/library/timeit.html


import timeit


def oneline_tryexcept():
    print(timeit.timeit(setup='i = 5', stmt='try:\n getattr(i, "__cmp__")\nexcept:\n pass')) # 0.469642877579


if __name__ == '__main__':
    oneline_tryexcept()