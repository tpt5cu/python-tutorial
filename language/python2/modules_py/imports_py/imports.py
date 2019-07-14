# https://realpython.com/python-modules-packages/
# https://stackoverflow.com/questions/18486469/how-to-print-contents-of-pythonpath/18486534
# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/50194143#50194143
# https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py


"""This group of imports has no errors because sys and what_is_init are both found inside of sys.path."""
import sys # This type of import merely creates a namespace. Nothing is added this module's symbol table
from what_is_init_py import foo # This adds "foo" into this module's own symbol table.
#from what_is_init_py import * # This imports everything. Bad idea
from what_is_init_py import foo as bar # Add "foo" to this namespace under the alias "bar"
import what_is_init_py as baz # Import the namespace of another module under an alias


"""In order to use relative import syntax, I have to RUN THE MODULE AS A PACKAGE (i.e. $ python -m $)."""
# importing a package (which is also technically a module) is valid but useless. None of the modules in the package are added to the local namespace
from .. import io_py 
# This is one option to import a module from a package in a useful way
from ..io_py import open_py

# This syntax is one option to get a module from a package into this local namespace
#from ..io_py import open_py
# This is the other valid option
#import ..io_py.open_py

#import what_is_init_py

def use_io_py_package():
    open_py.better_py_open()

def view_sys_path():
    """ When Python executes an import statement, it searches for the desired module in 3 locations:
    - The directory from which the current file was run, NOT where $ python $ was executed
    - The directories in $PYTHONPATH
    - An installation-dependent list of directories that were configured when Python was installed

    The paths from all 3 sources are combined into sys.path.
    """
    print(sys.path)

if __name__ == "__main__":
    #view_sys_path()
    use_io_py_package()