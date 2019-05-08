import os

"""
I could place os module notes in the /tutorials/python/libraries section, but I use these operations so often that they should go here.
"""

def os_path_join():
    """
    os.path.join() merely joins path and stops at the first absolute path. It does not eliminate redundant slashes.
    """
    # None of these paths is a absolute path. Therefore, the final resulting path is a relative path
    print(os.path.join("hello", "my", "name", "is", "Austin")) # hello/my/name/is/Austin
    # This function joins from right to left. As soon as the rightmost absolute path is found, everthing to the left of it is thrown away and
    # everything to the right of it is joined to it
    print(os.path.join("hello", "my", "/name", "is", "Austin")) # /name/is/Austin
    print(os.path.join("hello", "/my", "/name", "is", "Austin")) # /name/is/Austin
    print(os.path.join("hello", "my", "name", "/is", "Austin")) # /is/Austin

def os_path_normpath():
    """
    os.path.normpath removes redundant slashes and collapses relative separators. It does not remove spaces or place a path with spaces in quotations.
    """
    p = (os.path.join("hello/", "my//", "name///", "is", "../Austin")) # hello/my/name/Austin
    print(p)
    print(os.path.normpath(p))
    p = (os.path.join("this ", " path ", "  has  ", "spaces  ")) # hello/my/name/Austin
    print(p)
    print(os.path.normpath(p))

if __name__ == "__main__":
    #os_path_join()
    os_path_normpath()