"""
https://realpython.com/instance-class-and-static-methods-demystified/
"""

class MyClass(object):


    def __init__(self, data=1):
        self.data = data


    def set_instance_data(self, data):
        self.data = data


    def set_class_data(self, data):
        self.__class__.data = data


def modify_instance():
    obj = MyClass(5)
    print(obj.data) # 5
    obj.set_instance_data(6)
    print(obj.data) # 6


def modify_class():
    """
    The class of an instance may be accessed through the __class__ attribute. If an instance and class have the same attribute, the instance attribute
    gets preference due to how __dict__ look-up works.
    """
    obj = MyClass(2)
    #print(MyClass.data) # MyClass has no attribute "data"
    obj.set_class_data(7)
    print(MyClass.data) # 7
    print(obj.data) # 2
    print(obj.__class__.data) # 7
    obj.__class__.data = 8
    print(MyClass.data) # 8


def use_instance_method_through_class():
    """
    It is possible to use an instance method through a class. However, the instance method MUST receive an instance of the class instance as the first
    argument.
    """
    #MyClass.set_instance_data(5, 7) # TypeError: unbound method
    obj = MyClass()
    print(obj.data) # 1
    MyClass.set_instance_data(obj, 8)
    print(obj.data) # 8



if __name__ == "__main__":
    #modify_instance()
    #modify_class()
    use_instance_method_through_class()
