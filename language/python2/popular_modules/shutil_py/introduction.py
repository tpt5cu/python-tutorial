# https://docs.python.org/2.7/library/shutil.html


import shutil, os


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


if __name__ == "__main__":
    #print(os.path.dirname(__file__)) # /Users/austinchang/tutorials/python/language/python2/popular_modules/shutil_py
    #print(os.getcwd()) # /Users/austinchang/tutorials/python/language
    #copy_file()
    copy()
    #remove_directory_tree()