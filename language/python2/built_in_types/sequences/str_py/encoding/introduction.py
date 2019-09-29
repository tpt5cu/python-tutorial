# -*- coding: UTF-8 -*-

# http://kunststube.net/encoding/
# https://docs.python.org/2.4/lib/standard-encodings.html - encodings for fun


import io, sys, os


text = """
An encoding scheme is a mapping between a sequence of bits and a human understandable character, such as 'a', '1', or '['. An encoding scheme is
simply a mapping that can be used to either 1) encode characters into bytes or 2) decode bytes into characters
- To encode means to convert into a coded form, such as bytes. To encode text that is already in ascii, take each letter and substitute the
  corresponding sequence of bytes. 
    - ascii maps 8-bits to a character
- To decode means to convert from a coded form into something that's understandable by humans. To decode bytes into ascii, take each byte and
  substitute the corresponding character

One byte can represent a maximum of 256 values [0, 255]. That isn't sufficient for languages that contain more than 256 characters (e.g. Chinese).
There are encodings that use 2 bytes to rectify this problem (e.g. BIG-5), which can represent 65,536 characters! But that still wasn't enough, so
Unicode was created. So how many bits does Unicode use to encode a character? None! Unicode is not an encoding!

Unicode defines a table of 1,114,112 code points for characters (e.g. code point 65 stands for 'A'). 2 bytes wasn't enough for that many code points,
and 3 bytes is enough but is awkward to use, so 4 bytes is the comfortable minimum. But using 4 bytes for every character would waste a LOT of space!
To solve this, there are several ways to encode Unicode code points into bits (Yes, CODE POINTS are encoded into bits). 
- UTF-32 is an encoding that encodes all Unicode code points (into bits) using 4 bytes. It's easy to understand, but wastes a lot of space
- UTF-16 and UTF-8 are variable-length encodings.
    - In UTF-8, if a character CAN be represented in a single byte, it will be encoded in a single byte. If it requires 2 bytes, UTF-8 will use 2
      bytes, etc. UTF-8 has an elaborate system to use the highest bit in a byte to show how many bytes a character consists of. However, if these
      signal bits are used often, it can waste space
    - UTF-16 follows the same principles, but uses 2 bytes minimum per code-point-to-bytes encoding
Different Unicode encodings can create entirely different sequences of bits, depending on the characters that are being encoded. Thus, the choice
between UTF-8, UTF-16, and UTF-32 is based on space efficiency, not on which code points will or won't be encoded.
"""


def encode_unicode_string():
    """
    The default encoding is ascii in Python 2 and utf-8 in Python 3. In fact, the unicode string will cause the parser to throw an error without
    declaring an encoding in Python 2
    """
    print(sys.getdefaultencoding())
    string = 'éééaéé[ ééé'.decode('hkscs')
    print(string)


def store_same_text_in_different_unicode_encodings():
    """
    The bits that are stored in both files encode the SAME Unicode code points. It's just that the UTF-32 encoding uses 4 bytes per code point, so the
    UTF-32 encoded file is larger.
    """
    unicode_text = unicode(text)
    with io.open(os.path.join(os.path.dirname(__file__), 'utf8.txt'), 'w', encoding='utf8') as f:
        f.write(unicode_text)
    with io.open(os.path.join(os.path.dirname(__file__), 'utf16.txt'), 'w', encoding='utf16') as f:
        f.write(unicode_text)
    with io.open(os.path.join(os.path.dirname(__file__), 'utf32.txt'), 'w', encoding='utf32') as f:
        f.write(unicode_text)


if __name__ == "__main__":
    encode_unicode_string()
    #store_same_text_in_different_unicode_encodings()