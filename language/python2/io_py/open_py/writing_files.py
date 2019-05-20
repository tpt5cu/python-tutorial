"""
https://docs.python.org/2/library/stdtypes.html#bltin-file-objects
"""

import os, time


def write_file():
    """ If using <file>.write(), the argument MUST be a string! """
    with open(os.path.join(os.path.dirname(__file__), "test-files/written.txt"), 'w') as f:
        #f.write("The time is: ")
        #f.write(time.time()) # TypeError
        f.write("The time is: ")
        f.write(str(time.time()))


if __name__ == "__main__":
    write_file()