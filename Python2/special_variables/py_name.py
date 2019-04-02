"""
http://exampleprogramming.com/specialvars.html
"""

"""
The __name__ special variable is a substitute for 1 of 2 things: 1) either the string "__main__" if the module is running in the __main__ namespace, 
or 2) the name of the module (i.e. the file name)

The __file__ special variable is a substitue for the absolute path (including file name) of this Python module (i.e. Python file)
"""

def my_cool_function():
    """ This prints "__main__"
    """
    print(__name__)
    print(__file__)

if __name__ == "__main__":
    my_cool_function()