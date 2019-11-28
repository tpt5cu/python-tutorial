# https://www.python.org/dev/peps/pep-3135/ - official documentation of new super() syntax


'''
The new super() syntax is syntactic sugar, but it is useful because I don't have to hard-code the name of the class anymore
'''


# TODO: resume this after bound methods


class Sphere:

    def __init__(self, diameter):
        self._diameter = diameter

    def get_function_class(self):
        '''
        As of Python 3.0, every function has a __class__ attribute that contains the class object within which the function was defined
        - This attribute does not exist in Python 2, although the __class__ attribute on instance objects does exist
        '''
        return __class__

    def get_diameter(self):
        return self._diameter


class Gumball(Sphere):

    def __init__(self, diameter, flavor):
        '''super() is equivalent to super(__class__, self)'''
        #super(__class__, self).__init__(diameter)
        super().__init__(diameter)
        self.flavor = flavor

    def get_diameter(self):
        #return f'The diameter is {super(Gumball, self).get_diameter()}'
        return f'The diameter is {super().get_diameter()}'


def examine_class_of_function():
    '''I still don't know what <class 'method'> is'''
    s = Sphere(1.0)
    print(s.get_function_class()) # <class '__main__.Sphere'>
    print(s.get_function_class() is Sphere) # True
    print(s.get_function_class.__class__) # <class 'method'>
    print(s.get_function_class.__class__ is Sphere) # False


def use_super():
    g = Gumball(3.0, 'strawberry')
    print(g.get_diameter()) # The diameter is 3.0


if __name__ == '__main__':
    #examine_class_of_function()
    use_super()