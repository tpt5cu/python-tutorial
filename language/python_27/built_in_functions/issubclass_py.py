# https://stackoverflow.com/questions/8107313/isinstance-and-issubclass-return-conflicting-results


import numbers


def numbers_hierarchy():
    '''
    issubclass(<cls>, <cls info>) is strictly for checking if a class object is a subclass of another class object. It's different from isinstance()
    because isinstance() checks to see if an object is an instance of a class.
    '''
    # issubclass() requires that both arguments are class objects
    #print(issubclass(4, numbers.Number)) # TypeError
    #print(issubclass(int, 4)) # TypeError
    print(issubclass(int, numbers.Number)) # True


if __name__ == '__main__':
    numbers_hierarchy()