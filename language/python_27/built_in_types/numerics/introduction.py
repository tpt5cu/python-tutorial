# https://docs.python.org/2.7/reference/datamodel.html#the-standard-type-hierarchy - section on numerics


import numbers


def numeric_types():
    '''There are 3 numeric types in Python: integral, real, and complex. All 3 types inherit from the abstract class numbers.Number'''
    print(isinstance(3, numbers.Number)) # True
    print(isinstance(3.1, numbers.Number)) # True
    print(isinstance(7 + 3j, numbers.Number)) # True


if __name__ == "__main__":
    numeric_types()