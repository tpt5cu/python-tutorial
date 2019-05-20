import inspect, os

"""
https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory
"""

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


def get_packages_location():
    """
    $ python -c "import site; print(site.getsitepackages())"
        - This command will print the directories where Python packages for the current interpreter are installed

    View the location of a module with the special variable <module>.__path__
    """
    print(inspect.__file__)

def get_attribute_module():
    """
    Let's say I'm interested in a specific attribute of an object and I want to look at the source code.
    """
    pass


def view_src_modules():
    pass

if __name__ == "__main__":
    #dir_py()
    #inspect_py()
    get_packages_location()