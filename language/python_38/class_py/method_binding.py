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

    get_age = just_a_function

    #def get_age(self):
    #    return "You can't ask a woman her age!"

    #@classmethod
    #def say_hello(cls):
    #    return cls.greeting


def unbound_method_vs_function():
    '''
    In Python 2, when is accessed through a class instance (it does not necessarily have to be defined within a class statement), it is TRANSFORMED
    into a unbound method. What can an unbound method do that a function cannot? It can:
    - 
    '''
    # Python 2: <unbound method Girl.get_age>
    # Python 3: <function Girl.get_age at ...>
    print(Girl.get_age)
    # Python 2 and 3: <function just_a_function at ...>
    print(Girl.__dict__['get_age'])





def examine_method_binding():
    # Python 3 does not have unbound methods. Hence, while this would be an unbound method in Python 2, it is simply a function in Python 3
    # - Recall that an unbound method is ...
    print(Girl.get_age) # <function Girl.get_age at 0x101403950>
    # - In Python 2, say_hello() is bound to type.
    # - In Python 3, say_hello() is bound to Girl.
    print(Girl.say_hello) # <bound method Girl.say_hello of <class '__main__.Girl'>>
    print(Girl.say_hello()) # Hi there!
    g = Girl(32, 'Tracy')
    print(g.get_age) # <bound method Girl.get_age of <__main__.Girl object at 0x10b46b650>>


if __name__ == '__main__':
    unbound_method_vs_function()
    #examine_method_binding()