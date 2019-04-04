"""See the self.py notes. This file exists to demonstrate that class functions are usually used as methods of an
instance, but they CAN be used as namespace-d functions.
"""


class DuperClass:

    def __init__(self, data=1):
        self.data = data

    def print_data(self):
        print(self.data)


class Dummy:
    pass


def use_method_as_function():
    obj = DuperClass()
    obj.print_data()
    # use a dummy because there are no "real" anonymous objects
    thing = Dummy()
    thing.data = 43
    DuperClass.print_data(thing)


if __name__ == "__main__":
    use_method_as_function()