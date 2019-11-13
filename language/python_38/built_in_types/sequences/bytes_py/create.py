# https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
# https://python-reference.readthedocs.io/en/latest/docs/str/escapes.html
# https://realpython.com/lessons/defining-literal-bytes-object/
# https://docs.python.org/2.4/lib/standard-encodings.html - encodings

# https://medium.com/better-programming/strings-unicode-and-bytes-in-python-3-everything-you-always-wanted-to-know-27dc02ff2686 - should I delete this?


'''
The new bytes type in Python 3 is roughly analogous to the Python 2 str type, but they have completely different methods, so I cannot swap them
'''


def create_bytes_literal():
    '''
    Only ASCII CHARACTERS can be a in a bytes literal, full stop. That means whenever I print a bytes literal, I will never see any character with a
    code point over 127
    '''
    strict_ascii = b'This is a bytes literal'
    print(type(strict_ascii)) # <class 'bytes'>
    print(strict_ascii[3]) # 115
    print(strict_ascii) # b'This is a bytes literal'
    #extended_ascii = b'A British beer is ÿ' # SyntaxError
    extended_ascii = b'A British beer is \xFF33.99'
    print(type(extended_ascii)) # <class 'bytes'>
    # A byte with a value of 255 corresponds to the ÿ in ISO 8859-1
    print(extended_ascii[18]) # 255
    print(extended_ascii) # b'A British beer is \xa33.99'


def create_bytes_object_with_length():
    '''Using the bytes built-in function will create a bytes object of the specified length, where each byte has a value of 0'''
    b = bytes(10)
    print(type(b)) # <class 'bytes'>
    print(len(b)) # 10
    print(b) # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'


def create_bytes_object_from_literal():
    '''I am creating a bytes object from a Unicode literal. This is completely different from directly creating a bytes literal'''
    #b = bytes('¡¢£¤¥¦', 'ascii') # UnicodeEncodeError
    b = bytes('¡¢£¤¥¦', 'latin_1')
    print(type(b)) # <class 'bytes'>
    print(len(b)) # 6
    print(b) # b'\xa1\xa2\xa3\xa4\xa5\xa6'
    for c in b:
        print(c) # 161\n162\n163\n164\n165\n166\n


if __name__ == '__main__':
    #create_bytes_literal()
    #create_bytes_object_with_length()
    create_bytes_object_from_literal()