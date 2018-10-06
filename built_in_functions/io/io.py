# https://www.programiz.com/python-programming/file-operation (shows open modes)
# https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
# https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
# https://docs.python.org/3/tutorial/inputoutput.html (talks about seek(), readlines(), etc.)

import os


def get_working_directory():
    print("The current working directory is: " + str(os.getcwd()))


def my_print():
    """Python2 accepts both syntax versions, but python3 requires parenthesis for print()"""
    print("hello world")
    # print "hello world"


def my_open():
    """open() returns a file object (also known as a 'handle') that is used to read/write the underlying file.
    A file object is an iterator, not an iterable. That's why it can only traverse a file once (barring the use of seek())

    -The encoding is a default argument, but it should always be specified b/c different systems will use different
    default encodings.
    -The path can be absolute, or relative to the current working directory.
    -The default open mode is 'r', or read. It's NOT in binary mode by default
    -A file must be closed to free up resources. It should be closed in a finally block in case an exception happens
    during file operations

    -A file may only be opened in ONE of the following modes: create/read/write/append
    """
    try:
        file = open('../.gitignore', encoding='utf-8')
        """read() without an argument reads the entire file"""
        print(file.read())
    finally:
        file.close()


def my_better_open():
    """The 'with' statement simplifies exception handling. It does the same thing as try-finally, but it can be used
    for much more than file handling.
    """
    with open('../.gitignore', encoding='utf-8') as f:
        print(f.read())


def offset_the_file_pointer_location():
    """Seek allows me to offset the file pointer from a defined point in the file."""
    with open('../.gitignore', encoding='utf-8') as f:
        """This skips the first 3 characters in the file. I think under the hood it's skipping the first 3 bytes,
        which correspond to the first 3 characters
        """
        f.seek(3)
        print(f.read())


def read_by_line():
    """list() and <file_object>.readlines() do the same thing, but their implementations might be different. I'll
    be surprised if I ever really need to know the difference in implementation.
    """
    with open('../.gitignore', encoding='utf-8') as f:
        content = f.readlines()
        x = 1
        for line in content:
            print(str(x) + ": " + line)
            x += 1


if __name__ == "__main__":
    # get_working_directory()
    # my_print()
    # my_open()
    # my_better_open()
    # offset_the_file_pointer_location()
    read_by_line()
