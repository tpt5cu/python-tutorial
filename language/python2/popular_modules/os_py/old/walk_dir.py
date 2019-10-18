# https://docs.python.org/2/library/os.html


import os


"""
Remember that os.path.join() does not resolve parent directory path component navigation (i.e. "../"). Only os.path.normpath() does that. However,
directory operations in Python are smart enough to resolve parent path components themselves even if the string still has the dots.
"""


def traverse_directories():
    """
    os.walk() returns a generator which will return a 3-tuple of (<dirpath>, <dirnames>, <filenames>) for each call.
    """
    dirpath = os.path.join(os.path.dirname(__file__), "../../../")
    #print(dirpath)
    #print(os.path.isdir(dirpath))
    x = os.walk(dirpath)
    print(type(x))

    
def traverse_specific_directories():
    pass


if __name__ == "__main__":
    traverse_directories()