# https://realpython.com/introduction-to-python-generators/
# https://www.python.org/dev/peps/pep-0289/


"""
Sometimes I want an iterable object, but I don't want to load the entire iterable object into memory. A list comprehension loads the entire iterable
into a list, so it isn't appropriate for this task. A generator only stores the current object that was return in memory, not the entire iterable
object.
"""


def equivalent_generator():
    """
    This generator function looks like it should be equivalent to the confusing version of the generator comprehension in the next function, but it
    isn't!
    """
    for i in range(10):
        (yield i * 5)


def create_generator_comprehension():
    """
    The syntax is almost identical to that of a list comprehension. There is no such thing as a tuple comprehension.
    - If the yield keyword is unnecessarily used within a generator comprehension, then the generator.next() alternatively returns None. This is
      because "the current yield expression always evaluated to None." It must be the case that what I think of as the same line of code is actually
      executing twice. Regardless, don't do this ever.
    """
    #gen = equivalent_generator()
    #gen = ((yield i * 5) for i in range(10)) # Don't do this
    gen = (i * 5 for i in range(10)) # This is good
    print(gen.next())
    print(gen.next())
    print(gen.next())
    print(gen.next())
    print(gen.next())


if __name__ == "__main__":
    create_generator_comprehension()