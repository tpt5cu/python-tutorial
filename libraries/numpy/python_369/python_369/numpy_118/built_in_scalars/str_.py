

import numpy as np


def what_is_str():
    '''
    There are only four string-like attributes on the numpy object: str, str0, str_, and string_
    - The only interesting one is np.str_ because the others are just aliases
    '''
    # Show which types are aliases
    print(np.string_ is np.bytes_) # True
    print(np.str0 is np.str_) # True
    print(np.str is str) # True
    print(np.str_) # <class 'numpy.str_'>
    # Show that dtype objects are not singletons
    ary1 = np.array(1, dtype=str)
    print(type(ary1.dtype)) # <class 'numpy.dtype'>
    print(ary1.dtype) # <U21
    print(ary1.dtype.type) # <class 'numpy.str_'>
    ary2 = np.array(1, dtype=np.str_)
    print(ary2.dtype) # <U21
    print(ary1.dtype is ary2.dtype) # False
    print(ary1.dtype == ary2.dtype) # True
    ary3 = np.array('foobar', np.str_)
    print(ary3.dtype) # <U6
    print(ary1.dtype == ary3.dtype) # False


if __name__ == '__main__':
    what_is_str()
