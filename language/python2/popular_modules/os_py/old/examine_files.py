# https://docs.python.org/2/library/os.path.html


import os


'''The file checking operations seem to mostly be in the os.path module as opposed to the os module.'''


def file_exists():
    """os.path.isfile() only returns True if the object is 1) a file and 2) exists"""
    filepath = __file__
    dir_path = os.path.dirname(__file__)
    print(os.path.isfile(filepath)) # True
    print(os.path.isfile(dir_path)) # False


def directory_exists():
    """os.path.isdir() only returns True if the object is 1) a directory and 2) exists"""
    filepath = __file__
    dir_path = os.path.dirname(__file__)
    print(os.path.isdir(filepath)) # False
    print(os.path.isdir(dir_path)) # True


def filesystem_object_exists():
    """os.path.exists() returns True if the object is a file or a directory and it exists"""
    filepath = __file__
    dir_path = os.path.dirname(__file__)
    print(os.path.exists(filepath)) # True
    print(os.path.exists(dir_path)) # True


def get_directory_contents():
    """os.listdir() does not return "./" and "../" in the directory. However it will include hidden files and hidden directories (i.e. those that start with ".")"""
    for f in os.listdir(os.getcwd()):
        print(f)
    print("")
    for s in [f for f in os.listdir(os.getcwd()) if not f.startswith(".")]:
        print(s)


if __name__ == "__main__":
    #file_exists()
    directory_exists()
    #filesystem_object_exists()
    #get_directory_contents()