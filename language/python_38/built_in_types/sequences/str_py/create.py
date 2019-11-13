# https://realpython.com/python-string-formatting/
# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals


# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme


'''
Strings are immutable sequences of Unicode code points
- In Python 3, str is always the Unicode type
- Recall that a Unicode code point is simply a number that is given special meaning by Unicode
'''


def string_interpolation():
    '''
    String interpolation, aka f-strings, only exist in Python 3
    - Arbitrary Python expressions can be embedded within f-strings
    - string interpolation can also use format
    '''
    name = 'Austin'
    print(f'Hello there, {name}') # Hello there, Austin
    print(f'There are {365 * 24 * 60 * 60} seconds in a year!') # There are 31536000 seconds in a year!
    print(f'There are {365 * 24 * 60 * 60:e} seconds in a year!') # There are 3.153600e+07 seconds in a year!
    print(f'There are {365 * 24 * 60 * 60:.2f} seconds in a year!') # There are 31536000.00 seconds in a year!




if __name__ == '__main__':
    string_interpolation()