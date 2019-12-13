# https://docs.python.org/2/library/functions.html#slice


def get_slice():
    '''
    The slice() function takes start, stop, step arguments. That's all! However, since slice() is a function, the arguments must be passed in like any
    other function. start and stop are REQUIRED arguments
    '''
    my_list = [1, 2, 3, 4, 5]
    # Wrong syntax for passing function arguments
    #my_slice = slice(1::2)
    # Wrong syntax again
    #my_slice = slice(1,,2)
    my_slice = slice(1, len(my_list), 2)
    print(my_list[my_slice]) # [2, 4]


def inspect_slice():
    '''
    <slice object>.indices(<len>) -> (<start>, <stop>, <stride>)
    - Assuming a sequence of length <len>, calculate the <start> and <stop> indices, and the <stride> length of the extended slice described by S. Out
      of bounds indices are clipped in a manner consistent with the handling of normal slices.
    - All indices() appears to do is return values that already exist as attributes on a slice object
        - <stop> == <stop> or <len>, whichever is smaller
    '''
    #print(slice.indices) # <method 'indices' of 'slice' objects>
    #print(slice.start) # <member 'start' of 'slice' objects>
    #print(slice.step) # <member 'step' of 'slice' objects>
    #print(slice.stop) # <member 'stop' of 'slice' objects>
    s = slice(0, 17, 7)
    #print(s.indices) # <built-in method indices of slice object at ...>
    print(s.start) # 0
    print(s.step) # 7
    print(s.stop) # 17
    print(s.indices(19)) # (0, 17, 7)


if __name__ == '__main__':
    #get_slice()
    inspect_slice()