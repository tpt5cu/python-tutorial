# https://docs.python.org/3.7/library/stdtypes.html#string-methods


def mix_unicode_and_str():
    '''unicode and str objects cannot be concatenated'''
    s = b'hello' + u'world' # TypeError: can't concat str to bytes


if __name__ == '__main__':
    mix_unicode_and_str()