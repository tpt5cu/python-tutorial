# https://stackoverflow.com/questions/338768/python-error-importerror-no-module-named

import sys


def need_init_py():
    """In Python 3 (which is what my IDE uses), ANY directory on sys.path that matches an imported package name
    will be treated as a package.

    In Python 2, to make an import statement walk through the directories in sys.path,
    EVERY directory MUST have an __init__.py, for the import to work correctly. This means that if I'm using Python 2,
    my sys.path can be configured correctly but if I forget to have an __init__.py somewhere, imports won't work.
    Actually, it seems like just the target directory needs to have an __init__.py inside of it.

    This code executes just fine in my IDE because I'm using Python 3. It doesn't work in my terminal because
    /Users/austinchang/pycharm/python_tutorial is NOT in my sys.path by default in the terminal.
    """
    import python_objects.identity
    python_objects.identity.identify_object()


def append_to_sys_path():
    """The python_tutorial package is located within the pycharm directory. The pycharm directory is not on my
    sys.path until I append it as shown. Once the pycharm directory (aka Python package) is appended to sys.path,
    Python 3 has no trouble importing python_tutorial.

    Python 2 in my terminal also executes this function successfully.
    """
    sys.path.append("/Users/austinchang/pycharm/")
    import python_tutorial


def configure_sys_path():
    """Now that I've added an __init__.py to my root directory, manually configuring the sys.path variable SHOULD
    allow this particular function to execute in the terminal with Python 2. It works!
    """
    sys.path.append("/Users/austinchang/pycharm/python_tutorial")
    import python_objects.identity
    python_objects.identity.identify_object()


if __name__ == "__main__":
    #need_init_py()
    #append_to_sys_path()
    configure_sys_path()
