

"""
In Python 2, map() returns a list. In Python 3, map() returns a generator. THIS IS IMPORTANT FOR MATPLOTLIB.
"""


def divide_list_elements():
    my_list = [2, 4, 6, 8, 10, 12]
    divided = map(lambda x: x / 2, my_list)
    print(type(divided)) # <type 'list'>
    print(divided) # [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    divide_list_elements()