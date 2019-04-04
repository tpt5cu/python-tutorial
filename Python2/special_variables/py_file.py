"""
The __file__ special variable is a substitue for the absolute path (including file name) of this Python module (i.e. Python file)
"""

def print_name():
    """ If this module was run as the entry point, __name__ would of course be substituted with "__main__".
    However, when this function is imported and run, __name__ is: "py_file"
    """
    print("py_file __name__ is: " + __name__)