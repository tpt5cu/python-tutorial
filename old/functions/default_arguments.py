# https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
# http://effbot.org/zone/default-values.htm

"""Python functions are first-class objects, just like in JavaScript. Since a function is evaluated purely during
its definition, and default arguments are like member data of the function object.
"""


def mutable_argument(data=[]):
    """Any default argument is ALWAYS bound a function-definition time (i.e. in the def statement itself), not at
    function execution time. If the default argument is mutable, then the same object will be modified each time
    and confusing behavior can occur."""
    data.append(1)
    return data


def call_mutable():
    """I would think that the returned dictionary would simply be [1], but it isn't.  """
    for x in range(10):
        data = mutable_argument()
    print(data)


def immutable_argument(data="I'm immutable"):
    """Immutable default arguments result in expected behavior. Since the argument is immutable, a new object is
    operated on when I pretend to modify the immutable object.
    """
    data += ". And a string!"
    return data


def call_immutable():
    for x in range(10):
        data = immutable_argument()
    print(data)


if __name__ == "__main__":
    call_mutable()
    call_immutable()
