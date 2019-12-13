# -*- coding: UTF-8 -*-


# http://www.macfreek.nl/memory/Encoding_of_Python_stdout
# https://stackoverflow.com/questions/492483/setting-the-correct-encoding-when-piping-stdout-in-python


import sys


'''Simply printing Unicode isn't difficult in Python 2. Piping Unicode between processes is another story'''


def view_encoding():
    print(sys.stdout.encoding) # UTF-8


def print_decoded_bytes():
    '''
    In order for Python 2 to even use a non-ASCII encoding, the encoding must be declared at the top of the file
    - Once the encoding has been properly declared, Python can decode bytes into the correct Unicode code points
        - print() will work in the terminal and when the file is run as a script
    '''
    str_ = 'éééaéé[ ééé' # SyntaxError: Non-ASCII character ... but no encoding declared
    print(str_) # éééaéé[ ééé
    # The é is encoded as two bytes in UTF-8 (0xC3 0xA9). str_[0] only returns the first byte, which isn't in itself a valid encoding in UTF-8. That's
    # why the � character is printed
    print(str_[0]) # �
    print(str_[0:2]) # é


def print_unicode():
    '''Unicode objects are also printed just fine. A custom decoding will overwrite the default encoding declared at the top of the file'''
    str_ = 'éééaéé[ ééé'
    u = str_.decode('utf-8')
    print(type(u)) # <type 'unicode'>
    print(u) # éééaéé[ ééé
    print(u[0]) # é
    # The bytes are the exact same, it's just that the decoding is different
    u = str_.decode('hkscs')
    print(type(u)) # <type 'unicode'>
    print(u) # 矇矇矇a矇矇[ 矇矇矇


if __name__ == '__main__':
    #view_encoding()
    print_decoded_bytes()
    #print_unicode()