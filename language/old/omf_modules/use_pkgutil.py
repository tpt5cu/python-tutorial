
import sys
import python_pkgutil as p

"""This file imports and uses my own python_pkgutil package that I made in order to understand the real pkgutil package
"""

if __name__ == "__main__":
    """When extend_path() is NOT used in __init__.py, the python_pkgutil.__path__ is:
    ['/Users/austinchang/pycharm/python_tutorial/omf_modules/python_pkgutil']

    When extend_path() IS used in __init__.py, the python_pkgutil.__path__ is:
    ['/Users/austinchang/pycharm/python_tutorial/omf_modules/python_pkgutil', '/Users/austinchang/pycharm/python_tutorial/python_pkgutil']
    """
    print("sys.path:\n" + str(sys.path))
    print("python_pkgutil path:\n" + str(p.__path__))