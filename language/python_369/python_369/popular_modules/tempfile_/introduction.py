# https://docs.python.org/3.7/library/tempfile.html


import tempfile, pathlib, os


this_dir = pathlib.Path(__file__).parent


'''
- TemporaryFile, NamedTemporaryFile, TemporaryDirectory, and SpooledTemporaryFile are high-level interfaces whose resources can be automatically
  removed when the script is finished
- mkstemp() and mkdtemp(): low-level interfaces whose resources require manual cleanup

- TemporaryFile, NamedTemporaryFile, SpooledTemporaryFile
    - All have a default open mode of "w+b"
        - w+ is to allow writing and reading without closing the file
        - Binary mode is to ensure consistent behaivor on all platforms without regard to the data that is being stored
            - I don't think I need to care about this
    - "buffering", "encoding", and "newline" have the same meaning as for open()
'''


def mkstemp_():
    '''
    Creates a temporary file securely. Returns (<os-level file handle>, <absolute filename>)
    - File is not automatically deleted
    - "suffix", "prefix", and "dir" control the filename and file location
    - "text" == False opens the file in binary mode (default)
    '''
    handle, filename = tempfile.mkstemp(suffix='.temp', dir=this_dir)
    print(filename)
    os.write(handle, b'This is a temporary file!') # os.write() requires a byte string
    os.close(handle)


def temporary_file():
    '''
    The file will be destroyed as soon as it is closed. As a simplification: do not rely on the filesystem being able to see or not see that this file
    existed. 
    - The temporary file does not show up in the filesystem according to os.scandir()
    - The "name" attribute of this type of temporary file is a number, so it's not very helpful
    '''
    with tempfile.TemporaryFile('w+', suffix='.mytemp', dir=this_dir) as f:
        print(type(f)) # <class '_io.TextIOWrapper'>
    #with tempfile.TemporaryFile(suffix='.mytemp', dir=this_dir) as f:
    #    print(type(f)) # <class '_io.BufferedRandom'>
        for entry in os.scandir(this_dir):
            print(entry.path)
        f.write('Hello from TemporaryFile()')


def optionally_deleted_named_temporary_file():
    '''
    Exactly the same as TemporaryFile, except that 
    - "delete" == True (default) controls whether or not the file will be deleted
    - The file WILL have a visible name in the file system
        - See it with the "name" attribute
    '''
    with tempfile.NamedTemporaryFile('w', suffix='.visibletemp', dir=this_dir, delete=True) as f:
        #for entry in os.scandir(this_dir):
        #    print(entry.path)
        f.write('Hello from NamedTemporaryFile()')
        print(f.name) # /Users/austinchang/tutorials/python/language/python_369/popular_modules/tempfile_/tmph5kyfy36.visibletemp


def mkdtemp_():
    '''Parameters are exactly the same as mkstemp. Directory is not automatically deleted. Returns the absolute path of the directory'''
    temp_dir = tempfile.mkdtemp(dir=this_dir)    
    print(temp_dir)


def deleted_temporary_directory():
    '''
    Same as mkdtemp, except that
    - It can be used as a context manager
    - The directory will be automatically deleted
    - The absolute path of the temporary directory is returned as the alias of the with-statement
    '''
    with tempfile.TemporaryDirectory(dir=this_dir) as d:
        print(d)


if __name__ == '__main__':
    #mkstemp_()
    #temporary_file()
    optionally_deleted_named_temporary_file()
    #mkdtemp_()
    #deleted_temporary_directory()
