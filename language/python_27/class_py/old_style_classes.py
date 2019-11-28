# https://realpython.com/python-metaclasses/ - class and type are different
# https://stackoverflow.com/questions/4162578/python-terminology-class-vs-type - link to official PEP and great summary
# https://www.python.org/download/releases/2.2.3/descrintro/ - the official PEP
# https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python - another great summary
# https://makina-corpus.com/blog/metier/2014/python-tutorial-understanding-python-mro-class-search-path - old-style vs new-style mro. Not needed, but
# intellectually interesting


'''
TLDR: don't ever use old-style classes. It's not just that they're older, but the documentation explicitly states that recent (since around 2013)
"fixes" to Python simply don't apply to old-style classes
- Old-style classes don't have super() or descriptors


Definitions:
- A class is a data structure that can be used as a template to create instances of that class
    - Instances of a class are typically called objects, but in Python everything is an object, so that informal definition of an object is less
      useful as a distinction
- A type is a class that can be used as a template for other classes (via inheritance)
    - In Python, all classes can be used to derive other classes, so all classes are types

What do new-style classes do?
- They unify the type hierarchy of user-defined classes with the built-in types. User-defined classes were always types, but now new-style classes are
  the SAME kind of types as the built-in types
- A new-style class is simply a user-defined type, no more, no less
- New-style classes can inherit from built-in types. Apparently this couldn't be done with old-style classes
    - I would have to run a 2.1 Python interpreter to double check this

What is a metaclass?
- A metaclasses is a class whose instances are other classes. All metaclasses MUST derive from the "type" class, just as all new-style objects derive
  from "object"
'''


class Foo:
    pass


def old_style_class_and_type():
    '''
    All old-style instances are implemented with a single built-in type, called "instance"
    - Old-style classes don't have the __mro__ attribute
    '''
    f = Foo()
    print(f.__class__) # __main__.Foo
    print(type(f)) # <type 'instance'>
    print(f.__class__ is type(f)) # False
    #print(Foo.__mro__) # AttributeError


class Bar(object):
    pass


def new_style_class_and_type():
    '''
    The type and class of a new-style instance are typically the same, although this is not guaranteed since __class__ can be modified on an instance
    '''
    b = Bar()
    print(b.__class__) # <class '__main__.Bar'>
    print(type(b)) # <class '__main__.Bar'>
    print(b.__class__ is type(b)) # True
    print(Bar.__mro__) # (<class '__main__.Bar'>, <type 'object'>)


if __name__ == '__main__':
    old_style_class_and_type()
    #new_style_class_and_type()