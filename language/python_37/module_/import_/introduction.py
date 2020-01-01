# https://softwareengineering.stackexchange.com/questions/159503/whats-wrong-with-relative-imports-in-python


import sys
print(sys.path[0])

#import awesome_module # Doesn't work sometimes
#awesome_module.awesome_function()

'''
Even if a module is successfully imported on a line, a subsequent from-style import of that same module is done completely independently of any prior
import(s). As a result, the line "from awesome_module import ..." fails for the same reason as the line "import awesome_module"
'''
from module_.import_ import awesome_module
from awesome_module import awesome_function # ModuleNotFoundError: No module named 'awesome_module'
awesome_function()

'''Yes, it is perfectly reasonable to import a function from a module'''
#from module_.import_.awesome_module import awesome_function
#awesome_function()


'''
Python 3 completely removes implicit relative imports. This means that when Python is run with the -m flag, sys.path[0] is NO LONGER equal to "",
which previously instructed the interpreter to search the directory of the main entrypoint script for an imported module (to boot, this implicit
relative lookup behaivor would shadow site-package AND built-in modules)
- Instead, sys.path[0] is now equal to the directory where $ python -m $ was run instead of ""
- There is no difference in behavior between Python 2 and 3 regarding running Python without the -m flag

Concerete example
- This works in Python 2 and Python 3
    - $ python -m introduction (this file)
    - It works because sys.path[0] is either "" or /Users/austinchang/tutorials/python/language/python_37/module_/import_, so "awesome_module" can
      always be found
- This works in Python 2 but fails in Python 3:
    - $ python -m import_.introduction (this file)
    - It fails because sys.path[0] = /Users/austinchang/tutorials/python/language/python_37/module_, so "awesome_module" can't be resolved as a
      top-level script from anything in sys.atph
'''

def introduction_function():
    print('Hello from introduction function')
