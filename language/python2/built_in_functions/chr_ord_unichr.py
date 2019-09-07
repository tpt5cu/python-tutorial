# -*- coding: UTF-8 -*-

# https://stackoverflow.com/questions/12238307/declaring-encoding-in-python/12241076


def text_to_integer():
    """
    - ord() will return an integer whose value is the ascii code of a string argument
    - ord() will return an integer whose value is the Unicode code point of a unicode argument
    """
    print(ord("r")) # 114
    print(ord(u"r")) # 114
    #int("r") # ValueError
    #print(ord("ra")) # A string MUST have len() == 1
    print(ord(u"\u4e2d")) # 20013, or 中
    print("中")


def integer_to_bytestring():
    """chr() will return a string whose ascii code is the integer argument"""
    print(chr(97)) # a
    #print(chr(256)) # ValueError because ascii codes are [0, 255] inclusive


def integer_to_unicode():
    """unichr() will return a unicode object whose code point is the integer argument"""
    print(unichr(555)) # ȫ


if __name__ == "__main__":
    #text_to_integer()
    #integer_to_bytestring()
    integer_to_unicode()