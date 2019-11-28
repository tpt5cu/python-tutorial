# https://docs.python.org/2/library/functions.html#locals


config = 'I\'m a global var'


def examine_local_symbol_table(name=None):
    '''The locals() dict is not read-only, but should be treated as such'''
    foo = 'fooey!'
    bar = 'you passed!'
    if name is not None:
        cat = 'cats are great pets'
    print(locals()) # {'foo': 'fooey!', 'bar': 'you passed!', 'name': None}


if __name__ == '__main__':
    '''This is in the global scope'''
    yoda = 'jedi master, I am'
    #examine_local_symbol_table()
    print(locals())
    #{
    #    '__builtins__': <module '__builtin__' (built-in)>,
    #    '__file__': '/Users/austinchang/tutorials/python/language/python_27/built_in_functions/locals_py.py',
    #    '__package__': None,
    #    'yoda': 'jedi master, I am',
    #    '__name__': '__main__',
    #    'examine_local_symbol_table': <function examine_local_symbol_table at 0x10c68b9d0>,
    #    'config': "I'm a global var",
    #    '__doc__': None
    #}