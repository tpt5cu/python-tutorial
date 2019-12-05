# https://docs.python.org/2.7/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange


"""
All (7) sequence types: str, unicode, list, tuple, bytearray, buffer, and xrange
- range is NOT a sequence type

All (3) immutable sequence types: str, unicode, tuple
- All immutable sequence types have the following operations:
    - "in", "not in" operators
    - concatentation via "<seq1> + <seq2>" operator
    - repetition via the "<seq> * <times>" operator
    - indexing via "<seq>[]" operator
    - slicing via "<seq>[:]" or "<seq>[::]" operators
    - len(<seq>)
    - min(<seq>), max(<seq>)
    - <seq>.index(<val>) returns the index of the first instance of <val>
    - <seq>.count(<val>)
    - comparison

All (2) mutable sequence types: list, bytearray
- All mutable sequence types support all of the immutable operations and several additional ones:
    - assignment via the above operators, e.g. "seq[<idx>] = <val>", "seq[:] = <val>", "<seq> *= <times>"
    - deletion via the above operators, e.g. "del "seq<idx>", "del seq[:]"
    - <seq>.append()
    - <seq>.extend()
    - <seq>.insert(), equivalent to "<seq>[:] = <val>"
    - <seq>.pop()
    - <seq>.remove(), equivalent to "del <seq>[<seq>.index(<val>)]"
    - <seq>.reverse()
    - <seq>.sort()

All (2) oddball sequence types: buffer, xrange
- a buffer is not an essential Python data structure
- xrange doesn't support [:], "+", or "*". Also, using min(), max(), "in", or "not in" on an xrange is inefficient
"""


def length():
    """
    Any sequence can have its length measured with len(). Other types (mappings, sets, etc.) can also have their length measured.
    """
    print(len("Nice string you got there")) # 25
    print(len(('w', 'x', 'y'))) # 3


def slicing():
    '''
    A slice of a sequence always returns another sequence of the same type. Slicing is always performed from left to right. There is no such thing as a
    reverse slice!
    - Slicing is [<inclusive>:<exclusive>]
    - Some also support stepped-slicing with [<start>:<stop>:<step>].
    '''
    tup_s = ("good", "stuff", "in", "here")[1:3]
    print(type(tup_s)) # <type 'tuple'>
    print(tup_s) # ("stuff", "in")
    str_s = "This is the best sentence ever"[0::2]
    print(str_s) # Ti stebs etneee
    print('hello'[0:3]) # hel


def negative_index_slicing():
    '''
    A negative index is located relative to the right end of the sequence
    - Exceeding the length of a sequence (either from the left or from the right) will not raise an Exception.
    - "-0" is equivalent to "0" for slicing purposes
    '''
    l = ['apple', 'banana', 'orange']
    # Think of negative indexes as starting from -1. Also remember that the right index is exclusive, but that's unrelated to whether the index is
    # negative or not
    print(l[0:-1]) # [0:-1] -> [0:len(l)-1] -> [0:3-1] -> [0:2] -> ['apple', 'banana']
    print(l[0:-2]) # [0:-2] -> [0:len(l)-2] -> [0:3-2] -> [0:1] -> ['apple']
    # Slice index is out of bounds, but interpeter doesn't care
    print(l[0:-30]) # [0:-30] -> [0:len(l)-30] -> [0:3-30] -> [0:-27] -> []
    # Right index is less than left index, so the slice must be empty
    print(l[-2:0]) # [-2:0] -> [1:0] -> []


def repetition():
    """Repetition does nothing for an empty sequence. The sequence must contain at least 1 value"""
    print([] * 20) # []
    print('' * 5) # ''
    print(() * 2) # ()
    print('a' * 3) # aaa


def unpack():
    '''In order to use unpacking syntax, an entire sequence must be unpacked at once. Also, whatever is being unpacked must also be iterable'''
    string = 'boomerang'
    #s, t = string # ValueError
    a, b, c, d, e, f, g, h, j = string
    print(a) # b
    print(b) # o
    x = None
    a, b = x # TypeError: 'NoneType' object is not iterable


if __name__ == "__main__":
    #length()
    #slicing()
    #negative_index_slicing()
    #repetition()
    unpack()