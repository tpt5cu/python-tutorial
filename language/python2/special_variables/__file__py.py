"""
https://stackoverflow.com/questions/7116889/is-module-file-attribute-absolute-or-relative
https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package
"""

"""
See the modules_py.imports.py notes too
"""

import sys, os

"""
A Python module is an object that exists in the memory of the Python interpreter. Strictly speaking, a Python module is NOT the same as a .py file.

__file__ is the pathname of the file from which the module was loaded, if it was loaded from a file.

The __file__ attribute may be missing for certain types of modules, such as C modules that are statically linked into the interpreter; for extension
modules loaded dynamically from a shared library, it is the pathname of the shared library file.
"""

"""
If the path of this file is inside of sys.path, __file__ will always be set to some relative path.
When this file is run as a script (i.e. without the -m flag), __file__ is equivalent to the directories that were traversed to reach this file, plus
this file name. For example, __file__ could be different things, depending on where the $ python $ command was run from.
- file_py.py
- special_variables/file_py.py
- python2/special_variables/file_py.py

ALSO note that os.path.dirname(__file__) could be:
- "" from $ cd ~/tutorials/python/language/python2/special_variables && python file_py.py
- "special_variables" from $ cd ~/tutorials/python/language/python2 && python special_variables/file_py.py
- etc.

sys.path is always initialized on program startup. sys.path[0] equals the directory containing the script that was used to invoke the Python
interpreter, unless the script directory isn't available, in which case path[0] is an empty string.
- The script directory isn't available if this file is run as a module (i.e. with the -m flag) because python imports the specified file for me. Thus,
  running this file as a module doesn't put the absolute path of this file's directory into sys.path, which is why __file__ will then be an absolute
  path.

The main point is that __file__ is NOT always an abosolute path to this file like I though it was, and os.path.join(os.path.dirname(__file__),
<something>) isn't foolproof like I thought it was.
"""
def print_file():
    print("__file__ is: " + __file__)

def print_name():
    """ If this module was run as the entry point, __name__ would of course be substituted with "__main__".
    However, when this function is imported and run, __name__ is: "file_py"
    """
    print("file_py __name__ is: " + __name__)

def print_sys():
    print("sys.path:")
    for p in sys.path:
        if p == "":
            print("\"\"")
        else:
            print(p)
    print_file()

if __name__ == "__main__":
    print("os.path.dirname(__file__): " + os.path.dirname(__file__))