"""
https://realpython.com/python-super/
"""

"""
The super() function allows Python to support inheritance.
"""

class SuperClass(object):

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("My name is " + self.name)


class SubClass(SuperClass):

    def __init__(self, name):
        """

        """
        super(SubClass, self).__init__(self, name)


def use_subclass():
    sub = SubClass("Austin Chang")
    sub.print_name()

if __name__ == "__main__":
    use_subclass()
