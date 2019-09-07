# https://www.djangospin.com/python-file-buffering/ - a summary of pretty much everything else here
# https://stackoverflow.com/questions/29712445/what-is-the-use-of-buffering-in-pythons-built-in-open-function - examples of how buffering is useful
# https://docs.python.org/2.7/library/functions.html#open - open() buffering argument
# https://docs.python.org/2.7/library/io.html - Python 3 actually uses THIS interface instead of the old high-level file object interface for file
# access
# https://docs.python.org/2/library/stdtypes.html#bltin-file-objects - Python file flush() method
# https://stackoverflow.com/questions/5607117/python-question-about-write-and-truncate - flush() method details
# https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fsync.2.html - macOS fsync() details
# https://stackoverflow.com/questions/2447143/does-close-imply-flush-in-python - Python <file>.close() DOES implicitly call <file>.flush()


import os, io, timeit


"""
From Python buffer to disk:
- <file>.flush() will clear Python's own internal buffer. This does not mean the buffer data is written to disk
    - <file>.close() implicitly calls <file>.flush()
- Now the OS buffer should contain all of the information I want to write
- os.fsync(<file descriptor>) supposedly force-writes the file descriptor to disk. It uses the native fsync() function on Unix
- On macOS fsync() will send the data from the OS to the drive, but the drive can 1) write the data out of order to disk and 2) the timing of the
  writes to disk is asynchronous
"""


"""
Buffering during write:
- If I want to write data to a file, buffering can increase the speed of the write by 1) storing everything that I want to write in memory until some
  defined event (e.g. a newline is reached or the file is closed) 2) when the event occurs, write everything in the buffer to disk.
  - This will reduce the number of disk accesses, thereby speeding up the write. In reality, there are several buffers between Python and the actual
    disk, including but not limited to Python's internal buffer, the OS buffer, some kind of drive buffer? Therefore, it is not necessarily true that
    buffering in Python will always result in better performance.

Buffering during read:
- If I want to read data from a file, buffering can increase the speed of the read by 1) reading a large chunk of the file from the OS filesystem 2)
  the process can read a small chunk of data from the buffer instead of reading a small chunk from the OS filesystem. This will reduce filesystem
  access and speed up the read. This example makes sense when a process has timed intervals at which it is interested in consuming small chunks of
  data.
"""


filepath = os.path.join(os.path.dirname(__file__), "test.txt")


def prepare_file():
    """Make a 278.9 MB file"""
    with open(filepath, 'w') as f:
        for x in range(0, 10000000): # 10 million lines
            f.write("This is line number " + str(x) + "\n")

        
def inspect_system_buffer():
    """
    This is the buffer size used by the io module and its classes. The built-in open() function uses a files blksize instead if possible. As a review,
    - 2^10 B = 1 KB
    - 2^20 B = 1 MB
    - 2^30 B = 1 GB
    """
    print(io.DEFAULT_BUFFER_SIZE) # 8192 bytes or 2^13 B or 8 KB
    # posix.stat_result(st_mode=33188, st_ino=14739305, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=278888890, st_atime=1567192889,
    # st_mtime=1567192885, st_ctime=1567192888)
    # - mode: the inode protection mode (i.e. permissions)
    # - ino: The inode number of the file
    # - dev: ID of the device that contains the inode
    # - nlink: The number of hard links to the inode
    # - uid: user id
    # - gid: group id
    # - size: the exact byte size of the file (I think this is the blksize (i.e. block size) that the io documentation mentioned)
    # - atime: last accessed time
    # - mtime: last modified time
    # - ctime: last time inode was modified
    print(os.stat(filepath))


def fully_buffered_read():
    """
    If the buffering argument is omitted or the argument is set to a negative number, the system default buffer size is used. The system default is
    usually line-buffered for a tty and fully buffered for other files. I assume there is some absolute limit (Python couldn't read an 8GB file into
    memory)
    """
    with open(filepath, "r") as f:
        data = f.read()


def unbuffered_read():
    """If the buffering argument is 0, the read is unbuffered by Python"""
    with open(filepath, "r", 0) as f:
        data = f.read()


def line_buffered_read():
    """If the buffering argument is 0, the read is unbuffered by Python"""
    with open(filepath, "r", 1) as f:
        data = f.read()


def time_execution():
    """
    There is not an appreciable difference between fully buffered and unbuffered. Perhaps this is because "unbuffered" means read directly from the OS
    buffer. A line-buffered read is slow though! This must be because the Python buffer has to repeatedly load and clear its own buffer.
    """
    #print(timeit.timeit("fully_buffered_read()", setup="from __main__ import fully_buffered_read", number=1000)) # 244 seconds
    #print(timeit.timeit("unbuffered_read()", setup="from __main__ import unbuffered_read", number=1000)) # 241 seconds
    #print(timeit.timeit("line_buffered_read()", setup="from __main__ import line_buffered_read", number=1000)) # 841 seconds
    pass


if __name__ == "__main__":
    #prepare_file()
    #inspect_system_buffer()
    time_execution()