# https://numpy.org/doc/1.18/reference/arrays.dtypes.html


import numpy as np


'''
A NumPy dtype object encapsulates several attributes that describe how the bytes in a fixed-size block of memory corresponding to an array item should
be interpreted:
- Type of data: a NumPy scalar type, a NumPy object type, some other Python object, etc.
- Size of the data
- Byte order (little or big endian)
- Additional attributes depending on if the data is a structured (i.e. composite) data type

dtype quick reference:
- Types
    - "U": unicode string
    - "u": unsigned integer
    - "i": signed integer
    - "?": boolean
- Byte order
    - "<": little-endian byte order
    - ">": big-endian byte order
    - "=": hardware-native byte order (default)
- Every dtype has a size measured in a number of bytes
        - E.g. "i4" is a 32-bit signed integer
        - E.g. "U25" is a 25-character unicode string
'''


def create_dtype_from_scalar_type():
    '''
    All 24 scalar types and their subclasses can be used to create an associated dtype object
    - The results below show the attributes of scalar types and dtype objects have some, but not all, values in common
    '''
    my_dtype = np.dtype(np.int64)
    print(type(my_dtype)) # <class 'numpy.dtype'>
    print(repr(my_dtype)) # dtype('int64')
    print(str(my_dtype)) # int64
    #print(dir(np.int64))
    #['T', '__abs__', '__add__', '__and__', '__array__', '__array_interface__', '__array_priority__', '__array_struct__', '__array_wrap__', '__bool__',
    #'__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__',
    #'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__',
    #'__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__',
    #'__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__',
    #'__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
    #'__truediv__', '__xor__', 'all', 'any', 'argmax', 'argmin', 'argsort', 'astype', 'base', 'byteswap', 'choose', 'clip', 'compress', 'conj',
    #'conjugate', 'copy', 'cumprod', 'cumsum', 'data', 'denominator', 'diagonal', 'dtype', 'dump', 'dumps', 'fill', 'flags', 'flat', 'flatten',
    #'getfield', 'imag', 'item', 'itemset', 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'numerator', 'prod',
    #'ptp', 'put', 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield', 'setflags', 'shape', 'size', 'sort',
    #'squeeze', 'std', 'strides', 'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view']
    #print(dir(my_dtype))
    # ['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
    # '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    # '__repr__', '__rmul__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'alignment', 'base', 'byteorder', 'char',
    # 'descr', 'fields', 'flags', 'hasobject', 'isalignedstruct', 'isbuiltin', 'isnative', 'itemsize', 'kind', 'metadata', 'name', 'names', 'ndim',
    # 'newbyteorder', 'num', 'shape', 'str', 'subdtype', 'type']


def create_custom_dtype():
    '''
    This syntax is the "[(<field name>, <field dtype>, [<field shape>]), ...]" syntax
    - <field_name> can be any string
    - <field shape> is needed if the overall dtype is intended to be an array where each element has a type of <field dtype> 
    - <field_dtype> ::= <data type character>[<size in bytes>]
        - <size in bytes> is restricted depending on the <data type character>
            - E.g. "U25" is fine because it is a 25-character unicode string
            - E.g. "i7" is rejected because it doesn't make sense to have an integer with 56 bits
    '''
    dt = np.dtype([('foo', 'i8'), ('bar', 'M')])
    print(dt) # [('foo', '<i8'), ('bar', '<M8')]


if __name__ == '__main__':
    #create_dtype_from_scalar_type()
    create_custom_dtype()
