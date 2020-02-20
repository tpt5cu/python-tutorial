# https://docs.python.org/2.7/library/shutil.html


import shutil, os, pathlib


'''Like os, shutil operates from the cwd. That means relative paths are relative to the cwd.'''


def copy_file():
    '''
    - copyfile() WILL:
        - copy an existing file to create a new file in an existing directory
        - copy an existing file and overwrite an existing file
    - copyfile() will NOT
        - Copy the file into a nonexistent directory (OSError errno == 2)
    '''
    shutil.copyfile(os.path.join(os.path.dirname(__file__), 'src.txt'), os.path.join(os.path.dirname(__file__), 'dst.txt'))


def copy():
    '''
    - copy() WILL:
        - copy a file to an existing directory. The new file will have the same basename
        - copy a file to a new file. The new file will have whatever name was passed
    - copy() will NOT:
        - copy a directory
    '''
    shutil.copy(os.path.join(os.path.dirname(__file__), 'src.txt'), os.path.join(os.path.dirname(__file__), 'src-dir/imnew.txt'))


def remove_directory_tree():
    """
    Attempting to remove a nonexistent directory raises an OSError with errno == 2. rmtree() will delete all subdirectories if their parent directory
    is deleted.
    """
    dir_path = os.path.join(os.path.dirname(__file__), "parent")
    shutil.rmtree(dir_path)


def move():
    '''
    - move() will:
        - Move a file from dir A to dir B
            - If the file is moved from A to A, then the net result is that the file is renamed in A
        - Move a directory from dir A to dir B
            - If the directory is moved from A to A, then the net result is that the directory is renamed in A
        - Move a directory from dir A to dir B (nonexistent)
            - The net result is that the directory is renamed to be B
        - Move a directory from dir A to dir B/C (both nonexistnet)
            - Whatever nonexistent intermediary directories are needed will be created, then the directory will be renamed to be dir C
    - move() will not:
        - Move a file from dir A to dir B (nonexistent)
            - The file just gets renamed to be dir B, which is confusing!
        - Move a directory inside of itself
    Under the hood, move() is just using os.reanme() and shutil.copy2()
    '''
    #shutil.move(os.path.join(os.path.dirname(__file__), 'src.txt'), os.path.join(os.path.dirname(__file__), 'src-dir'))
    #shutil.move(os.path.join(os.path.dirname(__file__), 'src.txt'), os.path.join(os.path.dirname(__file__), 'made-up-dir'))
    # shutil Error
    #shutil.move(os.path.join(os.path.dirname(__file__), 'src-dir'), os.path.join(os.path.dirname(__file__), 'src-dir/hello'))
    #shutil.move(os.path.join(os.path.dirname(__file__), 'src-dir'), os.path.join(os.path.dirname(__file__), 'inner-dir/whatever/yes'))


def copyfileobj():
    '''
    - copyfileobj(<src>, <dst> [, <length>]) will:
        - Copy the contents of one file-like object into another file-like object
            - If the current file position of <src> is not 0, only bytes from the current position onward will be copied into <dst>
            - <length> is the buffersize, which if negative means to read without chunks into an unlimited buffer size
    '''
    # This is cuckoo syntax, but it works
    shutil.copyfileobj((pathlib.Path(__file__).parent / 'src.txt').open(), (pathlib.Path(__file__).parent / 'inner-dir' / 'whatever' / 'no').open('w'))


if __name__ == "__main__":
    #print(os.path.dirname(__file__)) # /Users/austinchang/tutorials/python/language/python2/popular_modules/shutil_py
    #print(os.getcwd()) # /Users/austinchang/tutorials/python/language
    #copy_file()
    #copy()
    #remove_directory_tree()
    #move()
    copyfileobj()
