# https://docs.python.org/3/tutorial/classes.html - surprisingly unhelpful resource
# https://portingguide.readthedocs.io/en/latest/classes.html


class Road:
    '''The "object" is the default superclass of all classes in Python 3'''

    def __init__(self, length, width, material):
        self.length = length
        self.width = width
        self.material = material


def examine_road():
    r = Road(10, 10, 'asphalt')
    print(dir(r)) # Has all of the attributes of the Python "object"


if __name__ == '__main__':
    examine_road()