# https://realpython.com/python-modules-packages/
# https://stackoverflow.com/questions/1489599/how-do-i-find-out-my-python-path-using-python

import sys, os


def print_pythonpath():
    """The PYTHONPATH is different when I run this function from within my IDE vs in my terminal."""
    try:
        user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
    except KeyError:
        user_paths = []
    print("PYTHONPATH is:\n" + str(user_paths))


def print_search_path():
    """The interpreter searches for imported modules in the following sources in order:
    0) Python's built-in modules that are compiled into the actual Python interpreter. Whether or not a module
    is 'built-in' or just part of the Python standard library is installation-dependent. For example, 'sys' is an
    actual built-in module
    1) The directory from which the input script was RUN or the current directory if in a repl session.
    This corresponds to the absolute path of this file's parent directory, regardless of whether I run the file
    from within my IDE or in my terminal from an arbitrary directory
    2) The list of directories contained in the PYTHONPATH variable, IF it is set
    3) An installation-dependent list of directories configured when Python was installed.

    The search path can be viewed with sys.path
    """
    print("The search path is:\n" + str(sys.path))


def view_module_location():
    print("The os module is located at: " + str(os.__file__))


if __name__ == "__main__":
    print_pythonpath()
    print_search_path()
    #view_module_location()