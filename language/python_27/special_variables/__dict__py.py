"""
https://codesachin.wordpress.com/2016/06/09/the-magic-behind-attribute-access-in-python/
https://stackoverflow.com/questions/25440694/whats-the-purpose-of-dictproxy
"""

"""
Most of the time, I use the "." operator to access attributes of an object and I don't care how it works. However, there is a lot that goes on behind
the scenes. Every object in Python has a __dict__ attribute. __dict__ is a dictionary-like object of all of the object's own attributes. 
"""

class MyClass(object):
    cool_field = "I'm a class field"

    def __init__(self):
        self.instance_field = "I'm an instance field"


def instance_dict():
    """
    The __dict__ of a regular object is simply a regular Python dictionary. It does not contain any class properties, only properties defined on the
    class instance.
    """
    mc = MyClass()
    mc.number = 5 # Yes, I can add attributes to an object.
    print(mc.__dict__) # {'number', 'instance_field'}


def class_dict():
    """
    The __dict__ of a class object is not a regular dictionary. It is a dictproxy. It has class properties and other stuff. A dictproxy has separate
    behavior from a normal dictionary:
    - A dictproxy is read-only.
    """
    print(MyClass.__dict__) # {'cool_field', ...}
    #MyClass.__dict__["foo"] = "bar" # This throws an error because a dictproxy is read-only


if __name__ == "__main__":
    #instance_dict() 
    class_dict() 