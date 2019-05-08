"""
https://docs.python.org/2/library/stdtypes.html#bltin-file-objects
"""

import os, re

src_path = os.path.join(os.path.dirname(__file__), "test-text.txt")
target_path = os.path.join(os.path.dirname(__file__), "new-file.txt")

def read_lines():
    """
    readlines() uses readline() to insert all of the lines into a list! This won't work for really large files, but it's convenient. The counterpart
    to readlines() is writelines(). readlines() is different from read() in that read() returns a string.
    """
    with open(src_path) as f:
        lines = f.readlines()
    with open(target_path, 'w') as f:
        f.writelines(lines)

def use_iterator():
    """
    A file object is its own iterator. That means its next() method is implicitly called when used in a for-loop. This is quite efficient
    """
    with open(target_path, 'w') as fw:
        with open(src_path) as f:
            for line in f:
                fw.write(line)

def use_iterator_with_seek():
    """
    Sometimes its useful to move the file pointer around. I cannot correctly move the pointer around with readlines()
    """
    with open(target_path, 'w') as fw:
        with open(src_path) as f:
            for line in f:
                # Skip lines with numbers for fun
                if re.search(r"\d", line) == None:
                    fw.write(line)

def inplace_modification():
    """ 
    Opening a file in r+ mode is NOT enough to perform in-place modification. Lines just get written to the end of the file. Using seek() does not
    work
    - Anytime there is a call to f.write(), the file pointer gets moved to the end of the file AFTER the method invocation, but BEFORE the write
      happens.
    - They say I can use seek() to modify a file in place, and that the new content must be EXACTLY the same number of bytes as the original content.
    - Just use the fileinput module.
    """
    EOF = os.path.getsize(target_path)
    print(EOF)
    with open(target_path, 'r+') as f:
        f.seek(0)
        while (f.tell() < EOF):
            print(f.tell())
            line = f.readline()
            print(f.tell())
            if re.search(r"\d", line) != None:
                f.write("Hello there!\n")
            else:
                print(f.tell())
                f.write(line)
                print(f.tell())

if __name__ == "__main__":
    #read_lines()
    #use_iterator()
    #use_iterator_with_seek()
    # Use both together
    use_iterator()
    inplace_modification()