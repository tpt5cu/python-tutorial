# https://stackoverflow.com/questions/3589311/get-defining-class-of-unbound-method-object-in-python-3/25959545#25959545
# https://stackoverflow.com/questions/11949808/what-is-the-difference-between-a-function-an-unbound-method-and-a-bound-method/11950331


def just_a_function():
    '''A function is created by a def statement or a lambda.'''
    print('You invoked just_a_function()')


class Girl(object):

    greeting = 'Hi there!'

    def __init__(self, age, name):
        self._age = age
        self._name = name

    girl_function = just_a_function

    def get_age(self):
        return "You can't ask a woman her age!"

    @classmethod
    def say_hello(cls):
        return cls.greeting


def unbound_method_vs_function():
    '''
    - In Python 2, when a function accessed through a class instance (it does not necessarily have to be defined within a class statement), it is
      TRANSFORMED into a unbound method. See python_27 function notes
    - In Python 3, there are no more unbound methods, just bound methods and functions
    '''
    # Python 2: <unbound method Girl.just_a_function>
    # Python 3: <function just_a_function at ...>
    print(Girl.girl_function)
    # Python 2 and 3: <function just_a_function at ...>
    print(Girl.__dict__['girl_function'])



def examine_method_binding():
    '''
    - Functions accessed on instance objects are bound the same way
    - Functions accessed on class objects are bound slightly differently, but I don't think it matters
    '''
    # Python 2: <unbound method Girl.get_age>
    # Python 3: <function Girl.get_age at ...>
    print(Girl.get_age)
    # - Python 2: <bound method type.say_hello of <class '__main__.Girl'>>
    # - Python 3: <bound method Girl.say_hello of <class '__main__.Girl'>>
    print(Girl.say_hello)
    print(Girl.say_hello()) # Hi there!
    g = Girl(32, 'Tracy')
    # Python 2: <bound method Girl.get_age of <__main__.Girl object at 0x108598d90>>
    # Python 3: <bound method Girl.get_age of <__main__.Girl object at 0x10d0f2810>>
    print(g.get_age)


if __name__ == '__main__':
    #unbound_method_vs_function()
    examine_method_binding()