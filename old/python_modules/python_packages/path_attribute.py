# https://docs.python.org/3/reference/import.html
# https://stackoverflow.com/questions/2003859/where-is-the-path-comes-from

"""
A package can be thought of as a directory that can contain other packages and/or regular Python modules (which can
be thought of as .py files). Any module that contains a __path__ attribute is considered a package. 

__path__ has the same function as sys.path: it provides a list of locations to search for the
modules that exist within the package.

The __path__ attribute is used when a package needs to import its subpackages. Since all packages are by definition
modules, this means the attribute is used to import modules inside of the package.

A package’s __init__.py file may set or alter the package’s __path__ attribute.

__path__ can be an iterable of strings or empty. 

Packages support one more special attribute, __path__. This is initialized to be a list containing the name of 
the directory holding the package’s __init__.py before the code in that file is executed. This variable can 
be modified; doing so affects future searches for modules and subpackages contained in the package.

While this feature is not often needed, it can be used to extend the set of modules found in a package.
"""