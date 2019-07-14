# https://docs.python.org/2/library/os.path.html


import os


"""
The file checking operations seem to mostly be in the os.path module as opposed to the os module.
"""


def check_file_exists():
    if os.path.isfile(__file__):
        print(str(__file__) + " exists")


if __name__ == "__main__":
    check_file_exists()