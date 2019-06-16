"""
https://realpython.com/instance-class-and-static-methods-demystified/
"""


class MyClass(object):


    def __init__(self, data):
        self.data = data


    @classmethod
    def class_method(cls, data):
        """
        The only difference between a class method and an instance method is that a class method receives the class as the first argument, as opposed
        to an instance of the class.
        """
        cls.data = data


def modify_class_through_instance():
    """ Class methods can be accessed through instances, although this is confusing """
    obj = MyClass(7)
    #print(MyClass.data) # MyClass has no attribute "data"
    obj.class_method(12) # valid, but confusing
    print(MyClass.data) # 12


def modify_class():
    """ Classes are regular old objects. Therefore, a class method can be invoked without creating an instance of the class """
    MyClass.class_method(-10) # valid, and not confusing
    print(MyClass.data) # -10


if __name__ == "__main__":
    #modify_class_through_instance()
    modify_class()