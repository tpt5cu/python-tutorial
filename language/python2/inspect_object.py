import inspect

def dir_py():
    """
    dir() returns different things depending on the object being inspected. It will return:
        - A list of a module's attributes
        - A list of a class's attributes, and recursively the attributes of its base classes
        - A list of an object's attributes, its class's attributes, and recursively the attributes of its base classes 
    """
    for x in dir(list):
        print(x)
    print(len(dir(list)))

def inspect_py():
    """ inspect.getmembers() gives more detail than dir(), but the list of attributes is exactly the same """
    for x in inspect.getmembers(list):
        print(x)
    print(len(inspect.getmembers(list)))

if __name__ == "__main__":
    #dir_py()
    inspect_py()