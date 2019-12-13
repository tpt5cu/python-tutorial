# https://www.pydanny.com/python-partials-are-fun.html
# https://stackoverflow.com/questions/17388438/python-functools-partial-efficiency - paritals are slow because 1) functools.partial merely forwards
# arguments to the original function and 2) function calls are expensive (functools.partial is adding an additional function call)
# https://github.com/dabeaz/python-cookbook/blob/master/src/9/defining_a_decorator_that_takes_an_optional_argument/example.py - partial with decorator
# example. It appears the partial is used to allow the explicit @logged() syntax. But is that useful? It's cool, but is it useful?


from functools import partial


'''
functools.partial creates a new version of a function, where the new version has some arguments filled in by default. This is useful if I need to
create 1000 slightly different versions of a single function. Neat!
- Partials can be used to implement decorators that take optional arguments. See decorator notes.
'''


def power(base, exponent):
    return base ** exponent


def square(base):
    '''This is the old, un-cool way'''
    return power(base, 2)


'''This is the new, cool way'''
cube = partial(power, exponent=3)
fourth_power = partial(power, exponent=4)


if __name__ == '__main__':
    # Boring
    print(power(5, 2)) # 25
    # Not DRY
    print(square(4)) # 16
    # Cool
    print(cube(2)) # 8
    print(fourth_power(5)) # 625
