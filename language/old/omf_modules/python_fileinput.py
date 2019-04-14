# https://docs.python.org/2/library/fileinput.html
# https://stackoverflow.com/questions/5453267/is-it-possible-to-modify-lines-in-a-file-in-place

import fileinput, os
# import pathlib
# I'm getting some kind of ImportError for pathlib and I don't have time to go into specifics right now.

"""Basically, fileinput is a helper class to make it easy to loop over standard input or a list of files."""


def read_file():
    """If I didn't provide any files arguments in fileinput.input(), it would default to looking at sys.argv[1] for files
    to loop over. If sys.argv[1] was empty, it would wait for sys.stdin. If I provide a path to some files, it loops
    over those.

    Normally, it is not safe to write to a file that I am also reading, as any changes I make could overwrite content
    that I have not written yet. A backup file (or reading the file into a buffer) makes it possible to avoid this
    problem. inplace=1 uses a backup file to pretend like it modified the file in question in-place.

    -printing each line of a fileinput actually writes whatever was supposed to be printed into the file LOL.
    -trying to add each line of a fileinput to a list just adds every single character as a string to the list LOL.
    -apparently, after reading a file with fileinput.input() and NOT doing ANYTHING, the file becomes empty!! Is it
    opening the file in 'w' mode? That must be it.
    """

    real_path = "/Users/austinchang/pycharm/python_tutorial/temp.txt"
    content = []
    for line in fileinput.input(real_path, inplace=1):
        pass
        # content.append(type(line))
        # content += line
    print(content)
    print("fileinput is done")


if __name__ == "__main__":
    read_file()