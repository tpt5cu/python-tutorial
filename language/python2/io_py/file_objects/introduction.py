# https://docs.python.org/2.7/library/stdtypes.html#bltin-file-objects - high-level file object returned by open() built-in
# https://docs.python.org/2.7/c-api/file.html - this describes the underlying C API that is used by Python. Not what I want


import os, subprocess


filepath = os.path.join(os.path.dirname(__file__), "test.txt")


def get_a_file_object():
    """
    High-level file objects (which will henceforth be called simply file objects) are returned by several Python functions
    - subprocess.Popen() stdin, sdout, or stderr
    - built-in open()
    - os.fdopen(), NOT os.open()
        - Build-in open() could be implemented with os.open() + os.fdopen()

    Using the low-level file descriptor operations (e.g. os.open(), os.read(), etc.) instead of the high-level file interface will ignore aspects like
    internal bufferring of data
    """
    #with open(filepath) as f:
    #    print(type(f)) # <type 'file'>

    # This function is obsolete. Use the subprocess module instead
    #os.popen()
    #pipe = subprocess.Popen("ls", stdout=subprocess.PIPE).stdout
    #print(pipe.read()) # prints the contents of /Users/austinchang/tutorials/python/language
    #pipe.close()
    #print(type(pipe)) # <type 'file'>

    #fd = os.open(filepath, os.O_RDONLY)
    #print(fd) #3
    #some_file = os.fdopen(fd)
    #print(some_file.readline()) # This is line number 0
    #some_file.close()
    #print(type(some_file)) # <type 'file'>


if __name__ == "__main__":
    get_a_file_object()