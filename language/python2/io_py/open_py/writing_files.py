# https://docs.python.org/2/library/stdtypes.html#bltin-file-objects
# https://stackoverflow.com/questions/5607117/python-question-about-write-and-truncate
# https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fsync.2.html

import os, time


"""
When a call to f.write() is made, the string is actually BUFFERRED to the Python process's own internal IOBuffer. Nothing is immediately written to the
file. Only once flush() is called is the buffer written to the file. The buffer is written to the file when 1) f.flush() is explicitly called 2)
f.close() is called (which implicitly happens at the end of the with statement) or 3) the buffer fills up

Also, the OS does its OWN layer of buffering. When a file is f.flush() from Python, the Python buffer is written to the OS buffer. The OS doesn't
write the data to disk until fsync() is called or after some time has passed (at the end of which I assume the OS implicitly calls fsync()). If the OS
crashes or the computer loses power before data is written to disk, the data is lost because the buffer's volatile memory is cleared.
- It's actually even more complicated. fsync() moves the data from the OS buffer to the drive. The drive ITSELF won't physically write the data until later.
"""


def write_file():
    """If using <file>.write(), the argument MUST be a string!"""
    with open(os.path.join(os.path.dirname(__file__), "test-files/written.txt"), 'w') as f:
        #f.write("The time is: ")
        #f.write(time.time()) # TypeError
        f.write("The time is: ")
        f.write(str(time.time()))


def write_nothing():
    """
    Opening a file in write mode IMMEDIATELY clears the entire file, regardless of whether or not I write something else! This is a HUGE problem for
    simultaneous writes!
    """
    with open(os.path.join(os.path.dirname(__file__), "test-files/written.txt"), 'w') as f:
        pass


if __name__ == "__main__":
    write_file()
    write_nothing()