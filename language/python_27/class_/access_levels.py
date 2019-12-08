# https://stackoverflow.com/questions/6930144/underscore-vs-double-underscore-with-variables-and-methods


'''TLDR: the single underscore convention is good enough'''


class MyClass(object):

    def __init__(self, name, age):
        '''
        A single underscore prefix indicates that an attribute or method is only intended for internal use. Modules in the same package (package-private),
        subclasses that are outside of the package (protected), and the general public should probably not use the variable.
        '''
        self._name = name # Convention to indicate that this is not part of the public interface
        self.__age = age # Performs name-mangling. Should be avoided because it's fragile


def use_myclass():
    o = MyClass('Dave', 33)
    print(o._name) # Dave
    #print(o.__age) # AttributeError
    print(o._MyClass__age) # 33


if __name__ == '__main__':
    use_myclass()