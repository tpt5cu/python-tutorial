# https://jfine-python-classes.readthedocs.io/en/latest/metaclass-attribute.html - kinda confusing, but maybe useful in the future?
# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python - what is a metaclass, conceptually?
# https://realpython.com/python-metaclasses/ - somewhat redundant after reading stackoverflow
# https://stackoverflow.com/questions/40171871/difference-between-type-classobj-type-object - old style classes
# https://realpython.com/python-metaclasses/


'''
A regular class defines how an object (an instance of that class) will behave. A metaclass defines how a class (an instance of the metaclass) will
behave. A metaclass can technically be any callable object. However, it really should be a class itself. 'type' is the usual, default metaclass in
Python. 'type' is its own class, and its own metaclass ('type' is very special). To create my own realistically useful metaclass, I should subtype
'type'. A metaclass is often used as a class factory. What does that mean? It means that calling the metaclass will create a new class object and that
I can do extra configuration things when a class is created.

Normally, a 'class' statement (for a new-style class) actually makes an implicit call to type() with the appropriate arguments (i.e. name, bases,
attributes)
- This is true so long as there is no __metaclass__ attribute defined. If __metaclass__ is defined, then THAT callable (as opposed to 'type') will be
    used to create the class object
    - Python will first search for a __metaclass__ attribute defined within the class body
    - If no __metaclass__ attribute was defined within the class body, Python will search for the __metaclass__ attribute in the module scope
        - Python only does this for classes that don't inherit from anything, which basically means old-style classes
    - If Python still didn't find a __metaclass__ attribute, then it will use the metaclass of the first superclass (if any) to create the current
          class object. If there were no superclasses, then I'm using an old-style class in which case all bets are off.
'''

# It doesn't matter whether the parentheses are here or not. It will still be an old-style class because it doesn't inherit from anything
class OldStyleClass(): 
    pass


class NewStyleClass(object):
    pass


def examine_default_metaclasses():
    '''
    New-style classes have their metaclass set to 'type', presumably because the metaclass of 'object' is 'type'. Old-style classes don't have a
    __class__ attribute. The metaclass of an old-style class is a special kind of type called 'classobj'. 
    - old-style classes really are weird and it's probably a waste of time to understand them in-depth
    '''
    osc = OldStyleClass()
    print(type(OldStyleClass)) # <type 'classobj'>
    print(osc.__class__) # __main__.OldStyleClass
    #print(osc.__class__.__class__) # Attribute Error: OldStyleClass does not have __class__ attribute
    nsc = NewStyleClass()
    print(type(NewStyleClass)) # <type 'type'>
    print(nsc.__class__) # <class '__main__.NewStyleClass'>
    print(nsc.__class__.__class__) # <type 'type'>
    print(object.__class__) # <type 'type'>


def get_a_string():
    return 'Hello world'


class HasOwnMetaclass(object):
    # __metaclass__ must be CALLABLE that takes at least 3 arguments. That's the only strict requirement
    __metaclass__ = lambda name, bases, attrs: 'Hello World!'


class HasTypeMetaclass():

    __metaclass__ = type


def examine_custom_metaclass():
    # This class has str as its metaclass
    print(type(HasOwnMetaclass)) # <type 'str'>
    print(HasOwnMetaclass.__class__) # <type 'str'>
    print(HasOwnMetaclass.replace('o', 'u')) # Hellu Wurld!
    # This class has type as its metaclass, so its essentially a new-style class even though the class statement is old-style
    print(type(HasTypeMetaclass)) # <type 'type'>
    print(HasTypeMetaclass.__class__) # <type 'type'>


if __name__ == '__main__':
    examine_default_metaclasses()
    #examine_custom_metaclass()