"""
http://exampleprogramming.com/specialvars.html
https://medium.freecodecamp.org/whats-in-a-python-s-name-506262fe61e8
"""

import file_py

"""
The __name__ special variable is a substitute for 1 of 2 things: 1) either the string "__main__" if the module is running in the __main__ namespace, 
or 2) the name of the module (i.e. the file name)
"""

def my_cool_function():
    """ This prints "__main__" """
    print("py_name __name__ is: " + __name__)
    print(__file__)
    py_file.print_name()

if __name__ == "__main__":
    my_cool_function()