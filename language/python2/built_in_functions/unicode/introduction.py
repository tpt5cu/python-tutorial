# https://docs.python.org/2/library/functions.html#sorted


import csv, os, io


def unicode_list():
    """
    If no optional parameters (e.g. encoding) are given, unicode() will return a unicode string instead of an 8-bit string like str(). However,
    methods that expect unicode will not accept such a returned object.
    """
    my_list = [1, 2, 'cat']
    u = unicode(my_list)
    print(type(u)) # <type 'unicode'>
    print(u) # [1, 2, 'cat']
    u = unicode(str(my_list), encoding='utf-8')
    print(type(u)) # <type 'unicode'>
    print(u) # [1, 2, 'cat']


def write_csv():
    """
    Why doesn't this work? This should go in io.open() as well
    """
    #my_list = unicode([1, 2, 'cat']) # Bad
    my_list = unicode(''.join(['1', '2', 'cat']), encoding='utf8')
    print(type(my_list)) # <type 'unicode'>
    print(my_list)
    with io.open(os.path.join(os.path.dirname(__file__), 'testcsv.csv'), 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(my_list)


if __name__ == '__main__':
    #unicode_list()
    write_csv()