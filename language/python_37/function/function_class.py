class Sphere:

    def __init__(self, diameter):
        self._diameter = diameter

    def get_function_class(self):
        '''
        As of Python 3.0, every function has a __class__ attribute that contains the class object within which the function was defined
        - This attribute does not exist in Python 2, although the __class__ attribute on instance objects does exist
        '''
        return __class__


def examine_class_of_function():
    '''
    I still don't know what <class 'method'> is
    '''
    s = Sphere(1.0)
    print(s.get_function_class()) # <class '__main__.Sphere'>
    print(s.get_function_class() is Sphere) # True
    print(s.get_function_class.__class__) # <class 'method'>
    print(s.get_function_class.__class__ is Sphere) # False


if __name__ == '__main__':
    examine_class_of_function()