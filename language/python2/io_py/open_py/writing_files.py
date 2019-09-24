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


filepath = os.path.join(os.path.dirname(__file__), "test-files/written.txt")


def write_file():
    """If using <file>.write(), the argument MUST be a string!"""
    with open(filepath, 'w') as f:
        #f.write("The time is: ")
        #f.write(time.time()) # TypeError
        f.write("The time is: ")
        f.write(str(time.time()))


def write_nothing():
    """
    Opening a file in write mode IMMEDIATELY clears the entire file, regardless of whether or not I write something else! This is a HUGE problem for
    simultaneous writes!
    """
    with open(filepath, 'w') as f:
        pass


def read_write_mode():
    """
    Opening in read-write mode does NOT truncate the file. It starts from the very beginning of the file (by default) and writes the prescribed text,
    overwriting anything that was there before.
    - It's easy to get nonsense if I open the file in read-write mode and write in new content without truncating the file first
    - I can use seek() to adjust the position of the file descriptor
    """
    with open(filepath, 'r+') as f:
        f.seek(0, os.SEEK_END) # This will set the file descriptor position to the end of the file. Now this operation is identical to 'a' mode
        f.write("Hello read_write_mode()!")


def write_plus_mode():
    """
    Opening in w+ mode does indeed truncate the file. So what's the difference betweeen it and 'w' mode? I can read from the file. That's it.
    - The file is still created if it does not exist
    """
    with open(filepath, 'w+') as f:
        f.write("Hello from write_plus_mode")
        f.seek(0, os.SEEK_SET)
        data = f.read()
    print(data)


if __name__ == "__main__":
    #write_file()
    #write_nothing()
    #read_write_mode()
    write_plus_mode()