# https://stackoverflow.com/questions/8220801/how-to-use-timeit-module
# https://www.pythoncentral.io/time-a-python-function/

import timeit


def wrapper(func, *args, **kwargs):
    """This wrapper is needed to wrap a function with arguments so that it can be called by timeit"""
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def big_loop(num):
    for x in range(num):
        list = [x**4 for x in range(100)]


def my_timer():
    """Notice how I have to wrap my function and arguments before passing them to timeit."""
    wrapped = wrapper(big_loop, 10)
    print("Timer starts...")
    time = timeit.timeit(wrapped, number=1000)
    print("Timer ends.")
    print(time)


if __name__ == "__main__":
    my_timer()

