# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder

import os, sys
import pkg_resources


def import_from_some_parent():
    """Often times, I want to read/write a file that is in some parent directory relative to this directory.

    os.path.dirname(): return the direct PARENT DIRECTORY of the argument
    os.path.basename(): return the END element of a path, which corresponds to the file name
    """
    # dir
    print(os.path.dirname(__file__)) # /Users/austinchang/pycharm/python_tutorial/useful_packages/python_os
    print(os.path.basename(__file__)) # path_manipulations.py
    pkg_resources.resource_filename


if __name__ == "__main__":
    get_parent_directory()