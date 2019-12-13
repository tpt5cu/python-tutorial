# -*- coding: UTF-8 -*-

# https://docs.python.org/2.4/lib/standard-encodings.html - encodings for fun


import io, sys, os


#print(sys.getdefaultencoding()) # ascii


def store_same_text_in_different_unicode_encodings():
    '''
    The bits that are stored in both files encode the SAME Unicode code points. It's just that the UTF-32 encoding uses 4 bytes per code point, so the
    UTF-32 encoded file is larger.
    '''
    unicode_text = unicode(text)
    with io.open(os.path.join(os.path.dirname(__file__), 'utf8.txt'), 'w', encoding='utf8') as f:
        f.write(unicode_text)
    with io.open(os.path.join(os.path.dirname(__file__), 'utf16.txt'), 'w', encoding='utf16') as f:
        f.write(unicode_text)
    with io.open(os.path.join(os.path.dirname(__file__), 'utf32.txt'), 'w', encoding='utf32') as f:
        f.write(unicode_text)


if __name__ == '__main__':
    encode_unicode_string()
    #store_same_text_in_different_unicode_encodings()