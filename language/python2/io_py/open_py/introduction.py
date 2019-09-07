# https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files - shows open modes
# https://docs.python.org/2/library/functions.html#open - actually shows ALL open modes


import os


"""
r - read only
w - write only (an existing file with the same name will be IMMEDIATELY truncated to 0 bytes!)
r+ - open for reading and writing (does NOT modify a file in place)
a - append only (anything written is added to the end of the file)
b - only needed for binary files when using a Windows OS, but add the 'b' it on Unix so it's platform independent (e.g. 'rb' or 'r+b')

r+, a+, w+ - open the file for reading and writing. Other conditions of the same respective mode apply.
"""


def open_py():
    """
    open() returns a Python file object that is used to read/write the underlying file
    - The path can be absolute, or relative to the current working directory (THIS IS IMPORTANT)
    - The default open mode is 'r', or read. It's NOT in binary mode by default
    - A file must be closed to free up resources. It should be closed in a finally block in case an exception happens during file operations
    - A file may only be opened in ONE of the following modes: create/read/write/append
    """
    try:
        file = open(os.path.join(os.path.dirname(__file__), '../../../.gitignore'))
        # read() without an argument reads the entire file (into a string object)
        print(file.read())
    finally:
        file.close()


def better_py_open():
    """The 'with' statement simplifies exception handling. It does the same thing as try-finally, but it can be used for much more than file handling."""
    with open(os.path.join(os.path.dirname(__file__), '../../../.gitignore')) as f:
        print(f.read())


if __name__ == "__main__":
    #open_py()
    better_py_open()