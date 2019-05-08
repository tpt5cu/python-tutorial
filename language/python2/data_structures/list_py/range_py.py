"""
The built-in range() function in Python2 returns a list of the specified size immediately upon invocation.
This is different from xrange(), which returns an xrange type. An xrange type is an iterable, but it is not an iterator. It is also not a generator.

range() can take 1, 2, or 3 arguments
"""

def print_numbers():
    """ Prints from 0-9 """
    for num in range(0, 10):
        print(num)

def print_with_step():
    """ Prints 0, 2, 4, 6, 8 """
    for num in range(0, 10, 2):
        print(num)

def print_backwards():
    for num in range(10, 0, -1):
        print(num)

if __name__ == "__main__":
    #print_numbers()
    #print_with_step()
    print_backwards()
