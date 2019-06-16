"""
https://realpython.com/instance-class-and-static-methods-demystified/
"""


"""
A static method is used to namespace a regular old function.
"""


class MyClass(object):

    def __init__(self, data=1):
        self.data = data


    @staticmethod
    def static_method(data):
        """ A static method does not have any implicit parameters """
        print("The data was " + str(data))


def use_static_method():
    MyClass.static_method(100) # 100


if __name__ == "__main__":
    use_static_method()
