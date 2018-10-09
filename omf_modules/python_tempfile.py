# https://docs.python.org/2/library/tempfile.html

import os

"""This module generates temporary files and directories. It is supported on all platforms."""


def what_is_file():
    """__file__ CAN BE the absolute path of the module within which __file__ is written. In this case, this __file__ is:
    /Users/austinchang/pycharm/python_tutorial/omf_modules/python_tempfile.py

    __file__ is only the absolute path of the module within which __file__ is written WHEN the main method of the
    module is executed.

    I don't really understand __file__ at all.
    """
    print(__file__)


def what_is_dirname():
    """dirname() itself is a function. It takes a path and returns the absolute path to the directory of provided path.

    In this case, it returns /Users/austinchang/pycharm/python_tutorial/omf_modules because that is the directory within
    which __file__ (i.e. this module) is contained.
    """
    print(os.path.dirname(__file__))


if __name__ == "__main__":
    # what_is_file()
    what_is_dirname()