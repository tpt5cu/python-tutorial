# https://docs.python.org/2.7/reference/datamodel.html#objects-values-and-types - The whole flippin data model
# https://docs.python.org/2/library/stdtypes.html - 


import numbers


"""
There are many, many types in Python. I must decide what the most important types are, and whether or not to classify a type as a "type" or an object
that follows a protocol. 

There are x basic catagories of types:
- Numerics: integral, float, complex
- Sequences: see notes
- Sets: set, frozenset
- Mappings: only dict

There are additional catagories of types that I don't consider as concrete as the other types:
- Callable objects
- Protocol based objects: iterator types, descriptor types




There are 7 basic catagories of types: numerics, sequences, mappings, files, classes, instances, and exceptions.
- Therefore, I shouldn't make a distinction between traditionally primitive types like int, str, bool and "objects" like lists, sets, etc. because
  that is not a valid distinction in Python.

Numeric types: int, float, long, complex
- bool is a subtype of int

Sequence types: str, unicode, list, tuple, bytearray, buffer, xrange
- range is NOT a sequence type
"""


def what():
    print(numbers.Number)
    print(type(numbers.Number))


if __name__ == "__main__":
    what()
