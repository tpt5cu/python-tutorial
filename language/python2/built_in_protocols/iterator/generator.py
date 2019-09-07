# https://docs.python.org/2/glossary.html#term-generator - official definition
# https://docs.python.org/2/reference/expressions.html#yieldexpr - generator implementation


"""
A generator is a function that when invoked returns an iterator (that iterator is known as a generator). This returned generator then controls the
execution of the generator function. The generator saves the previous state upon each "yield", and picks up where it left off the next time it is
called.
"""


def basic_generator():
    """
    This single yield-statement must be contextualized in such a way that it will continue to execute upon subsequent calls to next(). The generator
    stops when it finds a yield statement and resumes executing on the line after the yield statement it returned with on the previous invocation.
    - Thus, a generator never stops on a yield statement and stays there. It finds it, returns, and the subsequent call resumes AFTER the previous
      yield
    """
    my_list = [1, 2, 3, 4, 5]
    count = 0
    # Here, the first next() call executes but any subsequent next() call will raise StopIteration because the generator will exit without yielding
    # another value. The count += 1 statement is irrelevant
    #yield my_list[count]
    #count += 1
    while True:
        try:
            # Without this try-except, the generator will eventually raise an IndexError
            yield my_list[count]
            count += 1
        except:
            raise StopIteration


def use_basic_generator():
    gen = basic_generator()
    for item in gen:
        print(item)


def modifiable_generator():
    """Even though this generator function doesn't have any parameters, the send() function can still modify its state"""
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    while True:
        try:
            # If send(<arg>) is called, then the count variable will be <arg>. If it isn't called, then the count variable will be None. In this way,
            # I can modify the state of a generator during execution if I want, or I can let it be
            count = yield my_list[count]
            if count is None:
                count += 1
        except:
            raise StopIteration


def modify_generator_state():
    gen = modifiable_generator()
    # gen is an iterator, so I can't access it with an index. 
    for item in gen:
        print(item)





if __name__ == "__main__":
    use_basic_generator()