# https://docs.python.org/2.7/library/os.html
# https://stackoverflow.com/questions/32115715/os-mknod-fails-on-macos
# https://www.holadevs.com/pregunta/61063/how-to-use-mknod-from-python
# https://unix.stackexchange.com/questions/10723/what-is-the-mknod-command-used-for


import os, stat


'''
mknod() is a Unix system call. Originally it was used to create block and character devices. There should be almost no reason ever why I would need to
make this system call.
'''


def create_file():
    '''
    - os.mknod() always fails on macOS without super-user privilages (i.e. sudo)
    - With super-user privilages, the function fails anyway. Is it because of System Integrity Protection?
    - Just use open() instead
    '''
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test'))
    print(path)
    print(type(path)) # <type 'str'>
    #os.mknod(path) # This is valid path, but the function raises an exception
    mode = 0o600|stat.S_IRUSR
    os.mknod(path, mode) # This also appear to be valid, but the function raises an exception


def remove_file():
    '''
    - os.remove() will not:
        - remove a nonexistent file
        - remove an existing directory
    '''
    path = os.path.join(os.path.dirname(__file__), 'test.txt')
    with open(path, 'w'): pass
    os.remove(path)
    #os.remove('blah.txt') # OSError: errno 2
    path = os.path.join(os.path.dirname(__file__), 'new-dir')
    os.mkdir(path)
    os.remove(path) # OSError: errno 1



if __name__ == '__main__':
    #create_file()
    remove_file()