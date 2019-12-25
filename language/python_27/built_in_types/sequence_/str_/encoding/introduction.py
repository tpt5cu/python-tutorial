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


def unicode_to_str():
    '''
    There are many ways of doing this. Check the source. Note that regardless of the approach, one of two things must happen to convert a unicode
    object to a str object: 1) drop the unicode characters that cannot be encoded in extended ascii 2) replace those characters with something else
    '''
    a = u'aaaàçççñññ'
    print(type(a)) # <type 'unicode'>
    print(a) # aaaàçççñññ
    #print(len(a)) # 10
    # Use the 'replace' option to replace any non-encodable characters
    b = a.encode('ascii', 'replace')
    print(type(b)) # <type 'str'>
    print(b) # aaa???????
    print(len(b)) # 10
    # 63 is question mark in extended ascii, so the characters really are replaced
    print(ord(b[9])) # 63
    # Use the 'ignore' option to just remove any non-encodable characters
    b = a.encode('ascii', 'ignore')
    print(b) # aaa
    print(len(b)) # 3


def mix_unicode_and_str():
    '''unicode and str objects can be concatenated to form a unicode object'''
    s = b'hello' + u'world'
    print(type(s)) # <type 'unicode'>
    print(s) # helloworld


if __name__ == '__main__':
    #store_same_text_in_different_unicode_encodings()
    unicode_to_str()
    #mix_unicode_and_str()