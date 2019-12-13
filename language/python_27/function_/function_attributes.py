# https://www.python.org/dev/peps/pep-0232/
# https://docs.python.org/2.7/reference/datamodel.html#the-standard-type-hierarchy - see callable section at top. Has built-in function attributes


'''
Currently, Python 2 and 3 only support function attributes on user-defined functions
- Function attributes should really only be used for metadata. Anything else is just confusing
'''


class Economics(object):

    def __init__(self, professor):
        self._professor = professor
        self._enrollment = []

    def add_student(self, student):
        self._enrollment.append(student)


def add_arbitrary_function_attributes():
    '''
    A function object can have attributes added and removed from it as needed. Unbound and bound methods are permitted to access such attributes, but
    not set them
    '''
    econ101 = Economics('Elzinga')
    print(econ101.__class__.__dict__['add_student']) # <function add_student at ...>
    econ101.__class__.__dict__['add_student'].annotation = 'I hate economics'
    print(econ101.__class__.__dict__['add_student'].annotation) # I hate economics
    print(econ101.__class__.add_student.annotation) # I hate economics
    print(econ101.add_student.annotation) # I hate economics


def cannot_add_arbitrary_method_attributes():
    '''Unbound and bound methods may not set function attributes. They may only reference them if they exist'''
    econ101 = Economics('Elzinga')
    print(econ101.add_student) # <bound method Economics.add_student of <__main__.Economics object at ...>>
    econ101.add_student.annotation = 'I\'m falling asleep in this class' # AttributeError
    print(econ101.__class__.add_student) # <unbound method Economics.add_student>
    #econ101.__class__.add_student.annotation = 'The add_student method is neat' # AttributeError


def arbitrary_function_attributes(arg1, arg2, arg3):
    pass
arbitrary_function_attributes.foo = 'bar'


def examine_function_attributes():
    '''This is neat, but I really should rely on this in code. Who the heck would understand this?'''
    # Get the names of the function parameters
    print(arbitrary_function_attributes.__code__.co_varnames) # ('arg1', 'arg2', 'arg3')


if __name__ == '__main__':
    #add_arbitrary_function_attributes()
    #cannot_add_arbitrary_method_attributes()
    examine_function_attributes()