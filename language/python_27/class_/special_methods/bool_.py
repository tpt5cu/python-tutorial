'''
- Python 2 relies on the __nonzero__() method to get a bool() representation of an object. It ignores __bool_()
    - If a __nonzero__() method doesn't exist, then I don't know what bool() uses
- Python 3 relies on __bool__() to get a bool() representation of an object. It ignores __nonzero__()
'''


class Question(object):

    def __nonzero__(self):
        return True

    def __bool__(self):
        return False


def get_truthiness():
    q = Question()
    # Python 2: True
    # Python 3: False
    print(bool(q))


if __name__ == '__main__':
    get_truthiness()