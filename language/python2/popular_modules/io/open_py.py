# https://docs.python.org/2/library/io.html
# https://stackoverflow.com/questions/33891373/difference-between-io-open-vs-open-in-python


import io


def io_open_identity():
    """
    io.open is identical to open is False for Python 2, but True for Python 3 as expected.
    - In Python 3, both file objects are instances of <class '_io.TextIOWrapper'>
    """
    print(io.open is open)
    with open('test.txt', 'w') as f:
        print(type(f)) # <type 'file'>
    with io.open('test.txt', 'w') as f:
        print(type(f)) # <type '_io.TextIOWrapper'>


if __name__ == "__main__":
    io_open_identity()