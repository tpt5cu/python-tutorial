"""
https://docs.python.org/2/library/functions.html#reduce
"""


def sum_numbers():
    numbers = (1, 2, 3, 4, 5) # (n * (n + 1))/2
    # sum() is a built-in function
    my_sum = reduce(lambda x, y: x + y, numbers)
    print(my_sum)


def use_initializer():
    """
    reduce() takes an optional initial value which is placed before the elements in the iterable
    """
    # (3) is an expression that evaluates to the int 3, which is not iterable
    #num = (3)
    # (3,) is a tuple
    num = (3,)
    my_sum = reduce(lambda x, y: x + y, num, 5) # 3 + 5 = 8
    print(my_sum)


if __name__ == "__main__":
    #sum_numbers()
    use_initializer()