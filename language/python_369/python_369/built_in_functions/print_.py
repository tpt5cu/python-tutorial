# http://www.macfreek.nl/memory/Encoding_of_Python_stdout
# https://stackoverflow.com/questions/492483/setting-the-correct-encoding-when-piping-stdout-in-python


import sys


def view_encoding():
    print(sys.stdout.encoding) # UTF-8


def print_unicode():
    '''
    Python 3 uses UTF-8 by default, so no encoding must be declared at the top of the file.
    - Unlike Python 2, printing a bytes object will NOT apply any decoding to the bytes
    '''
    # Rememer that str_ IS the unicode type in Python 3
    str_ = 'éééaéé[ ééé'
    print(str_) # éééaéé[ ééé
    print(str_[0]) # é
    b = bytes(str_, 'utf-8')
    print(b) # b'\xc3\xa9\xc3\xa9\xc3\xa9a\xc3\xa9\xc3\xa9[ \xc3\xa9\xc3\xa9\xc3\xa9'


def print_decoded_bytes():
    '''The only difference with Python 3 is that a bytes literal can only contain ASCII characters'''
    # The bytes are the exact same, it's just that the decoding is different
    b = b'\xc3\xa9\xc3\xa9\xc3\xa9a\xc3\xa9\xc3\xa9[ \xc3\xa9\xc3\xa9\xc3\xa9'
    str_ = b.decode('hkscs')
    print(type(str_)) # <class 'str'>
    print(str_) # 矇矇矇a矇矇[ 矇矇矇


def avoid_newline():
    '''print() automatically appends a newline to whatever is printed, unless the "end"="\n" default argument is overridden'''
    print('No newline here',end='')
    print('Hi there')
    print('Bye there')


def control_separator():
    print('These', 'Arguments', 'Will', 'Be', 'Concatenated', 'Into', 'A', 'Tuple', 'Because', 'All', 'Subsequent', 'Parameters', 'Are', 'Keyword', 'Parameters', sep='->')


if __name__ == '__main__':
    #view_encoding()
    #print_unicode()
    #print_decoded_bytes
    #avoid_newline()
    control_separator()
