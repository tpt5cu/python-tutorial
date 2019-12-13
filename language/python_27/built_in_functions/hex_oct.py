# https://stackoverflow.com/questions/11620151/what-do-numbers-starting-with-0-mean-in-python


from types import SimpleNamespace as sn


def get_hexadecimal_representation():
    print(hex(17)) # 0x11


def get_octal_representation():
    '''It's quirky but in Python 2 ONLY, oct() returns an old-style octal representation that is missing a 'o' or 'O' after the 0'''
    print(oct(17)) # 021
    #print(021 == 0o21) # True
    print(0O21 == 0o21) # True


class MyClass():

    def __index__(self):
        return 22


def get_representation_of_object():
    '''
    So long as an object defines an __index__() method that returns an integer, bin(), hex(), and oct() will all use that intger to return the
    appropriate representation
    - IDK why I can't do it with an anonymous object. Does it look up __index__ on the class itself?
    '''
    o = MyClass()
    print(oct(o)) # 0o26
    #o = sn()
    #o.__index__ = lambda self=o: 69
    #print(oct(o)) # TypeError: 'types.SimpleNamespace' object cannot be interpreted as an integer

    #setattr(sn, '__index__', lambda self=o: 69) # TypeError: can't set attributes of built-in/extension type 'types.SimpleNamespace'


if __name__ == '__main__':
    #get_hexadecimal_representation()
    #get_octal_representation()
    get_representation_of_object()