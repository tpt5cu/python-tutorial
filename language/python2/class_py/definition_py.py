"""
https://stackoverflow.com/questions/4015417/python-class-inherits-object
"""

"""
There are many differences between old style and new style class definitions in Python 2.x.x. Always use the new style.
- I haven't used classes enough to identify relevant differences
"""

# CapitalCase is the correct convention for naming Python classes
class OldStyle:

    def __init__(self):
        self.name = "OldStyle"

    @staticmethod
    def add_two_numbers(x, y):
        return x + y


class NewStyle(object):

    def __init(self):
        self.name = "NewStyle"

    @staticmethod
    def add_two_numbers(x, y):
        return x + y

def base_classes():
    """
    The OldStyle class does not inherit from the Python object type.
    The NewStyle class inherits from the Python object type.
    """
    print("OldStyle base classes: " + str(OldStyle.__bases__)) # ()
    print("NewStyle base classes: " + str(NewStyle.__bases__)) # (<type 'object'>,)
    #print(OldStyle.add_two_numbers(1, 2))

if __name__ == "__main__":
    base_classes()