# -*- coding: UTF-8 -*-

# https://docs.python.org/2/library/csv.html
# https://stackoverflow.com/questions/18449233/2-7-csv-module-wants-unicode-but-doesnt-want-unicode - the whole csv with unicode mess. It is possible
# to write Unicode-encoded bytes to a file, but custom classes are required (see examples)


import os, csv, io


filepath = os.path.join(os.path.dirname(__file__), 'my-csv.csv')
data = [
    [6, 2345, 7, 2345, 234],
    [15, 15, 456, 347, 1234],
    [46, 4, 45, 67, 2, 45, 35],
    [7, 87, 65, 872, 5, 5637, 34]
]


def basic_write():
    '''This is the simplest way to write with a csv writer. writerows() must get a sequence of sequences, not just a 1D sequence'''
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def examine_excel_dialect():
    '''
    There are different CSV dialects across applications because there is no single CSV standard. A dialect is simply a grouping of certain format
    parameters. Examples of format parameters include the delimiter (defaults to ',') and how double quotes (') that appear inside data fields should
    be handled.
    - The only built-in dialects on my machine appear to be 'excel-tab' and 'excel'
    '''
    print(csv.list_dialects()) # ['excel-tab', 'excel']
    print(dir(csv.excel)) # delimiter, doublequote, etc.
    print(csv.excel.delimiter) # ','


def write_header():
    '''
    Only csv.DictWriter (as opposed to csv.writer) has writeheader() method. To write a header row with csv.writer, just use the regular methods
    '''
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        header = ['Header1', 'Header2', 'Header 3', 'Header 4', 'Header5']
        writer.writerow(header)
        writer.writerows(data)


def write_strings():
    # This data behaves exactly as expected
    #data = [
    #    ['This', 'is', 'a', 'sentence', 'of', 'words', '.'],
    #    ['I', 'like', 'soft', 'cake', 'because', 'it's', 'subtle', '.'],
    #    ['Red', 'bananas', 'look', 'weird', '.']
    #]
    # This data is interpreted so that every character of a sentence is split into a csv datum! That's almost never what I want
    data = ["This is a sentence of words', 'I like soft cake because it's subtle"]
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def write_unicode():
    '''
    The CSV module does NOT support unicode. What does this mean? It means that:
    - I cannot use io.open() in 'w' mode, with or without the 'encoding' parameter
    - I can only use io.open() in 'wb' mode, which doesn't accept an 'encoding' parameter. 
        - Given that, if I try to write a unicode object anyway I could get a UnicodeDecodeError because the csv writer tries to encode the unicode
          object into ascii.
        - If I try to write a str object, csv writer will happily write the bytes to the file without trying to encode anything because it thinks
          the str object (i.e. a bunch of bytes) is already encoded properly
    - These limitations appear to exist in Python 3 as well, although I get slightly different errors
    '''
    u = 'aaaàçççñññ'; print(type(u)) # <type 'str'>
    #u = u'aaaàçççñññ'
    #print(type(u)) # <type 'unicode'>
    #u = u.encode('ascii') # UnicodeEncodeError
    with io.open(os.path.join(os.path.dirname(__file__), 'my-csv.csv'), 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(u) # Possible UnicodeEncodeError IF 'u' is a unicode object


def dict_writer():
    '''
    The beauty of a DictWriter is that 1) I can specify the order of the columns with ease and 2) it doesn't matter what order the data dictionaries
    are, because dictionaries are unordered!
    '''
    with open(filepath, 'w') as f:
        dw = csv.DictWriter(f, fieldnames=('name', 'age', 'favorite'), restval='None')
        dw.writeheader()
        dw.writerow({'name': 'Austin', 'age': 99, 'favorite': 'table'})
        dw.writerow({'favorite': True, 'name': 'Foo', 'age': -1})
        dw.writerow({'age': 5, 'name': 'Dude'})


if __name__ == '__main__':
    #basic_write()
    #examine_excel_dialect()
    #write_header()
    #write_strings()
    write_unicode()
    #dict_writer()