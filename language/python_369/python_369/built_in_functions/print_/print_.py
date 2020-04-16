# https://docs.python.org/3.6/library/functions.html#print - print documentation
# http://www.macfreek.nl/memory/Encoding_of_Python_stdout
# https://stackoverflow.com/questions/492483/setting-the-correct-encoding-when-piping-stdout-in-python


import sys, pathlib


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
    list_ = [1, 2, 'hello world', '29.5']
    print(*list_, sep=',')
    

def print_to_file():
    '''
    - Using print() with the "file" kwarg might seem like a good idea, but the output is really sloppy (e.g. list brackets are printed)
        - Fortunately, I can unpack a list and control the separator to get around this (see above)
    - By default, print() is invoked with file=sys.stdout
    '''
    file_path = (pathlib.Path(__file__).parent / 'output.txt').resolve()
    file_ = open(file_path, 'w')
    print('Hello World', file=file_)
    list_ = [1, 2, '3', 'four']
    print(list_, file=file_)
    print(*list_, sep=',', file=file_)
    file_.close()


if __name__ == '__main__':
    #view_encoding()
    #print_unicode()
    #print_decoded_bytes
    #avoid_newline()
    control_separator()
    #print_to_file()
