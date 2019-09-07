# https://docs.python.org/2.7/reference/datamodel.html#objects-values-and-types - this document is huge, but it touches on immutability
# https://docs.python.org/2.7/glossary.html#term-hashable - hashable definition
# https://docs.python.org/2.7/reference/datamodel.html#object.__hash__ - relationship between __hash__, __eq__, and immutability


"""
Mutable types:
- Sequences
    - list
    - bytearray
- dict
- set

Immutable types:
- Sequences
    - str
    - unicode
    - tuple
- numbers.Number and all subclasses
- frozenset
"""


def object_identity():
    """
    Object identity is affected by whether an object is mutalbe or immutable.
    - When multiple variables are assigned to point to immutable objects, they may return a refernce to the exact same immutable object in memory.
      When and if this is the case is implementation-dependent. This is allowed because it is memory-efficient.
    - When multiple variables are assigned to point to mutable objects, they will absolutely never point to the same object in memory
    """
    a = 1
    b = 1
    print(id(a) == id(b)) # True
    a = 34560090.1
    b = 34560090.1
    print(id(a) == id(b)) # True
    a = []
    b = []
    print(id(a) == id(b)) # False


"""See hash_py.py notes for how immutability affects hashing"""


if __name__ == "__main__":
    object_identity()