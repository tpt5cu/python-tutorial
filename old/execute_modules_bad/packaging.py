# https://realpython.com/python-modules-packages/
# https://www.python.org/dev/peps/pep-0257/
import sys

""" Package names should only consist of lowercase letters (underscores are discouraged). But for the 
sake of learning I'll ignore this convention for now. 
"""

""" A Python file (ending in .py) is called a 'module.'
A Python package is a collection of modules that are organized inside of a directory.
Technically, a package is just a special type of module. A regular package must have an '__init__.py' file inside
of the directory to indicate that the directory is also a package.
Python also has the concept of 'namespace packages'. These are ... 
"""


def search_for_modules():
    """ Python searches for imported modules in the following order:
    1. Current directory OR directory from which the input script was run.
    2. Directories contained in the PYTHONPATH environment variable.
    3. An installation-dependent list of directories that was configured when Python was installed.
    The search path can be viewed with the path variable in the sys module.
    """
    print("Here is the import resolution path: " + str(sys.path))


if __name__ == "__main__":
    search_for_modules()
