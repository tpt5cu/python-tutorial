"""
https://docs.python.org/2.7/library/os.html
https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
"""

""" 
The os module contains low level functions for interacting with the operating system. Higher-level modules should be used for file operations when
possible. The os.open() function is not the same as the built in open() function
"""

import os, glob

test_file_directory = "/Users/austinchang/Desktop/testfiles"
components_directory = "/Users/austinchang/Desktop/testfiles/components"

def examine_single_directory_with_glob():
    print("Moving to: " + os.getcwd())
    # The os module operates in the current working directory. If I want the os functions to apply somewhere else, I need to change directories
    os.chdir(components_directory)
    print("Moving to: " + os.getcwd())
    # glob also operates in the current working directory. glob uses os.listdir() under the hood
    for path in glob.glob("*.glm"):
        print(path)

def create_path():
    """ The os.path module has useful functions for manipulating paths.
    """
    root = "/Users/austinchang/pycharm/python_tutorial"
    git_ignore = "testCsv.csv"
    """ os.path.join() intelligently joins paths, so if I forget a slash it isn't a big deal. """
    path = os.path.join(root, git_ignore)
    print(path)

def traverse_directories():
    """ os.walk returns a tuple that is (<string>, <list>, <list>). Each directory that is traversed returns its own tuple.
    """
    for dirpath, dirnames, file_names in os.walk(test_file_directory):
        print(dirpath)
        for n in dirnames:
            print(n)
        for n in file_names:
            if n.endswith(".glm"):
                print(n)

if __name__ == "__main__":
    #examine_single_directory_with_glob()
    #create_path()
    traverse_directories()
