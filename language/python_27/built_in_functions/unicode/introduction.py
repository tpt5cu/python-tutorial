# https://docs.python.org/2/library/functions.html#unicode
# https://stackoverflow.com/questions/1207457/convert-a-unicode-string-to-a-string-in-python-containing-extra-symbols


import csv, os, io


def unicode_list():
    """
    If no optional parameters (e.g. encoding) are given, unicode() will return a unicode string instead of an 8-bit string like str().
    """
    my_list = [1, 2, 'cat']
    u = unicode(my_list)
    print(type(u)) # <type 'unicode'>
    print(u) # [1, 2, 'cat']
    u = unicode(str(my_list), encoding='utf-8')
    print(type(u)) # <type 'unicode'>
    print(u) # [1, 2, 'cat']


if __name__ == '__main__':
    unicode_list()