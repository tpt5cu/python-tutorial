# https://realpython.com/python-modules-packages/
# https://stackoverflow.com/questions/18486469/how-to-print-contents-of-pythonpath/18486534
# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/50194143#50194143 - The real solution to the whole packaging mess
# https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py


'''
Hard-coding absolute or relative imports paths into Python modules is a losing battle. They will break when folders get moved around.
- In order to use relative import syntax, I have to RUN THE MODULE AS A PACKAGE (i.e. $ python -m $).
'''


def view_sys_path():
    """
    When Python executes an import statement, it searches for the desired module in 3 locations:
    - The directory from which the current script was run (i.e. the directory where $ python -m ... $ was executed), OR the cwd if python is running interactively
    - The directories in $PYTHONPATH
    - An installation-dependent list of directories that were configured when Python was installed

    The paths from all 3 sources are combined into sys.path.
        - sys.path appends the cwd automatically, so the cwd is always in the import path
    """
    import sys
    print(sys.path)


'''
These do not work:
- $ python -Bm rel_and_abs_imports $: No module named 'what_is_init_py'
    - 'what_is_init_py' is 1) above the scope of this packaged run and 2) not itself a package
- $ python -Bm imports_py.rel_and_abs_imports$: No module named 'rel_and_abs_imports' 
    - This happens when there is no __init__.py or __init__.pyc in the /imports_py directory
- $ python -Bm imports_py.rel_and_abs_imports$: ValueError: Attempted relative import beyond toplevel package 
    - This happens when I try to import 'io_py' because that package is above the scope of this packaged run
- $ python -Bm modules_py.imports_py.rel_and_abs_imports$: No module named 'modules_py.rel_and_abs_imports' 
    - This happens when there is no __init__.py(c) in the /modules_py directory
- $ python -Bm modules_py.imports_py.rel_and_abs_imports$: ValueError: Attempted relative import beyond toplevel package
    - This happens when I try to import 'io_py' because that package is above the scope of this packed run
- $ python -Bm python2.modules_py.imports_py.rel_and_abs_imports: ImportError: No module named modules_py.what_is_init_py
    - This happens because the interpeter will search for a package from where the script was RUN. 

This works, assuming that all of the directories have __init__.py(c) files
- $ python -Bm python2.modules_py.imports_py.rel_and_abs_imports
    - This works assuming that the relative import statements are written correctly AND the python command is executed with the correct flag in the
      correct directory
'''


'''These are absolute import paths. They are preferrable to relative import paths'''
# This type of import merely creates a namespace. Nothing is added this module's symbol table
import sys 

# This adds "foo" into this module's own symbol table.
from python2.modules_py.what_is_init_py import foo
#from modules_py.what_is_init_py import foo # Does not work because /modules_py can't be directy found in the directory in which the packaged python command MUST be executed for this whole script to work
#from what_is_init_py import foo # Does not work based on same principle as above

from python2.modules_py.what_is_init_py import * # This imports everything. Bad idea

from python2.modules_py.what_is_init_py import foo as bar # Add "foo" to this namespace under the alias "bar"

import python2.modules_py.what_is_init_py as baz # Import the namespace of another module under an alias


# Importing a package (which is also technically a module) is valid, but none of the modules in the package are added to the local namespace.
# Additionally, modules objects (i.e. packages) cannot have inner modules accessed through '.' syntax. That's because such '.' syntax must refer to
# attributes inside of the __init__.py file of the package itself
from python2 import io_py 
# For example, these are all invalid:
#open_py # name 'open_py' is not defined. Module was not added to local namespace
#io_py.open_py.introduction.better_py_open() # AttributeError: 'module' object has no attribute 'open_py'

# This works!
from python2.io_py.open_py.introduction import better_py_open

'''
This is a relative import path
- EACH '.' means go up one directory. 
    - First '.': current directory (i.e. /imports_py)
    - Second '.': /modules_py
    - Third '.': /python2_py
- This is confusing because '.' in Unix is cwd and '..' is go up 1 directory, so logically I would think that '....' would mean go up 2 directories
'''
from ...io_py import open_py


def use_io_py_package():
    better_py_open() # IOError because the hard-coded relative path in this function points to '/language', while the .gitignore file exists in '/python'
    pass


if __name__ == "__main__":
    #view_sys_path()
    use_io_py_package()