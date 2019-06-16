"""
https://beginnersbook.com/2018/03/python-constructors-default-and-parameterized/
"""

class MyClass:
    """
    When I don't explicitly create a constructor (i.e. __init__), Python creates an empty one for me that does nothing.
    """

    def do_stuff(self):
        print("I'm doing stuff")


def use_default_constructor():
    obj = MyClass()
    obj.do_stuff()

if __name__ == "__main__":
    use_default_constructor()