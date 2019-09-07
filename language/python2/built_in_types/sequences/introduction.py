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
- All mutalbe sequence types support all of the immutable operations and several additional ones:
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
    """A slice of a sequence always returns another sequence of the same type. Some also support stepped-slicing with [i:j:k]"""
    tup_s = ("good", "stuff", "in", "here")[1:3]
    print(type(tup_s)) # <type 'tuple'>
    print(tup_s) # ("stuff", "in")
    str_s = "This is the best sentence ever"[0::2]
    print(str_s) # Ti stebs etneee


if __name__ == "__main__":
    #length()
    slicing()