"""
https://www.b-list.org/weblog/2017/sep/05/how-python-does-unicode/
http://www.pgbovine.net/unicode-python.htm
https://nedbatchelder.com/text/unipain.html
https://pymotw.com/2/codecs/
https://stackoverflow.com/questions/2596714/why-does-python-print-unicode-characters-when-the-default-encoding-is-ascii
"""

""" The reason I have Unicode strings in web.py is because User.cu() returns a Unicode string.
Whenever a Unicode and byte string are joined, the result is always a Unicode string. 
Unicode uses code points (i.e. an integer that is mapped to a character), not bytes.
    - There are variations of Unicode. UTF-8 is one such variation. It uses 1 to 4 bytes to encode a code point. 
"""

""" This whole Unicode vs byte string distinction in Python 2 (and Python 3) is quite complex. I will need to come back to this later.
The most important thing is to 1) decode all str objects to unicode objects and work with unicode objects in Python 2) encode Unicode objects back to str before writing to an external file.

Python 3 has byte strings and Unicode strings, but the str name is always for Unicode strings. Byte strings get a 'b' prefix.
Python 3 does not allow implicit mixing of byte strings and Unicode strings, which is a good thing.

Python 2 also has byte strings and Unicode strings. The str name refers to a byte string. If a string lacks a prefix (e.g. it is a normal string literal), it is a byte string.
A byte string represents a sequence of bytes in some particular encoding, which defaults to ASCII. Thus, str is NOT a string, it is a sequence of bytes!
A Unicode string literal is prefixed with the 'u' character.
"""

def create_unicode_string():
    """ A Unicode string is interpreted as a sequence of code points. See source to understand how printing works
    """
    u = u"I'm a Unicode string \u03c0"
    print(type(u))
    print(u)

def create_byte_string():
    s = "I'm a byte string \u03c0"
    print(type(s))
    print(s)

def unicode_to_byte():
    """
    Use decode() to go from byte to unicode. Use encode() to go from unicode to byte.
    """
    s = "I'm a byte string"
    """
    The decode() function translates a sequence of bytes into a sequence of code points, and returns the sequence of code points as a <'unicode'> instance.
    The function assumes I know what I'm doing and that the bytes SHOULD be translated using whatever encoding I specify (e.g. "utf-8")
    """
    u = s.decode("utf-8")
    print(type(u))
    """
    The encode() function translates a sequence of code points into a sequence of bytes.
    """
    s = u.encode("utf-8")
    print(type(s))


def parse_unicode_string():
    """ When I pass Python strings to JavaScript, the little 'u' for unicode encoding messes things up and I need to get rid of it before the Python string gets passed to JavaScript.
    """
    dicts = [{'model': u'My demo cvr', 'name': u'ABEC Frank pre calib'}]
    print(dicts)
    for dict in dicts:
        dict['model'] = str(dict['model'])
    print(dicts)

if __name__ == "__main__":
    create_unicode_string()
    create_byte_string()
    #unicode_to_byte()
