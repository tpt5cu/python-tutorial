# https://docs.python.org/3/library/base64.html


import base64


def encode_bytes():
    '''
    There appear to be two basic methods for encoding a base64 bytes-like object.
    - encodebytes() adds a trailing newline after every 76 characters AND at the end of the string
    - standard_b64encode() does not add any newlines
        - I like this one better
    '''
    bytes_ = b'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    x = base64.encodebytes(bytes_)
    print(type(x)) # <class 'bytes'>
    print(x) # b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXphYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5emFiY2Rl\nZmdoaWprbG1ub3BxcnN0dXZ3eHl6\n'
    y = base64.standard_b64encode(bytes_)
    print(y) # b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXphYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5emFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6'
    print(x == y) # False


if __name__ == '__main__':
    encode_bytes()
