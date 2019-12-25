# https://docs.python.org/3.7/library/csv.html


import csv, pathlib


'''
DictReader/reader always expects a file-like object as the first parameter, but a list of strs works too
- I guess they just expect something iterable that returns strs
'''


def read_unicode_csv():
    '''
    - A reader is iterable and must be consumed. Just creating a reader object doesn't consume anything
    - Just like a writer, a reader must be opend in text mode. It handles Unicode just fine
    '''
    path = (pathlib.Path(__file__).parent / 'my-csv.csv').resolve()
    #with open(path, 'rb') as f: # _csv.Error
    with open(path, 'r') as f: # _csv.Error
        rows = [r for r in csv.reader(f)]
    # There is indeed one row in the csv, so it return a list of one list
    print(rows) # [['a', 'a', 'a', 'à', 'ç', 'ç', 'ç', 'ñ', 'ñ', 'ñ']]


if __name__ == '__main__':
    read_unicode_csv()