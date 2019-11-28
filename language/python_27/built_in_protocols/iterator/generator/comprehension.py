# https://realpython.com/introduction-to-python-generators/
# https://www.python.org/dev/peps/pep-0289/


'''
Sometimes I want an iterable object, but I don't want to load the entire iterable object into memory. A list comprehension loads the entire iterable
into a list, so it isn't appropriate for this task. A generator only stores the current object that was return in memory, not the entire iterable
object. The syntax is:
- (<expression> for <var> in <iterable> if <condition>)
'''


def equivalent_generator():
    '''This generator function IS equivalent to the GOOD example of a generator comprehension'''
    for i in range(1000):
        # I believe this is simply an expression, not a generator comprehension, because it doesn't follow the generator comprehension syntax
        (yield i * 5)


def create_generator_comprehension():
    """
    The syntax is almost identical to that of a list comprehension. There is no such thing as a tuple comprehension.
    - If the yield keyword is unnecessarily used within a generator comprehension, then the generator.next() alternatively returns None. This is
      because "the current yield expression always evaluated to None." It must be the case that what I think of as the same line of code is actually
      executing twice. Regardless, don't do this ever.
    """
    gen = equivalent_generator() # 0 5 10 15 20
    # This is a tricky bug
    #gen = ((yield i * 5) for i in range(1000)) # 0 None 5 None 10
    # This is good
    gen = (i * 5 for i in range(1000)) # 0 5 10 15 20
    print(gen.next())
    print(gen.next())
    print(gen.next())
    print(gen.next())
    print(gen.next())


if __name__ == "__main__":
    create_generator_comprehension()