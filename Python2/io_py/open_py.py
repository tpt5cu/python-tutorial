"""
https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files - shows open modes
https://docs.python.org/2/library/functions.html#open
"""

import os

"""
r - read only
w - write only (an existing file will be completely overwritten)
a - append only (anything written is added to the end of the file)
r+ - open for reading and writing
w+ - open for reading and writing (but also truncate the file)
b - only needed for binary files when using a Windows OS, but append it on Unix so it's platform independent (e.g. 'rb')
"""

def open_py():
    """ open() returns a file object that is used to read/write the underlying file
    - The path can be absolute, or relative to the current working directory (THIS IS IMPORTANT)
    - The default open mode is 'r', or read. It's NOT in binary mode by default
    - A file must be closed to free up resources. It should be closed in a finally block in case an exception happens during file operations
    - A file may only be opened in ONE of the following modes: create/read/write/append
    """
    try:
        file = open(os.path.join(os.path.dirname(__file__), '../../.gitignore'))
        # read() without an argument reads the entire file (into a string object)
        print(file.read())
    finally:
        file.close()

def better_py_open():
    """ The 'with' statement simplifies exception handling. It does the same thing as try-finally, but it can be used for much more than file 
    handling.
    """
    with open(os.path.join(os.path.dirname(__file__), '../../.gitignore')) as f:
        print(f.read())

if __name__ == "__main__":
    #open_py()
    better_py_open()

"""
def open():
    # https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    # https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
    # https://docs.python.org/3/tutorial/inputoutput.html (talks about seek(), readlines(), etc.)

    import os

    def my_print():
        Python2 accepts both syntax versions, but python3 requires parenthesis for print()
        print("hello world")
        # print "hello world"

    def offset_the_file_pointer_location():
        Seek allows me to offset the file pointer from a defined point in the file.

        with open('../.gitignore', encoding='utf-8') as f:
            This skips the first 3 characters in the file. I think under the hood it's skipping the first 3 bytes,
            which correspond to the first 3 characters
            
            f.seek(3)
            print(f.read())

    def read_by_line():
        list() and <file_object>.readlines() do the same thing, but their implementations might be different. I'll be surprised if I ever really need to know the difference in implementation.

        with open('../.gitignore', encoding='utf-8') as f:
            content = f.readlines()
            x = 1
            for line in content:
                print(str(x) + ": " + line)
                x += 1
"""