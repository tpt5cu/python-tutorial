"""
https://realpython.com/python-for-loop/
https://stackoverflow.com/questions/818828/is-it-possible-to-implement-a-python-for-range-loop-without-an-iterator-variable
"""

def iterate_with_value():
    """ This is the most basic form of iteration that Python implements """
    for x in range(10):
        print(x)


def iterate_without_index():
    """ There is no easy built-in way of iterating in Python without some index value """
    pass


if __name__ == "__main__":
    iterate_with_value()