# https://stackoverflow.com/questions/15556813/python-why-cmp-is-useful


'''
- cmp() was removed in Python 3 because it isn't very useful
- cmp() returns -1, 0, or 1 if the first argument was less than, equal to, or greater than the second argument
'''


def compare_int_to_str():
    '''I think these comparisons are the way they are because "int" is lexicographically less than "str"'''
    print(cmp(1, '1')) # -1
    print(cmp(11, '1')) # -1


def compare_str_tuples():
    print(cmp(('Austin', 'Chang'), ('David', 'Chang'))) # -1
    print(cmp(('Cattle', 'Foo'), ('Gnat', 'Ardvark', 'Foo', 'Bar'))) # -1


def compare_list_to_file():
    '''What does this mean? 'list' comes after 'file' perhaps?'''
    f = file(__file__)
    l = []
    print(cmp(l, f)) # 1


if __name__ == '__main__':
    #compare_int_to_str()
    #compare_str_tuples()
    compare_list_to_file()