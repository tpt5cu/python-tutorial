# https://docs.python.org/2/library/timeit.html


import timeit


def oneline_tryexcept():
    print(timeit.timeit(setup='i = 5', stmt='try:\n getattr(i, "__cmp__")\nexcept:\n pass', number=1000000)) # 0.275973081589


if __name__ == '__main__':
    oneline_tryexcept()