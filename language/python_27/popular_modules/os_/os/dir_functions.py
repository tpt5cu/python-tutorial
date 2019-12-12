# https://docs.python.org/2.7/library/os.html


import os


def make_dir():
    '''
    os.mkdir() will only create a single new directory. It will not:
    - create a tree of new directories
    - overwrite an existing directory with the new directory
    '''
    #os.mkdir(os.path.join(os.path.dirname(__file__), 'hello/world/yay')) # OSError errno == 2
    os.mkdir(os.path.join(os.path.dirname(__file__), 'hello')) # OSError errno == 17


def make_dirs():
    '''
    os.mkdir() will create an entire tree of new directories. Here's what happens if a directory already exists somewhere in the tree:
    - If the existing directory is a leaf node, an error is thrown
    - If the existing directory is a parent directory of the new leaf node, the operation succeeds. Why? Because all the operation cares about is
      creating the leaf node. It will create new parent directories as necessary, but will accept existing parent directories and not modify them
    '''
    os.makedirs(os.path.join(os.path.dirname(__file__), 'hello/world/yay'))


if __name__ == '__main__':
    #make_dir()
    make_dirs()